# [Bronze IV] Driving Dilemma - 34363 

[문제 링크](https://www.acmicpc.net/problem/34363) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 9월 20일 13:12:15

### 문제 설명

<p>The day has finally come for Rishi to take his driving test. He's learned all of the rules of the road. He has practiced for many hours, and now he just needs to follow all of the rules of the road to pass the driving test.</p>

<p>Rishi's first challenge comes at the first intersection. As he approaches the intersection, the light turns yellow! If he does not make it to the other side of the intersection before the light turns red, he will have violated the rules of the road and will fail the test.</p>

<p>Because Rishi is a good driver, he is driving at exactly the speed limit, and will continue going at exactly the speed limit as he goes through the intersection. Rishi is also very good at determining distances, so he knows exactly how many feet away from the end of the intersection he is. And, since Rishi has practiced driving so much, he also knows exactly how many seconds the light will remain yellow before turning red. After turning red, the traffic light will remain red.</p>

<p><strong>If Rishi continues driving at exactly the speed limit, will he make it to the end of the intersection or beyond that point before the light turns red?</strong> (For the purpose of this problem, you can assume that Rishi and his car are a single point with no length or width.)</p>

### 입력 

 <p>The first line of input will contain of a single integer $10 \leq S \leq 10\,000$, the speed limit (in miles per hour) of the road Rishi is driving on.</p>

<p>The second line of input will contain of a single real number $0 \leq D \leq 100\,000$, the distance (in feet) to the end of the intersection. The number will have at most $4$ digits after the decimal point.</p>

<p>The third line of input will contain a single real number $0 \leq T \leq 100\,000$, the amount of time (in seconds) before the traffic light turns red. The number will have at most $4$ digits after the decimal point.</p>

<p>In order to avoid problems with rounding, you are guaranteed that Rishi will be at least one foot from the end of the intersection, or at least one foot after the end of the intersection when the light turns red. Note your comparisons should still be exact; do not factor in this guarantee into your answer.</p>

### 출력 

 <p>If Rishi will make it through the intersection before the light turns red, output "MADE IT" (without the quotes). Otherwise, output "FAILED TEST" (without the quotes).</p>

