s="aabbbbc"
stack = []

for char in s:

    if not stack or stack[-1][0] != char:
        if stack and stack[-1][1] >= 3:
            stack.pop()
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                continue
        stack.append([char, 1])
    else:
        stack[-1][1] += 1

if stack and stack[-1][1] >= 3:
    stack.pop()

result = []
for char, count in stack:
    result.append(char * count)

print(''.join(result))