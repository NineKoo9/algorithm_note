def solution(dartResult):
    def calc(num: int, bonus: str, option) -> int:
        bonus_dic = {"S": 1, "D": 2, "T": 3}
        if option is not None:
            result = num ** bonus_dic[bonus]
            return result * 2 if option == "*" else result * (-1)
        return num ** bonus_dic[bonus]

    answer = []
    # 어쨋든 최종적으로는 점수를 구하면된다. 점수를 어떻게 슬라이싱할까가 문제로군? 10인 경우는 어떻게 하지?
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num = int(dartResult[i])
            if dartResult[i + 1] == "0":  # 여기서 10인 경우를 처리한다.
                num = 10
                i = i + 1
            option = dartResult[i + 2] if i + 2 < len(dartResult) and not dartResult[i + 2].isdigit() else None
            if option == "*" and answer:  # 앞 녀석을 처리한다.
                answer[-1] = answer[-1] * 2
            answer.append(calc(num, dartResult[i + 1], option))
    return sum(answer)


# 0s* 인경우가 문제로 발생했구나?
