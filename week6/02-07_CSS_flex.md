### flex

#### display: flex;

- 가로축, 세로축을 중심으로 배치하는 것이 가능하다!
- `flex-direction : main axis를 설정해준다.
  - row, row-reverse, column, column-reverse

- `flex-wrap` : wrap: 넘치면 다음줄, nowrap: 한줄에 무조건 배치

- `justify-content` : main axis 기준
  - flex-start, flex-end : 좌측정렬, 우측정렬
  - center : 중앙정렬
  - space-between : 좌, 우측에 딱 붙고 3개 이상일 경우 1---2---3처럼 같은 공간을 가지고 배치
  - space-around : -1--2--3- 처럼 좌우는 한칸, 요소 사이는 두칸으로 배치됨
  - space-evenly : -1-2-3- 처럼 모두 동일한 간격으로 배치

- `align-items` : cross axis를 기준으로 정렬하기
  - stretch : 세로로 쭉 늘려서 배치
  - flex-start, flex-end, center : 위, 아래, 센터
  - baseline : 첫 번째 요소를 좀 크게, 이미지와 문자가 조화롭게 출력되고싶을 때 자주 사용.
- `align-self` : 뭔지 찾아보기!

- `order` : 순서 설정, 기본은 0이다.
