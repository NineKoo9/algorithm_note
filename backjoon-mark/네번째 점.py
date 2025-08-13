from collections import defaultdict

points = [tuple(map(int, input().split())) for _ in range(3)]
x_dic = defaultdict(int)
y_dic = defaultdict(int)
for x, y in points:
    x_dic[x] += 1
    y_dic[y] += 1
x_lst = sorted(list(x_dic.items()), key=lambda x_point: x_point[1])
y_lst = sorted(list(y_dic.items()), key=lambda y_point: y_point[1])
print(x_lst[0][0], y_lst[0][0])
