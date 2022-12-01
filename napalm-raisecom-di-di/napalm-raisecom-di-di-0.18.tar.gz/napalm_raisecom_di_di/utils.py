def to_seconds(time_format):
    # ----
    # '225d17h39m'
    # ----
    seconds = minutes = hours = days = weeks = 0

    number_buffer = ''
    for current_character in time_format:
        if current_character.isdigit():
            number_buffer += current_character
            continue
        if current_character == 's':
            seconds = int(number_buffer)
        elif current_character == 'm':
            minutes = int(number_buffer)
        elif current_character == 'h':
            hours = int(number_buffer)
        elif current_character == 'd':
            days = int(number_buffer)
        elif current_character == 'w':
            weeks = int(number_buffer)
        else:
            raise ValueError(f'Invalid specifier - [{current_character}]')
        number_buffer = ''

    seconds += (minutes * 60)
    seconds += (hours * 3600)
    seconds += (days * 86400)
    seconds += (weeks * 604800)

    return seconds
