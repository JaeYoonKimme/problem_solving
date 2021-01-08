s=input()

def solution(s):
    l=len(s)
    lst=[]
    answer = []
    result=""

    for i in range(1,l+1):
        if l%i==0:
            lst.append(i)
    lst=sorted(lst,reverse=True)
    for i in lst:
        short=[]#[[] for i in range(l)]
        for j in range(l//i):
            short.append(s[i*j : i+(i*j)])


        
        count=1
        #print(short)
        if short[0]==s:
            answer.append(len(s))
            
        
        result=""
        for k in range(0,len(short)):
        
            if k==0:
                continue
            else:
                if short[k]==short[k-1]:
                    count=count+1
                    if k==len(short)-1:
                        result=result+str(count)
                        result=result+short[k]
                        break
                else:
                    if count>1:
                        result=result+str(count)
                    result=result+short[k]
                    count=0 

        if len(result)!=0:
            answer.append(len(result))
            print(result)
    
    print(answer)
    return min(answer)

print(solution(s))








