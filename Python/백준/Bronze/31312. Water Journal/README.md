# [Bronze III] Water Journal - 31312 

[문제 링크](https://www.acmicpc.net/problem/31312) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2025년 8월 30일 21:52:26

### 문제 설명

<p>Every day, Eugene logs how many cups of water he drank. He forgot to log one entry in his journal though, but he remembers the minimum number and maximum number of cups of water he drank every day since he started logging his journal, and that there was at least one day where he drank the minimum and one day where he drank the maximum. Compute all possible amounts of cups of water he could have imbibed on the day he forgot to log.</p>

### 입력 

 <p>The first line of input contains three integers $n$ ($2 \le n \le 50$), $a$ and $b$ ($1 \le a \le b \le 50$), where $n$ is the number of days in Eugene's log, $a$ is the minimum number of cups of water he drank on any day, and $b$ is the associated maximum.</p>

<p>Each of the next $n-1$ lines contains a single integers $w$ ($a \le w \le b$). These are the entries in Eugene's log for every day except the day he forgot to log an entry. </p>

### 출력 

 <p>Output in increasing order, all of the possible values for the missing entry separated by whitespace, or simply output -1 if Eugene's memory is faulty and it isn't possible. </p>

