def teamOracle(team_size, start_times, finish_times):

    # if there is no team
    if team_size <= 0:
        return True

    # if there is no work
    if len(start_times) <= 0:
        return True

    # initialize assignments
    assignments = [-1 for _ in range(len(start_times))]
    last_selected = [-1 for _ in range(team_size)]

    start_times, finish_times = \
        [list(x) for x in zip(*sorted(zip(start_times, finish_times), key=lambda pair: pair[0]))]


    # print(start_times, finish_times)

    for team_mem in range(team_size):   # assign work to each member
        for asgmnt in range(len(assignments)):
            if assignments[asgmnt] == -1:  # find unassigned
                if start_times[asgmnt] >= last_selected[team_mem]:
                    assignments[asgmnt] = team_mem
                    last_selected[team_mem] = finish_times[asgmnt]

    # print(assignments)

    if -1 in assignments:
        return False
    else:
        return True


team_size = 4
start_times = [1, 5, 10]
finish_times = [3, 7, 15]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 0
start_times = [1, 5, 10]
finish_times = [3, 7, 15]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 2
start_times = []
finish_times = []
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 1
start_times = [1, 2, 3]
finish_times = [3, 5, 5]
# check that your code works correctly on provided example
assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 2
start_times = [1, 2, 3]
finish_times = [3, 5, 5]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 3
start_times = [1, 2, 3]
finish_times = [3, 5, 5]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 3
start_times = [1, 2, 1]
finish_times = [3, 5, 5]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 3
start_times = [1, 1, 2, 6]
finish_times = [5, 3, 4, 8]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'


team_size = 1
start_times = [1, 1]
finish_times = [2, 2]
# check that your code works correctly on provided example
assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 2
start_times = [1, 1]
finish_times = [2, 2]
# check that your code works correctly on provided example
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 1
start_times = [1, 3]
finish_times = [3, 4]
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

team_size = 7
start_times = [7, 5, 8, 5, 8, 15, 1, 5, 27, 27, 25, 9, 17, 19, 13]
finish_times = [29, 8, 25, 18, 10, 28, 21, 10, 29, 28, 32, 27, 29, 25, 15]
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

'''
------------------------------------------------------------------------------
'''


def minRestarts(m, t, no_request_times):
    min_restarts = 0
    n = len(no_request_times)
    curr_restart = 0
    limit = t

    while limit < m:

        if curr_restart >= n or no_request_times[curr_restart] > limit:
            return -1

        while curr_restart < n-1 and no_request_times[curr_restart+1] <= limit:
            # print('restart at', no_request_times[curr_restart+1])
            curr_restart += 1

        min_restarts += 1
        limit = no_request_times[curr_restart] + t + 1
        curr_restart +=1

    return min_restarts

m = 100
t = 20
no_request_times = [50]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

m = 950
t = 400
no_request_times = [200, 375, 550, 750]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 2, 'Wrong answer'

m = 100
t = 20
no_request_times = [4, 5, 30, 35, 38, 40,60, 70,80]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

m = 100
t = 20
no_request_times = []
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

m = 21
t = 20
no_request_times = [19]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 1, 'Wrong answer'

m = 70
t = 50
no_request_times = [51]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

m = 70
t = 50
no_request_times = [50]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 1, 'Wrong answer'


m = 100
t = 50
no_request_times = [49, 98]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 1, 'Wrong answer'

m = 0
t = 50
no_request_times = [49, 98]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 0, 'Wrong answer'

m = 100
t = 110
no_request_times = [49, 98]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 0, 'Wrong answer'

m = 120
t = 50
no_request_times = [50, 101]
# check that your code works correctly on provided example
assert minRestarts(m, t, no_request_times) == 2, 'Wrong answer'

'''
------------------------------------------------------------------------------
'''

def minUnionCost(set_sizes):
    n = len(set_sizes)
    min_sum = 0

    set_sizes.sort()

    while len(set_sizes) >= 2:
        min_number = set_sizes.pop(0)
        set_sizes[0] += min_number
        min_sum += set_sizes[0]
        set_sizes.sort()
        # print(set_sizes, min_sum)

    return min_sum

set_sizes = [2, 6]
# check that your code works correctly on provided example
assert minUnionCost(set_sizes) == 8, 'Wrong answer'

set_sizes = [2, 6, 4]
# check that your code works correctly on provided example
assert minUnionCost(set_sizes) == 18, 'Wrong answer'

set_sizes = [1, 2, 3, 4]
# check that your code works correctly on provided example
assert minUnionCost(set_sizes) == 19, 'Wrong answer'

set_sizes = [2, 6, 8, 9, 14]
# check that your code works correctly on provided example
assert minUnionCost(set_sizes) == 86, 'Wrong answer'