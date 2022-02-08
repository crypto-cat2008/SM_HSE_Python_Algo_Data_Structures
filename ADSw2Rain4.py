def check_for_water(heights, positions, next_height, next_position, max_value, total):

    print('in', heights, positions, next_height, next_position, max_value, total)

    new_max = max_value
    found_water = False
    result = 0

    while heights and positions and next_height >= heights[-1]:
        prev_height = heights.pop()
        prev_pos = positions.pop()
        result = (next_position - prev_pos) * (min(next_height, max_value) - prev_height)
        if result:
            found_water = True
        total += result
        print('valley', heights, positions, next_height, max_value, total)


    heights.append(next_height)
    if found_water:
        positions.append(prev_pos)
    else:
        positions.append(next_position)

    if next_height > new_max:
        new_max = next_height

    print('out', heights, positions, total)

    return total, new_max


def calc_rain_water(h):

    if not h:
        return 0

    heights = []
    positions = []
    end_of_first_increase = True
    curr_max = 0
    total_water = 0

    for p, h in enumerate(h):

        if not heights and not positions:  # empty stacks - add first element
            heights.append(h)
            positions.append(p)
            curr_max = h

        if h > heights[-1]:  # height increase
            total_water, curr_max = \
                check_for_water(heights, positions, h, p, curr_max, total_water)

        elif h < heights[-1]:  # height decrease
            # if first decrease - drop all except the last value
            if end_of_first_increase:
                last_height = heights.pop()
                last_pos = positions.pop()
                while heights and positions:
                    heights.pop()
                    positions.pop()
                heights.append(last_height)
                positions.append(last_pos)
                end_of_first_increase = False

            heights.append(h)
            positions.append(p)
        else:  # if equal do nothing
            pass

    print(heights, positions)
    return total_water


# some test code
if __name__ == "__main__":
    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    # print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    # print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    # print(calc_rain_water(test_h))

    test_h = [1, 4, 1]
    # 0
    # print(calc_rain_water(test_h))

    test_h = [1, 5, 4, 2, 4, 5, 4, 2, 4, 7, 6, 7, 1]
    # 11
    # print(calc_rain_water(test_h))

    test_h = [8, 4, 4, 2, 4, 5, 4, 2, 1, 2, 4, 8]
    # 48
    # print(calc_rain_water(test_h))

    test_h = [8, 5, 4, 8]
    # 7
    print(calc_rain_water(test_h))
