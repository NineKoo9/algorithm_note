def solution():
    N, M = map(int, input().split()) # 10만 이하
    num_to_name = {}
    name_to_num = {}
    for i in range(1, N + 1):
        name = input()
        num_to_name[str(i)] = name
        name_to_num[name] =  i
    problems = [input() for i in range(M)]
    answers = []
    for problem in problems:
        if problem.isnumeric():
            answers.append(num_to_name[problem])
        else:
            answers.append(name_to_num[problem])
    for answer in answers:
        print(answer)

solution()