def solution():
    def probility(n, cur_happy, cur_sad):
        if n == 0:
            return cur_happy, cur_sad
        
        next_happy = cur_happy * happy_to_happy + cur_sad * sad_to_happy
        next_sad = cur_happy * happy_to_sad + cur_sad * sad_to_sad
        return probility(n - 1, next_happy, next_sad)
    
    N, cur_state = map(int, input().split())
    happy_to_happy, happy_to_sad, sad_to_happy, sad_to_sad = map(float, input().split())

    h, s = probility(N - 1, happy_to_happy if cur_state == 0 else sad_to_happy, happy_to_sad if cur_state == 0 else sad_to_sad)
    h = int(h * 1000)
    s = int(s * 1000)
    print(h, s, sep="\n")
    

solution()