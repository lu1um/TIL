# Callback function

### 일급객체

- **JavaScript의 함수는 일급객체이다**
  - 인자로 넘길 수 있다
  - 함수의 반환값으로 사용할 수 있다
  - 변수에 할당할 수 있다



### Promise

- 비동기 작업의 완료, 실패를 나타내는 객체
  - 성공하면 .then(function)을 실행
  - 실패하면 .catch(function)을 실행

```
axios.get(URL)
	.then(response => {
		return response.data
	})
	.then(response => {
		return response.title
	})
	.catch(error => {
		console.log(error)
	})
	.finally(function () {
		console.log('마지막에 실행!!')
	})
```

