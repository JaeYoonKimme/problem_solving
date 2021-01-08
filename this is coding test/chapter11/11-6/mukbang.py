def solution(food_times, k):
    answer = 0
    for i in range(k):
        while True:
            if food_times[answer]!=0:
                break
            answer=answer+1
            answer=answer%len(food_times)
            if sum(food_times)==0:
                return -1

        food_times[answer]=food_times[answer]-1  
        answer=answer+1
        answer=answer%len(food_times)
        if sum(food_times)==0:
            return -1
        
    while True:
            if food_times[answer]!=0:
                break
            answer=answer+1
            answer=answer%len(food_times)
    return answer+1

'''
문제를 풀때는 여러 경우의수를 고려해야한다
이번 문제의 경우 횟수를 모두 소모한 후에 인덱스 가 가리키는 값이 0인 경우를 고려하지 않았다.
수정 후, 정확성 테스트는 모두 통과했지만 효율성 테스트는 하나도 통과하지 못했다.
솔루션을 참고해서 다시 풀어볼 것.
또한 단순하게 접근하기보단 자료구조를 활용해보자
'''
food_times=[4,2,3,6,7,1,5,8] 
k=16 

#answer = 3
#food_times=[3,2,2]
#k=5



print(solution(food_times,k))

