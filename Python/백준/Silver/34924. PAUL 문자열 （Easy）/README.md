# [Silver V] PAUL 문자열 (Easy) - 34924 

[문제 링크](https://www.acmicpc.net/problem/34924) 

### 성능 요약

메모리: 32412 KB, 시간: 52 ms

### 분류

구현, 문자열, 홀짝성

### 제출 일자

2026년 1월 6일 22:23:56

### 문제 설명

<p><strong>이 문제는 Hard 버전과 굵게 표시된 제약 조건을 제외하면 동일합니다.</strong></p>

<p>PAUL 문자열은 <span style="color:#e74c3c;"><code>P</code></span>,<span style="color:#e74c3c;"><code>A</code></span>,<span style="color:#e74c3c;"><code>U</code></span>,<span style="color:#e74c3c;"><code>L</code></span>을 각각 하나 이상 포함하는 알파벳 대문자로 이루어진 문자열이다. 모그는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 PAUL 문자열을 선물받았다. 선물받은 문자열을 가지고 놀던 모그는 "이 문자열의 이웃한 두 문자를 삭제한 뒤 남은 부분을 이어 붙이는 연산을 반복해 정확히 <span style="color:#e74c3c;"><code>PAUL</code></span>만 남길 수 있을까?" 하는 궁금증이 생겼다.</p>

<p>머리가 좋지 않은 모그 대신 궁금증을 해결해 주자.</p>

### 입력 

 <p>첫째 줄에 모그가 선물받은 PAUL 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>4</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(4\le N\le 100\,000)$</span> </mjx-container></p>

<p>둘째 줄에 모그가 선물받은 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 PAUL 문자열이 주어진다. 이 문자열에서 <span style="color:#e74c3c;"><code>P</code></span>,<span style="color:#e74c3c;"><code>A</code></span>,<span style="color:#e74c3c;"><code>U</code></span>,<span style="color:#e74c3c;"><code>L</code></span>은 <strong>정확히 한 번씩</strong> 등장한다.</p>

### 출력 

 <p>정확히 <span style="color:#e74c3c;"><code>PAUL</code></span>만 남길 수 있다면 <span style="color:#e74c3c;"><code>YES</code></span>, 그렇지 않다면 <span style="color:#e74c3c;"><code>NO</code></span>를 출력한다.</p>

