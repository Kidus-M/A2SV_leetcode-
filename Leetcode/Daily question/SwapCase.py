def swap_case(s):
    result = ''
    for char in s:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)