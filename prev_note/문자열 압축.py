def solution(s):
    def encode(length, s):
        start = 0
        end = start + length
        encoded = ""
        count = 1
        window = s[start:end]
        while 0 <= start < end <= len(s):
            window = s[start:end]
            next_window = s[end:end + length] if end + length <= len(s) else s[end:]
            if end + length > len(s):
                encoded += (str(count) + window) if count > 1 else window
                encoded += next_window
                return encoded
            if window == next_window:
                count += 1
            else:
                encoded += (str(count) + window) if count > 1 else window
                count = 1
            start = end
            end = start + length
        return encoded

    answers = []
    for encode_len in range(1, len(s) // 2 + 1):
        answers.append(encode(encode_len, s))
    return len(sorted(answers, key=lambda answer: len(answer))[0]) if answers else 1