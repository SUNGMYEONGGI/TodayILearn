# [level 0] 정사각형으로 만들기 - 181830 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181830) 

### 성능 요약

메모리: 11.4 MB, 시간: 0.78 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 30일 00:00:28

### 문제 설명

<p style="user-select: auto !important;">이차원 정수 배열 <code style="user-select: auto !important;">arr</code>이 매개변수로 주어집니다. <code style="user-select: auto !important;">arr</code>의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 원소의 길이 ≤ 100

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">arr</code>의 모든 원소의 길이는 같습니다.</li>
</ul></li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 원소의 원소 ≤ 1,000</li>
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
<td style="user-select: auto !important;">[[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]</td>
<td style="user-select: auto !important;">[[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[[57, 192, 534, 2], [9, 345, 192, 999]]</td>
<td style="user-select: auto !important;">[[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[[1, 2], [3, 4]]</td>
<td style="user-select: auto !important;">[[1, 2], [3, 4]]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 1번의 <code style="user-select: auto !important;">arr</code>은 행의 수가 4, 열의 수가 3입니다. 행의 수가 더 많으므로 열의 수를 4로 만들기 위해 <code style="user-select: auto !important;">arr</code>의 각 행의 끝에 0을 추가한 이차원 배열 [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]를 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 2번의 <code style="user-select: auto !important;">arr</code>은 행의 수가 2, 열의 수가 4입니다. 열의 수가 더 많으므로 행의 수를 4로 만들기 위해 <code style="user-select: auto !important;">arr</code>의 각 열의 끝에 0을 추가한 이차원 배열 [[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]]을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 3번의 <code style="user-select: auto !important;">arr</code>은 행의 수와 열의 수가 2로 같습니다. 따라서 0을 추가하지 않고 [[1, 2], [3, 4]]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges