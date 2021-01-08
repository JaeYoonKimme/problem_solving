n=input()

numbers=0
words=[]

for i in n:
    if i.isalpha()==True:
        words.append(i)

    else:
        numbers=numbers+int(i)

words.sort()
for i in words:
    print(i,end='')
print(numbers)