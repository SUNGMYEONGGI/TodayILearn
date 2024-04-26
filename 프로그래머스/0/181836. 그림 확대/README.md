# [level 0] 그림 확대 - 181836 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181836) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 26일 14:41:28

### 문제 설명

<p style="user-select: auto !important;">직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 이 그림 파일을 나타낸 문자열 배열 <code style="user-select: auto !important;">picture</code>과 정수 <code style="user-select: auto !important;">k</code>가 매개변수로 주어질 때, 이 그림 파일을 가로 세로로 <code style="user-select: auto !important;">k</code>배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">picture</code>의 길이 ≤ 20</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">picture</code>의 원소의 길이 ≤ 20</li>
<li style="user-select: auto !important;">모든 <code style="user-select: auto !important;">picture</code>의 원소의 길이는 같습니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">picture</code>의 원소는 '.'과 'x'로 이루어져 있습니다.</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">k</code> ≤ 10</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">picture</th>
<th style="user-select: auto !important;">k</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx", "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..", "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......", "........xx........", "........xx........"]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["x.x", ".x.", "x.x"]</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><p style="user-select: auto !important;">예제 1번의 <code style="user-select: auto !important;">picture</code>는 다음과 같습니다.</p>
<div class="highlight" style="user-select: auto !important;"><pre class="codehilite" style="user-select: auto !important;"><code style="user-select: auto !important;">.xx...xx.
x..x.x..x
x...x...x
.x.....x.
..x...x..
...x.x...
....x....
</code></pre></div>
<p style="user-select: auto !important;">이를 가로 세로로 <code style="user-select: auto !important;">k</code>배, 즉 2배 확대하면 그림 파일은 다음과 같습니다.</p>
<div class="highlight" style="user-select: auto !important;"><pre class="codehilite" style="user-select: auto !important;"><code style="user-select: auto !important;">..xxxx......xxxx..
..xxxx......xxxx..
xx....xx..xx....xx
xx....xx..xx....xx
xx......xx......xx
xx......xx......xx
..xx..........xx..
..xx..........xx..
....xx......xx....
....xx......xx....
......xx..xx......
......xx..xx......
........xx........
........xx........
</code></pre></div>
<p style="user-select: auto !important;">따라서 ["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx", "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..", "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......", "........xx........", "........xx........"]를 return 합니다.</p></li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><p style="user-select: auto !important;">예제 2번의 <code style="user-select: auto !important;">picture</code>는 다음과 같습니다.</p>
<div class="highlight" style="user-select: auto !important;"><pre class="codehilite" style="user-select: auto !important;"><code style="user-select: auto !important;">x.x
.x.
x.x
</code></pre></div>
<p style="user-select: auto !important;">이를 가로 세로로 <code style="user-select: auto !important;">k</code>배, 즉 3배 확대하면 그림 파일은 다음과 같습니다.</p>
<div class="highlight" style="user-select: auto !important;"><pre class="codehilite" style="user-select: auto !important;"><code style="user-select: auto !important;">xxx...xxx
xxx...xxx
xxx...xxx
...xxx...
...xxx...
...xxx...
xxx...xxx
xxx...xxx
xxx...xxx
</code></pre></div>
<p style="user-select: auto !important;">따라서 ["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"]를 return 합니다.</p></li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges