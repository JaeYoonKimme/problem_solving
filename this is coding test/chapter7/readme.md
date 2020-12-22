# 7.이진 탐색

* 데이터리스트 가운데 특정한 데이터를 찾는것을 탐색이라고 한다.  
탐색의 방법중 순차탐색, 그리고 이진탐색에 대해서 알아보자
<br/>
<br/>

## <순차 탐색>
* 순차탐색은 특정한 데이터를 찾기 위해 앞에서부터 순차적으로 데이터를 확인하는 방법이다.
### 순차 탐색의 구현  
```python
def sequentialSearch(n, target, array):
    for i in range(n):
        if array[i]==target:
            return(i+1)
```  
순차탐색은 N개의 데이터에대해서 최대 N번의 연산을 수행하므로 복잡도가 O(N)이다.
<br/>
<br/>

## <이진 탐색>
* 이진 탐색은 데이터를 반씩 나누어가며 특정 데이터를 찾는 방법이다.  
start,middle,end라는 변수를 사용하여 중간값을 타겟(찾는 데이터)과 비교해가며 점점 범위를 좁혀나가는 방식이다
### 이진 탐색의 구현  
1. 재귀함수를 이용한 구현
```python
def binarySearch(array,target,start,end):
    if start>end:
        return None
    middle=(start+end)//2
   
    if array[middle]==target:
        return middle

    elif array[middle]>target:
        return binarySearch(array,target,start,middle-1)
    
    else :
        return binarySearch(array,target,middle+1,end)
```  
2. 반복문을 이용한구현
```python
def binarySearch(array,target,start,end):
    
    while start<=end:
        middle=(start+end)//2

        if array[middle]==target:
            return middle
        
        elif array[middle]>target:
            end=middle-1
        
        elif array[middle]<target:
            start=middle+1

    return None
```
</br>
</br>

## <이진 탐색 트리>
* 자료구조에서 트리구조는 루트노드와 그 자식노드들로 이루어진 구조를 말한다.  
그중에서도 이진트리는 한 노드에 대해서 자식노드가 최대 두개까지만을 가지는 구조이다.  
이진 탐색 트리는 이진트리에 몇가지 조건을 걸어 이진탐색이 가능하도록 고안한 구조인데 조건은 다음과 같다.
```
-왼쪽 자식노드는 부모 노드보다 작다
-오른쪽 자식노드는 부모 노드보다 크다 
```
