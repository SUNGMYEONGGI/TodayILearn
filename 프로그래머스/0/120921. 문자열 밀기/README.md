# [level 0] 문자열 밀기 - 120921 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120921) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 05월 01일 18:52:39

### 문제 설명

<p style="user-select: auto !important;">문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 <code style="user-select: auto !important;">A</code>와 <code style="user-select: auto !important;">B</code>가 매개변수로 주어질 때, <code style="user-select: auto !important;">A</code>를 밀어서 <code style="user-select: auto !important;">B</code>가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 <code style="user-select: auto !important;">B</code>가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 &lt; <code style="user-select: auto !important;">A</code>의 길이 = <code style="user-select: auto !important;">B</code>의 길이 &lt; 100</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">A</code>, <code style="user-select: auto !important;">B</code>는 알파벳 소문자로 이루어져 있습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">A</th>
<th style="user-select: auto !important;">B</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"hello"</td>
<td style="user-select: auto !important;">"ohell"</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"apple"</td>
<td style="user-select: auto !important;">"elppa"</td>
<td style="user-select: auto !important;">-1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"atat"</td>
<td style="user-select: auto !important;">"tata"</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"abc"</td>
<td style="user-select: auto !important;">"abc"</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">"hello"를 오른쪽으로 한 칸 밀면 "ohell"가 됩니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">"apple"은 몇 번을 밀어도 "elppa"가 될 수 없습니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">"atat"는 오른쪽으로 한 칸, 세 칸을 밀면 "tata"가 되므로 최소 횟수인 1을 반환합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #4</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">"abc"는 밀지 않아도 "abc"이므로 0을 반환합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 공지 - 2023년 4월 24일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges