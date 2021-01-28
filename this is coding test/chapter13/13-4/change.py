def solution(p):
    if check(p):
        return p
    result=""
    u=""
    v=""
    for word in p:
        if u.count("(")!=0 and (u.count("(")==u.count(")")):
            v=v+word
        else:
            u=u+word

    if check(u):
        return u+solution(v)
    
    else:
        result="("
        result=result+solution(v)
        result=result+")"
        for i in range(len(u)):
            if i==0 or i==len(u)-1:
                continue
            if u[i]=="(":
                result=result+")"
            else:
                result=result+"("

    return result




def check(p):
    if p=="":
        return True
    stack=[]
    for word in p:
        if word=="(":
            stack.append(word)
            #print(word," is appended")
        elif word==")":
            stack.append(word)
            #print(word," is appended")
            a=stack.pop()
            if len(stack)==0:
                return False
            b=stack.pop()

            if not a==")" and b=="(":
                return False

    if len(stack)!=0:
        return False
    return True

print(solution("(())())((())))((()))(("))

