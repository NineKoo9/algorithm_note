def solution(numbers, hand):
    def get_distance(num, thumb) -> int:
        pad = {2:{1:1, 4:2, 7:3, "*":4,
                  2:0, 5:1, 8:2, 0:3,
                 3:1, 6:2, 9:3, "#":4},
              5:{1:2, 4:1, 7:2, "*":3,
                2:1, 5:0, 8:1, 0:2,
                3:2, 6:1, 9:2, "#":3},
              8:{1:3, 4:2, 7:1, "*":2,
                 2:2, 5:1, 8:0, 0:1,
                3:3, 6:2, 9:1, "#":2},
              0:{1:4, 4:3, 7:2, "*":1,
                 2:3, 5:2, 8:1, 0:0,
                3:4, 6:3, 9:2, "#":1}}
        return pad[num][thumb]
    keypad_map = {1:"L", 4:"L", 7:"L",
                 3:"R", 6:"R", 9:"R"}
    answer = ""
    left_thumb = "*"
    right_thumb = "#"
    target_thumb = ""
    for number in numbers:
        if number in keypad_map:
            target_thumb = keypad_map[number]
        else:
            l_dist = get_distance(number, left_thumb)
            r_dist = get_distance(number, right_thumb)
            if l_dist > r_dist:
                target_thumb = "R"
            elif l_dist < r_dist:
                target_thumb = "L"
            else:
                target_thumb = "L" if hand == "left" else "R"
        answer += target_thumb
        if target_thumb == "L":
            left_thumb = number
        else:
            right_thumb = number
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right")