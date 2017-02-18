# MapQuestAPI.py
#
# James Nguyen: 45298461
# ICS 32 Fall 2016
# Project 3
#
# This module talks with the MapQuest API


import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'oFNAbzSkZn5dhq0b3GYtsnR0qFM5tSFN'
DIRECTIONS_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'
ELEVATION_MAPQUEST_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'


def build_direction_url(locations: list) -> str:
    """Build API URL for these locations

    :param locations: list of locations
    :return: URL that will return the information about the route and locations
    """
    direction_parameters = [
        ('key', MAPQUEST_API_KEY), ('from', locations[0])
    ]
    for location in locations[1:]:
        direction_parameters.append(('to', location))

    return DIRECTIONS_MAPQUEST_URL + urllib.parse.urlencode(direction_parameters)


def build_elevation_url(lat_long: list) -> str:
    """Build API URL for the elevation of the specific location

    :param lat_long:  list of of the latitude and longtitude
    :return: API URL for the elevation of the location
    """
    lat_long_str = str(lat_long[0]) + ', ' + str(lat_long[1])
    elevation_parameter = [
        ('key', MAPQUEST_API_KEY), ('latLngCollection', lat_long_str), ('unit', 'f')
    ]

    return ELEVATION_MAPQUEST_URL + urllib.parse.urlencode(elevation_parameter)


def get_result(url: str) -> dict:
    """Get result from the url, format it from json to dictionary, and returns it

    :param url: The API URL
    :return: Result from the API URL dictionary
    """
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        #        print(json_text)
        return json.loads(json_text)
    except Exception as E:
        print(E)
        return
    finally:
        if response is not None:
            response.close()
