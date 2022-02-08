from heapq import heappop, heappush
import random


def edge_to_adjacency(edge_list, n):
    adj_list = [[] for i in range(n)]

    for e in edge_list:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    return adj_list


def dfs(v, visited_list, graph, comp):
    visited_list[v] = True
    comp.append(v)

    for u in graph[v]:
        if not visited_list[u]:
            dfs(u, visited_list, graph, comp)


def film_recommendation(movies, similar_movies, friends, friends_movies):
    num_friends = len(friends)
    num_movies = len(movies)
    visited = [False for i in range(num_movies)]
    watched_m_list = [[0, set(), 0, 0] for i in range(len(movies))]
    arr_scores = []

    # list of movies is empty, return None - nothing to recommend
    if num_movies == 0:
        return None

    # if no friends or they have not watched any movies - all F scores are equal to 0, pick a random movie
    if num_friends == 0 or len(friends_movies) == 0:
        return movies[random.randint(0, num_movies - 1)]

    # collect stats on all watched movies; movies that have not been watched will have F score equal 0
    for f, f_movies in enumerate(friends_movies):
        for m in f_movies:
            watched_m_list[m][0] += 1
            watched_m_list[m][1].add(f)

    # Find connected components in graph of similar movies. All movies in a connected component are similar
    adj_list = edge_to_adjacency(similar_movies, num_movies)

    for i in range(num_movies):
        component = []
        if not visited[i]:
            dfs(i, visited, adj_list, component)

            total_watches = 0
            total_w_friends = 0
            for m in component:
                total_watches += watched_m_list[m][0]
                total_w_friends += len(watched_m_list[m][1])
            for m in component:
                watched_m_list[m][2] = total_watches - watched_m_list[m][0]
                watched_m_list[m][3] = total_w_friends - len(watched_m_list[m][1])

    # print(watched_m_list)

    for i, m_stats in enumerate(watched_m_list):
        if m_stats[0] != 0 and m_stats[3] != 0:
            score = m_stats[0] / (m_stats[2] / m_stats[3])
            heappush(arr_scores, (-score, movies[i]))

    # print(arr_scores)

    return heappop(arr_scores)[1]


movies_t = ['10 Years', '101 Dalmatians', '17 Again', '27 Dresses', '3 Ninjas',
            '8 Mile', 'About Time', 'Almost Famous', 'American Beauty', 'Bad Words',
            'Lady and the Tramp', 'Just Go with It', 'The proposal', 'The Accidental Husband',
            'Camp Nowhere', 'Notorious', 'Begin Again', 'Singles', 'A Beautiful Mind']

# similar_movies_t = [(0, 9), (1, 10), (2, 11), (3, 12), (13, 3), (4, 14), (5, 15), (6, 16), (7, 17), (8, 18)]
similar_movies_t = [(0, 1), (0, 2), (0, 3), (3, 2), (1, 2), (1, 3), (4, 5)]

friends_t = ['Anna', 'John', 'David', 'Sara', 'Peter', 'Alice']
'''
friends_movies_t = [[3, 8, 18, 3],
                    [4, 11, 12],
                    [15, 5, 18],
                    [2, 7, 10, 6, 13],
                    [9, 14, 4]]'''

friends_movies_t = [[0, 1, 2, 3, 4], [0, 2, 3, 4, 5], [0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]

print(film_recommendation(movies_t, similar_movies_t, friends_t, friends_movies_t))
