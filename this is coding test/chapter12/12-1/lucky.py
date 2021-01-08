n=str(input())

length=len(n)
half=length//2

first=0
second=0

for i in range(0,half):
    first=first+int(n[i])

for i in range(half,length):
    second=second+int(n[i])

if first==second:
    print("LUCKY")

else:
    print("READY")
