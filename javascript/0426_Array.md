# Array 메서드

### push, pop

- 가장 뒤에 요소에 더하기/빼기



### unshift, shift

- 가장 앞에 요소에 더하기/빼기

```javascript
const numbers = [1, 2]
numbers.unshift(100) // [100, 1, 2]
numbers.shift() // [1, 2]
```



### includes, indexOf

- includes(value) : value를 포함하는지 true or false
- indexOf(value) : value의 위치를 출력, 없으면 -1을 출력한다.



### join

- 배열의 모든 요소를 연결해서 반환한다. 구분자가 파라미터로 들어갈 수 있으며, 생략시 쉼표가 기본값

```javascript
const numbers = [1, 2, 3]
let result

result = numbers.join() // 1,2,3
result = numbers.join('') // 123
```



### ...

- Spread operator라고 하며, 파이썬의 *와 같은 역할을 한다.



### forEach

- Array.forEach(callback) : Array의 각 요소마다 callback함수를 실행해준다.

```javascript
const fruits = ['딸기', '수박', '사과']

fruits.forEach( (fruit, index) => {
    console.log(fruit, index)
})
// 딸기 0
// 수박 1
// 사과 2
```

- forEach안에 함수를 선언한 것이다.
- 인자로 함수가 들어간 모습, 표현식이므로 함수의 이름을 지정해주지 않았다.



### map

- Array.map(callback) : Array의 각 요소마다 callback을 실행, 반환 값을 요소로 하는 새로운 배열을 반환한다.

```javascript
const numbers = [1, 2, 3, 4, 5]

const double = num => {
    return num * 2
}

const doubleNums = numbers.map(double)
// doubleNums = [2, 4, 6, 8, 10]
```



### filter

- Array.filter(callback) : callback 반환 값이 참인 요소들만 모은 새로운 배열을 반환한다.

```javascript
const numbers = [1, 2, 3, 4, 5]

const odd = num => {
    return num % 2
}

const oddNums = numbers.map(odd)
// oddNums = [1, 3, 5]
```



### find

- Array.find(callback) : 참인 첫 번째 요소를 반환한다. 만약 참인 것이 없으면 undefined 반환



### some, every

- Array.some(callback) : 하나라도 참이면 true를 반환, 빈 배열은 항상 false 반환
- Array.every(callback) : 하나라도 거짓이면 false를 반환, 빈 배열은 항상 true 반환



### reduce

- Array.reduce(callback(acc, element ~), initialValue) : callback 함수의 반환값을 acc에 누적하고, acc를 반환한다. initialValue의 값이 acc의 초기 값이 된다.
