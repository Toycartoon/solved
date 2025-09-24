# [Bronze II] Turnering - 26943 

[문제 링크](https://www.acmicpc.net/problem/26943) 

### 성능 요약

메모리: 34900 KB, 시간: 56 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 9월 25일 04:01:18

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6bb1553b-b271-4e14-86f7-3013477fe85b/-/preview/"></p>

<p>Om man vill ordna t.ex. en bordshockeyturnering där alla möter alla kan man använda sig av ett praktiskt rotationsschema som kallas round robin. Det går till så att spelarna i den första omgången möter varandra enligt figuren ovan (vi antar att antalet spelare $n$ är jämnt). När första omgången är klar förflyttar sig alla spelare ett steg medurs, utom spelaren i det nedre vänstra hörnet som hoppas över (därav namnet, man förflyttar sig "runt" Robin, d.v.s. den sista spelaren). Med detta rotationsschema är man garanterad att alla har mött alla precis en gång efter $n-1$ omgångar.</p>

<p>Din uppgift är att skriva ett program som skriver ut vilka spelare som ska möta vilka en viss omgång.</p>

### 입력 

 <p>Indata består av två heltal: antal spelare i turneringen (ett jämnt tal $n$ mellan $2$ och $100$) och omgången (mellan $1$ och $n-1$).</p>

### 출력 

 <p>Programmet ska skriva ut $n/2$ rader som beskriver vilka som möter vilka, där varje rad är på formatet <code>a-b</code>. Ordningen på matcherna spelar ingen roll.</p>

