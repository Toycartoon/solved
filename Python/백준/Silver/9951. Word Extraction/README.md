# [Silver III] Word Extraction - 9951 

[문제 링크](https://www.acmicpc.net/problem/9951) 

### 성능 요약

메모리: 36980 KB, 시간: 104 ms

### 분류

자료 구조, 문자열, 집합과 맵, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 파싱, 정규 표현식

### 제출 일자

2025년 10월 13일 14:34:35

### 문제 설명

<p>I am trying to create a dictionary of all the words in common use by my students. To do this, I am planning to feed text from their work, discussion forum entries, and emails through a program that extracts the words.</p>

<p>To make it easy to check if a word has been seen before, I am formatting the text carefully. Firstly I put everything in lower case, then I strip out all punctuation leaving the words separated by single spaces. If the punctuation comes within a word (i.e. there is a letter on either side of it), it is removed. If a "word" consists only of digits, it is ignored. Finally, I sort the words into alphabetical order, removing duplicates.</p>

### 입력 

 <p>Input will consist of a number of lines, each line representing a piece of text to be analysed, and terminated by a single #. No line will contain more than 250 characters.</p>

### 출력 

 <p>Output will be the qualifying words extracted from the text, one per line, in alphabetical order within each set. Each set of words from a piece of text will be separated from the next set by a blank line.</p>

