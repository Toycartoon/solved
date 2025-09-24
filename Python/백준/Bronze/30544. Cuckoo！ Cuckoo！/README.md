# [Bronze II] Cuckoo! Cuckoo! - 30544 

[문제 링크](https://www.acmicpc.net/problem/30544) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 9월 24일 14:26:21

### 문제 설명

<p>The cuckoo bird pops out of the cuckoo clock and sounds off once on the quarter hour, half hour, and three-quarter hour. At the beginning of each hour, it sounds off the hour (1--12). Given the current time and a target number $N$, your task is to determine what time it will be when the cuckoo bird finishes sounding off $N$ times. If the cuckoo bird would be sounding off at the starting time, include those sounds in the count.</p>

<p>If the count is reached on the hour, report the time at the start of that hour. That is, you may assume the cuckoo finishes sounding off before the minute is up.</p>

### 입력 

 <p>The input consists of 2 lines. The first line contains the current time in the form <code>HH:MM</code> where $1 \leq$ <code>HH</code> $\leq 12$ and $0 \leq$ <code>MM</code> $\leq 59$, with leading 0's if necessary. The second line contains a single integer representing the target number $N$ such that $1 \leq N \leq 200$.</p>

### 출력 

 <p>Print the time at which the cuckoo bird has sounded off $N$ times. The time should be printed in the same format as the input.</p>

