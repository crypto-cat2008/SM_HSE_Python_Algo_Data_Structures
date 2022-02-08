def calc_rain_water(h):
    positions = []
    ans = 0

    for i in range(len(h)):
        
        while positions and (h[positions[-1]] < h[i]):

            pop_height = h[positions[-1]]
            positions.pop()

            if len(positions) == 0:
                break

            width = i - positions[-1] - 1

            min_height = min(h[positions[-1]], h[i]) - pop_height

            ans += width * min_height

        positions.append(i)

    return ans
