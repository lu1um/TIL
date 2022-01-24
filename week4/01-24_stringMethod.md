### 01-24 string method

#### bool 반환

- .find('a') : a가 있으면, 있는 첫 번째 위치를 반환, 없으면 -1 반환
- .index('a') : a가 있으면, 있는 첫 번째 위치를 반환, 없으면 오류남
- .isupper, .islower, .istitle : 각 대문자, 소문자, 띄어쓰기 이후 모두 대문자인지를 판별

#### string 반환

- **string 은 immutable한 객체다!!!**

- 주의할 점은, argument로 넘어간 string은 자체적으로 변화하지 않으므로, 그 string을 변화시키고 싶으면 반드시 string = string.~()와 같이 재정의해줘야한다.

- .replace(old, new, [count]) : old문자를 모두 new문자로 바꿔줌, count입력시 count만큼만

- .strip('a'), .lstrip('a'), .rstrip('a') : 양쪽, 왼쪽, 오른쪽 a를 제거한다.

- .split('a') : a 단위로 나눠 리스트로 반환해준다.

- 'a'.join(<iterable>) : iterable 요소들을 'a'로 합쳐 문자열을 반환

  - **만약 iterable에 문자열이 아닌 값이 있으면, type error발생!**

  ```python
  '!'.join('hello')
  '?'.join(['he', 'llo'])
  -------------------------
  'h!e!l!l!o'
  'he?llo?'
  ```

- .upper(), .lower(), .swapcase() : 대문자, 소문자, 반대로 변환

- .capitalize() : 첫 문자만 대문자로

- .title() : 공백과 어퍼스트로피 다음은 대문자로 변환