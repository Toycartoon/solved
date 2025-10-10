# [Bronze II] Copier Reduction - 4623 

[문제 링크](https://www.acmicpc.net/problem/4623) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 10월 10일 13:21:39

### 문제 설명

<p>What do you do if you need to copy a 560x400mm image onto a standard sheet of US letter-size paper (which is about 216x280mm), while keeping the image as large as possible? You can rotate the image 90 degrees (so that it is in "landscape" mode), then reduce it to 50% of its original size so that it is 200x280mm. Then it will fit on the paper without overlapping any edges. Your job is to solve this problem in general.</p>

### 입력 

 <p>The input consists of one or more test cases, each of which is a single line containing four positive integers A, B, C, and D, separated by a space, representing an AxBmm image and a CxDmm piece of paper. All inputs will be less than one thousand. Following the test cases is a line containing four zeros that signals the end of the input.</p>

### 출력 

 <p>For each test case, if the image fits on the sheet of paper without changing its size (but rotating it if necessary), then the output is 100%. If the image must be reduced in order to fit, the output is the largest integer percentage of its original size that will fit (rotating it if necessary). Output the percentage exactly as shown in the examples below. You can assume that no image will need to be reduced to less than 1% of its original size, so the answer will always be an integer percentage between 1% and 100%, inclusive.</p>

