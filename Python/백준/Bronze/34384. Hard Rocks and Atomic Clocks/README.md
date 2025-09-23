# [Bronze III] Hard Rocks and Atomic Clocks - 34384 

[문제 링크](https://www.acmicpc.net/problem/34384) 

### 성능 요약

메모리: 34536 KB, 시간: 36 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 9월 23일 09:00:17

### 문제 설명

<p>As a bright physics student, you have been put in charge of overseeing Mines' most promising new high-tech invention: a titanium-alloy drilling apparatus capable of boring through the toughest igneous rocks at record speeds. In theory.</p>

<p>In order to test this durable drill, it must be run continuously to ensure it will not break from strain. However, because of the heat it creates, power must be cycled to prevent it from overheating catastrophically. This power cycle must occur every hour, less than a minute after the turn of the hour. That's your job {\textemdash} to prevent disaster by periodically resetting the drill.</p>

<p>The issue is that the only clock available in the physics lab is a high-precision atomic clock which displays the number of seconds since midnight. That is your input {\textemdash} the whole number of seconds as displayed on the atomic clock. You want to maximize how long you can doze off until you have to wake up and power-cycle the drill, because you did not get nearly enough sleep last night. Output the maximum whole number of minutes you can sleep for, so that when you wake up, it will be less than a minute before you need to reset the drill. You can assume that the drill was last reset at exactly the hour, so you can always sleep for at least one minute.</p>

### 입력 

 <p>A single positive integer between <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>86</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>400</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$86\,400$</span></mjx-container> representing the number of seconds since midnight, as displayed on the atomic clock.</p>

<p>You can assume that the input will never be exactly on the hour.</p>

### 출력 

 <p>Print a single positive integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>60</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq x \leq 60$</span></mjx-container> representing the maximum whole number of minutes you can sleep for before needing to wake up and reset the drill.</p>

