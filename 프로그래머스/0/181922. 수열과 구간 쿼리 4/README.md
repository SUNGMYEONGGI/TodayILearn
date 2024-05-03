# [level 0] 수열과 구간 쿼리 4 - 181922 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181922?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 26.12 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 05월 03일 16:38:26

### 문제 설명

<p style="user-select: auto !important;">정수 배열 <code style="user-select: auto !important;">arr</code>와 2차원 정수 배열 <code style="user-select: auto !important;">queries</code>이 주어집니다. <code style="user-select: auto !important;">queries</code>의 원소는 각각 하나의 <code style="user-select: auto !important;">query</code>를 나타내며, <code style="user-select: auto !important;">[s, e, k]</code> 꼴입니다.</p>

<p style="user-select: auto !important;">각 <code style="user-select: auto !important;">query</code>마다 순서대로 <code style="user-select: auto !important;">s</code> ≤ <code style="user-select: auto !important;">i</code> ≤ <code style="user-select: auto !important;">e</code>인 모든 <code style="user-select: auto !important;">i</code>에 대해 <code style="user-select: auto !important;">i</code>가 <code style="user-select: auto !important;">k</code>의 배수이면 <code style="user-select: auto !important;">arr[i]</code>에 1을 더합니다.</p>

<p style="user-select: auto !important;">위 규칙에 따라 <code style="user-select: auto !important;">queries</code>를 처리한 이후의 <code style="user-select: auto !important;">arr</code>를 return 하는 solution 함수를 완성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 ≤ 1,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 ≤ <code style="user-select: auto !important;">arr</code>의 원소 ≤ 1,000,000</li>
</ul></li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">queries</code>의 길이 ≤ 1,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 ≤ <code style="user-select: auto !important;">s</code> ≤ <code style="user-select: auto !important;">e</code> &lt; <code style="user-select: auto !important;">arr</code>의 길이</li>
<li style="user-select: auto !important;">0 ≤ <code style="user-select: auto !important;">k</code> ≤ 5</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr</th>
<th style="user-select: auto !important;">queries</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[0, 1, 2, 4, 3]</td>
<td style="user-select: auto !important;">[[0, 4, 1],[0, 3, 2],[0, 3, 3]]</td>
<td style="user-select: auto !important;">[3, 2, 4, 6, 4]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">각 쿼리에 따라 <code style="user-select: auto !important;">arr</code>가 다음과 같이 변합니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[0, 1, 2, 4, 3]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[1, 2, 3, 5, 4]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[2, 2, 4, 5, 4]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[3, 2, 4, 6, 4]</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">따라서 [3, 2, 4, 6, 4]를 return 합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 2023년 04월 27일 입출력 예 설명이 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges