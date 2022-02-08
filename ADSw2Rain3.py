def fill_with_water(heights, positions, water_total, next_pos, next_height, curr_max, curr_max_pos):

    # print('in', heights, positions, next_height, next_pos, curr_max, curr_max_pos, water_total)

    if next_height > heights[-1]:
        if next_height > curr_max:
            water_total = water_total + (next_pos - positions[-1]) * (curr_max - heights[-1])
            heights.pop()
            tmp = positions.pop()
            if next_height != heights[-1]:
                heights.append(next_height)
                positions.append(tmp)
            curr_max = next_height
            curr_max_pos = next_pos
        else:
            water_total = water_total + (next_pos - positions[-1]) * (next_height - heights[-1])
            heights.pop()
            tmp = positions.pop()
            if next_height != heights[-1]:
                heights.append(next_height)
                positions.append(tmp)

    elif next_height == heights[-1]:
        pass

    else:
        heights.append(next_height)
        positions.append(next_pos)

    # print('out', heights, positions, next_height, next_pos, curr_max, curr_max_pos, water_total)

    return water_total, curr_max


def calc_rain_water(h):

    if len(h) == 0:  # handle stupid cases
        return 0

    heights = []
    positions = []
    result = 0
    start = True

    for p, h in enumerate(h):

        if not heights:  # load first value
            heights.append(h)
            positions.append(p)
            curr_max = h
            curr_max_pos = p
        else:
            if h > curr_max and start:  # skip all increasing bars in the beginning
                heights.pop()
                positions.pop()
                heights.append(h)
                positions.append(p)
                curr_max = h
                curr_max_pos = p
            else:
                start = False
                result, curr_max = \
                    fill_with_water(heights, positions, result, p, h, curr_max, curr_max_pos)
    if heights:
        next_height = heights.pop()
        next_pos = positions.pop()

    if heights and next_height > heights[-1]:
        result = result + (next_pos - positions[-1]) * (next_height - heights[-1])
        heights.pop()
        tmp = positions.pop()
        if next_height != heights[-1]:
            heights.append(next_height)
            positions.append(tmp)

    return result

# some test code
if __name__ == "__main__":

    test_h = [1, 4, 1]
    # 0
    print(calc_rain_water(test_h))

    test_h = [1, 5, 4, 2, 4, 5, 4, 2, 4, 7, 6, 7, 1]
    # 11
    # print(calc_rain_water(test_h))

    test_h = [8, 4, 4, 2, 4, 5, 4, 2, 1, 2, 4, 8]
    # 48
    # print(calc_rain_water(test_h))

    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    # print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    # print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    # print(calc_rain_water(test_h))
