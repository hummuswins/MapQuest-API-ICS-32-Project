# output_class.py
#
# James Nguyen: 45298461
# ICS 32 Fall 2016
# Project 3
#
# This module creates different class for different outputs


class LatLong:
    """This class contains the latitude and longitude of every locations

    Attributes:
        listLatLng (list): list of latitude and longitude

    """
    def __init__(self, result: dict):
        """
        :param result: Result returned from the server
        """
        self.listLatLng = []
        locations = result['route']['locations']
        for location in locations:
            lat = location['latLng']['lat']
            lng = location['latLng']['lng']
            self.listLatLng.append([lat, lng])

    def print(self):
        """print out every latitude and longitude in the listLatLng """
        print('LATLONGS')
        for location in self.listLatLng:
            output = ''

            if location[0] < 0:
                lng = format(location[0] * -1, '.2f')  # Will round the latitude or longitude to the nearest hundredths
                output += lng + 'S '
            else:
                lng = format(location[0], '.2f')
                output += lng + 'N '

            if location[1] < 0:
                lat = format(location[1] * -1, '.2f')
                output += lat + 'W'
            else:
                lat = format(location[1], '.2f')
                output += lat + 'E'

            print(output)

    def get_lat_long(self):
        """return listLatLng

        :return: list of latitude and longitude
        """
        return self.listLatLng


class Steps:
    """Class that will contains the

    Attributes:
        steps (list): list of directions steps
    """
    def __init__(self, result: dict):
        """
        :param result: Result from MapQuest API
        """
        self.steps = []
        legs = result['route']['legs']
        for leg in legs:
            for maneuver in leg['maneuvers']:
                self.steps.append(maneuver['narrative'])

    def print(self):
        """Print every single steps in the directions"""
        print('DIRECTIONS')
        for step in self.steps:
            print(step)


class Time:
    """Class contains total time of route

    Attributes:
        time (int): Total time in minutes
    """
    def __init__(self, result: dict):
        """
        :param result: Result from the MapQuestAPI
        """
        seconds = result['route']['time']
        self.time = round(seconds/60)

    def print(self):
        """Print the total time"""
        response = 'TOTAL TIME: ' + str(self.time) + ' minutes'
        print(response)


class Distance:
    """Class contains the total distance of the route

    Attributes:
        distance (int): Total distance in miles
    """
    def __init__(self, result: dict):
        self.distance = round(result['route']['distance'])

    def print(self):
        """Print the total distance"""
        response = 'TOTAL DISTANCE: ' + str(self.distance) + ' miles'
        print(response)


class Elevation:
    """Class contains elevation of a single location

    Attributes:
        height (int): The height (elevation) of a location.
    """
    def __init__(self, result: dict):
        distance_height_collection = result['elevationProfile']

        for distanceHeight in distance_height_collection:
            height = distanceHeight['height']
            self.height = round(height)

    def print(self):
        """Print the height of the location"""
        print(self.height)
