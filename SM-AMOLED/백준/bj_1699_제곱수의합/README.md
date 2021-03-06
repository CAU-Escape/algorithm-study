# 제곱수의 합

문제 번호: 1699
알고리즘 분류: DP
푼 날짜: 2021년 2월 20일 오후 6:16

## 문제링크

[https://www.acmicpc.net/problem/1699](https://www.acmicpc.net/problem/1699)

## 문제

어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

## 출력

주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

## 조건

- 시간 제한 : 2s
- 메모리 제한 : 128MB

---

## 해설

제곱수의 합으로 나타내고자 하였으므로, 해당 수를 만들 수 있는 가장 큰 제곱수를 최대한 이용하여야 한다. DP 벡터를 만들어 이전에 선택했던 최소의 방법에서 1가지 방법을 늘리는 방법으로 최소의 방법을 이어나간다.

## 풀이

자연수 i에 대해 1부터 i보다 작은 제곱수까지 각 k라고 할 때, dp[i-k] 의 값에 1을 더한 값 중 가장 작은 값이 dp[i]가 된다. 예를 들어, i가 43일 때, dp[43]은 43에서 제곱수를 종류별로 하나씩 뺐을 때 dp의 값이 가장 작은 방법을 선택하는 것이 가장 최소의 방법을 사용할 수 있다. dp[42], dp[39], dp[34], dp[27], dp[18], dp[7] 중 가장 작은 값 + 1이 된다.

```cpp
for(int i = 1; i <= N; i++) {
    int temp = 1;
    int min = 100000;
    while (temp*temp <= i) {
        if(dp[i-temp*temp] + 1 < min) {
            min = dp[i-temp*temp] + 1;
        }
        temp++;
    }
    
    dp[i] = min;
}
```

---

## 코멘트

할 만 했군 그래.

---

## 코드

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int N;
    cin >> N;
    vector<int> dp(N+1);
    
    dp[0] = 0;
    
    for(int i = 1; i <= N; i++) {
        int temp = 1;
        int min = 100000;
        while (temp*temp <= i) {
            if(dp[i-temp*temp] + 1 < min) {
                min = dp[i-temp*temp] + 1;
            }
            temp++;
        }
        
        dp[i] = min;
    }
    
    cout << dp[N];
    return 0;
}
```