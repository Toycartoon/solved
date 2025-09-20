# [Bronze III] Bad Directions - 34447 

[문제 링크](https://www.acmicpc.net/problem/34447) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 구현, 문자열, 사칙연산

### 제출 일자

2025년 9월 20일 17:40:09

### 문제 설명

<p>Due to the empire's strict control over the galaxy, one of the Rebels droids, A-P5, started to encrypt the distance of hyperspace jumps so that the empire is unable to track the rebel fleet. You are currently being followed by the empire and must calculate the jump to hyperspace. Your incompetent droid co-pilot failed to download the correct decryption program back on the base. Thus, in order to get the proper hyperspace coordinates, you must write a program to decrypt the hyperspace distance you will travel.</p>

<p>Decryption involves two numbers. The first number will be the decryption key, and the second is the number to decrypt. In order to decrypt the number, you must take the key and add it to each digit of the encrypted number. Any carried digits should be removed.</p>

### 입력 

 <p>The first line of input consists of a single integer $t$ ($1 \le t < 100$), which indicates the number of test cases that follow.</p>

<p>Each test case consists of a single line containing two integers: $k$ ($0 \le k \le 9$), which indicates the encryption key, and $n$ ($1 \le n < 2^{31}$), which indicates the encrypted number. $n$ will never have any leading zeroes.</p>

### 출력 

 <p>For each test case, output the decrypted number on its own line. <strong>Be sure to include leading zeroes in your output as necessary so that the output has the same number of digits as $n$.</strong></p>

