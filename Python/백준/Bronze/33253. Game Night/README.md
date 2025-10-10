# [Bronze II] Game Night - 33253 

[문제 링크](https://www.acmicpc.net/problem/33253) 

### 성능 요약

메모리: 35344 KB, 시간: 444 ms

### 분류

구현, 문자열

### 제출 일자

2025년 10월 10일 20:11:28

### 문제 설명

<p>Every Saturday, Geronimo is organizing a game night for all his friends. One after the other, his friends keep asking him for his Wi-Fi password. Because Geronimo has many friends and does not want to be continuously disturbed just to share his password, he decides to grab an old box of fridge magnets that have the shape of letters, and spells out the password on the fridge.</p>

<p>Since Geronimo cares about the security of his Wi-Fi network, he wants to change the Wi-Fi password after the game night, to make sure that his password is not shared with strangers who will then use his network. However, that means he also has to update the password displayed on the fridge. The box with fridge magnets is a complete mess, so Geronimo does not want to spend too much time searching through the box for the right letters, especially when a new password contains some letters that were also in the old password.</p>

<p>Given Geronimo's old and new Wi-Fi password, can you calculate how many letters he has to search for in the box to spell out the new password on the fridge?</p>

### 입력 

 <ul>
	<li>One line with one integer: $1 \leq n \leq 10^6$, the length of the passwords. Both passwords have the same length.</li>
	<li>Two lines with each one password of length $n$. The passwords only contain lowercase letters ('<code>a</code>' through '<code>z</code>').</li>
</ul>

### 출력 

 <p>One line, containing one integer: the number of letters that cannot be re-used between the two passwords.</p>

