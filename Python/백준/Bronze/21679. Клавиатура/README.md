# [Bronze III] Клавиатура - 21679 

[문제 링크](https://www.acmicpc.net/problem/21679) 

### 성능 요약

메모리: 38072 KB, 시간: 52 ms

### 분류

구현

### 제출 일자

2025년 6월 23일 14:32:55

### 문제 설명

<p>Всем известно, что со временем клавиши на клавиатуре начинают залипать, а для нажатий приходиться использовать большую силу. Это связано с тем, что каждая клавиша на клавиатуре выдерживает определенное число нажатий.</p>

<p>Вам требуется написать программу, определяющую, какие клавиши уже сломались в процессе эксплуатации клавиатуры.</p>

### 입력 

 <p>Первая строка входного файла содержит целое число n (1 ≤ n ≤ 100) – количество клавиш на клавиатуре. Вторая строка содержит n целых чисел с<sub>1</sub>, с<sub>2</sub>…с<sub>n</sub>, где с<sub>i</sub> (1 ≤ с<sub>i</sub> ≤ 100000) – количество нажатий, выдерживаемых i-ой клавишей.</p>

<p>Третья строка содержит целое число k (1 ≤ k ≤ 100000) – количество нажатий. Последняя строка содержит k целых чисел p<sub>j</sub> (1 ≤ p<sub>j</sub> ≤ n) – последовательность нажатых клавиш.</p>

### 출력 

 <p>В выходной файл выведите n строк, содержащих информацию об исправности клавиш. Если i-ая клавиша сломалась, i-ая строка должна содержать слово “yes” (без кавычек), если же клавиша работоспособна – слово “no”.</p>

