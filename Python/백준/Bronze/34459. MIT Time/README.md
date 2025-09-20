# [Bronze III] MIT Time - 34459 

[문제 링크](https://www.acmicpc.net/problem/34459) 

### 성능 요약

메모리: 32412 KB, 시간: 300 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 9월 20일 17:29:13

### 문제 설명

<p>Busy Beaver arrived to his MIT class late! However, thanks to "MIT time", all classes actually start $5$ minutes later than the posted time.</p>

<p>Busy Beaver wants to make a generalization of this system. Namely, if someone arrives $N$ minutes late to an event, then:</p>

<ul>
	<li>if $N \le 5$, they arrived on "MIT time";</li>
	<li>if $5 < N \le 25$, they arrived on "MIT$^2$ time";</li>
	<li>if $25 < N \le 125$, they arrived on "MIT$^3$ time";</li>
	<li>and so on. Formally, if $k \ge 2$, then "MIT$^k$ time" is when $5^{k-1} < N \le 5^k$.</li>
</ul>

<p>Given $N$, determine on which of "MIT time", "MIT$^2$ time", etc. this person arrived at.</p>

### 입력 

 <p>The first line contains a single integer $T$ $(1 \leq T \leq 10^5)$ --- the number of test cases.</p>

<p>The only line of each test case contains a single integer $N$ ($1 \le N \le 10^9$) --- the number of minutes late to an event the person is.</p>

### 출력 

 <p>For each test case, output a single line that consists of either "<code>MIT time</code>" or "<code>MIT^</code>$k$ <code>time</code>" for some integer $k \geq 2$, corresponding to the time this person arrives at.</p>

