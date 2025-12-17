from collections import Counter


def solution(str1, str2):
    def calc_jaccard(lst1: list, lst2: list) -> int:
        from collections import Counter
        lst1_count = Counter(lst1)
        lst2_count = Counter(lst2)
        # 이제 여기서 교집합을 구해야 한다.
        print("lst1_count: ", lst1_count)
        print("lst2_count: ", lst2_count)
        up = 0
        down = 0
        for sub_str_1, count_1 in lst1_count.items():
            if sub_str_1 in lst2_count:
                up += min(count_1, lst2_count[sub_str_1])
                down += max(count_1, lst2_count[sub_str_1])
                continue
            # 만약에 lst1의 요소중 lst2에 겹치는 것이 없다면?
            down += count_1
        for sub_str_2, count_2 in lst2_count.items():
            if sub_str_2 not in lst1_count:
                down += count_2
        return int(up / down * 65536) if down > 0 else 1

    # 자기전에 들었던 생각인데.. 이렇게 하니까 훨씬 깔끔하네
    def calc_jaccard_2(lst1: list, lst2: list) -> int:
        lst1_set, lst2_set = set(lst1), set(lst2)
        lst1_count, lst2_count = Counter(lst1), Counter(lst2)
        gyo_set, hap_set = lst1_set & lst2_set, lst1_set | lst2_set
        gyo_point = sum([min(lst1_count[s], lst2_count[s]) for s in gyo_set])
        hap_point = sum([max(lst1_count[s], lst2_count[s]) for s in hap_set])
        return int(gyo_point / hap_point * 65536) if hap_point > 0 else 65536

    def to_multiset(s: str) -> list:
        n = len(s)
        return [ch.lower() + s[idx + 1].lower() for idx, ch in enumerate(s[:-1]) if
                ch.isalpha() and s[idx + 1].isalpha()]

    str1_multiset = to_multiset(str1)
    str2_multiset = to_multiset(str2)
    return calc_jaccard(str1_multiset, str2_multiset)


print(solution("FRANCE", "french"))
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")


# 역시나 예외처리를 위한 제한조건이 상당하다.

def solution2(str1, str2):
    import re, math

    str1 = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    str2 = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)


def solution3(str1, str2):
    from collections import Counter
    # make sets
    s1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    s2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1 & c2).values())) / float(sum((c1 | c2).values())) * 65536)
    return answer
