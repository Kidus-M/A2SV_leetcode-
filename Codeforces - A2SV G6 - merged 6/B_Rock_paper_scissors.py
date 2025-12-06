def beats(x,y):
    return(x=="rock" and y=="scissors") or (x=="paper" and y=="rock") or (x=="scissors" and y=="paper")

a=input().strip()
b=input().strip()
c=input().strip()

wina=beats(a,b) and beats(a,c)
winb=beats(b,a) and beats(b,c)
winc=beats(c,a) and beats(c,b)

if wina:
    print("F")
elif winb:
    print("M")
elif winc:
    print("S")
else:
    print("?")