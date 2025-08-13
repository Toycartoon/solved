# [Bronze II] Fifty Shades of Pink - 20735 

[문제 링크](https://www.acmicpc.net/problem/20735) 

### 성능 요약

메모리: 32412 KB, 시간: 56 ms

### 분류

구현, 문자열

### 제출 일자

2025년 8월 14일 03:38:38

### 문제 설명

<p>Thore is a fashionable man. Every time he meets up with his programming team, he wears his hot pink team hoodie over a salmon colored shirt with shirt buttons in a dashing rose or pink shade. Of course, he can't show up to two training sessions with the same buttons on his shirt, that would cause unbearable ridicule. If he can't find buttons for this perfect color combination, he will come up with some poor excuse for not showing up. He has a box full of different colored buttons in labeled packages. Unfortunately, Thore is color blind, so his helpful daughter has labeled each package with the color of the buttons. Her writing is terrible though, she mixes uppercase and lowercase arbitrarily and has no spacing between words, so Thore needs your help to decipher the names on the labels and select buttons with either "<code>pink</code>" or "<code>rose</code>" somewhere in the name, ignoring case. </p>

### 입력 

 <p>Input starts with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 1\,000$</span></mjx-container>, the number of button packages in the box. The following <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines each has a color name, one for each package. The names consist of up to 30 characters of letters A - Z, a - z.</p>

### 출력 

 <p>Print one integer, the number of training sessions Thore can attend. If he can't attend any session because there are no pink buttons, output his standard excuse "<code>I must watch Star Wars with my daughter</code>".</p>

