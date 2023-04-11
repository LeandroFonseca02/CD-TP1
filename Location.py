from datetime import datetime
import math


class Location:
    def __init__(self, latitude, longitude, altitude, date, time):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.datetime = datetime.strptime(date + ' ' + time[0:8], '%d/%m/%Y %H:%M:%S')
        self.date = self.datetime.date()
        self.time = self.datetime.time()

    # Calcula a distância de dois pontos em kilómetros segundo a fórmula de Haversine
    @staticmethod
    def calculate_distance(location, location2):
        dist_lat = (location2.latitude - location.latitude) * math.pi / 180.0
        dist_lon = (location2.longitude - location.longitude) * math.pi / 180.0

        lat1 = location.latitude * math.pi / 180.0
        lat2 = location2.latitude * math.pi / 180.0

        exp = (pow(math.sin(dist_lat / 2), 2) +
               pow(math.sin(dist_lon / 2), 2) *
               math.cos(lat1) * math.cos(lat2))
        radius_earth = 6371
        exp2 = 2 * math.asin(math.sqrt(exp))
        distance = exp2 * radius_earth
        return distance

    # Calcula a velocidade entre dois pontos em metros por segundo
    @staticmethod
    def calculate_velocity_ms(distance, delta_time):
        return (distance * 1000) / (abs(delta_time))

    # Calcula a velocidade entre dois pontos em kilómetros por hora
    @staticmethod
    def calculate_velocity_kmh(distance, delta_time):
        return distance / (abs(delta_time / 3600))

    # Calcula a diferença de tempo entre dois pontos em segundos
    @staticmethod
    def delta_time_sec(location_start, location_end):
        return (location_end.datetime - location_start.datetime).total_seconds()
