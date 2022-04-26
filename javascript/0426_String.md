# String 메서드

### includes

- 특정 문자열의 존재여부

```javascript
str.includes('santa') // true or false
```



### split

- value로 나눈 배열을 반환

```javascript
const str = 'a cup'

str.split() // ['a cup']
str.split('') // ['a', ' ', 'c', 'u', 'p']
str.split(' ') // ['a', 'cup']
```



### replace

- str.replace(from, to) : from값을 to로 1개만 교체 후 반환
- str.replaceAll(from, to) : from값을 to로 모두 교체 후 반환



### trim

- str.trim(), str.trimStart(), str.trimEnd() : 공백문자(스페이스, 탭, 엔터)를 제거한 문자열 반환



