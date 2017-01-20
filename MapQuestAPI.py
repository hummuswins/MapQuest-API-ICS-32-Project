# MapQuestAPI.py
#
# James Nguyen: 45298461
# ICS 32 Fall 2016
# Project 3
#
# This program talks with the MapQuest API
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'oFNAbzSkZn5dhq0b3GYtsnR0qFM5tSFN'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'


def build_search_url(locations) -> str:
    query_parameters =[
        ('key', MAPQUEST_API_KEY), ('from', locations[0])
    ]
    for location in locations[1:]:
        query_parameters.append(('to', location))

    return BASE_MAPQUEST_URL + urllib.parse.urlencode(query_parameters)


def get_result(url: str) -> dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')

        return json.loads(json_text)
    finally:
        if response is not None:
            response.close()


def print_result(result: dict):
    legs = result['route']['legs']
    for leg in legs:
        for maneuver in leg['maneuvers']:
            print(maneuver['narrative'])
        print()
