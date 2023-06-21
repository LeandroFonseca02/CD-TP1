import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GeoLocator',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'GeoLocatorHome'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double? _latitude;
  double? _longitude;
  double? _altitude;
  DateTime? _time;
  List<String> _parsedDate = [];
  String filePath = '';

  @override
  void initState(){
    super.initState();
    _getCurrentLocation();
  }

  Future<Position> _determinePosition() async{
    LocationPermission permission;
    permission = await Geolocator.checkPermission();
    externalFolder();

    if(permission == LocationPermission.denied){
      permission = await Geolocator.requestPermission();
    }
    return await Geolocator.getCurrentPosition();
  }

  void _getCurrentLocation() async {
    Position position = await _determinePosition();
    scheduleTimeout(5000);

    setState(() {
      _latitude = position.latitude;
      _longitude = position.longitude;
      _altitude = position.altitude;
      _time = position.timestamp;
      _parsedDate = ParseDate(_time!);
      writeData("$_latitude;$_longitude;$_altitude;${_parsedDate.elementAt(0)};${_parsedDate.elementAt(1)}\n");
    });
  }

  List<String> ParseDate(DateTime date){
      List<String> parsedDate = [];
      parsedDate.add(date.toString().substring(0, 10));
      parsedDate.add(date.toString().substring(11, 22));
      return parsedDate;
  }


  Future<File> writeData(String locationData) async {
    File file = File('/storage/emulated/0/GeoLocatorData.csv');

    if (!(await file.exists())) {
      return file.writeAsString('Latitude;Longitude;Altitude;Date;Time\n');
    }

    return file.writeAsString(locationData, mode: FileMode.append);
  }

  Timer scheduleTimeout([int milliseconds = 1000]) =>
      Timer(Duration(milliseconds: milliseconds), _getCurrentLocation);

///////////////////////////// pede acesso ao user para usar storage
  externalFolder() async {
    if(await Permission.manageExternalStorage.isGranted){
      final path = Directory('/storage/emulated/0/');
      filePath = '';
      if(await path.exists()){
        filePath = path.path;
      }else{
        final Directory appDocNewFolder = await path.create(recursive: true);
        filePath = appDocNewFolder.path;

      }
       File file = File('${filePath}GeoLocatorData.csv');

      if (!(await file.exists())) {
        return file.writeAsString('Latitude;Longitude;Altitude;Date;Time\n');
      }
    }else{
      await Permission.storage.request();
    }
  }
  /////////////////////////////////

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("GeoLocator"),
      ),
      body: Center(

        child: ListView(
            children: _latitude == null ? [const Text("Failed to fetch location")] :
                  [Text("Latitude: $_latitude"),
                  Text("Longitude: $_longitude"),
                  Text("Altitude: $_altitude"),
                  Text("Date: ${_parsedDate.elementAt(0)}"),
                  Text("Time: ${_parsedDate.elementAt(1)}"),
                  ]
        ),
      ),
    );
  }
}
