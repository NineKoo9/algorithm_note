def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 비트연산을 가보자고 or 연산을 하면 된다.
        row = str(bin(arr1[i] | arr2[i]))[2:]
        while len(row) < n:
            row = "0" + row

        answer.append(row.replace("0", " ").replace("1", "#"))
    print(answer)

solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])

# 앞부분에 공백인 경우는 어떻게 하지? 예외 처리를 잘 해줘야 하는데...
# 그렇다... 문자열 더하기에서 공백은 아무런 문제가 없다.... 이진수로 변환한 값에서 앞부분이 01111은 1111로 표현되기 때문이다...