# [Silver III] 신나는 분수 계산 - 9215 

[문제 링크](https://www.acmicpc.net/problem/9215) 

### 성능 요약

메모리: 41804 KB, 시간: 120 ms

### 분류

수학, 구현, 문자열, 정수론, 파싱, 임의 정밀도 / 큰 수 연산, 유클리드 호제법

### 제출 일자

2025년 9월 5일 02:57:25

### 문제 설명

<p>유리수는 두 정수의 비로 나타낼 수 있다. 분자(n)와 분모(d)가 주어지면 이 분수를 n/d으로 쓴다. 유리수의 표현 방법은 유일하지 않다. 예를 들어, 1/2과 2/4는 그 값이 같다. 어떤 유리수 표현법 n/d이 gcd(|n|, |d|) = 1이라면 이것이 "기약분수로 표현되었다"라고 한다. 따라서 1/2은 기약분수로 표현되었지만 2/4는 아니다.</p>

<p>유리수의 덧셈은 다음과 같이 정의된다. 오른쪽 항이 기약분수로 표현되어 있다는 보장은 없음에 주목하라.</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mfrac space="3"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mfrac space="4"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mrow><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-msub space="3"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mfrac><msub><mi>n</mi><mn>1</mn></msub><msub><mi>d</mi><mn>1</mn></msub></mfrac><mo>+</mo><mfrac><msub><mi>n</mi><mn>2</mn></msub><msub><mi>d</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><msub><mi>d</mi><mn>1</mn></msub></mrow><mrow><msub><mi>d</mi><mn>1</mn></msub><msub><mi>d</mi><mn>2</mn></msub></mrow></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[\frac{n_1}{d_1} + \frac{n_2}{d_2} = \frac{n_1d_2 + n_2d_1}{d_1d_2}\]</span> </mjx-container></p>

<p>분자가 분모보다 크거나 같은 유리수는 대분수 꼴로 표현할 수 있는데, 이것은 정수부와 소수부로 이루어 진다. 예를 들어, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-texatom></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mrow data-mjx-texclass="ORD"><mfrac><mrow data-mjx-texclass="ORD"><mn>1</mn></mrow><mrow data-mjx-texclass="ORD"><mn>3</mn></mrow></mfrac></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5 {{1}\over{3}}$</span></mjx-container>은 16/3과 같은 값을 가지는 대분수 표현이다.</p>

<p>당신이 할 일은 유리수열을 읽어 그 합을 출력하는 것이다.</p>

### 입력 

 <p>입력은 몇 개의 테스트로 구성된다. 각 테스트의 정보는 첫 줄에 n(1 ≤ n < 1000)을 포함한다. n = 0인 경우 입력이 끝난다.</p>

<p>다음 n개의 줄은 공백이 없는 하나의 문자열이다. 각 문자열은 유리수 하나를 나타내며, 다음 세 형태 중 하나이고 기약분수로 표현되지 않을 수 있다 (w, n과 d는 정수이다: 0 ≤ w,n < 1000, 1 ≤ d < 1000).</p>

<ul>
	<li>w,n/d: (w * d + n) / d와 값이 같은 대분수</li>
	<li>n/d: 정수부가 0인 유리수</li>
	<li>w: 소수부가 0인 정수</li>
</ul>

### 출력 

 <p>출력은 화면에 나온 대로 테스트 번호를 포함하여 합을 기약분수로 표현하여 출력한다. 만약 합의 정수부나 소수부가 없다면 각 부분을 생략하여 출력한다. 특수한 경우로, 정수부와 소수부가 모두 없다면 0을 출력해야 한다.</p>

