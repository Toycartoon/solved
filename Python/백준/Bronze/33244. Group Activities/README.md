# [Bronze I] Group Activities - 33244 

[문제 링크](https://www.acmicpc.net/problem/33244) 

### 성능 요약

메모리: 38152 KB, 시간: 68 ms

### 분류

유클리드 호제법, 수학, 정수론

### 제출 일자

2025년 9월 4일 16:28:50

### 문제 설명

<p>The lockdown is still in place, so organizing the yearly group excursion is a no-go. Instead, the study association is organizing the Fictional Programmer Convention (FPC): a digital event where programmers can meet other programmers while performing various digital activities. You are on the committee that is concerned with planning the events of the FPC. They give you the following task: determine how many programmers you want to invite.</p>

<p>The committee will plan different activities that will take place for all participants at the same time, with the participants divided into groups. Each activity requires an exact number of participants per group. For example, a variety of digital games are played in groups of 5, a pop quiz about programming history is played in teams of 3, and a workshop on clean coding practices is given in separate sessions of 31.</p>

<p>Because of a limited budget, you want to invite as few people as possible, but still at least one person of course. Can you determine the exact number of people you must invite to exactly fill each activity?</p>

### 입력 

 <p>\item One line containing one integer $ 1 \leq n \leq 10^5 $, the number of activities organized. \item For each of the $ n $ activities, one line with an integer $ 1 \leq i \leq 10^{18} $: this activity requires exactly $ i $ participants per group.</p>

### 출력 

 <p>An integer indicating the smallest number of people $p$ you can invite, such that each activity can exactly fill a number of groups. It is guaranteed that $ 1 \leq p \leq 10^{18} $.</p>

