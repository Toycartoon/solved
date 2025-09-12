# [Bronze II] Mines Motor Company - 34309 

[문제 링크](https://www.acmicpc.net/problem/34309) 

### 성능 요약

메모리: 32412 KB, 시간: 100 ms

### 분류

수학, 구현, 문자열, 사칙연산

### 제출 일자

2025년 9월 12일 23:15:35

### 문제 설명

<p>A group of highly successful Mines Computer Science and Mechanical Engineering graduates decided to create an electric car company called Mines Motor Company. The company has been very successful and recently opened their production plant. In the production plant, there are multiple workstations in a grid layout. The rows and columns of the grid are both labeled using uppercase letters (A-Z for rows from top to bottom, and A-Z for columns from left to right). Figure <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> shows this grid. Travel between two workstations can only occur via the horizontal and vertical paths, and each workstation is exactly <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> unit away from its four cardinally-adjacent workstations (above, below, right, and left). For instance to go from AA to BB a product must first visit either AB or BA before proceeding on to BB, resulting in a distance of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0acb30b7-e40a-4f7d-be0e-b528f64bf488/-/preview/" style="width: 400px; height: 397px;"></p>

<p style="text-align: center;"><strong>Figure 1</strong>: The production plant grid layout.</p>

<p>In the current layout, the engineers noticed that products must travel a long distance through the plant to be completed. To optimize the location of the workstations, the company wants to track a single product's travel within the plant. As a start for our tracking software, we need to program an algorithm that answers the following question:</p>

<p>Given the order of workstations that a product has to visit, what is the total distance traveled?</p>

### 입력 

 <p>The first line of input is <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$ \leq N \leq 100\,000$</span></mjx-container>, the number of workstations that have to be visited. The remaining <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines are the locations of the workstations in the format <code>[ROW][COLUMN]</code> where <code>[ROW]</code> and <code>[COLUMN]</code> are both single uppercase letters indicating the row and column of the workstation. You can assume that the product is already at the first workstation and will stay at the last workstation.</p>

### 출력 

 <p>Output an integer representing the total distance traveled to complete that path. </p>

