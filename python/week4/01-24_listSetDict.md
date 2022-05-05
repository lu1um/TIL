### 01-24 list, set

#### list method

- .append(), .extend() : extend는 iterable을 받아 하나씩 추가해주는 형식
- .remove() : 가장 왼쪽의 값을 제거, 존재하지 않을 때 error
- .pop() : 가장 오른쪽, 만약 값 입력시 인덱스의 값을 반환하고 제거
- .sort(), .reverse(), .count

#### set method

- **순서가 없는 mutable이라는 것에 명심!@**
- .pop() : 임의의 원소를 제거해 반환 - list와 비교해서 보기
- .add() : 항목이 없다면 추가
- .remove() : 항목을 제거, 만약 없을 때 error

- .discard() : 항목을 제거, 없어도 에러발생 없음.

#### dictionary method

- .get(key, [default]) : key값의 value반환, 없을 때 default반환

- .pop(key, [default]) : key값의 value반환하고 제거, 없으면 default반환, default없으면 error

- .update(...) : key, value로 덮어쓰기

  ```python
  dic = {'apple' : '사', 'banana': '바나나'}
  dic.update(apple='사과')
  ----------------------------
  {'apple': '사과', 'banana': '바나나'}
  ```

  

