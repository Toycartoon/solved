# [Gold II] PLATiNA::LAB - 34931 

[문제 링크](https://www.acmicpc.net/problem/34931) 

### 성능 요약

메모리: 102264 KB, 시간: 1060 ms

### 분류

구현, 애드 혹, 시뮬레이션, 홀짝성

### 제출 일자

2025년 12월 24일 19:30:27

### 문제 설명

<p>플래티넘은 은하 대학교의 교수로 자신의 이름을 딴 연구소인 플래티나 랩(PLATiNA::LAB)에서 미생물 연구를 하고 있다.</p>

<p>플래티넘은 최근에 미생물 <span style="color:#e74c3c;"><code>A</code></span>와 <span style="color:#e74c3c;"><code>B</code></span>에 대해서 연구를 하고 있는데, 두 종류의 미생물을 일렬로 배치하고 관찰하면 한 시간마다 미생물에 재미있는 변화가 일어난다는 사실을 알게 되었다.</p>

<ul>
<li>만약 <span style="color:#e74c3c;"><code>A</code></span>의 양 옆에 <span style="color:#e74c3c;"><code>B</code></span>가 두 마리 있었다면 한 시간 뒤 <span style="color:#e74c3c;"><code>B</code></span>로 변하게 된다.</li>
<li>만약 <span style="color:#e74c3c;"><code>B</code></span>의 양 옆에 <span style="color:#e74c3c;"><code>A</code></span>가 두 마리 있었다면 한 시간 뒤 <span style="color:#e74c3c;"><code>A</code></span>로 변하게 된다.</li>
</ul>

<p>예를 들어 플래티넘이 처음에 미생물을 <code><span style="color:#e74c3c;">ABABAAA</span></code> 순서대로 놓았다면 1시간 뒤에는 <span style="color:#e74c3c;"><code>AABAAAA</code></span>가 되고, 2시간 뒤에는 <span style="color:#e74c3c;"><code>AAAAAAA</code></span>가 된다.</p>

<p>대학원생 브론즈는 플래티넘의 지시에 따라 $N$개의 미생물을 일렬로 배치한 후에 $T$시간이 지나고 나서 변화한 상태를 기록해야 했지만, 잠에 드는 바람에 결과를 기록하지 못했다. 브론즈를 위해 $T$시간이 지난 후의 미생물의 상태를 대신 기록해 주자.</p>

### 입력 

 <p>첫째 줄에 미생물의 수 $N$과 시간 $T$가 공백으로 구분되어 주어진다. $(1\leq T\leq N\leq 10^6)$</p>

<p>둘째 줄에 미생물의 배치를 의미하는 길이 $N$의 문자열이 주어진다. 이 문자열은 <code><span style="color:#e74c3c;">A</span></code>와 <code><span style="color:#e74c3c;">B</span></code>로만 이루어져 있다.</p>

### 출력 

 <p>$T$시간 뒤의 미생물의 상태를 출력한다.</p>

