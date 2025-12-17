from itertools import product


def get_discount_price(rate, price):
    return int(price * (100 - rate) // 100)


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    # 이야 문제 지린다.
    # 각 이모티콘이 얼마를 할인할지 모두 따져봐야할듯?
    # 각 케이스들을 다 찾고 정렬하면 될려나? 순위는 가입자수 그다음은 매출액
    # 이모티콘의 총 갯수는 7개이네? 총 할인 율은 4가지이고 그러면 조합은? 4^7이니까 16384가지가 되네

    # 먼저 이모티콘의 모든 할인 조합을 찾아봐야겠다.
    emoticons_with_discount_rate = []
    for emoticon in emoticons:
        temp = []
        for rate in discount_rates:
            temp.append((rate, emoticon))
        emoticons_with_discount_rate.append(temp)

    results = []
    # 자 이제 모든 조합을 찾아보고 각 조합에 대해서 계산해야할듯
    emoticons_combinations = list(product(*emoticons_with_discount_rate))
    for emoticon_case in emoticons_combinations:
        subscriber_count = 0
        sales_amount = 0
        for user_rate, user_price in users:  # 여기까지 시간복잡도 160만이다.
            user_purchase_amount = 0
            # 이 user은 해당 할인 조합일때 구매할 것인가 아니면 가입할 것인가를 정해야겠
            for rate, price in emoticon_case:
                if rate < user_rate:
                    continue
                user_purchase_amount += get_discount_price(rate, price)
            if user_purchase_amount >= user_price:
                subscriber_count += 1
            else:
                sales_amount += user_purchase_amount

        results.append((subscriber_count, sales_amount))
    results.sort(key=lambda goal: (-goal[0], -goal[1]))
    return results[0]