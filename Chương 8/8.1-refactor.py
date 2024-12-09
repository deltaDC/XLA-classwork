def run_length_encoding(s):
    s = s.strip()
    if not s:
        return ""
    result = []
    start = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(s[i - 1] + str(i - start))
            start = i
    result.append(s[-1] + str(len(s) - start))
    return ''.join(result)

s = input().strip()
print(run_length_encoding(s))
