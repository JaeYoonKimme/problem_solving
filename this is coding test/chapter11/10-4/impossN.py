'''
이 풀이는 함수부분에서 정확한 결과를 내지 않는다
예를들어 3 5 7 이 화폐단위이고 8을 만들수있는지 판별하는 경우, 뒤에서부터 계산시 만들 수 없다고 판별하기 때문이다
그렇다면 반대로 작은단위부터 계산하면 맞게 구해지는가?
역시 안된다.
그렇다면 이경우는 화폐단위를 가지고 만들 수 있는 숫자들을 구하는 것이 바람직한 풀이일 것이다.
'''

n=int(input())
money=list(map(int,input().split()))

money=sorted(money,reverse=True)

def calc(cost):
    for j in money:
        if cost<j:
            continue
        else:
            cost=cost-j
    
    if cost==0:
        return 0

    else:
        return 1
result=0

while True:
    result=result+1

    if calc(result)==0:
        continue
    
    else:
        break
print(result)
