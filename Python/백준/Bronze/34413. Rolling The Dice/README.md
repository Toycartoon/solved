# [Bronze II] Rolling The Dice - 34413 

[문제 링크](https://www.acmicpc.net/problem/34413) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 문자열, 사칙연산, 파싱

### 제출 일자

2025년 9월 23일 16:30:19

### 문제 설명

<p>In Dungeons and Dragons, we use dice rolls very often to determine which actions succeed and which fail. There are many different dice with varying numbers of sides so we have a shorthand for representing different rolls. A single roll is written as "d#," with the "#" representing the number of sides on the die. If you need to roll multiple dice of the same type, there will be a number before the "d". For example, if you are required to roll 4d6, you would roll four six-sided dice and add the results together. There will also be a + after the notation, meaning that you add that number to the total results of the dice (not to each individual die rolled).</p>

<p>Higher numbers are better, and I want to make my character as powerful as possible, so I need to know what number I'll get on average for different rolls. It's relatively simple to do statistics on dice because every value has an equal chance of being rolled. <strong>If you average the minimum value and the maximum value of the roll, it will give you the value that you would get on average if you rolled it many times.</strong> For example, the roll 2d6+5 has a minimum value of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container> if you roll two 1s and a maximum value of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$17$</span></mjx-container> if you roll two <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$6$</span></mjx-container>'s which gives an average of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$12$</span></mjx-container> overall (for 2d6+5). Given the notation for a roll, find the average value of that roll.</p>

### 입력 

 <p>The input will be a single line in the form of "XdY+Z". X, Y, and Z are all integers and will fall within the same range, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>X</mi><mo>,</mo><mi>Y</mi><mo>,</mo><mi>Z</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le X, Y, Z \le 100$</span></mjx-container>.</p>

### 출력 

 <p>Your program needs to output the average value that you would expect for the given roll values.</p>

