# [Silver IV] Poetry - 6906 

[문제 링크](https://www.acmicpc.net/problem/6906) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2025년 10월 17일 18:15:18

### 문제 설명

<p>A simple poem consists of one or more four-line verses. Each line consists of one or more words consisting of upper or lowercase letters, or a combination of both upper and lowercase letters. Adjacent words on a line are separated by a single space.</p>

<p>We define the last syllable of a word to be the sequence of letters from the last vowel (<code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, or <code>u</code>, but not <code>y</code>) to the end of the word. If a word has no vowel, then the last syllable is the word itself. We say that two lines rhyme if their last syllables are the same, ignoring case.</p>

<p>You are to classify the form of rhyme in each verse. The form of rhyme can be <em>perfect, even, cross, shell</em>, or <em>free</em>:</p>

<ul>
	<li>perfect rhyme: the four lines in the verse all rhyme</li>
	<li>even rhyme: the first two lines rhyme and the last two lines rhyme</li>
	<li>cross rhyme: the first and third lines rhyme, as do the second and fourth</li>
	<li>shell rhyme: the first and fourth lines rhyme, as do the second and third</li>
	<li>free rhyme: any form that is not perfect, even, cross, or shell.</li>
</ul>

<p>The first line of the input file contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, the number of verses in the poem, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 5$</span></mjx-container>. The following <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4N$</span></mjx-container> lines of the input file contain the lines of the poem. Each line contains at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$80$</span></mjx-container> letters of the alphabet and spaces as described above.</p>

<p>The output should have <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines. For each verse of the poem there should be a single line containing one of the words <code>perfect</code>, <code>even</code>, <code>cross</code>, <code>shell</code>, or <code>free</code> describing the form of rhyme in that verse.</p>

### 입력 

 Empty

### 출력 

 Empty

