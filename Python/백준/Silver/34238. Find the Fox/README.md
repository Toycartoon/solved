# [Silver V] Find the Fox - 34238 

[문제 링크](https://www.acmicpc.net/problem/34238) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 8월 31일 16:18:09

### 문제 설명

<p>$N$행 $M$열의 글자판이 주어지고, 글자판의 각 칸에는 영어 알파벳 <span style="color:#e74c3c;"><code>F</code></span>, <span style="color:#e74c3c;"><code>O</code></span>, <span style="color:#e74c3c;"><code>X</code></span> 중 하나가 쓰여 있다.</p>

<p>당신은 이 글자판에서 영단어 <span style="color:#e74c3c;"><code>FOX</code></span>를 모두 찾아야 한다. <span style="color:#e74c3c;"><code>FOX</code></span>는 다음과 같은 규칙으로 찾아야 한다.</p>

<ol>
	<li>처음에 알파벳 <span style="color:#e74c3c;"><code>F</code></span>를 선택한다.</li>
	<li>1에서 선택한 <code><span style="color:#e74c3c;">F</span></code>와 상하좌우/대각선으로 인접한 알파벳 <code><span style="color:#e74c3c;">O</span></code>를 선택한다.</li>
	<li>2에서 선택한 <code><span style="color:#e74c3c;">O</span></code>와 상하좌우/대각선으로 인접한 알파벳 <span style="color:#e74c3c;"><code>X</code></span>를 선택한다.</li>
	<li>1, 2, 3 에서 선택한 <span style="color:#e74c3c;"><code>F</code></span>,<span style="color:#e74c3c;"> <code>O</code></span>,<span style="color:#e74c3c;"> <code>X</code></span>가 모두 같은 행, 또는 같은 열, 또는 같은 대각선에 있을 경우 <span style="color:#e74c3c;"><code>FOX</code></span>를 하나 찾은 것이다.</li>
</ol>

<p style="text-align: center;"><img alt="" src="" style="height: 205px; width: 600px;"></p>

<p>위 그림은 <span style="color:#e74c3c;"><code>FOX</code></span>를 바르게 찾은 예시이다.</p>

<p style="text-align: center;"><img alt="" src="" style="height: 71px; width: 600px;"></p>

<p>위 그림은 <span style="color:#e74c3c;"><code>FOX</code></span>를 바르게 찾은 예시가 아닌 것들이다.</p>

<p style="text-align: center;"><img alt="" src="" style="height: 171px; width: 600px;"></p>

<p>위 그림처럼 알파벳의 배치에 따라 한 알파벳이 여러 개의 <span style="color:#e74c3c;"><code>FOX</code></span>에 포함될 수도 있다. 겹쳐진 <span style="color:#e74c3c;"><code>FOX</code></span>들도 모두 구분해서 세어야 한다.</p>

<p>글자판이 주어지면 <span style="color:#e74c3c;"><code>FOX</code></span>가 모두 몇 개 있는지 구하여라.</p>

### 입력 

 <p>첫째 줄에 글자판의 행과 열의 수 $N,M$이 공백으로 구분되어 주어진다. $(3 \leq N,M \leq 100)$</p>

<p>둘째 줄부터 $N$개의 줄에 걸쳐 글자판의 각 칸에 쓰인 알파벳이 각 행마다 $M$개 주어진다. 주어지는 알파벳은 모두 영어 알파벳 대문자 <span style="color:#e74c3c;"><code>F</code></span>, <span style="color:#e74c3c;"><code>O</code></span>, <span style="color:#e74c3c;"><code>X</code></span> 중 하나이다.</p>

### 출력 

 <p>첫째 줄에 글자판에서 찾을 수 있는 <span style="color:#e74c3c;"><code>FOX</code></span>의 총 개수를 출력한다.</p>

