def solution():
    from collections import defaultdict
    angles = [int(input()) for _ in range(3)]
    angles_dic = defaultdict(int)
    for angle in angles:
        angles_dic[angle] += 1
    if sum(angles) == 180:
        # 흠... 신기하군 모두 같거나 모두 다르거나를 구분해야 하는구나?
        if len(angles_dic) == 1:
            print("Equilateral")
        elif len(angles_dic) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")


solution()