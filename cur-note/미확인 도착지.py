# import heapq
#
#
# def solution1():
#     T = int(input())
#     for _ in range(T):
#         vertex_n, road_n, dest_candi_n = map(int, input().split())  # 교차로, 도로, 목적지 후보의 개수
#         start, point_g, point_h = map(int, input().split())
#         lines = [tuple(map(int, input().split())) for _ in range(road_n)]
#         graph = [[] for _ in range(vertex_n + 1)]
#
#         for node1, node2, d in lines:
#             graph[node1].append((node2, d))
#             graph[node2].append((node1, d))
#         destination_candidates = [int(input()) for _ in range(dest_candi_n)]
#         # 다익스트라를 구현하면 되겠다.
#         q = []
#         pre_table = [i for i in range(vertex_n + 1)]
#         dp = [int(1e9) for _ in range(vertex_n + 1)]
#         dp[start] = 0
#         heapq.heappush(q, (start, 0))
#         while q:
#             node, dist = heapq.heappop(q)
#             if dist > dp[node]:
#                 continue
#             for n_node, n_dist in graph[node]:
#                 if dp[n_node] > dist + n_dist:
#                     dp[n_node] = dist + n_dist
#                     pre_table[n_node] = node
#                     heapq.heappush(q, (n_node, dp[n_node]))
#         result = []
#         for dest in destination_candidates:
#             # dest 의 경로를 구해보자
#             now = dest
#             while now != start:
#                 prev = pre_table[now]
#                 if (now == point_h and prev == point_g) or (now == point_g and prev == point_h):
#                     result.append(dest)
#                 now = prev
#         print(*sorted(result))
#
#
# def solution2():
#     import heapq
#
#     def tak_study(start):
#         q = []
#         dp = [int(1e9) for _ in range(vertex_n + 1)]
#         dp[start] = 0
#         heapq.heappush(q, (start, 0))
#         while q:
#             node, dist = heapq.heappop(q)
#             if dist > dp[node]:
#                 continue
#             for n_node, n_dist in graph[node]:
#                 if dp[n_node] > dist + n_dist:
#                     dp[n_node] = dist + n_dist
#                     heapq.heappush(q, (n_node, dp[n_node]))
#         return dp
#
#     T = int(input())
#     for _ in range(T):
#         vertex_n, road_n, dest_candi_n = map(int, input().split())  # 교차로, 도로, 목적지 후보의 개수
#         s, point_g, point_h = map(int, input().split())
#         lines = [tuple(map(int, input().split())) for _ in range(road_n)]
#         graph = [[] for _ in range(vertex_n + 1)]
#         for node1, node2, d in lines:
#             graph[node1].append((node2, d))
#             graph[node2].append((node1, d))
#         destination_candidates = [int(input()) for _ in range(dest_candi_n)]
#         # 다익스트라를 구현하면 되겠다.
#         min_dist = tak_study(s)
#         min_dist_start_g = tak_study(point_g)
#         min_dist_start_h = tak_study(point_h)
#         result = []
#         for dest_node in destination_candidates:
#             if (min_dist[dest_node] == min_dist[point_g] + min_dist_start_g[point_h] + min_dist_start_h[dest_node]) \
#                     or (
#                     min_dist[dest_node] == min_dist[point_h] + min_dist_start_h[point_g] + min_dist_start_g[dest_node]):
#                 result.append(dest_node)
#         print(*sorted(result))

# import heapq
#
# def tak_study(start_node):
#     distance = [int(1e9) for _ in range(vertex_num + 1)]
#     distance[start_node] = 0
#     q = []
#     heapq.heappush(q, (0, start_node))
#     while q:
#         dist, current_node = heapq.heappop(q)
#         if distance[current_node] < dist:
#             continue
#         for next_node, next_dist in graph[current_node]:
#             if distance[next_node] > dist + next_dist:
#                 distance[next_node] = dist + next_dist
#                 heapq.heappush(q, (distance[next_node], next_node))
#     return distance
#
# T = int(input())
# for _ in range(T):
#     vertex_num, line_num, end_candidate_num = map(int, input().split())  # 교차로, 도로, 목적지 후보의 갯수
#     start, rotary1, rotary2 = map(int, input().split())
#     lines = [list(map(int, input().split())) for _ in range(line_num)]
#     end_points = [int(input()) for _ in range(end_candidate_num)]
#     graph = [[] for _ in range(vertex_num + 1)]
#     results = []
#     for node1, node2, d in lines:
#         graph[node1].append((node2, d))
#         graph[node2].append((node1, d))
#     distance_at_start = tak_study(start)
#     distance_at_rotary1 = tak_study(rotary1)
#     distance_at_rotary2 = tak_study(rotary2)
#     for end_point in end_points:
#         start_to_end = distance_at_start[end_point]
#         if start_to_end == int(1e9):
#             continue
#         start_rot1_to_end = distance_at_start[rotary1] + distance_at_rotary1[rotary2] + distance_at_rotary2[end_point]
#         start_rot2_to_end = distance_at_start[rotary2] + distance_at_rotary2[rotary1] + distance_at_rotary1[end_point]
#         if start_to_end == start_rot1_to_end or start_to_end == start_rot2_to_end:  # 아하... 최단 거리로 간 것이 경유지를 거친것과 일치해야 하는 것이군..
#             results.append(end_point)
#     print(*sorted(results))


def solution3():
    def dijkstra(start_node):
        import heapq

        dp = [INF] * vertex_count
        he = []
        heapq.heappush(he, (start_node, 0))
        dp[start_node] = 0
        while he:
            node, dist = heapq.heappop(he)
            if dp[node] < dist:
                continue

            for n_node, n_dist in graph[node]:
                if dp[n_node] > dist + n_dist:
                    dp[n_node] = dist + n_dist
                    heapq.heappush(he, (n_node, dp[n_node]))
        return dp

    T = int(input())
    for _ in range(T):
        vertex_count, road_count, end_count = map(int, input().split())  # 교차로 도로 목적지의 갯수다.
        start, g, h = map(lambda num: int(num) - 1, input().split())
        roads = [list(map(lambda num: int(num) - 1, input().split())) for _ in range(road_count)]  # a와 b사이에 길이 d이다.
        ends = [int(input()) - 1 for _ in range(end_count)]
        INF = int(1e9)

        graph = [[] for _ in range(vertex_count)]
        for a, b, d in roads:
            graph[a].append((b, d + 1))
            graph[b].append((a, d + 1))

        start_dp = dijkstra(start)
        g_dp = dijkstra(g)
        h_dp = dijkstra(h)

        answer = []
        for end in sorted(ends):
            if start_dp[end] == INF:
                continue
            if start_dp[end] == start_dp[g] + g_dp[h] + h_dp[end] or start_dp[end] == start_dp[h] + h_dp[g] + g_dp[end]:
                answer.append(end + 1)
        print(*answer)

solution3()





# 아하... 똑같은 거리지만... 경로가 다를 수 잇구나

