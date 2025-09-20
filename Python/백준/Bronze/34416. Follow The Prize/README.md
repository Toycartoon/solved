# [Bronze III] Follow The Prize - 34416 

[문제 링크](https://www.acmicpc.net/problem/34416) 

### 성능 요약

메모리: 40660 KB, 시간: 1108 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 9월 20일 17:36:27

### 문제 설명

<p>A total of $n$ cups were placed upside-down on a table, a prize was placed under one of them, and then the cups were shuffled. Luckily, you know under which cup the prize began, and how the cups were shuffled. Can you determine the final position of the prize?</p>

<p>A cup (and the prize which it might cover) can only be in one of $n$ distinct positions at any given time: $1, 2, \ldots, n$. No two cups can be in the same position at any given time.</p>

<p>The cups are shuffled by performing a series of swaps. A swap is defined as exchanging the location of two cups. For example if the cups in positions $4$ and $7$ were swapped, the cup originally in position $4$ would end in position $7$, and the cup originally in position $7$ would end in position $4$. If the prize were originally under cup $7$, this swap would have moved the prize to position $4$.</p>

### 입력 

 <p>The first line is $n$, an integer between $2$ and $1\,000\,000$, inclusive, defining the number of cups.</p>

<p>The second line is an integer between $1$ and $n$, inclusive, which defines the initial position of the prize.</p>

<p>The third line is $m$, a non-negative integer less than or equal to $1\,000\,000$, defining the number of swaps performed to shuffle the cups.</p>

<p>The final $m$ lines report the swaps that were performed, in order. Each line consists of two different space-separated integers, between $1$ and $n$, defining the positions of the cups that were exchanged for that swap.</p>

### 출력 

 <p>The output is a single integer between $1$ and $n$, which is the position of the prize after all of the swaps are performed.</p>

