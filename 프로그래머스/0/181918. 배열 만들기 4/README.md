# [level 0] 배열 만들기 4 - 181918 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181918) 

### 성능 요약

메모리: 10.3 MB, 시간: 6.82 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 30일 00:00:20

### 문제 설명

<p style="user-select: auto !important;">정수 배열 <code style="user-select: auto !important;">arr</code>가 주어집니다. <code style="user-select: auto !important;">arr</code>를 이용해 새로운 배열 <code style="user-select: auto !important;">stk</code>를 만드려고 합니다.</p>

<p style="user-select: auto !important;">변수 <code style="user-select: auto !important;">i</code>를 만들어 초기값을 0으로 설정한 후 <code style="user-select: auto !important;">i</code>가 <code style="user-select: auto !important;">arr</code>의 길이보다 작으면 다음 작업을 반복합니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">만약 <code style="user-select: auto !important;">stk</code>가 빈 배열이라면 <code style="user-select: auto !important;">arr[i]</code>를 <code style="user-select: auto !important;">stk</code>에 추가하고 <code style="user-select: auto !important;">i</code>에 1을 더합니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">stk</code>에 원소가 있고, <code style="user-select: auto !important;">stk</code>의 마지막 원소가 <code style="user-select: auto !important;">arr[i]</code>보다 작으면 <code style="user-select: auto !important;">arr[i]</code>를 <code style="user-select: auto !important;">stk</code>의 뒤에 추가하고 <code style="user-select: auto !important;">i</code>에 1을 더합니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">stk</code>에 원소가 있는데 <code style="user-select: auto !important;">stk</code>의 마지막 원소가 <code style="user-select: auto !important;">arr[i]</code>보다 크거나 같으면 <code style="user-select: auto !important;">stk</code>의 마지막 원소를 <code style="user-select: auto !important;">stk</code>에서 제거합니다.</li>
</ul>

<p style="user-select: auto !important;">위 작업을 마친 후 만들어진 <code style="user-select: auto !important;">stk</code>를 return 하는 solution 함수를 완성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 ≤ 100,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 원소 ≤ 100,000</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[1, 4, 2, 5, 3]</td>
<td style="user-select: auto !important;">[1, 2, 3]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">각 작업을 마친 후에 배열의 변화를 나타내면 다음 표와 같습니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">i</th>
<th style="user-select: auto !important;">arr[i]</th>
<th style="user-select: auto !important;">stk</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">[1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">[1, 4]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">[1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">[1, 2]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">[1, 2, 5]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">[1, 2]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">[1, 2, 3]</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">따라서 [1, 2, 3]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges