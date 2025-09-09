# [Bronze I] QWERTY - 34311 

[문제 링크](https://www.acmicpc.net/problem/34311) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2025년 9월 9일 13:01:56

### 문제 설명

<p>Riley is a very fast typist. She can easily reach <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$180$</span></mjx-container> words per minute (WPM) without looking at the keyboard. Her muscle memory is accustomed to the standard QWERTY keyboard layout (Figure 1). Unfortunately, she didn't realize that the keyboard she was typing on was actually the ABCDEF layout (Figure 2), so her message looks like gibberish.</p>

<p>For example, if her message read <code>visidkmi lvpiis in zhycl</code>, then what she actually wanted to type was <code>colorado school of mines</code>. Note that the space key is in the same position on both keyboards. This example corresponds to Sample Input 1.</p>

<p>Given an arbitrary message, can you figure out what Riley was trying to type?</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fe6b5179-fe5c-4e0a-b7f6-570ee3a2f41e/-/preview/" style="width: 500px; height: 175px;"></p>

<p style="text-align: center;"><strong>Figure 1</strong>: The standard QWERTY layout that Riley thought she was using. Made with <a href="http://www.keyboard-layout-editor.com">www.keyboard-layout-editor.com</a>.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b850f30b-4f59-4c9c-a559-e96debf27362/-/preview/" style="width: 500px; height: 175px;"></p>

<p style="text-align: center;">Figure 2: The ABCDEF layout keyboard that Riley actually used. Made with <a href="http://www.keyboard-layout-editor.com">www.keyboard-layout-editor.com</a>.</p>

### 입력 

 <p>The first line of input is an integer, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 1\,000$</span></mjx-container>, corresponding to the number of characters in the second line.</p>

<p>The second line of input is the text Riley typed with the ABCDEF keyboard. It is guaranteed to contain only the lowercase letters <code>a</code>--<code>z</code> and the space character.</p>

### 출력 

 <p>Your output should be a single line: the text Riley was trying to type.</p>

