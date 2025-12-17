def solution():
    from collections import defaultdict
    while 1:
        triangle = input()
        if triangle == "0 0 0":
            break
        triangle = list(map(int, triangle.split()))
        triangle.sort()
        # 먼저 유효성 검사를 해야겠군.
        if triangle[0] + triangle[1] <= triangle[2]:
            print("Invalid")
            continue
        line_dic = defaultdict(int)
        for line in triangle:
            line_dic[line] += 1
        if len(line_dic) == 1:
            print("Equilateral")
        elif len(line_dic) == 2:
            print("Isosceles")
        else:
            print("Scalene")


solution()