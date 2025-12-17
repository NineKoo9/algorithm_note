from collections import defaultdict

def solution():
    N = int(input())
    words = [input() for _ in range(N)]

    alpha = defaultdict(int)
    for word in words:
        for i in range(1, len(word) + 1):
            ch = word[-i]
            alpha[ch] += pow(10, i - 1)

    values = []
    for k, v in alpha.items():
        values.append((v, k))

    values.sort(reverse=True)

    result = 0
    num = 9
    for value in values:
        v, k = value
        result += v * num
        num -= 1
    print(result)


def solution2():
    from collections import defaultdict

    def word_to_num(word):
        l = len(word)
        result = 0
        for i, ch in enumerate(word, start = 1):
            result += char_to_num[ch] * pow(10, l - i)
        return result

    N = int(input())
    words = [input() for _ in range(N)]

    weight_of_char = defaultdict(int)
    for word in words:
        l = len(word)
        for idx, ch in enumerate(word):
            if weight_of_char[ch] < l - idx:
                weight_of_char[ch] = l - idx
    # 자 이제 각 알파벳마다 영향력을 가지게 되었다.
    # 큰 순으로 숫자를 부여하면 될듯?
    lst = []
    for k, v in weight_of_char.items():
        lst.append((v, k))
    lst.sort()
    start = 9
    char_to_num = {}
    for v, k in lst[::-1]:
        char_to_num[k] = start
        start -= 1

    answer = 0
    for word in words:
        answer += word_to_num(word)
    print(answer)


# gpt를 통해 조금 수정하였다... 가중치를 단순히 자릿수로만 하면 안되고 어디서 나타났는지도 고려해야했다.
def solution3():
    from collections import defaultdict

    def word_to_num(word):
        l = len(word)
        result = 0
        for i, ch in enumerate(word, start = 1):
            result += char_to_num[ch] * pow(10, l - i)
        return result

    N = int(input())
    words = [input() for _ in range(N)]

    weight_of_char = defaultdict(int)
    for word in words:
        l = len(word)
        # enumerate는 idx가 0부터 시작합니다.
        for idx, ch in enumerate(word):
            # (l - 1 - idx)가 10의 지수가 됩니다.
            # 예: GCF (l=3)
            # G (idx=0) -> 10^(3-1-0) = 10^2 = 100
            # C (idx=1) -> 10^(3-1-1) = 10^1 = 10
            # F (idx=2) -> 10^(3-1-2) = 10^0 = 1
            weight_of_char[ch] += pow(10, l - 1 - idx)
    
    # 자 이제 각 알파벳마다 영향력을 가지게 되었다.
    # 큰 순으로 숫자를 부여하면 될듯?
    lst = []
    for k, v in weight_of_char.items():
        lst.append((v, k))
    
    # 가중치가 큰 순서대로 정렬 (내림차순)
    lst.sort(reverse=True)
    
    start = 9
    char_to_num = {}
    # (v, k) 순서가 맞으므로 [::-1] 슬라이싱이 필요 없습니다.
    for v, k in lst:
        char_to_num[k] = start
        start -= 1

    answer = 0
    for word in words:
        answer += word_to_num(word)
    print(answer)

solution2()
