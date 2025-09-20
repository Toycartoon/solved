# [Bronze III] Number Reduction - 34437 

[문제 링크](https://www.acmicpc.net/problem/34437) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 구현, 시뮬레이션

### 제출 일자

2025년 9월 20일 17:46:05

### 문제 설명

<p>Christopher loves the number one. In fact, he loves it so much that if he ever has more than one of something, he makes sure to get rid of all but one of his items. Christopher has one pencil, one notebook, one sweatshirt, and so on.</p>

<p>However, Christopher has gotten bored of just giving away all but one of his possessions of each type. Instead, he has come up with a new strategy, which depends on the number of items he has already. If he has an even number of something, then he will give away half of what he has. If he has an odd number of things, then he will buy some more of that item: he will add twice as many items as he currently has, plus one more item, to his collection. He does this until he has just one item left.</p>

<p>For example, if he has $5$ phone chargers, then to get rid of them he would first buy $11$ more (for a total of $16$), then give away $8$, then give away $4$, then give away $2$, then give away $1$.</p>

<p>Christopher wants to know how long it will take to get rid of his items using this technique.</p>

<p>Given a number, you must tell Christopher how many steps the technique takes to convert the number to one. For example, for the number $5$ above, the number of steps needed would be $5$.</p>

### 입력 

 <p>The input consists of one integer, $N$ ($1 \leq N \leq 100\ 000$).</p>

### 출력 

 <p>Output the number of steps it takes for the input number to be converted to one.</p>

