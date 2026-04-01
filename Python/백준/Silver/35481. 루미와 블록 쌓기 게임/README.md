# [Silver IV] 루미와 블록 쌓기 게임 - 35481 

[문제 링크](https://www.acmicpc.net/problem/35481) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 많은 조건 분기

### 제출 일자

2026년 4월 2일 02:19:46

### 문제 설명

<p>루미의 친구 코코는 다음과 같은 블록 쌓기 게임을 루미에게 선물하려고 한다.</p>

<ul>
<li>이 게임은 가로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>칸, 세로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>칸의 사각 격자에서 이루어진다. 게임을 시작할 때 이 격자는 비어 있다.</li>
<li>플레이어들은 이 격자 위에 여러 가지 모양의 블록들을 원하는 대로 놓는다. 단, 블록은 단위 정사각형을 변끼리 연결한 모양이며, 블록을 이루는 각각의 단위 정사각형이 격자 내부의 칸에 맞도록 블록을 놓아야 하고, 블록이 겹치거나 한 가로줄의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>칸을 모두 채우면 안된다.</li>
</ul>

<p>이 게임이 끝났을 때의 랭크는 다음과 같이 계산한다.</p>

<ul>
<li>다음과 같은 패턴을 만들었을 경우 <span style="color:#e74c3c;"><code>GM</code></span> 랭크를 받는다. 아래 패턴에서 흰색 칸은 비어 있어야 하는 칸, 회색 칸은 채워져 있어야 하는 칸, 물음표가 쓰여 있는 칸은 비어 있든 채워져 있든 상관 없는 칸을 의미한다.</li>
</ul>

<p style="text-align:center;"><img alt="" src="https://upload.acmicpc.net/a85909a6-e4dd-43c5-a6b2-3d2e4059dea1/-/preview/" style="height: 382px; width: 200px;"></p>

<ul>
<li>이 패턴의 맨 아래 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>개의 줄까지 일치하고, 추가로 아래에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>번째 줄의 빈 칸의 바로 위 칸이 채워져 있다면 다음의 규칙에 따른 랭크를 받는다.
<ul>
<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>⋯</mo><mo>,</mo><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k=1,2,\cdots,9$</span></mjx-container>일 경우 순서대로 <span style="color:#e74c3c;"><code>9</code></span>, <span style="color:#e74c3c;"><code>8</code></span>, ..., <span style="color:#e74c3c;"><code>1</code></span>의 랭크를 받는다.</li>
<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>10</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>⋯</mo><mo>,</mo><mn>18</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k=10,11,\cdots,18$</span></mjx-container>일 경우 순서대로 <span style="color:#e74c3c;"><code>S1</code></span>, <span style="color:#e74c3c;"><code>S2</code></span>, ..., <span style="color:#e74c3c;"><code>S9</code></span>의 랭크를 받는다.</li>
</ul>
</li>
<li>위의 조건을 한 줄도 충족하지 못했다면 랭크를 받지 못한다.</li>
<li>패턴은 주어진 모양 그대로 맨 아래 줄부터 등장해야 한다. 맨 아래 줄이 아닌 다른 줄에서부터 시작하는 패턴이나 대칭 모양의 패턴 등은 인정되지 않는다.</li>
</ul>

<p>게임의 결과가 주어질 때, 랭크를 계산해 보자.</p>

### 입력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>줄에 걸쳐서 각 줄의 상태를 나타내는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>의 문자열이 주어진다.</p>

<p>문자열의 각 문자는 해당하는 칸이 채워져 있으면 <span style="color:#e74c3c;"><code>#</code></span>, 비어 있으면 <span style="color:#e74c3c;"><code>.</code></span>이다.</p>

<p>한 줄의 모든 글자가 <span style="color:#e74c3c;"><code>#</code></span>인 입력은 주어지지 않는다.</p>

### 출력 

 <p>주어진 게임 결과에 해당하는 랭크를 출력한다. 랭크를 받지 못하는 경우 <span style="color:#e74c3c;"><code>X</code></span>를 출력한다.</p>

