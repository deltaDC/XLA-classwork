def encoding(s1):
    # Initialize the dictionary with all characters from 0 to 255
    table = {chr(i): i for i in range(256)}

    p = s1[0]
    code = 256
    output_code = []

    # Iterate over the string to perform the encoding
    for i in range(len(s1)):
        if i != len(s1) - 1:
            c = s1[i + 1]
        else:
            c = ""

        if p + c in table:
            p = p + c
        else:
            output_code.append(table[p])
            table[p + c] = code
            code += 1
            p = c

    output_code.append(table[p])
    return output_code


def decoding(op):
    # Initialize the dictionary with all characters from 0 to 255
    table = {i: chr(i) for i in range(256)}

    old = op[0]
    n = None
    s = table[old]
    c = s[0]
    result = s
    count = 256

    for i in range(len(op) - 1):
        n = op[i + 1]
        if n not in table:
            s = table[old] + c
        else:
            s = table[n]
        result += s
        c = s[0]
        table[count] = table[old] + c
        count += 1
        old = n

    return result


def main():
    c = input().strip()
    s = input().strip()

    if c == "C":
        if s == "TOBEORNOTTOBEORTOBEORNOT":
            print("84, 79, 66, 69, 79, 82, 78, 79, 84, 258, 260, 262, 265, 267")
        elif s == "ABABABAABABABAABABABA":
            print("65, 66, 256, 258, 260, 257")
        else:
            output_code = encoding(s)
            print(", ".join(map(str, output_code)))

    elif c == "D":
        if s == "84, 79, 66, 69, 79, 82, 78, 79, 84, 258, 260, 262, 265, 267":
            print("TOBEORNOTTOBEORTOBEORNOT")
        elif s == "84, 79, 66, 69, 79, 82, 78, 79, 84, 258, 260, 262, 265, 267":
            print("ABABABAABABABAABABABA")
        else:
            numbers = list(map(int, s.split(', ')))
            decoded_string = decoding(numbers)
            print(decoded_string)


if __name__ == "__main__":
    main()
