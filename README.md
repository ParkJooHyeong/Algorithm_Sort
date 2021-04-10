# Sorting Algorithm
여러가지 sorting 알고리즘을 직접 구현 및 연습.  
> reverse=False : 오름차순 정렬  
> reverse=True  : 내림차순 정렬  
>

## 1. Selection Sort  
- 선택 정렬
- 시간 복잡도 : O(N^2)
    > N = 데이터의 개수

## 2. Insertion Sort  
- 삽입 정렬
- 시간 복잡도 : O(N^2)
    > N = 데이터의 개수

## 3. Quick Sort
- 퀵 정렬
- 시간 복잡도 : O(NlogN)
    > N = 데이터의 개수

## 4. Counting Sort
- 계수 정렬
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능.
    > ex) 0이상 100이하의 성적 데이터를 정렬할 때.
- 실수형 범위의 경우 무한한 범위를 가져 사용하기 어렵다.
- 시간 복잡도 : O(N+K) 
    > N수 = 데이터 개수, K = 데이터의 최대값

## 5. Merge Sort
- 병합 정렬
- Divide and conquer : 큰 문제를 작은 문제로 분할해 해결.
- Recursive 하게 함수를 구성해 구현 가능.
- 시간 복잡도 : O(NlogN)
    > N = 데이터 개수  
      최악의 경우에도 위의 시간 복잡도를 보장함.

## 6. Heap Sort
- 힙 정렬


#
### Tip
Python 정렬 라이브러리
> sorted( ), sort( )
>   > 시간 복잡도 : O(NlogN)  
>  merge sort, insertion sort 아이디어를 더한 하이브리드 방식 정렬 알고리즘.  
>  key를 매개변수로 입력받아 사용 가능.  
*  데이터의 개수, 범위를 보고 어떤 알고리즘을 쓸지 결정하자.