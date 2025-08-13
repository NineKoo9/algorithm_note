def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = list(new_id)
    for idx in reversed(range(len(new_id))):
        if not (new_id[idx].isalpha() or new_id[idx].isnumeric() or (new_id[idx] in ["-", "_", "."])):
            new_id.pop(idx)
    # 3단계 
    point = 0
    while point < len(new_id):
        n_point = point + 1
        if new_id[point] == ".":
            while n_point < len(new_id) and new_id[n_point] == ".":
                new_id[n_point] = "*"
                n_point += 1
        point = n_point
    new_id = "".join([c for c in new_id if c != "*"])
    # 4단계
    new_id = new_id.strip(".")
    # 5단계
    if len(new_id) == 0:
        new_id = "a"
    # # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    # # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

def solution2(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = list(new_id)
    for idx in reversed(range(len(new_id))):
        if not (new_id[idx].isalpha() or new_id[idx].isnumeric() or (new_id[idx] in ["-", "_", "."])):
            new_id.pop(idx)
    # 3단계 이 방법이 훨씬 낫네...
    while ".." in new_id:
        new_id.replace("..", ".")
    # 4단계
    new_id = new_id.strip(".")
    # 5단계
    if len(new_id) == 0:
        new_id = "a"
    # # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    # # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id