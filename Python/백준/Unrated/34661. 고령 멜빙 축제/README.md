# [Unrated] 고령 멜빙 축제 - 34661 

[문제 링크](https://www.acmicpc.net/problem/34661) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

분류 없음

### 제출 일자

2025년 10월 26일 19:08:26

### 문제 설명

<div class="center-image"><img alt="" src="" style="max-height:300px;max-width:100%"></div>

<p>미국 힙합신의 대부 <span class="kanye-text">Kanye West</span>가 올해 고령을 방문한다!</p>

<p>그는 고령군의 대표 축제인 고령 멜빙 축제의 Headliner로 서게 되었다. 마지막 하나 남은 그의 공연 티켓을 두고 세원이와 피자가 대결을 하고 있다.</p>

<p>이 대결이란 칸의 일부분에 장애물이 설치되어 있는 $N \times M$ 격자에 $1 \times 1$ 또는 $3 \times 3$ 블록을 놓는 것이다. 장애물과 블록이 겹치게 놓을 수는 없으며, 이미 블록을 놓은 곳에도 다른 블록이 겹치게 놓을 수 없다. 세원이와 피자는 이 규칙에 따라 번갈아 가면서 블록을 놓는다. 자신의 차례에 더 이상 블록을 놓을 수 없는 사람이 게임을 지게 된다.</p>

<p>게임은 세원이가 먼저 시작한다고 할 때, 공연 티켓을 얻어갈 사람은 누구인가?</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 $T$가 주어진다. $(1 \le T \le 10)$</p>

<p>각 테스트 케이스의 첫째 줄에 격자의 크기를 나타내는 정수 $N$과 $M$이 공백으로 구분되어 주어진다. $(1 \le N, M \le 100)$</p>

<p>각 테스트 케이스의 둘째 줄부터 $N$개의 줄에 걸쳐 길이 $M$의 문자열이 주어지며, 문자는 <span style="color:#e74c3c;"><code>.</code></span> 또는 <span style="color:#e74c3c;"><code>x</code></span>이다. $i$행 $j$열의 문자가 <span style="color:#e74c3c;"><code>.</code></span>라면 격자의 해당 칸에 장애물이 없으며 <span style="color:#e74c3c;"><code>x</code></span>라면 장애물이 있다는 뜻이다.</p>

<p>모든 테스트 케이스의 $N \times M$의 합은 $10\,000$을 넘지 않는다.</p>

### 출력 

 <p>각 테스트 케이스마다 공연 티켓을 얻어갈 사람의 이름을 출력한다. 세원이가 대결을 이긴다면 <span style="color:#e74c3c;"><code>sewon</code></span>, 피자가 대결을 이긴다면 <span style="color:#e74c3c;"><code>pizza</code></span>를 출력한다.</p>

