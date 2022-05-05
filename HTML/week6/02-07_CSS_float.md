### float

#### float

- Normal flow를 무시하고 설정되는 값이다.
- margin, padding처럼 css의 속성중 하나이다.
- none, left, right가 있고, 양 옆에 붙일 수 있다!
- 그림과 문자를 조화롭게 배치하고 싶을 때 사용한다.
- 그림 옆에 문자가 바로 배치되지만, 사실은 문자의 box가 그림과 겹쳐져있고, contents만 그림 옆으로 이동한 형태로 구성된다!



#### clear: both

- float된 자식을 가진 부모는 높이를 0으로 가지게 된다. (자식이 부유하고 있으므로)

- 이를 해결하기 위해서는 부모의 속성에 아래와 같이 작성하는 기술을 많이 쓴다.

  ```css
  .parent::after {
      content: "";
      display: block;
      clear: both;
  }
  ```

- 이를 통해 내가 원하는 요소만 floating하고, 다음 요소부턴 Normal flow를 따르도록 할 수 있다.
