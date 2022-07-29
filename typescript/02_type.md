# TypeScript Type

## Type

```typescript
let name :string = "hong gildong"
```

- 위와 같이 `:string`으로 타입을 지정하고, 다른 타입의 변수가 입력되지 않도록 할 수 있다.
  - string, number, boolean, null, undefined, bigint, [], {} 등이 있다.
  - void : 반환값 없음, never : 반환하지 않고 무한반복할 때
  - 여러가지 타입을 위해선 `:string | number`와 같이 표현하면 된다.
  - []과 같은 것은 내부에 들어갈 값의 타입도 지정해주어야한다.
  - {}는 key별로 타입을 지정해주어야한다.
    - key에 ?가 붙는다면, 해당 속성은 필수가 아니라는 뜻이다.

 ```typescript
 let names :string[] = ['kim', 'park']
 let info :{ region : string, age? : number } = { region : 'seoul' }
 ```

- `:string | number`와 같은 type을 선언하고, 나중에 쓸 수도 있다.

```typescript
type MyType = string | number;
let name :MyType = 123;
```

- 함수의 파라미터와 리턴값에도 타입을 지정할 수 있다.

```typescript
function plus (x :number, y :number) :number {
  return x+y
}
```



## 새로운 용법

- tuple

```typescript
type Member = [number, boolean]
```

- 위와 같이 선언하면, 첫 번째 요소로 숫자, 두 번째 요소로 참거짓값이 들어가야하는 튜플을 만들 수 있다.



- object 타입 일괄적용

```typescript
type Member = {
  [key :string] : string,
}
```

- 위와 같이 선언하면, key의 타입이 문자인 모든 속성들이 문자로 고정된다.