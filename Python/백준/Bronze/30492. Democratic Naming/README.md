# [Bronze II] Democratic Naming - 30492 

[문제 링크](https://www.acmicpc.net/problem/30492) 

### 성능 요약

메모리: 32544 KB, 시간: 228 ms

### 분류

구현, 문자열

### 제출 일자

2025년 9월 23일 20:10:44

### 문제 설명

<p>A new county has been created on artificially created land out from the coast, with code name "Built Anew Peninsula County", but the final name still needs to be chosen. To establish a new name, the cities within the county get to vote on the individual letters of the name.</p>

<p>As it happens, all cities in the county have a name with exactly $m$ letters, and so they decide the name of the county will also have exactly $m$ letters. Naturally, each city prefers their own name, and thus votes that the $i$th letter of the county name should match theirs. For each of the $m$ positions, the letter that received the most votes across all cities gets picked. In case of a tie between multiple letters, the one occurring earliest in the English alphabet gets picked.</p>

<p>Given the list of the city names, determine the result of the vote for the new county's name.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers $n$ and $m$ ($1\leq n\leq 1000$, $1 \leq m \leq 1000$), the number of cities and the number of letters in each city name.</li>
	<li>$n$ lines, each with a string of length $m$, the name of a city.</li>
</ul>

<p>The city names only consist of lowercase English letters (<code>a-z</code>).</p>

### 출력 

 <p>Output the name of the new county.</p>

