import sys


frequency_map = {
    'minutes': {'first': 0, 'last': 59},
    'hours': {'first': 0, 'last': 23},
    'days': {'first': 0, 'last': 31},
    'months': {'first': 1, 'last': 12},
    'weekdays': {'first': 0, 'last': 6}
}


def schedule(value, frequency_type):

    first = frequency_map[frequency_type]['first']
    last = frequency_map[frequency_type]['last']

    if value == '*':
        return ' '.join([str(h) for h in range(first, last + 1)])

    if ',' in value:
        return ' '.join(value.split(','))

    if '/' in value:
        details = value.split('/')
        step = int(details[1])

        frequency = details[0].split('-')
        start = int(frequency[0])
        stop = int(frequency[1])

        assert start in range(first, last + 1), 'Invalid first value'
        assert stop in range(first, last + 1), 'Invalid last value'

        return ' '.join([str(v) for v in range(start, stop + 1, step)])

    if '-' in value:
        frequency = value.split('-')
        start = int(frequency[0])
        stop = int(frequency[1])

        assert start in range(first, last + 1), 'Invalid first value'
        assert stop in range(first, last + 1), 'Invalid last value'

        return ' '.join([str(v) for v in range(start, stop + 1)])

    try:
        int(value)
    except ValueError:
        raise ValueError('Invalid value')

    assert int(value) in range(first, last + 1), 'Value not in correct range'

    return value


def get_command(command):
    return ' '.join(command)


if __name__ == '__main__':
    args = sys.argv
    minute = args[1]
    hour = args[2]
    day = args[3]
    month = args[4]
    weekday = args[5]
    command = args[6:]


    print('Minute: ', schedule(minute, 'minutes'))
    print('Hour: ', schedule(hour, 'hours'))
    print('Day of the month: ', schedule(day, 'days'))
    print('Month: ', schedule(month, 'months'))
    print('Day of the week: ', schedule(weekday, 'weekdays'))
    print('Command: ', get_command(command))
