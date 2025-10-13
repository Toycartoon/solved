# [Bronze II] Cake Promise - 33221 

[문제 링크](https://www.acmicpc.net/problem/33221) 

### 성능 요약

메모리: 32412 KB, 시간: 276 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 10월 13일 18:00:04

### 문제 설명

<p>Today is the big day: professor P. Wright is organizing a programming contest. All of his students are participating, because he has promised to bake a cake for all teams that can beat him in the contest.<sup>1</sup> After the contest has ended, professor Wright receives a raw copy of the scoreboard, in which the teams are out of order. He is short on time: besides baking, he also has some exams to grade. Therefore, he needs a program to calculate how many teams beat him in the contest.</p>

<p>The contest consists of a given number of problems, which the teams will need to solve as fast as possible. One team beats another team if the number of problems solved by the first team is strictly greater. If the number of problems solved is equal between two teams, the team that required a lower sum of minutes to solve the problems beats the other. Professor Wright is also willing to bake a cake for teams that solved the same number of problems <em>and</em> required the same sum of minutes as himself.</p>

<hr>
<p><sup>1</sup>All characters and events in this problem description are fictional. Any resemblance to actual lecturers is purely coincidental.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line containing two integers $t$ and $p$ ($2\leq t, p\leq 1000$), the number of teams participating and the number of programming problems, respectively. Professor Wright counts as one of the teams.</li>
	<li>$t$ lines, each containing $p$ values, the results for each team. The first line represents the results of professor Wright. Each result is either "<code>X</code>", indicating that the team did not solve this problem, or an integer $r$ ($1\leq r\leq 10^6$), representing the number of minutes that this team needed to solve the problem.</li>
</ul>

### 출력 

 <p>Output the number of teams for which professor Wright needs to bake a cake.</p>

