### Bootstrap

[Bootstrap 설명서](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

#### 어떻게 사용하나요

- css를 예쁘게 만들 수 있는 10000줄 이상이 작성된 라이브러리이다.

- 파일에 bootstrap.css를 포함시켜 작동할 수도 있지만, 보통 bootstrap.min.css를 인터넷에서 불러와서 쓴다.

  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  ```

- 자바스크립트 보통 `</body>`직전에 포함시키는 것이 관례다.

  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  ```

  

#### 자주 쓰는 클래스

- .mt-1 : `margin-top: 0.25rem !important`이 적용된다. 보통 4px이다.
  - m-0도 있고, m-2, m-3, m-4는 각 0.5, 1, 1.5 이고 m-5는 3rem이다.
  - m-auto
- .p = padding

- t, b, s, e, x, y : m이나 p뒤에 붙는 것으로 top, bottom, start(left), end, x, y이다.
  - mx-0 : x축, 즉 margin-right, left: 0
  - ps-auto : padding-left: auto
- 색깔
  - primary, danger, warning 등이 있고, post gradient로 요소 뒤에 붙이면 된다.
  - bg-light : 배경이 흰색
  - bg-warning : 배경이 붉은색
  - text-dark: 글씨가 검정색
- .d-inline : display: inline
- 그리고 생각하는 대부분이 keyword-value로 적용된다.
  - position-absolute, top-50 : position이 absolute고 top 50%위치로
- sm, md, lg, xl, xxl등 모니터 크기를 미리 설정해놓은 속성도 있어서, 적응형에 활용할 수 있다.

