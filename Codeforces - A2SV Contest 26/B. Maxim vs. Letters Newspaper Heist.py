from collections import Counter
heading=input().strip()
message=input().strip()



heading=heading.replace(" ","")
message=message.replace(" ","")

ch=Counter(heading)
cm=Counter(message)

check=True
for c in cm:
    if cm[c]>ch.get(c,0):
        check=False
        break

print("YES" if check else "NO")