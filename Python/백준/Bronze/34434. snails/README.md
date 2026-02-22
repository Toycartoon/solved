# [Bronze I] snails - 34434 

[문제 링크](https://www.acmicpc.net/problem/34434) 

### 성능 요약

메모리: 99568 KB, 시간: 336 ms

### 분류

수학, 구현, 다이나믹 프로그래밍, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2026년 2월 23일 00:17:16

### 문제 설명

<p>In prehistoric times, there were many creatures with shells that lived in the ocean. You are part of a team of researchers who are looking at a collection of shell fossils with spiral shapes. You want to determine what kind of animal each one came from.</p>

<p>For each shell, you have taken a sequence of measurements along the spiral part. It is hypothesized that if the measurements $ M_1\ M_2\ \ldots\ M_k$ for a given shell follow the pattern of the following sequence, it is a nautilus shell: \begin{align*} M_1 &= 0 \\ M_2 &= 1 \\ M_3 &= 2 \\ M_4 &= 3 \\ M_{k} &= M_{k-1} + M_{k-2} + M_{k-3} + M_{k-4} & \text{when $k > 4$} \end{align*} Otherwise, it is a snail shell.</p>

<p>The team has collected a very large number of measurements. Being the member with the most programming experience, you have been asked to write a computer program to automate the task of determining whether each sequence of measurements is for a snail shell or nautilus shell.</p>

### 입력 

 <p>The first line of input shall be $n$, the number of lines of input that follow, where $1 \leq n < 2^{15} $.</p>

<p>The subsequent $n$ lines of input shall each be a sequence of $k$ (where $1 \leq k < 2^{15}$) measurements $M_1\ M_2\ \ldots\ M_k$ pertaining to one shell fossil. Measurements are separated by spaces. Each measurement shall be in the range $0 \leq M < 2^{32}$.</p>

### 출력 

 <p>For each line of input where the measurements came from a nautilus shell, the output shall be a line with only <code>NAUTILUS</code>. For each line of input where the measurements came from a snail shell, the output shall be a line with only <code>SNAIL</code>.</p>

