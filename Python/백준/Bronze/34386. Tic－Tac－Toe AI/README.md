# [Bronze II] Tic-Tac-Toe AI - 34386 

[문제 링크](https://www.acmicpc.net/problem/34386) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 많은 조건 분기

### 제출 일자

2025년 10월 9일 15:53:31

### 문제 설명

<p>After you helped to save last year's Tic-Tac-Toe World Championships, you were given a grant to write a new tic-tac-toe AI to determine the best move to play.</p>

<p>A Tic-Tac-Toe board looks like the following. Every square can be empty, filled with an <code>X</code>, or filled with a <code>O</code> (capital letter 'o').</p>

<p>Player <code>X</code> has won if they have three <code>X</code>'s in a row. Player <code>O</code> wins if they can do the same with the <code>O</code>'s. A row can be horizontal, vertical, or diagonal.</p>

<p>Given the player whose turn it is, and a board where there is one winning move for that player, can you output the row and column where that player should play?</p>

### 입력 

 <p>The first line of the input is either <code>X</code> or <code>O</code>, representing the player whose turn it is.</p>

<p>The next three lines each have <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> characters. Each of these lines represents a row on the board. Each character in a line represents a square in that row. This means you have <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> rows and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> columns just like a normal Tic-Tac-Toe board.</p>

<p>Each square in the board contains either an <code>X</code>, <code>O</code> (that's a capital letter, not a number), or <code>E</code>. An <code>X</code> or <code>O</code> represents markings made by the players while <code>E</code> represents an empty square.</p>

<p>Input Restrictions</p>

<ul>
	<li>It is guaranteed that there will be one and only one square that will win the game for the player specified on the first line.</li>
	<li>The input may not necessarily represent a valid tic-tac-toe game state. That is, one of the players may have skipped some of their turns.</li>
</ul>

### 출력 

 <p>Output two space-separated integers representing the row and the column where the player should play. Note, the rows and columns are <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>-indexed, so if the player should play in the top left corner, then you should output "<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>".</p>

