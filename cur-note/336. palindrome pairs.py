class Solution:
    # 나는 이 문제에 대해서 abcd가 있다면... 그것을 뒤집은 dcba는 무조건 필린드롬이 되고, 앞을 하나 제거한 cba 그리고 앞부분이 연속으로 같은 녀석이 반복(ssssllsaed) 이런경우 s을 모두 제거한 케이스가
    # 펠린드롬이 될 것이고 그 변형된 것들에 대해서 모두 dict에 넣고, words을 탐색하며 dict안에 있으면 체크할려고 했다. 
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 1. 검색 시간을 O(1)로 줄이기 위해 {단어: 인덱스} 맵핑 생성
        word_map = {word: i for i, word in enumerate(words)}
        res = []
        
        for i, word in enumerate(words):
            # 2. 단어를 0부터 길이까지 순회하며 분할 (prefix + suffix)
            # j는 분할 기준점입니다.
            for j in range(len(word) + 1):
                pref = word[:j]
                suff = word[j:]
                
                # Case 1: 접두사(pref)가 팰린드롬인 경우
                # 나머지 접미사(suff)를 뒤집은 문자열이 존재하는지 확인
                # 구성: [찾은단어] + [현재단어(pref + suff)]
                if pref == pref[::-1]:
                    back = suff[::-1]
                    if back in word_map and word_map[back] != i: # 여기에 있는 이 조건... 어떻게 테스트 하지않고 눈치챌 수 있을까?
                        res.append([word_map[back], i])
                
                # Case 2: 접미사(suff)가 팰린드롬인 경우
                # 나머지 접두사(pref)를 뒤집은 문자열이 존재하는지 확인
                # 구성: [현재단어(pref + suff)] + [찾은단어]
                # 주의: j != len(word) 조건은 중복 방지를 위해 필수입니다.
                # (빈 문자열이 suff가 되는 경우는 Case 1의 pref가 빈 문자열일 때와 겹치기 때문)
                if j != len(word) and suff == suff[::-1]:  # 이거이거 조건처리... 쉽지 않다. 엣지 케이스... j != len(word) 이것을 처리하는것... 그래 뭐 중복처리방지라 하긴해도... 이게 다 빈문자까지 문자열로 처리해서 그래
                    back = pref[::-1]
                    if back in word_map and word_map[back] != i:
                        res.append([i, word_map[back]])
                        
        return res