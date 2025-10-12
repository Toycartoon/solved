# [Bronze I] 드론 조작 - 32932 

[문제 링크](https://www.acmicpc.net/problem/32932) 

### 성능 요약

메모리: 32412 KB, 시간: 52 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 10월 12일 20:11:31

### 문제 설명

<p>좌표평면의 원점 위에 드론이 있다. 이 드론에는 네 가지 명령어를 입력할 수 있다. 입력할 수 있는 명령어는 다음과 같다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>U</code></span>: 드론의 $y$좌표를 $1$ 증가시킨다.</li>
	<li><span style="color:#e74c3c;"><code>D</code></span>: 드론의 $y$좌표를 $1$ 감소시킨다.</li>
	<li><span style="color:#e74c3c;"><code>R</code></span>: 드론의 $x$좌표를 $1$ 증가시킨다.</li>
	<li><span style="color:#e74c3c;"><code>L</code></span>: 드론의 $x$좌표를 $1$ 감소시킨다.</li>
</ul>

<p>좌표평면 위에는 장애물도 $N$개 있다. 만약 드론이 이동하려는 칸에 장애물이 있다면 이동하지 못하고 제자리에 있게 된다. 장애물들의 위치와 드론에 입력된 명령어가 주어졌을 때 드론의 최종 위치를 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 장애물의 개수 $N$과 입력된 명령어의 개수 $K$가 공백으로 구분되어 주어진다. $(1 \leq N,K \leq 500)$</p>

<p>두 번째 줄부터 $N$개의 줄에 걸쳐 $i$번째 장애물의 $x$좌표와 $y$좌표를 나타내는 두 정수 $x_i$와 $y_i$가 공백으로 구분되어 주어진다. 단, 모든 장애물들의 위치는 다르고 원점 위에는 장애물이 없다. $(-500 \leq x_i, y_i \leq 500)$</p>

<p>$N+2$번째 줄에는 드론에 입력된 명령어들이 문자열로 주어진다. 주어진 문자열의 각 문자는 <span style="color:#e74c3c;"><code>U</code></span>, <span style="color:#e74c3c;"><code>D</code></span>, <span style="color:#e74c3c;"><code>R</code></span>, <span style="color:#e74c3c;"><code>L</code></span>중 하나이다.</p>

### 출력 

 <p>모든 명령어가 입력되었을 때, 드론이 있는 위치의 $x$좌표와 $y$좌표를 공백으로 구분하여 출력한다.</p>

