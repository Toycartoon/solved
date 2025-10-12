# [Unrated] 연결그래프의 모든 간선의 저항이 1Ω일 경우 간선으로 직접 이어진 모든 쌍의 점 A, B 에 대해 A와 B 사이의 합성저항 값의 총합을 구한 뒤 소수점 넷째자리에서 반올림한 값을 출력하는 문제 - 17109 

[문제 링크](https://www.acmicpc.net/problem/17109) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

분류 없음

### 제출 일자

2025년 10월 13일 01:37:17

### 문제 설명

<h1 dir="ltr"><b id="docs-internal-guid-680b364c-7fff-23a1-d9f4-d55d49af48cf">1부터 <em>n</em>까지의 번호가 매겨진 <em>n</em>개의 점과 <em>m</em>개의 간선들로 이루어진 연결그래프가 주어진다. 두 점을 직접 잇는 간선은 최대 1개이며, 자기 자신을 잇는 루프는 없다. </b></h1>

<h1 dir="ltr"><b>여기서 이 그래프의 각 간선을 저항이 1Ω인 도선들로 생각하면 이 그래프를 전기회로로 생각할 수 있다.</b></h1>

<h1 dir="ltr"><b id="docs-internal-guid-680b364c-7fff-23a1-d9f4-d55d49af48cf">이 전기회로에 대하여, 간선으로 직접 이어진 모든 쌍의 점 <em>A, B </em>에 대해, <em>A</em>와 <em>B</em> 사이의 합성저항 값의 총합을 Ω 단위로 구하시오. 즉, <em>m</em>개 쌍의 점 사이의 합성저항의 총합을 구하면 된다.</b></h1>

### 입력 

 <h1 dir="ltr"><b id="docs-internal-guid-f3048aab-7fff-8d45-6dd6-5db8242fcb0a">첫 줄에 점의 개수 <em>m </em>과 간선의 개수 <em>n </em>이 주어진다. (</b><strong><em>m </em>과<em> n</em> 은 1000을 넘지 않는다.)</strong></h1>

<h1 dir="ltr"><b id="docs-internal-guid-f3048aab-7fff-8d45-6dd6-5db8242fcb0a">두 번째 줄부터 <em>n</em>+1 번째 줄까지는 간선으로 이어진 두 점의 번호가 주어진다.</b></h1>

### 출력 

 <h1 dir="ltr"><b id="docs-internal-guid-eb4308cb-7fff-cced-4b15-394539040d89">간선으로 직접 이어진 모든 쌍의 점 <em>A, B </em>에 대해 합성저항 값의 합을 소수점 넷째자리에서 반올림한 값을 출력한다.</b></h1>

