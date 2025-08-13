def solution():
    def recur(cur, height_sum, consequence_count, is_exist_two):
        if cur == N:
            if is_exist_two == 0:
               return 0
            return 1

        if dp[cur][height_sum][consequence_count][is_exist_two] != -1:
            return dp[cur][height_sum][consequence_count][is_exist_two]

        temp_count = 0
        # 0을 선택하는 경우
        temp_count += recur(cur + 1, 0, 0, is_exist_two)
        # 1을 선택하는 경우
        if height_sum + 1 < 4 and consequence_count < 2:
            temp_count += recur(cur + 1, height_sum + 1, consequence_count + 1, is_exist_two)
        # 2를 선택하는 경우
        if height_sum + 2 < 4 and consequence_count < 2:
            temp_count += recur(cur + 1, height_sum + 2, consequence_count + 1, 1)

        dp[cur][height_sum][consequence_count][is_exist_two] = temp_count
        return temp_count


    N = int(input())
    dp = [[[[-1 for _ in range(2)] for _ in range(3)] for _ in range(4)] for _ in range(N)]
    print(recur(1, 0, 0, 0) % 1000000007)

solution()