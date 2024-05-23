# [level 0] 배열 만들기 6 - 181859 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181859) 

### 성능 요약

메모리: 10.8 MB, 시간: 33.77 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 05월 23일 15:19:07

### 문제 설명

<p style="user-select: auto !important;">0과 1로만 이루어진 정수 배열 <code style="user-select: auto !important;">arr</code>가 주어집니다. <code style="user-select: auto !important;">arr</code>를 이용해 새로운 배열 <code style="user-select: auto !important;">stk</code>을 만드려고 합니다.</p>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">i</code>의 초기값을 0으로 설정하고 <code style="user-select: auto !important;">i</code>가 <code style="user-select: auto !important;">arr</code>의 길이보다 작으면 다음을 반복합니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">만약 <code style="user-select: auto !important;">stk</code>이 빈 배열이라면 <code style="user-select: auto !important;">arr[i]</code>를 <code style="user-select: auto !important;">stk</code>에 추가하고 <code style="user-select: auto !important;">i</code>에 1을 더합니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">stk</code>에 원소가 있고, <code style="user-select: auto !important;">stk</code>의 마지막 원소가 <code style="user-select: auto !important;">arr[i]</code>와 같으면 <code style="user-select: auto !important;">stk</code>의 마지막 원소를 <code style="user-select: auto !important;">stk</code>에서 제거하고 <code style="user-select: auto !important;">i</code>에 1을 더합니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">stk</code>에 원소가 있는데 <code style="user-select: auto !important;">stk</code>의 마지막 원소가 <code style="user-select: auto !important;">arr[i]</code>와 다르면 <code style="user-select: auto !important;">stk</code>의 맨 마지막에 <code style="user-select: auto !important;">arr[i]</code>를 추가하고 <code style="user-select: auto !important;">i</code>에 1을 더합니다.</li>
</ul>

<p style="user-select: auto !important;">위 작업을 마친 후 만들어진 <code style="user-select: auto !important;">stk</code>을 return 하는 solution 함수를 완성해 주세요.</p>

<p style="user-select: auto !important;">단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 ≤ 1,000,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">arr</code>의 원소는 0 또는 1 입니다.</li>
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
<td style="user-select: auto !important;">[0, 1, 1, 1, 0]</td>
<td style="user-select: auto !important;">[0, 1, 0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[0, 1, 0, 1, 0]</td>
<td style="user-select: auto !important;">[0, 1, 0, 1, 0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[0, 1, 1, 0]</td>
<td style="user-select: auto !important;">[-1]</td>
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
<th style="user-select: auto !important;">idx</th>
<th style="user-select: auto !important;">arr[idx]</th>
<th style="user-select: auto !important;">stk</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[0, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">[0, 1, 0]</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">따라서 [0, 1, 0]을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">각 작업을 마친 후에 배열의 변화를 나타내면 다음 표와 같습니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">idx</th>
<th style="user-select: auto !important;">arr[idx]</th>
<th style="user-select: auto !important;">stk</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[0, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0, 1, 0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[0, 1, 0, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">[0, 1, 0, 1, 0]</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">따라서 [0, 1, 0, 1, 0]을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">각 작업을 마친 후에 배열의 변화를 나타내면 다음 표와 같습니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">idx</th>
<th style="user-select: auto !important;">arr[idx]</th>
<th style="user-select: auto !important;">stk</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">[0, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">[0]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">[]</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">마지막에 빈 배열이 되었으므로 [-1]을 return 합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 2023년 04월 27일 지문이 수정되었습니다. </p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges