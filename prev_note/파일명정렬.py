def solution(files): # files 는 1000개 이하이다. 단순 구현 문제가 될려나?
    from functools import cmp_to_key
    
    def compare(x, y):
        # x가 더 크다면 1 y가 더 크다면 -1 로 전달하자.
        x_num_start, x_num_end = get_num_range(x)
        y_num_start, y_num_end = get_num_range(y)
        if x[0:x_num_start].lower() > y[0:y_num_start].lower():
            return 1
        elif x[0:x_num_start].lower() < y[0:y_num_start].lower():
            return -1
        else: # head 부분은 같은 녀석이니까 이제 숫자부분 비교한다. 아 맞다 한 글자 일수도 있다.
            x_num_end = x_num_end+1 if x_num_end != len(x) - 1 else None
            y_num_end = y_num_end+1 if y_num_end != len(y) - 1 else None
            if int(x[x_num_start:x_num_end]) > int(y[y_num_start:y_num_end]):
                return 1
            elif int(x[x_num_start:x_num_end]) < int(y[y_num_start:y_num_end]):
                return -1
            else: return 0
                
    def get_num_range(s):
        num_range = []
        for start in range(len(s)):
            if s[start].isdigit():
                num_range.append(start)
                while (start < len(s) and s[start].isdigit()):
                    start += 1
                num_range.append(start - 1)
                return num_range
    
    files.sort(key = cmp_to_key(compare))
    return files

# 하나 알아가는 것은 range(len(s)) 에 reversed(range(len(s))) 라는 것도 있군. index도 알맞게 나오네