# [Bronze II] Ten Player Bingo - 34644 

[문제 링크](https://www.acmicpc.net/problem/34644) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

분류 없음

### 제출 일자

2025년 10월 13일 10:43:21

### 문제 설명

<p>Bingo is a game of chance for multiple players. Each player receives a sheet with some numbers, and a game master then calls out these numbers in a random order. Players cross off the numbers that they have heard, and the first player to cross off all their numbers wins the game. This basic version of the game has a reputation for being, well, a bit sedate. No particular action is required of the players except for not falling asleep.</p>

<p>In this problem we will analyze a specific version of Bingo that requires exactly ten players. In our version, called Ten Player Bingo, each player is numbered from $1$ to $10$. Each player also receives a sheet that contains the integers from $1$ to $100$ that share the same units digit as the units digit of the player’s number. The game master has also been given a sheet that contains every integer from $1$ to $100$ exactly once, but the integers have been shuffled. The game master will read the integers in the order presented on the sheet. When a player has heard all of their integers, they shout “BINGO” and leave the game. The game continues until everyone has shouted “BINGO”.</p>

<p>Who is the last player to shout “BINGO”?</p>

### 입력 

 <p>The first and only line of input contains $100$ integers, each ranging from $1$ to $100$. It is guaranteed each integer appears exactly once.</p>

### 출력 

 <p>Output a single integer, which is the number of the player who shouts “BINGO” last.</p>

