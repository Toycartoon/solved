# [Bronze IV] Abby's Absolutes - 34308 

[문제 링크](https://www.acmicpc.net/problem/34308) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 9월 9일 12:21:39

### 문제 설명

<p>Abby has offered to buy you some apples. However, she is very absolute about things.</p>

<p>You may ask her to buy a certain number of apples, but she may buy more apples if she figures that you want a lot of apples, or just buy one apple if she figures that you do not want very many apples. So, if the number of apples you want is closer to Abby's upper threshold than it is to $1$, then she will buy a number of apples equal to her upper threshold. Otherwise, she will just buy one apple. If it is equally close to $1$ and her upper threshold, she will just buy $1$ apple.</p>

<p>You want to figure out the total number of apples Abby will buy for you after she takes one or more trips to the grocery store.</p>

### 입력 

 <p>The input will consist of two lines.</p>

<p>The first line will contain two space-separated integers. The first integer $1 \leq N \leq 10\,000$ is the number of apples Abby will buy if she is buying a lot of apples. The second integer $1 \leq K \leq 100$ is the number of trips to the store Abby will take.</p>

<p>The second line will contain $K$ space-separated integers representing the number of apples you want to buy on each of Abby's trips to the store, with each of these integers being between $1$ and $N$, inclusive.</p>

### 출력 

 <p>Output $K$ space-separated integers representing the number of apples Abby will buy for you for each of her trips to the store.</p>

