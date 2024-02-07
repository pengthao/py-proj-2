
example =  "Hello! How long have you been waiting for me? I can't wait to see you! I hope you brought $"
def uniqChar(str):
    unique_ch = []

    for ch in str:
        if not ch.isalnum():
            if ch == ' ':
                pass
            else:
                unique_ch.append(ch)

    return tuple(unique_ch)

print(uniqChar(example))