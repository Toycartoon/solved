# [Gold V] Pindala - 7196 

[문제 링크](https://www.acmicpc.net/problem/7196) 

### 성능 요약

메모리: 137152 KB, 시간: 828 ms

### 분류

기하학, 다각형의 넓이

### 제출 일자

2025년 9월 22일 02:16:47

### 문제 설명

<p>Ruudulisele paberile saab joonistada kinniseid hulknurki, järgides ainult ruudustiku jooni. See tähendab, et kõik hulknurga küljed on horisontaalsed või vertikaalsed ning täisarvuliste pikkustega. Iga hulknurga joonistamise eeskiri on antud sõnena üksikute lõikude kaupa: <code>W</code> — vasakule, <code>N</code> — üles, <code>E</code> — paremale, <code>S</code> — alla. On teada, et hulknurk ei puutu ega lõika iseennast, s.t iga punkt hulknurga kirjelduses esineb ainult uks kord.</p>

<p>Hulknurk on ka ortogonaalselt kumer. See tähendab, et iga horisontaalne või vertikaalne sirge, mis hulknurka lõikab, siseneb sellesse ja väljub sellest ainult ühe korra. Lihtsustatult, hulknurk ei sisalda näiteks U-kujulisi osi. Näiteks <code>NNWSWSEE</code> (joonisel vasakul) annab ortogonaalselt kumera hulknurga, aga <code>SSEEENNWSWNW</code> (joonisel paremal) mitte.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/91a5eefa-b293-4b0d-9544-20036a93c15f/-/preview/" style="width: 356px; height: 93px;"></p>

<p>Leida selliselt antud hulknurga pindala.</p>

### 입력 

 <p>Tekstifailis on täpselt kaks rida. Esimesel real on lõikude arv K (4 ≤ K ≤ 1 000 000). Teisel real on sõne pikkusega K, mis koosneb märkidest <code>N</code>, <code>E</code>, <code>S</code> ja <code>W</code>.</p>

### 출력 

 <p>Tekstifaili väljastada täpselt üks täisarv, sisendis kirjeldatud hulknurga pindala.</p>

