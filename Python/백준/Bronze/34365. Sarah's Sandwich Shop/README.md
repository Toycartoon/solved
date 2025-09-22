# [Bronze I] Sarah's Sandwich Shop - 34365 

[문제 링크](https://www.acmicpc.net/problem/34365) 

### 성능 요약

메모리: 32412 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2025년 9월 23일 01:13:03

### 문제 설명

<p>Sarah's Sandwiches is the hottest new restaurant Golden, and every student at Mines can't wait to try it. Like any reputable sandwich shop, they want a phone number that cleverly spells out a word or phrase so that customers can more easily recall their phone number. </p>

<p>The owners have a lot of ideas for what their phone number might spell out, but they're too busy making sandwiches to figure out the corresponding phone numbers which would be the most commercially viable.</p>

<p>You've been tasked to help them out, and create a program which converts a word to a telephone number using the standard keypad:</p>

<table class="table table-bordered td-center table-center-20">
	<tbody>
		<tr>
			<td>$2$</td>
			<td>A B C</td>
		</tr>
		<tr>
			<td>$3$</td>
			<td>D E F</td>
		</tr>
		<tr>
			<td>$4$</td>
			<td>G H I</td>
		</tr>
		<tr>
			<td>$5$</td>
			<td>J K L</td>
		</tr>
		<tr>
			<td>$6$</td>
			<td>M N O</td>
		</tr>
		<tr>
			<td>$7$</td>
			<td>P Q R S</td>
		</tr>
		<tr>
			<td>$8$</td>
			<td>T U V</td>
		</tr>
		<tr>
			<td>$9$</td>
			<td>W X Y Z</td>
		</tr>
	</tbody>
</table>

<p>To perform the conversion, every character in the given word is mapped to the single corresponding digit in the same row of the table above. For example, the word "MINES" would be mapped to the phone number "$64637$" because the letter "M" maps to the digit "$6$", the letter "I" maps to the digit "$4$", the letter "N" maps to the digit "$6$", and so on.</p>

### 입력 

 <p>The first line of input will be an integer $1 \leq N \leq 1\,000$ indicating the number of different words that the owners' of Sarah's Sandwiches are considering to use for their phone number. Each of the following $N$ lines contains a word of length $1 \le M \leq 45$, that consists only of upper and lowercase letters in the English alphabet (A-Z, a-z).</p>

### 출력 

 <p>The output should contain $N$ lines with the $i^{th}$ line containing the phone number conversion of the $i^{th}$ word of the input.</p>

<p>Note that outputted phone numbers may not match the standard phone number length.</p>

