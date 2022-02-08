def lines(a):
    result = 0

    if len(a) < 3:  # nothing to remove
        return result

    current_color = a[0]
    new_a = [-1] * 1002
    new_a[0] = current_color
    curr_color_count = 1
    next_ball = 1

    for i in range(1, len(a)):

        if a[i] == current_color:
            curr_color_count += 1
            new_a[next_ball] = a[i]
            next_ball += 1
            # print('i=', i, new_a[0:20])

        else:
            last_color = new_a[next_ball - 1]
            # print('last color', last_color, next_ball, result)
            remove_count = 1
            for j in range(next_ball - 2, -1, -1):
                if new_a[j] == last_color:
                    remove_count += 1
                else:
                    break
            if remove_count >= 3:
                next_ball -= remove_count
                result += remove_count
            current_color = a[i]
            curr_color_count += 1
            new_a[next_ball] = a[i]
            next_ball += 1
            # print('i=', i, new_a[0:20])

    if next_ball >= 3:
        last_color = new_a[next_ball - 1]
        # print('last color', last_color, next_ball, result)
        remove_count = 1
        for j in range(next_ball - 2, -1, -1):
            if new_a[j] == last_color:
                remove_count += 1
            else:
                break
        if remove_count >= 3:
            next_ball -= remove_count
            result += remove_count

    return result
