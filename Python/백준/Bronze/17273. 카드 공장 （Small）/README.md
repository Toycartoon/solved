# [Bronze II] 카드 공장 (Small) - 17273 

[문제 링크](https://www.acmicpc.net/problem/17273) 

### 성능 요약

메모리: 32544 KB, 시간: 36 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 6월 18일 00:24:55

### 문제 설명

<p>진서는 CTP 카드 공장의 노동자이다. 공장에는 <em>N</em>개의 카드가 있으며 각 카드에는 앞면과 뒷면에 숫자가 쓰여있다. 공장장 노진의 명령에 따라서 진서는 카드를 뒤집어야 한다. 명령은 <em>M</em>번 내려지게 되며, 명령은 다음과 같다.</p>

<p><strong>“공장장 노진이 <em>K</em>라는 수를 말하게 되면 진서는 <em>N</em>개의 카드 중 보이고 있는 면이 <em>K</em>이하인 카드를 모두 뒤집어야 한다.”</strong></p>

<p>그리고 공장장의 명령이 끝났을 때, 카드의 보이는 면의 수들의 합을 공장장에게 보고해야 한다.</p>

<p>예를 들면 다음 그림과 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/5e43f5c7-2b66-4e72-9887-9f70e8cee266/-/preview/" style="width: 650px; height: 348px;"></p>

<p><strong>카드들은 처음에 모두 앞면이 보여지도록 세팅되어 있고, 카드에 적힌 수는 10,000 이하의 자연수이다.</strong></p>

### 입력 

 <p>첫 번째 줄에 <em>N</em>과 <em>M</em>이 주어진다. (<em>N </em>= 1, <em>M은 </em>100 이하의 자연수)</p>

<p>그리고 다음 <em>N</em>개의 줄에 카드의 앞면 A<sub>i</sub>와 뒷면 B<sub>i</sub>가 주어진다. (A<sub>i</sub>와 B<sub>i</sub>는 10,000 이하의 자연수)</p>

<p>그리고 다음 <em>M</em>개의 줄에 공장장이 말하는 수 <em>K</em>가 주어진다. (<em>K</em>는 10,000 이하의 자연수)</p>

### 출력 

 <p>명령이 끝났을 때 보이고 있는 카드들의 합을 출력한다.</p>

