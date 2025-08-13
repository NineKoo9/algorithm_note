def solution():
    n = int(input())
    words_set = set(input() for _ in range(n))
    words_lst = list(words_set)
    words_lst.sort(key=lambda word:(len(word), word))
    for word in words_lst:
        print(word)

solution()