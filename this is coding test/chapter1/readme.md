# 복잡도 비교하기
복잡도는 프로그램이 얼마나 효율적인지를 나타내는 척도이다
크게 두가지로 나뉘는데 다음과 같다
* 시간 복잡도 - 프로그램의 연산의 횟수와 시간에 관련한 내용
* 공간 복잡도 - 프로그램이 할당하는 데이터 공간과 관련한 내용

일반적으로 프로그래밍에서 복잡도는 시간 복잡도를 의미한다

N개의 데이터에 대해서 프로그램의 연산 횟수가 대략 N번일때 프로그램의 복잡도는 O(N)으로 나타낼 수 있다   


<br/>
<br/>

## Selection Sort
----------------
```python
for i in range(len(array1)):
    min_idx=i
    for j in range(i+1,len(array1)):
        if array1[min_idx]>array1[j]:
            min_idx=j
    array1[i], array1[min_idx] = array1[min_idx], array1[i] #swap
```
선택정렬은 10000개의 데이터에 대해서 대략 10000^10000번의 연산을 수행한다

따라서 복잡도는 O(N^N)으로 나타낼 수 있다 

선택정렬의 구현에 대해서는 6장에서 다시 다룬다   

<br/>
<br/>

## python 내장 라이브러리
----------------
```python
array2.sort()
```
파이썬에는 기본적으로 리스트를 정렬하는 sort()를 내장하고있다

이 기능의 복잡도는 O(NlogN)이다   

<br/>
<br/>

## 시간 측정 방법
----------------
```python
start_time=time.time()
#프로그램 내용
end_time=time.time()
print(end_time-start_time)
```
파이썬에서 제공하는 time 기능을 사용하면 위와같이 프로그램이 동작하는데 걸리는 시간을 측정할 수 있다   

<br/>
<br/>

## 파이썬 Swap 기능
----------------
```python
array1[i], array1[min_idx] = array1[min_idx], array1[i]
```
파이썬에서는 두 변수의 값을 쉽게 바꿔주는 swap기능을 제공한다

위의 코드는 array1[i]과 array1[min_idx]의 값을 바꾸게 된다