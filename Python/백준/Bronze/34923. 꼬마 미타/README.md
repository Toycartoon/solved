# [Bronze I] 꼬마 미타 - 34923 

[문제 링크](https://www.acmicpc.net/problem/34923) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2026년 1월 3일 02:35:51

### 문제 설명

<p>브론즈는 꼬마 미타와 함께 방탈출 게임을 하고 있다.</p>

<p>이 방에 있는 수많은 벽시계가 같은 시각을 가리킨 채로 멈춰 있다. 브론즈는 그중 다른 시각을 가리키는 자명종 시계를 발견했다.</p>

<p>자명종 시계를 다른 시계들과 같은 시각을 가리키도록 맞추면 이곳에서 탈출할 수 있다.</p>

<p>남은 시간이 많지 않기 때문에 시계의 분침을 최소한으로 돌려서 시계를 맞추려고 한다. 시계의 시침은 분침을 돌려서만 움직일 수 있다. 분침을 적어도 얼마나 돌려야 할지 구해보자.</p>

### 입력 

 <p>첫째 줄에 자명종 시계가 가리키는 시각이 <span style="color:#e74c3c;"><code>hh:mm</code></span>의 형식으로 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mi class="mjx-n"><mjx-c class="mjx-c68"></mjx-c><mjx-c class="mjx-c68"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c3B"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>01</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mi data-mjx-auto-op="false">hh</mi></mrow><mo>≤</mo><mn>12</mn><mo>;</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(01 \leq \mathrm{hh} \leq 12;$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mi class="mjx-n"><mjx-c class="mjx-c6D"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>00</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mi data-mjx-auto-op="false">mm</mi></mrow><mo>≤</mo><mn>59</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$00 \leq \mathrm{mm} \leq 59)$</span> </mjx-container></p>

<p>둘째 줄에 벽시계들이 가리키는 시각이 <span style="color:#e74c3c;"><code>hh:mm</code></span>의 형식으로 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mi class="mjx-n"><mjx-c class="mjx-c68"></mjx-c><mjx-c class="mjx-c68"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c3B"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>01</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mi data-mjx-auto-op="false">hh</mi></mrow><mo>≤</mo><mn>12</mn><mo>;</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(01 \leq \mathrm{hh} \leq 12;$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mi class="mjx-n"><mjx-c class="mjx-c6D"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>00</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mi data-mjx-auto-op="false">mm</mi></mrow><mo>≤</mo><mn>59</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$00 \leq \mathrm{mm} \leq 59)$</span> </mjx-container></p>

<p><strong>시침이 가리키는 수의 범위에 유의하라.</strong> 방 안에 있는 모든 시계는 오전과 오후를 구분하지 않는다.</p>

<p>입력으로 주어지는 <span style="color:#e74c3c;"><code>hh:mm</code></span>은 모두 정확히 <span style="color:#e74c3c;"><code>hh</code></span>시 <span style="color:#e74c3c;"><code>mm</code></span>분을 의미한다.</p>

### 출력 

 <p>자명종 시계를 벽시계가 가리키는 시각으로 맞추기 위해 돌려야 하는 분침의 최소 회전 각도(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-texatom texclass="ORD"></mjx-texatom><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2218"></mjx-c></mjx-mo></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow data-mjx-texclass="ORD"></mrow><mrow data-mjx-texclass="ORD"><mo>∘</mo></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">${}^{\circ}$</span></mjx-container>)를 출력한다.</p>

