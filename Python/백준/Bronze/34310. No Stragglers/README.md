# [Bronze III] No Stragglers - 34310 

[문제 링크](https://www.acmicpc.net/problem/34310) 

### 성능 요약

메모리: 32412 KB, 시간: 680 ms

### 분류

수학, 애드 혹, 사칙연산

### 제출 일자

2025년 9월 9일 12:57:43

### 문제 설명

<p>Mines Market, the premier on-campus dining hall option, has had some security issues over the past few weeks; some troublemakers have been hiding overnight to score free breakfast and steal ice cream from the fridges! Thus, the Mines Market staff and Mines PD have installed a new, state-of-the-art security and CCTV system which can detect people coming and going from Mines Market. This new security system is remarkable, it can even tell the difference between students, faculty, and visitors!</p>

<p>As the technician for this new security solution, you've been tasked to determine whether, at the end of the day, there are stragglers present in Mines Market or not. Assume there are no students, faculty, or visitors present in Mines Market at the beginning of the day.</p>

### 입력 

 <p>The first line of input is an integer, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 1\,000\,000$</span></mjx-container>, representing the number of entry or exit events logged by the new security system. Each of the subsequent <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines of input represent a single entry or exit event. These <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines will be formatted as three space-separated values:</p>

<ul>
	<li>The type of person entering or exiting Mines Market; will be one of <code>STU</code>, <code>FAC</code>, or <code>VIS</code> denoting students, faculty, and visitors, respectively.</li>
	<li>The direction the person is going; will be either <code>IN</code> or <code>OUT</code> representing a person entering or exiting, respectively.</li>
	<li>The integer number of people entering or exiting Mines Market of the specified type; this integer will be in the range <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c5B"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c5D"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">[</mo><mn>0</mn><mo>,</mo><mn>16</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>383</mn><mo stretchy="false">]</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$[0, 16\,383]$</span></mjx-container>.</li>
</ul>

<p>Assume that there will be no more than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>767</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$32\,767$</span></mjx-container> of any type of person (students, faculty, or visitors) present in Mines Market at any given time. Also assume that it is impossible for there to be a negative quantity of any type of person (students, faculty, or visitors) present in Mines Market at any given time.</p>

### 출력 

 <p>Output "NO STRAGGLERS" (without the quotes) if there are no stragglers present in Mines Market at the end of the day. Otherwise, output the total number of stragglers (of any person type) present at the end of the day.</p>

