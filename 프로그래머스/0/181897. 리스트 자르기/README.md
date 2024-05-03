# [level 0] 리스트 자르기 - 181897 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181897) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 05월 03일 16:45:23

### 문제 설명

<p style="user-select: auto !important;">정수 <code style="user-select: auto !important;">n</code>과 정수 3개가 담긴 리스트 <code style="user-select: auto !important;">slicer</code> 그리고 정수 여러 개가 담긴 리스트 <code style="user-select: auto !important;">num_list</code>가 주어집니다. <code style="user-select: auto !important;">slicer</code>에 담긴 정수를 차례대로 a, b, c라고 할 때, <code style="user-select: auto !important;">n</code>에 따라 다음과 같이 <code style="user-select: auto !important;">num_list</code>를 슬라이싱 하려고 합니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">n = 1</code> : <code style="user-select: auto !important;">num_list</code>의 0번 인덱스부터 <code style="user-select: auto !important;">b</code>번 인덱스까지</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">n = 2</code> : <code style="user-select: auto !important;">num_list</code>의 <code style="user-select: auto !important;">a</code>번 인덱스부터 마지막 인덱스까지</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">n = 3</code> : <code style="user-select: auto !important;">num_list</code>의 <code style="user-select: auto !important;">a</code>번 인덱스부터 <code style="user-select: auto !important;">b</code>번 인덱스까지</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">n = 4</code> : <code style="user-select: auto !important;">num_list</code>의 <code style="user-select: auto !important;">a</code>번 인덱스부터 <code style="user-select: auto !important;">b</code>번 인덱스까지 <code style="user-select: auto !important;">c</code> 간격으로</li>
</ul>

<p style="user-select: auto !important;">올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">n</code> 은 1, 2, 3, 4 중 하나입니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">slicer</code>의 길이 = 3</li>
<li style="user-select: auto !important;"><p style="user-select: auto !important;"><code style="user-select: auto !important;">slicer</code>에 담긴 정수를 차례대로 a, b, c라고 할 때</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 ≤ a ≤ b ≤ <code style="user-select: auto !important;">num_list</code>의 길이 - 1 </li>
<li style="user-select: auto !important;">1 ≤ c ≤ 3</li>
</ul></li>
<li style="user-select: auto !important;"><p style="user-select: auto !important;">5 ≤ <code style="user-select: auto !important;">num_list</code>의 길이 ≤ 30</p></li>
<li style="user-select: auto !important;"><p style="user-select: auto !important;">0 ≤ <code style="user-select: auto !important;">num_list</code>의 원소 ≤ 100</p></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">n</th>
<th style="user-select: auto !important;">slicer</th>
<th style="user-select: auto !important;">num_list</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">[1, 5, 2]</td>
<td style="user-select: auto !important;">[1, 2, 3, 4, 5, 6, 7, 8, 9]</td>
<td style="user-select: auto !important;">[2, 3, 4, 5, 6]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">[1, 5, 2]</td>
<td style="user-select: auto !important;">[1, 2, 3, 4, 5, 6, 7, 8, 9]</td>
<td style="user-select: auto !important;">[2, 4, 6]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">[1, 2, 3, 4, 5, 6, 7, 8, 9]에서 1번 인덱스부터 5번 인덱스까지 자른 리스트는 [2, 3, 4, 5, 6]입니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">[1, 2, 3, 4, 5, 6, 7, 8, 9]에서 1번 인덱스부터 5번 인덱스까지 2개 간격으로 자른 리스트는 [2, 4, 6]입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges