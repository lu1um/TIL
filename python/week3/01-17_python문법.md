### 01-17

#### python 문법

##### 문자열에 변수넣기

- %-formatting `'안녕하세요 %s' % string`

- str.format() `'안녕하세요 {}'.format(string)`

- **f-strings** : python 3.6+부터 사용가능

  `f'안녕하세요 {string}'`



  ##### 패킹/언패킹 연산자

- 패킹 : 대입문 왼쪽에서 *이 쓰였을 떄로, 우변이 좌변 수보다 많을 때 사용된다.

  ```
  x, *y = 1, 2, 3, 4
  print(y)
  --------------
  [2, 3, 4]
  ```

- 언패킹 : argument를 *로 넣었을 때, 튜플형태로 대입한다.

  ```
  def sum(x, y, z):
  	print(x + y + z)
  number = [1, 2, 3]
  sum(*number)
  ----------------------
  6
  ```




##### Set과 Dictionary

- Set은 **중복 X**, 순서 X, 인 자료형이다.
- 딕셔너리는 키와 값으로 이루어진 자료형이다.
  - Key로는 List와 Dictionary를 제외한 자료형 모두 사용가능
  - Value로는 모든 자료형 사용 가능
  - 형 변환시, **Key**만 나오는 것을 주의하자!



##### 논리 연산자의 단축평가

- 결과가 확실한 경우, 두 번째 값은 확인하지 않고 첫 번째 값을 반환한다.

  ```
  print(3 and 5)
  print(0 and 5)
  ------------------
  5
  0
  ```

  ```
  print(3 or 5)
  print(0 or 5)
  -------------------
  3
  5
  ```



##### 멤버십 연산자 in, not in

- `'a' in ['a', 'b']`의 형태로 사용하며, 우항에 좌항이 포함되는지 확인하는 연산자.



##### 슬라이싱

- `list[a:z:n]`

  - a = 시작(포함)
  - z = 끝(미포함)
  - n = 몇 개 단위로 볼지

  ```
  [1, 2, 3, 5][0:4:2]
  ----------------------
  [1, 3]
  ```

- list[::] == list[0:len(list):1]과 동일하므로 list와 거의 같은 문구이다.
- list[::-1]는 뒤집어서 출력하는 효과가 있는 문구이다.



##### Set의 연산자

- 비트연산자랑 거의 똑같게 사용한다.

- | : 합집합 == OR
- & : 교집합 == AND
- \- : 여집합 == 없음, 그냥 빼기로 생각
- ^ : 대칭차 == XOR



##### Input()

- Input의 출력은 항상 **string**이라는 것에 유의하자!!!!!
  - int(input())같은 형변환을 통해 숫자를 입력받자.



##### 조건문 comprehension

- `<true> if <condition> else <false>`으로 작성할 수 있다.



##### for문은 순회 반복문

- 단순히 반복이 아니라, `for <variable> in <container>`로 컨테이너를 하나씩 순회하며 반복하는 것이 다른 언어의 for문과의 차이이다.

- Dictionary를 순회할 경우, 기본적으로 Key를 순회함.

  - .keys(), .values(), .items()로 각 요소 혹은 두 요소의 튜플에 접근 가능하다.

- enumerate(<container>) 함수로 인덱스와 원소를 같이 순회시킬 수 있다.

  - (인덱스, 원소)형태의 튜플이 모인 리스트를 출력한다.
  - `list(enumerate(<container>))`를 해서 enumerate의 주소값이 아닌 실제 값을 확인해볼 수 있다.

  ```
  list1 = ['spring', 'summer', 'fall', 'winter']
  for idx in enumerate(list1):
  	print(idx)
  --------------------------------------------------
  0 spring
  1 summer
  2 fall
  3 winter
  ```

- `[<expression> for <variable> in <container> {if <조건문>}]`으로 expression을 적용한 리스트를 쉽게 만들 수 있다. ex) 각 수의 세제곱이 담긴 리스트

- break, continue, pass, else를 활용하자
  - else : 반복문이 끝까지 실행된 후에 else문이 실행된다. 보통 break가 끼어있는 for문에서 활용된다. break가 된다면 else가 실행되지 않기 때문이다.



##### 활용팁

- `if lst[]:`와 같이 **list에 아무 원소도 없으면 False**로 인식하는 것을 이용할 수 있다.