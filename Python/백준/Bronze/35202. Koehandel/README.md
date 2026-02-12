# [Bronze IV] Koehandel - 35202 

[문제 링크](https://www.acmicpc.net/problem/35202) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 사칙연산

### 제출 일자

2026년 2월 13일 01:51:20

### 문제 설명

<p>You are playing a game of <em>Betting and Purchasing Cows</em> (BAPC), and Old MacDonald wants to buy one of your cows using a bid-off. This works as follows.</p>

<p>He bets some number of BAPC coins, which he puts in a cup that he places upside down on the table. You then openly bet some number of your own coins. The cup is removed to reveal MacDonald's bet. The bets are exchanged: you receive the bet from MacDonald and he receives your bet. The player that bet the most BAPC coins receives one cow from the opponent, regardless of who started the bidding. In case of a tie, no cows are exchanged.</p>

<p>You love the cows in the game, so your primary goal is to have the most possible cows after the trade. Your secondary goal is to have the highest possible number of coins after the trade. You pay close attention when Old MacDonald is secretly putting their coins in the cup, and by listening very carefully, you have determined the exact number of coins that he put in the cup. Given this information and the number of coins you have, how many coins should you bet?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
<li>One line with two integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>c</mi><mo>,</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0\leq c, n\leq 10^9$</span></mjx-container>), the number of BAPC coins in Old MacDonald's cup and the number of coins that you have.</li>
</ul>

### 출력 

 <p>Output the number of coins that you should bet, keeping your goals in mind.</p>

