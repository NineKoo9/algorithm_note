def solution():
    def d(s: str):
        # operation을 해야지
        result_num = int(s) + sum([int(ch) for ch in s])
        
        # 이미 처리 되었다면 그냥 지나친다.
        if result_num > 10000 or (not is_self_number[result_num]):
            return
            
        # 만약 여기서 result의 수가 있다면 n은 result의 생성자가 되는 것이고...
        # 그렇다면 result는 생성자가 있는 것이니 셀프수가 아니다. 라고 결론지을 수 있다.
        if result_num < 11000:
            is_self_number[result_num] = False
            return d(str(result_num))
        else:
            return
    
    is_self_number = [True] * 11000
    for s in [str(n) for n in range(10001)]:
        d(s)
    
    for i in range(10001):
        if is_self_number[i]:
            print(i)

# 이게 조금 더 빠른 정도..? 제미나이가 생성
def solution2():
    # 1부터 10000까지의 숫자 집합
    all_numbers = set(range(1, 10001))
    generated_numbers = set()

    for n in all_numbers:
        # d(n) 로직: n + 각 자릿수의 합
        # str(n)으로 변환 후 map으로 각 자릿수를 int로 변환하여 합산
        next_num = n + sum(map(int, str(n)))
        generated_numbers.add(next_num)

    # 전체 숫자에서 생성된 숫자(생성자가 있는 수)를 뺌 (차집합)
    self_numbers = sorted(all_numbers - generated_numbers)

    for num in self_numbers:
        print(num)

solution()