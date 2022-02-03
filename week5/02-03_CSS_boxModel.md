### Box Model

#### 모든 요소는 네모

- 위에서 아래, 왼쪽에서 오른쪽으로 box model이 쌓인 것이 CSS의 표현방식이다.![CSS BOX](02-03_CSS_boxModel.assets/margin,%20border,%20padding,%20and%20content.png)

- 위 사진처럼 네 영역으로 이루어져 있다. (Margin은 반드시 빈 공간이다.)

  - margin-top, margin-right, margin-bottom, margin-left

    - margin : 10px 20px 30px 40px
    - 1개: 상하좌우
    - 2개: 상, 좌우
    - 3개: 상, 좌우, 하
    - 4개: 상, 우, 하, 좌 (시계방향)

  - border-width, border-style, border-color

    - border:  2px dashed black
    - 두께, 모양, 색깔

    

#### box-sizing

- border까지 크기로 정하고싶다면, box-sizing속성을 border-box로 추가해주면 된다.

  ```
  box1{
    box-sizing: border-box;
  }
  ```

  

#### align

- margin-left : auto 로 우정렬이 가능하다!
- text는 margin이 없기때문에, `text-align: center`로 한다.



#### display, visibility

- display: none
  - 공간 x, 표시 x
- visibility : hidden
  - 공간 o, 표시 x



#### position

- relative : 자신의 static위치 기준으로 이동, 공간은 static과 동일하게 차지
- absolute : static공간에서 제거 후 부모 요소를 기준으로 이동
- fixed : static공간에서 제거 후 viewport기준으로 이동, 스크롤에 영향 x (리모컨같은거)
- -webkit-sticky : 일정 위치까지 relative, 일정 위치를 벗어나면 fixed되버림
  - 포지션 속성 선언 후, top, left로 움직이자!
