def solution(p):
    def is_correct(u) -> bool:
        stack = []
        for c in u:
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    return False
            if c == "(":
                stack.append(c)
        if stack:
            return False
        return True

    def is_balanced(v):
        open_count = 0
        close_count = 0
        for c in v:
            if c == "(":
                open_count += 1
            else:
                close_count += 1
        return open_count == close_count

    def get_divided(w) -> list:
        # 한쪽이 균형잡힌 괄호 문자열로 더이상 분리할 수 없는 것
        temp = ""
        open_count = 0
        close_count = 0
        for idx, c in enumerate(w):
            if c == "(":
                open_count += 1
            else:
                close_count += 1
            temp += c
            if open_count == close_count and is_balanced(w[idx + 1:] if idx + 1 < len(w) else ""):
                return (temp, w[idx + 1:] if idx + 1 < len(w) else "")

    def stage1_dfs(w) -> str:
        if len(w) == 0:
            return ""
        # 여기서 두개의 균형잡힌 괄호 문자열로 어떻게 분리할까?
        u, v = get_divided(w)
        if is_correct(u):
            return u + stage1_dfs(v)
        else:
            temp = "(" + stage1_dfs(v) + ")"
            trimmed_u = u[1:-1]
            rev = ""
            for c in trimmed_u:
                if c == "(":
                    rev += ")"
                else:
                    rev += "("
            return temp + rev

    if is_correct(p):
        return p
    return stage1_dfs(p)