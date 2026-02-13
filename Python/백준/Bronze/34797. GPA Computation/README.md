# [Bronze III] GPA Computation - 34797 

[문제 링크](https://www.acmicpc.net/problem/34797) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 구현, 문자열, 사칙연산

### 제출 일자

2026년 2월 14일 02:38:04

### 문제 설명

<p>Lydia wants to know if she is valedictorian!</p>

<p>Lydia's school computes the grade point averages of its students as follows - for each class that a student takes, they get assigned a letter grade from A to E. An A is worth 4 points, a B is worth 3 points, a C is worth 2 points, a D is worth 1 point, and an E is worth no points. The <em>unweighted</em> grade point average is therefore derived by computing the sum of these point values and dividing by the number of classes Lydia took.</p>

<p>To compute the <em>weighted</em> grade point average, each of the classes is assigned a tier from 1 to 3. If a student gets an A, B, or C in a tier 1 class, they get an additive bonus of 0.05 points. If a student gets an A, B, or C in a tier 2 class, they get an additive bonus of 0.025 points. These are the only ways to get additive bonuses. The <em>weighted</em> grade point average is computed by adding together all the additive bonuses to the <em>unweighted</em> grade point average.</p>

<p>Given Lydia's transcript, compute her weighted grade point average!</p>

### 입력 

 <p>The first line of input contains a single integer, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 50$</span></mjx-container>).</p>

<p>Each of the next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines contains a two-character string, the letter grade for one of the classes Lydia took followed by the tier of the class. It is guaranteed the first character will be in <code>ABCDE</code> and the second character will be in <code>123</code>.</p>

### 출력 

 <p>Output a single number, Lydia's weighted grade point average. Your answer will be considered correct if it has absolute or relative error at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>6</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-6}$</span></mjx-container>.</p>

