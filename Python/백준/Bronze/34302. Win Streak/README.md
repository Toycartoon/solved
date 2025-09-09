# [Bronze III] Win Streak - 34302 

[문제 링크](https://www.acmicpc.net/problem/34302) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현

### 제출 일자

2025년 9월 9일 12:50:40

### 문제 설명

<p>The Colorado School of Mines football team is just off of another great season which saw them reach the Division II finals for the second year in a row.</p>

<p>Unfortunately, the team lost the finals, but the Orediggers still had a great season, going on the longest winning streak in school history with fourteen games across the regular season and the playofffs until the final game. (A winning streak is a sequence of chronologically consecutive games where a team scores more points than their opponent.)</p>

<p>Orediggers head coach Pete Sterbick has tasked you with analyzing the games of the other teams in the Rocky Mountain Athletic Conference (RMAC) to determine how long their longest winning streaks were.</p>

<p>Given the scores for all of the games that one particular team has played, Coach Sterbick wants to know the length of the longest winning streak for that team.</p>

### 입력 

 <p>The first line of input will be a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>4</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 10^4$</span></mjx-container>, the number of games the team you are analyzing has played.</p>

<p>The next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines will each contain two integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>S</mi><mo>,</mo><mi>T</mi><mo>≤</mo><mn>222</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq S, T \leq 222$</span></mjx-container>, representing the score of the team you are analyzing, and the score of the opposing team, respectively. The scores are given in chronological order.</p>

### 출력 

 <p>Output a single integer, the length of the longest sequence of consecutive games where the team you are analyzing scored more points than their opponent.</p>

