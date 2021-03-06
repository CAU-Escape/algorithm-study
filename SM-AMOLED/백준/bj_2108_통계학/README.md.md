# 통계학

문제 번호: 2108
알고리즘 분류: 정렬
푼 날짜: 2021년 1월 26일 오후 6:07

### 문제 링크

[https://www.acmicpc.net/problem/2108](https://www.acmicpc.net/problem/2108)

## 문제

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

## 출력

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

## 조건

- 시간 제한 : 2s
- 메모리 제한 : 256MB

---

## 해설

입력받은 값들은 정렬 알고리즘을 통해 산술평균, 중앙값, 범위를 쉽게 구할 수 있다. 최빈값은 Vector를 이용해 구해주었다. 

값을 입력하는 과정에서 각 원소의 개수를 Array의 값에 +1을 해주는 방식으로 각 원소의 개수를 찾고, 최댓값인 원소들을 Vector에 넣어준다. 만약 최댓값이 1개라면 v[0]을, 최댓값이 여러 개라면 두 번째로 작은 값인 v[1]을 출력한다. 

## 풀이

### 산술평균

산술평균값은 단순하게 모든 값의 합을 N으로 나누어 구할 수 있다. 이때 소수 첫째자리에서 반올림하기 위해 변수를 float형으로 계산해준다. int형으로 형변환을 할 때 소숫점 아래는 절삭하는 특징을 이용해, 양수일 때는 0.5를 더하여 나오는 수를 절삭하면 반올림이 되고, 음수일 때는 0.5를 빼서 나오는 수를 절삭하면 반올림이 된다.

### 중앙값

정렬한 뒤 가운데 index에 접근하면 쉽게 구할 수 있다.

### 최빈값

이 문제의 포인트가 최빈값이라 생각된다. 값을 입력할 때 각 원소의 개수를 count하는 배열에 해당 원소가 입력될 때 마다 +1을 해주고, 가장 많은 원소의 개수를 max에 저장한다. vector에 max와 같은 원소의 개수를 갖는 원소를 작은 수부터 차례로 넣으면 최빈 원소가 오름차순으로 정렬된다. 여기에서 vector에 최빈 원소가 하나라면 v[0]을, 둘 이상이라면 v[1]을 출력하면 된다.

### 범위

가장 큰 값에서 가장 작은 값을 빼주면 범위를 구할 수 있다. 

---

## 코멘트

Vector가 참 편하긴 하구나.

---

## 코드

```cpp
/*
https://codingzzangmimi.tistory.com/17 를 보고 공부함!
*/
#include <cstdio>
#include <algorithm>
#include <vector>
 
using namespace std;
 
int d[500000];
 
int main() {
 
    int n;
    int countArr[8001] = {0,};
    vector<int> v;
    int sum = 0, bm = 0, cm = 0, dm = 0;
 
    scanf("%d", &n);
 
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &d[i]);
        sum += d[i];
        countArr[d[i]+4000]++;
    }
 
    sort(d, d + n);
 
    int max = 0;
    for(int i = 0; i < 8001; i++) {
        if(max < countArr[i]) {
            max = countArr[i];
        }
    }
    for(int i = 0; i < 8001; i++) {
        if(countArr[i] == max) {
            v.push_back(i);
        }
    }
    
    float am = float(sum) / float(n);
 
    if (am >= 0)
        am = int(am + 0.5);
    else
        am = int(am - 0.5);
 
    bm = d[n / 2];
 
    cm = (v.size()>1)? v[1]-4000: v[0]-4000;
 
    dm = d[n - 1] - d[0];
 
    printf("%d\n", int(am));
    printf("%d\n", bm);
    printf("%d\n", cm);
    printf("%d\n", dm);
 
    return 0;
}
```