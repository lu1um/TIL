### 01-19

#### keyword

- `def foo(x, y=1)`에서 y=1은 argument로 넣어도 되고, 없어도 되는 선택사항으로 만듬
- `foo(y=2, x=1)`처럼 기본 순서와 다르게 넣고싶을 때, keyword를 사용할 수 있다.
  - 단, `foo(x=1, y)`처럼 keyword가 앞에 올 수는 없다!

#### *arg, **arg

- `*arg`는 남는 여러 개의 argument를 튜플로 unpacking해 parameter로 받아들인다.

- `**arg`는 dictionary가 argument로 왔을 때 처리하는 parameter

  ```
  a = [1, 2, 3]
  
  def func1(x):
  	for i in x:
  		print(x, end="")
  def func2(*x):
  	for i in x:
  		print(x, end="")
  func1(a)
  func2(a)
  ------------------------------
  1 2 3 [1, 2, 3]
  ```

- 위 처럼 되는 이유 : func2에서는 `x = ([1,2,3],)`으로 튜플이 되기 때문이다.



#### sum함수의 이상한점

- `sum(<iterable>, <start_value>)`로, sum(1,2,3)같이 쓰는게 아니라 처음 argument로 iterable한 인자를 주고, 두 번째에 수 하나를 넣을 수 있다.

  ```python
  a = 1
  b = 2
  c = 3
  
  def func(x, *y):
      z = sum(y, x)  # do not -> sum(x, y)
      print(z)
  
  func(a, b, c)
  ---------------------------
  6
  ```

  

#### global과 nonlocal의 차이

- global : 함수의 최상단에 위치하게 되며, 없던 변수를 선언하기도 가능하다.
- nonlocal : 한 단계 상단의 함수 위치에 참조되며, 없던 변수를 선언하진 못한다.
- `globals()`, `locals()`로 현재 단계의 변수가 뭐가 있는지 print할 수 있다.
  - 특히 `globals()`는 `__name__`,`__file__`과 같은 built-in scope 변수도 다 불러온다.



#### map, filter, zip

- `map(<function>,<iterable>)`으로 모든 요소에 함수를 적용해 **결과**를 반환
- `filter(<function>,<iterable>)`으로 모든 요소에 적용하고, **결과가 True인 요소**를 반환

- `zip(*<iterable>)`으로 튜플을 만들어 반환한다.

  ```python
  a = [1, 2]
  b = [10, 20]
  pair = zip(a, b)
  print(list(pair)
  -----------------------
  [(1, 10), (2, 20)]
  ```

- 위 세 함수는 모두 각자의 object형태로 반환하기 때문에, 반드시 형변환을 거쳐야한다.

#### lambda

- `lambda [parameter] : <function>`



#### random.sample

- `random.sample(range(<start>,<end>), <number>)`로 활용가능



#### pip

- `pip freeze > <text.txt>   `를 통해 module==version 형태의 텍스트를 저장시킬 수 있다.

- `pip install -r <text.txt>`로 위에서 추출한 text의 내용대로 설치 가능!!



#### \_\_init\_\_.py

- 모듈화를 했다면, 같은 폴더내에 \_\_init\_\_.py를 꼭 생성해주자.



#### venv 가상환경 만들기

- 원하는 디렉토리에서 `python -m venv <가상환경이름>`으로 생성
  - 관례상 가상환경이름은 venv로 한다.
- `source venv/Scripts/activate`로 activate
- `deactivate`