# [Bronze III] Kathmandu - 23397 

[문제 링크](https://www.acmicpc.net/problem/23397) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 7월 21일 20:16:38

### 문제 설명

<p>The pandemic is getting better and you can finally do the thing you’ve been dreaming of for the past few years: eat at your favorite restaurant! The restaurant happens to be in Kathmandu, but that’s fine, you can always take a plane.</p>

<p>The problem is that planes almost always leave you restless. You consider yourself properly rested if you can sleep for T uninterrupted minutes, which means you are never awake from a certain moment t to t + T. Also, you’re a very easy sleeper: you can fall asleep at the start of any minute and wake up at the end of any minute.</p>

<p>Of course, if you sleep too much you will miss all the airplane meals! That is unacceptable, as no opportunity for free food should go to waste.</p>

<p>Luckily, the airplane company sent you the whole flight schedule: the duration of the flight, D minutes, the number of meals that are going to be served, M, and the exact time they will serve the meals, y<sub>i</sub>. You need to be awake at the time the meal is being served to be able to eat it, otherwise, the steward will not serve you. Since you’re always hungry, you will devour the meal instantly.</p>

<p>Now you are wondering, for the optimal plane traveling experience, can you get properly rested and still eat all meals during the flight?</p>

### 입력 

 <p>The first line of input contains three integers, T, D, M (1 ≤ T, D ≤ 10<sup>5</sup>, 0 ≤ M ≤ 1000), representing, respectively, the number of minutes you need to sleep without interruption to be properly rested, the duration of the flight and the number of meals that are going to be served during the flight.</p>

<p>Each of the next M lines contains an integer y<sub>i</sub> (0 ≤ y<sub>i</sub> ≤ D). These integers represent the times at which each meal is going to be served, and are given in chronological order.</p>

### 출력 

 <p>Output a line containing one character. If you can get properly rested and still eat all meals during the flight, write the upper case letter ‘<code>Y</code>’; otherwise write the uppercase letter ‘<code>N</code>’.</p>

