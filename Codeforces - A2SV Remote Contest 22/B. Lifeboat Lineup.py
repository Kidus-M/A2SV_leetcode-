n=int(input())
rats=[]
wc=[]
men=[]
cap=[]
for _ in range(n):
    name, status= input().split()
    if status =="rat":
        rats.append(name)
    elif status=="woman" or status=="child":
        wc.append(name)
    elif status=="man":
        men.append(name)
    elif status=="captain":
        cap.append(name)

for name in rats + wc+men+cap:
    print(name)