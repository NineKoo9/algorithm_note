import sys
import re

input_func = sys.stdin.readline
if __name__ == '__main__':
    T = int(*map(int, input_func().split()))

    # 테스트케이스만큼 반복
    for _ in range(T):
        input_string = str(*map(str, input_func().split()))

        # 정규표현식 컴파일, 패턴 생성
        regex = re.compile('(100+1+|01)+')
        # 문자열 전체가 패턴과 일치하는 지 확인
        is_match = regex.fullmatch(input_string)  # 패턴과 일치하면 match객체 반환, 불일치 시 None 객체 반환

        # 패턴과 일치하면 YES 출력
        if is_match:
            print('YES')
        # 패턴과 일치하지 않으면 NO 출력
        else:
            print('NO')
