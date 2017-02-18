# main.py
#
# James Nguyen: 45298461
# ICS 32 Fall 2016
# Project 3
#
# This module takes input from users, and return the result
import MapQuestAPI
import output_class


def check_number_input(number: int) -> int:
    """Get user input and check if the input number is valid

    :param number: the input number
    :return: number of destinations from user
    """
    while True:
        user_input = input()
        number_of_destinations = int(user_input)
        try:
            if number_of_destinations < number:
                print('Number must be larger than or equal to ' + str(number))
            else:
                return number_of_destinations
        except ValueError and TypeError:
            print('Must be an integer')


def build_location(number_of_locations: int) -> list:
    """Build locations from user input based on how many number of locations

    :param number_of_locations: Number of destinations
    :return: List of locations
    """
    locations = []

    for n in range(number_of_locations):
        location = input()
        locations.append(location)

    return locations


def build_outputs(number_of_outputs: int) -> list:
    """Get user_inputs on outputs they want

    :param number_of_outputs: Number of outputs
    :return: List of expected outputs types
    """

    outputs = []

    for n in range(number_of_outputs):
        user_input = input()
        outputs.append(user_input)

    return outputs


def print_outputs(result: dict, outputs: list):
    """

    :param result: Result from the MapQuest API
    :param outputs: List of outputs expected by the users
    :return: False if the API couldn't find the route
    """
    try:
        print()
        for output in outputs:
            if output == 'LATLONG':
                lat_long = output_class.LatLong(result)
                lat_long.print()

            elif output == 'STEPS':
                steps = output_class.Steps(result)
                steps.print()

            elif output == 'TOTALTIME':
                time = output_class.Time(result)
                time.print()

            elif output == 'TOTALDISTANCE':
                distance = output_class.Distance(result)
                distance.print()

            elif output == 'ELEVATION':
                lat_long_list = output_class.LatLong(result).get_lat_long()
                print('ELEVATIONS')
                # Instead of the usual class containing every information about every locations,
                # instead, we have to get elevations specific to each location using different url
                # to circumvent the distance limits
                for lat_long in lat_long_list:
                    elevation_url = MapQuestAPI.build_elevation_url(lat_long)
                    elevation_result = MapQuestAPI.get_result(elevation_url)

                    elevation = output_class.Elevation(elevation_result)
                    elevation.print()

            print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except KeyError:
        # This is because if the MapQuest API returns a line indicating that there isn't a route possible
        # There will be a key error as the classes looks for specific keys in the results dictionary.
        # Returning False will indicate that the route isn't found.
        return False


def main():
    number_of_locations = check_number_input(2)
    locations = build_location(number_of_locations)

    number_of_outputs = check_number_input(1)
    outputs = build_outputs(number_of_outputs)

    url = MapQuestAPI.build_direction_url(locations)
    result = MapQuestAPI.get_result(url)

    try:
        if result is None:
            # This means that the connection didn't work and so it is a MAPQUEST API errors
            print()
            print('MAPQUEST ERROR')
            return
        elif result['info']['messages'][0] == 'We are unable to route with the given locations.':
            # This is returned when two locations are impossible to reach from each other
            print()
            print('NO ROUTE FOUND')
            return
    except IndexError:
        # This means that nothing was wrong when testing if there was anything wrong with the result,
        # so now we will print the outputs
        print_outputs(result, outputs)


if __name__ == '__main__':
    main()
