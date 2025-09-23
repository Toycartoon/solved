# [Bronze III] Ski Traffic - 34441 

[문제 링크](https://www.acmicpc.net/problem/34441) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 9월 23일 11:49:22

### 문제 설명

<p>Students at the Colorado School Of Mines love to go skiing, but hate waiting in traffic. A student, Sam, has come up with a precise algorithm via machine learning to determine how long it will take to travel to a ski hill:</p>

<ol>
	<li>The expected time is doubled if it's a weekend (i.e. a Saturday or a Sunday).</li>
	<li>The expected time is doubled if there's bad weather on I-70.</li>
	<li>The expected time is tripled if it recently snowed on the Front Range.</li>
	<li>The expected time is tripled if it's a holiday.</li>
</ol>

<p>Note that many of these rules may apply to a single day. Sam would like to use her algorithm to predict how long it will take to travel to the hill. It is up to you to implement Sam's algorithm!</p>

### 입력 

 <p>The input consists of six lines; the following list gives the content of each of the lines.</p>

<ol>
	<li>The name of the hill (for example, "Lockstone", "Skistone", "Navajo Basin", etc.)</li>
	<li>The time needed to get to the ski area assuming perfect conditions; the line is of the format "$h$:$m$" where the integer $h$ is the number of hours ($0 \leq h \leq 10\,000$) and the integer $m$ is the number of minutes ($0 \leq m < 60$). $m$ is always given as two digits (i.e. zero-padded on the left) but $h$ may not be.</li>
	<li>The day of the week, which is one of strings "mon", "tue", "wed", "thr", "fri", "sat", or "sun"</li>
	<li>A "1" if the weather's bad on I-70 and a "0" otherwise</li>
	<li>A "1" if it recently snowed on the Front Range and a "0" otherwise</li>
	<li>A "1" if it's a holiday and a "0" otherwise</li>
</ol>

### 출력 

 <p>Output the expected time in the format "$h$:$m$" where $h$ is the integer number of hours and $m$ is the integer number of minutes. $m$ must be two digits (i.e. zero-padded on the left). The output should not have more than $59$ minutes. For instance, "1:61" is invalid and should be "2:01" instead.</p>

