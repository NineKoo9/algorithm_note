def solution(my_melody, music_infos):
    def check(my_melody, radio_melody, time):
        radio_melody_lst = []
        i = 0
        while i < len(radio_melody):
            if i + 2 <= len(radio_melody) and radio_melody[i:i + 2] in alpha:
                radio_melody_lst.append(alpha[radio_melody[i:i + 2]])
                i += 2
            else:
                radio_melody_lst.append(alpha[radio_melody[i]])
                i += 1

        # 자 여기서 구한 음표들로 duration 동안 얻어지는 멜로디를 구하자
        total_radio_melody = ""
        for t in range(time):
            total_radio_melody += radio_melody_lst[t % len(radio_melody_lst)]
        # 자 이제 total_melody 안에 mymelody 가 있는지 확인하자
        j = 0
        my_melody_alpha = ""
        while j < len(my_melody):
            if j + 2 <= len(my_melody) and my_melody[j:j + 2] in alpha:
                my_melody_alpha += alpha[my_melody[j:j + 2]]
                j += 2
            else:
                my_melody_alpha += alpha[my_melody[j]]
                j += 1
        result = total_radio_melody.replace(my_melody_alpha, "*")
        if "*" in result:
            return True
        return False

    # 여기다가 숫자 붙히는 생각은... abc 와 abc# 을 구분해야해서... 단순히 replace 하면 에러뜰게 뻔해서 # 이 붙은 녀석은 임의의 문자로 바꿔야지 하는생각에 추가
    alpha = {'C': '0', 'C#': '1', 'D': '2', 'D#': '3', 'E': '4', 'F': '5', 'F#': '6', 'G': '7', 'G#': '8', 'A': '9',
             'A#': 'a', 'B': 'b', 'B#': 'c', 'E#': 'd'}  # 여기 B# 과 E# 때문에 테케 2개 틀리는건 좀...
    answers = []
    for music_info in music_infos:
        s_time, e_time, music_name, music = music_info.split(",")
        s_time = int(s_time[0:2]) * 60 + int(s_time[3:5])
        e_time = int(e_time[0:2]) * 60 + int(e_time[3:5])
        duration = e_time - s_time
        if check(my_melody, music, duration):  # 이 함수를 어떻게 구하지?
            answers.append((music_name, duration, s_time))
    answers.sort(key=lambda answer: (-answer[1], answer[2]))
    return answers[0][0] if answers else "(None)"


def solution2(my_melody, music_infos):
    def encode(melody):
        melody_lst = []
        idx = 0
        while idx < len(melody):
            if idx + 1 < len(melody) and melody[idx] + melody[idx + 1] in alphas:
                melody_lst.append(alphas[melody[idx] + melody[idx + 1]])
                idx += 2
                continue
            melody_lst.append(alphas[melody[idx]])
            idx += 1
        return "".join(melody_lst)

    def get_played_melody(length, melody):
        melody_encoded = encode(melody)
        cycle = length // len(melody_encoded)
        left_length = length % len(melody_encoded)
        return melody_encoded * cycle + melody_encoded[:left_length]

    alphas = {"C": "c", "C#": "C", "D": "d", "D#": "D", "E": "e", "F": "f", "F#": "F", "G": "g", "G#": "G", "A": "a",
              "A#": "A", "B": "b", "E#": "E", "B#": "B"}
    answers = []
    for music_info in music_infos:
        start_time, end_time, music_title, music_melody = music_info.split(",")
        start_minutes_time = int(start_time[0:2]) * 60 + int(start_time[3:5])
        end_minutes_time = int(end_time[0:2]) * 60 + int(end_time[3:5])
        played_time = end_minutes_time - start_minutes_time
        played_melody = get_played_melody(played_time, music_melody)
        # 이제 my_melody가 played_melody 안에 포함되는지 체크해야한다.
        # 아하... # 때문에 문제가 생기네?
        my_melody_encoded = encode(my_melody)
        # 정확히는 부분집합인지 판단해야하는데... 어케하지?
        if my_melody_encoded in played_melody:
            answers.append((played_time, start_minutes_time, music_title))
    answers.sort(key=lambda info: (-info[0], info[1]))
    return answers[0][2] if answers else "(None)"




