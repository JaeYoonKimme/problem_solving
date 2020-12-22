# 6.정렬
정렬은 데이터를 기준에 따라서 순서대로 바꾸는 것을 의미한다.

여러가지 정렬 알고리즘이 있지만 각각 복잡도가 다르며 상황에 따라 각각 필요하므로 숙지해두자

* Selection Sort (선택정렬)

* Insertion Sort (삽입정렬)

* Quick Sort (퀵정렬)

* Count Sort (계수정렬)

* 파이썬 내림차순으로 정렬하는법
```python
array=sorted(array,reverse=True) 
#위와같이 reverse값을 인자로 주어 내림차순으로 정렬이 가능하다
```

* 리스트의 내용을 특정 키값으로 정렬하기
```python
array=sorted(array, key=lambda x : x[1])
#위와 같이 실행하면 원소 내 두번째의 원소들을 기준으로 정렬한다