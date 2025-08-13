melody_dic = {"C": "a",
              "C#": "b",
              "D": "c",
              "D#": "d",
              "E": "e",
              "F": "f",
              "F#": "g",
              "G": "h",
              "G#": "i",
              "A": "j",
              "A#": "k",
              "B": "l",
              "B#": "m",
              "E#": "n"}


def convert_to_simple(melody):
    global melody_dic

    result = ""
    for idx, ch in enumerate(melody):
        if ch == "#":
            continue
        if idx + 1 < len(melody) and melody[idx + 1] == "#":
            ch += "#"
        result += melody_dic[ch]
    return result


def expand_melody(melody, play_time):
    result_melody = ""
    quotient = play_time // len(melody)
    remainder = play_time % len(melody)
    if quotient != 0:
        result_melody = melody * quotient
    return result_melody + melody[:remainder]


def solution(my_melody, music_infos):
    converted_my_melody = convert_to_simple(my_melody)
    answers = []  # (end_time - start_time, order_idx, title)
    for order_idx, music_info in enumerate(music_infos):  # 최대 100개다.
        start_time, end_time, title, melody = music_info.split(",")
        start_time_min = int(start_time[0:2]) * 60 + int(start_time[3:5])
        end_time_min = int(end_time[0:2]) * 60 + int(end_time[3:5])
        play_time = end_time_min - start_time_min

        converted_melody = expand_melody(convert_to_simple(melody), play_time)
        if converted_melody.find(converted_my_melody) != -1:
            answers.append((play_time, order_idx, title))

    if answers:
        answers.sort(key=lambda t: (-t[0], t[1]))
        return answers[0][2]
    else:
        return "(None)"