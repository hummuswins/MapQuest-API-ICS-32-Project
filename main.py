import MapQuestAPI


def check_number_input(number: int) -> int:
    """
    Check if the input number is valid
    :return: number of destinations
    """
    while True:
        user_input = input()
        number_of_destinations = int(user_input)
        try:
            if number_of_destinations < number:
                print('Number must be larger than or equal to ' + number)
            else:
                return number_of_destinations
        except ValueError and TypeError:
            print('Must be an integer')


def main():
    number_of_destinations = check_number_input(2)
    locations = []
    for n in range(number_of_destinations):
        location = input()
        locations.append(location)
    number_of_outputs = check_number_input(1)
    outputs = []
    for n in range(number_of_outputs):
        output = input()
        outputs.append(output)
    url = MapQuestAPI.build_search_url(locations)
    result = MapQuestAPI.get_result(url)
    MapQuestAPI.print_result(result)


if __name__ == '__main__':
    main()
