# [Bronze III] 퐁당퐁당 1 - 17944 

[문제 링크](https://www.acmicpc.net/problem/17944) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

수학, 구현

### 제출 일자

2025년 7월 18일 22:17:39

### 문제 설명

<p>퐁당퐁당은 술게임 중 팀워크가 가장 중요한 MT 단골 게임이다. 매 차례마다 지정된 수의 팔을 동시에 들어야 하는데, 이를 실패하면 팔을 들어야했던 사람과 실수로 팔을 든 사람 모두 연좌제로 마셔야 하기 때문이다. 퐁당퐁당 게임의 규칙은 아래와 같다.</p>

<ol>
	<li>1번 사람부터 N번 사람까지 순서대로 총 N명의 사람들이 원 모양을 이루어 반시계방향으로 둘러앉는다. 이 때 모든 사람들은 원의 중앙을 바라보고 앉는다.</li>
	<li>게임은 1번 사람의 왼팔부터 시작하여 원의 바깥에서 보았을 때 왼쪽에서 오른쪽으로 진행한다. </li>
	<li>첫 번째 차례 이후 매 차례마다 가장 오른쪽 사람이 들었던 팔의 다음 팔부터 진행하고, 순서대로 지정된 수만큼의 팔을 들어올린다.</li>
	<li>게임을 시작할 때 들어야 하는 팔의 갯수는 1개이다. 시작하여 차례가 지날 때마다 들어야 하는팔의 개수는 1씩 증가한다.</li>
	<li>들어야 하는 팔의 갯수가 2 × N 개가 되었다면 다음 차례부터 1씩 감소시킨다.</li>
	<li>들어야 하는 팔의 갯수가 1개가 되었다면 다음 차례부터 다시 1씩 증가시킨다.<br>
	즉, 매 차례에 들어야 할 팔의 갯수는 1 이상 2 × N 이하로 유지된다.</li>
</ol>

<p>엠티에서 퐁당퐁당 게임을 하던 지원이는 게임을 못하는 친구들 때문에 술을 너무 많이 마셔서 각 차례마다 몇 개의 팔을 들어야 하는지 계산하려고 한다. 지원이가 살아남을 수 있도록 해당 차례에서 사람들이 들어야 하는 팔의 개수를 정확히 계산해보자.</p>

### 입력 

 <p>첫 번째 줄에 게임에 참여하는 사람 수 N과 계산해야하는 차례 T가 정수로 주어진다. (2 ≤ N ≤ 1000, 1 ≤ T ≤ 10<sup>7</sup>)</p>

### 출력 

 <p>해당 차례에 들어야 하는 정확한 팔의 개수를 계산하여 출력한다.</p>

