# [Bronze II] Klass - 7173 

[문제 링크](https://www.acmicpc.net/problem/7173) 

### 성능 요약

메모리: 32412 KB, 시간: 168 ms

### 분류

구현, 문자열

### 제출 일자

2025년 10월 12일 01:38:13

### 문제 설명

<p>Klass on täis õpilasi, kes istuvad ridade ja veergude kaupa. Iga õpilane huvitub mingil määral arvutitest ja spordist. Õpilased, keda huvitab ainult sport, on tähistatud $0$-ga. Õpilased, keda huvitavad ainult arvutid, on tähistatud $9$-ga. Teised õpilased on vastavalt oma huvi määrale tähistatud arvudega $1$--$8$.</p>

<p>Sarnaste huvidega õpilased lobisevad omavahel ja ei pööra õpetaja jutule tähelepanu. Mida väiksem on kahe naaberõpilase huvide erinevus, seda rohkem nad lobisevad. Seega, kui meil on näiteks õpilane huvidega $7$, keda ümbritsevad teised õpilased huvidega $7$, ei pane ta üldse õpetajat tähele.</p>

<p>Iga õpilase tähelepanu on määratud tema ja tema naabrite huvide erinevuste keskmisega. Naabriteks loetakse õpilasi, kes istuvad antud õpilasest vahetult ees, taga, vasakul või paremal.</p>

<p>Kogu klassi tähelepanu määr võrdub üksikute õpilaste tähelepanude summaga. Kirjutada programm, mis selle leiab.</p>

### 입력 

 <p>Tekstifaili esimesel real on arvud $M$ ja $N$ ($1 \le M \le 200$, $1 \le N \le 200$), mis näitavad ridade ja veergude arvu klassis. Klassis on vähemalt kaks õpilast. Järgmisel $M$ real on igaühel täpselt $N$ märki $0$ kuni $9$.</p>

### 출력 

 <p>Tekstifaili väljastada üks arv: kogu klassi tähelepanu määr. Väljastatud vastus ei tohi täpsest erineda rohkem kui $0{,}0001$ võrra.</p>

