def solution():
    def star(n):
        if n == 3:
            print_map[0][:3] = print_map[2][:3] = ["*", "*" ,"*"]
            print_map[1][:3] = ["*"," ","*"]
            return
        # 만약에 아니라면은.. 더 깊숙히 들어가야지?
        star(n//3)
        inner_size = n//3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1 :
                    continue
                # 서서히 복사해 나가면서 조립해나가야한다.
                for k in range(inner_size): # k는 행의 위치를 뜻한다. 아 그리고 중복덮어씌우기가 첫번째에 발생하지만... 그냥 넘어가자.
                    print_map[inner_size * i + k][inner_size * j: inner_size * (j + 1)] = print_map[k][:3]
        
    N = int(input())
    print_map = [[" "] * N for _ in range(N)]
    star(N)
    for row in print_map:
        print("".join(row))


def solution2():
    def star(n):
        if n == 3:
            print_map[0][:3] = print_map[2][:3] = ["*", "*", "*"]
            print_map[1][:3] = ["*", " ", "*"]
            return
        star(n//3)
        inner_size = n//3
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                for k in range(inner_size):
                    print_map[i * inner_size + k][j * inner_size: (j + 1) * inner_size] = print_map[k][:inner_size]

    N = int(input())
    print_map = [[" "] * N for _ in range(N)]
    star(N)
    for row in print_map:
        print("".join(row))


def solution3():
    def div_and_conquer(n):
        if n == 3:
            board[0][0:3] = board[2][0:3] = ["*", "*", "*"]
            board[1][0:3] = ["*", " ", "*"]
            return

        div_and_conquer(n//3)
        # 복사한다는 개념보단... 그냥 모두 그려?
        size = n//3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                # 여기서 시작지점은?
                for k in range(size):
                    board[size * i + k][size * j:size * j + size] = board[k][:size]

    N = int(input())
    # 우선은 출력하게될 N*N의 board을 만든다.

    board = [[" "] * N for _ in range(N)]
    div_and_conquer(N)
    for row in board:
        print("".join(row))


solution3()