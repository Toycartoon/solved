# [Bronze II] Circular Shortcut - 35071 

[문제 링크](https://www.acmicpc.net/problem/35071) 

### 성능 요약

메모리: 34536 KB, 시간: 36 ms

### 분류

기하학

### 제출 일자

2026년 1월 4일 23:27:47

### 문제 설명

<p>After the practice session, Katrin and her team join the guided city tour of Karlsruhe, where they learn all sorts of random fun facts about Karlsruhe. It is well-known that the first email in Germany was received here (sent by Laura Breeden, MIT) and that the bicycle was invented in Karlsruhe, but did you know that the palace has exactly 365 windows -- one for each day of the year? Or that there may (or may not) be an umbrella buried beneath the great pyramid in the city centre?</p>

<p>Later that evening, Katrin and her team find themselves in the western part of Karlsruhe, and they have to hurry to the Dining Hall to make it in time for dinner! They could take the direct route through the palace garden, which is a straight line. But on such a pleasant evening, the palace garden is crowded with pedestrians and cyclists who might slow them down. The alternative is to follow the <em>Adenauerring</em>, a street forming a perfect half-circle between their current location and the intersection close to the Dining Hall, and nothing will slow them down there.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fc0bb569-fedb-4346-8347-3e104dad9405/-/preview/" style="width: 400px; height: 269px;"></p>

<p style="text-align: center;"><small>Map data from <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a></small></p>

<p style="text-align: center;">Figure C.1: The two possible paths from their current location to the intersection close to the Dining Hall. The blue semi-circular road is the Adenauerring, and the orange straight path in the middle is the route through the palace garden.</p>

<p>Katrin and her team have arranged to meet up with their coach on the intersection close to the Dining Hall, as shown in Figure C.1. They would like to know: how much longer is the route along the Adenauerring?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$d$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>d</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\leq d\leq 10^9$</span></mjx-container>), the length of the straight way through the palace garden, in metres.</li>
</ul>

### 출력 

 <p>Output how much longer the route along the Adenauerring is, compared to going straight through the palace garden, in metres.</p>

<p>Your answer should have an absolute or relative error of at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>9</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-9}$</span></mjx-container>.</p>

