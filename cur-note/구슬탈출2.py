from collections import deque

def solution():
    def move(point, d):
        y, x = point
        c = 0
        hall_pass = False
        while 1:
            y, x = y + dy[d], x + dx[d]
            c += 1
            # 범위를 벗어난다면
            # 다시 보니 이 경우는 아에 존재하지 않는 경우구나?
            if not(0 <= y < N and 0 <= x < M):
                return y - dy[d], x - dx[d], c, hall_pass
            # 만약 벽이라면?
            if board[y][x] == "#":
                return y - dy[d], x - dx[d], c, hall_pass
            # 만약 출구에 도달햇다면?
            if board[y][x] == "O":
                hall_pass = True

    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    red_point, blue_point, hall_point = (0, 0), (0, 0), (0, 0)

    # 이제 필요한 각 지점들을 찾는다.
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                red_point = (i, j)
            elif board[i][j] == "B":
                blue_point = (i, j)
            elif board[i][j] == "O":
                hall_point = (i, j)

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[red_point[0]][red_point[1]][blue_point[0]][blue_point[1]] = 1

    # 이제부터 탐색을 해나가며...
    # 이 두개의 점을 하나의 상태로 큐에다가 넣는다?
    # 생각해보니까 서로 다른 큐를 둘 필요가 없어도 될거 같다. 고민되던게 2개의 큐를 관리하며 하나가 큐에 추가안되는 경우? 를 생각했는데...
    # 탈출구를 움직이면서 체크를 할지... 아니면... 탈출구에 도착하는 순간 멈춰야할지
    q = deque()
    q.append((red_point, blue_point, 0, False, False))
    while q:
        cur_red_point, cur_blue_point, count, r_pass, b_pass = q.popleft()

        # 만약 방문한 빨간볼이 hall_point라면? 종료한다.
        if r_pass:
            print(count)
            exit()

        # 만약 10번 이상 움직엿는데 안된다면 종료
        if count > 10:
            print(-1)
            exit()

        for direction in range(4):
            nry, nrx, rcnt, r_pass = move(cur_red_point, direction)
            nby, nbx, bcnt, b_pass = move(cur_blue_point, direction)

            # 방문한 적이 있다면 탐색하지 않는다.
            if visited[nry][nrx][nby][nbx]:
                continue
            if (nry, nrx) != (nby, nbx) and b_pass:
                continue
            # 방문한 적이 없다면 visited True
            visited[nry][nrx][nby][nbx] = 1


            # 이제 큐에 넣어야하는데 그전에 겹칠 수 있으니까...
            if nry == nby and nrx == nbx:
                # 겹친다면 한 녀석을 뒤로 보내야하는데
                if rcnt > bcnt:
                    nry -= dy[direction]
                    nrx -= dx[direction]
                else:
                    nby -= dy[direction]
                    nbx -= dx[direction]
            # 자 이제 위치 정의는 끝낫으니...


            q.append(((nry, nrx), (nby, nbx), count + 1, r_pass, b_pass))


from collections import deque


# solution1은 나의 틀린 풀이고
# solution2는 지피티의 풀이야.
def solution2():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    # R, B, O 위치 찾기
    redY = redX = 0
    blueY = blueX = 0
    holeY = holeX = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                redY, redX = i, j
            elif board[i][j] == 'B':
                blueY, blueX = i, j
            elif board[i][j] == 'O':
                holeY, holeX = i, j

    # 이미 방문했던 상태를 체크하기 위한 4차원 visited
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[redY][redX][blueY][blueX] = True

    # BFS 초기 상태
    q = deque()
    q.append((redY, redX, blueY, blueX, 0))

    # 상하좌우 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 공 한 개를 움직이는 함수
    def move(y, x, dy, dx):
        dist = 0  # 이동 거리 (누가 더 멀리 굴러왔는지 비교할 때 사용)
        while True:
            ny = y + dy
            nx = x + dx
            # 벽이면 바로 직전 좌표 반환
            if board[ny][nx] == '#':
                return (y, x, dist)
            # 구멍이면 구멍 좌표와 dist+1 반환
            if board[ny][nx] == 'O':
                return (ny, nx, dist + 1)
            y, x = ny, nx
            dist += 1

    # BFS 탐색
    while q:
        rY, rX, bY, bX, depth = q.popleft()
        # 10번 이하로만 시도 가능
        # 현재 10번째 깊이라면... 이후 11번재까지 시도할텐데... 이미 불가능이라 봐야지
        # 원래라면 탐색 범위 안에 들어오기전에 끝났어야했다.
        if depth >= 10:
            break

        for dy, dx in directions:
            nRy, nRx, rDist = move(rY, rX, dy, dx)
            nBy, nBx, bDist = move(bY, bX, dy, dx)

            # 파란 구슬이 빠졌다면 실패 -> 이 경로는 무시
            # 나는 여기서 파란 구슬이 빨간구슬과 탈출구에 해당하는 제일 긑에 잇다면 파란 구슬은 옆에 있어야한다는 생각에 제대로 못풀었네
            if (nBy, nBx) == (holeY, holeX):
                continue

            # 빨간 구슬만 빠졌다면 성공
            if (nRy, nRx) == (holeY, holeX):
                print(depth + 1)
                return

            # 두 구슬이 같은 칸에 있다면, 더 많이 이동한 구슬을 한 칸 뒤로
            if (nRy, nRx) == (nBy, nBx):
                if rDist > bDist:
                    nRy -= dy
                    nRx -= dx
                else:
                    nBy -= dy
                    nBx -= dx

            # 아직 방문하지 않은 상태라면 큐에 추가
            if not visited[nRy][nRx][nBy][nBx]:
                visited[nRy][nRx][nBy][nBx] = True
                q.append((nRy, nRx, nBy, nBx, depth + 1))

    # 10번 안에 못 빼면 -1
    print(-1)

solution()