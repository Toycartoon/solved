# [Bronze II] Knights Move - 34381 

[문제 링크](https://www.acmicpc.net/problem/34381) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2025년 9월 23일 15:59:48

### 문제 설명

<p>Before we get into the problem, let's go over algebraic notation in chess. Algebraic notation refers to the "names" of the squares on a chessboard. Starting from left to right (from white's perspective), the columns are named a--h. The rows are then named $1$--$8$ in increasing order (again from white's perspective). Each square's "name" is the column letter followed by the row number of that particular square.</p>

<p>In chess, a knight's move is unique. It may move two squares horizontally and one square vertically, or two squares vertically and one square horizontally (with both forming the shape of an L). For example, a knight on d3 can move to c1, b2, b4, c5, e5, f4, f2, and e1. </p>

<p>Your task is as follows: given the position of a knight on a chessboard in algebraic notation, output all of the knight's possible moves.</p>

### 입력 

 <p>The first (and only) line of input is the location of the knight in algebraic notation. It is guaranteed that it will be a valid square on an $8 \times 8$ chessboard.</p>

### 출력 

 <p>Output all of the knight's possible moves in lexicographic order, with each square on its own line. Lexicographic order is a generalization of alphabetical order that means c1 comes before d1, a1 comes before a2, etc.</p>

