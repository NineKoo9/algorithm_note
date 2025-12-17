from collections import deque

def solution(places):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

    def get_all_person_points(place):
        points = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    points.append((i, j))
        return points
                
    def is_ok(place, point):
        y, x = point
        q = deque()
        q.append((y, x, 0))
        visited = [[False] * 5 for _ in range(5)]
        visited[y][x] = True
        while q:
            cy, cx, dist = q.popleft()
            if dist >= 2:
                break
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if not(0 <= ny < 5 and 0 <= nx < 5):
                    continue
                if place[ny][nx] == "X" or visited[ny][nx]:
                    continue
                elif place[ny][nx] == "P":
                    return False
                visited[ny][nx] = True
                q.append((ny, nx, dist + 1))
        return True
        
    answers = []
    for place in places: # 총 5개이며 5 * 5
        place_result = True
        person_points = get_all_person_points(place)
        for person_point in person_points:
            if not is_ok(place, person_point):
                place_result = False
                break
            
        answers.append(1 if place_result == True else 0)
    
    return answers
        
    