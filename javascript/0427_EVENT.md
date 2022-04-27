# JavaScript Event

### Event

- 브라우저에서 발생하는 Event를 캐치해오고, 이에 따른 반응을 보여줘야한다.
- 클릭같은 것을 HTML로 구현할 수도 있지만, Javascript로도 할 수 있다.



### Event의 역할

- ~ 하면 ~ 한다.
- EventTarget.addEventListener(type, listener)
  - 지정한 이벤트가 발생할 때마다 호출할 함수, listener를 지정한다.
  - type은 어떤 이벤트가 발생하면 반응 할 것인지이다.

```javascript
myTag.addEventListener('input', callbackInput)
// callbackInput(event)가 전달된다. input의 경우엔 event엔 방금 입력한 문자 버퍼가 전달된다.
```

- type
  - 'click' : 클릭했을 때
  - 'input' : 키보드 입력을 받았을 때
    - event.target.value에 입력된 텍스트 전문이 저장되어있다.



- event.preventDefault()
  - 이벤트의 기본 동작을 중단 (a태그의 이동, form의 전송 같은 동작)
  - callback 함수에 넣어주는 식으로 한다.

```javascript
callback(event) {
    event.preventDefault()
    console.log(event)
}
```



- event.stopPropagation()
  - 상속받은 객체의 이벤트일 경우, 상위 객체의 이벤트가 중복되어 실행되는 것을 방지하기 위해 사용하는 것이다.
  - 주로 'click' 이벤트가 부모와 자식 모두 가지고 있을 때, 자식을 클릭했을 때 부모와 자식 이벤트 모두 발생하는 것을 방지하는 용도로 사용한다.
