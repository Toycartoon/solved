# [Bronze II] Strawberry - 34799 

[문제 링크](https://www.acmicpc.net/problem/34799) 

### 성능 요약

메모리: 32544 KB, 시간: 48 ms

### 분류

수학, 구현, 문자열, 사칙연산

### 제출 일자

2025년 11월 24일 10:44:32

### 문제 설명

<p>How many <code>r</code>'s are there in the word <code>strawberry</code>? That's easy, it's obvious the answer is $3$. But to LLMs, the answer is not so obvious, and early models would count the word to have only $2$.</p>

<p>To further trick LLMs, you decide to take a string $s$, and repeat it $N$ times. Each time it's repeated, you change each letter to be the previous letter in the alphabet, with <code>a</code> instead becoming <code>z</code>. For example, the word <code>abacus</code> becomes <code>zazbtr</code>.</p>

<p>If we take the word <code>strawberry</code> and repeat it $3$ times in total, we get the string <code>strawberryrsqzvadqqxqrpyuzcppw</code>. This string contains $5$ occurrences of the letter <code>r</code>.</p>

<p>Given a word and the total number of times it is repeated, count the number of times <code>r</code> appears in it!</p>

### 입력 

 <p>The first line of input contains a string $s$ of lowercase letters ($1 \le |s| \le 1000$).</p>

<p>The next line contains a single integer $N$ ($1 \le N \le 10^{15}$), the total number of times $s$ is repeated including the initial string, where each letter is replaced by the one before it in each repetition.</p>

### 출력 

 <p>Output the number of times <code>r</code> appears in the final string.</p>

