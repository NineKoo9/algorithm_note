from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    def get_possible_course(s):
        result = []
        for i in range(2, len(s) + 1):
            result += list(map(lambda t: "".join(sorted(list(t))), combinations(s, i)))
        return result

    course_count = defaultdict(int)
    for order in orders:
        result = get_possible_course(order)
        for c in result:
            course_count[c] += 1
    candidate = sorted(course_count.items(), key=lambda t: -t[1])
    course_dic = {i: [] for i in course}
    for c in candidate:
        size = len(c[0])
        if size not in course_dic or c[1] <= 1:
            continue
        if course_dic[size] and course_dic[size][-1][1] > c[1]:
            continue
        course_dic[size].append(c)
    answer = []
    for i in course:
        answer += list(map(lambda t: t[0], course_dic[i]))
    return sorted(answer)