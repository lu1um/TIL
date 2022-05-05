# Axios

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



### Axios

CDN - `<script src="https://unpkg.com/axios/dist/axios.min.js"></script>`

- Promise 기반의 HTTP client
- 비동기 함수들도 원하는 순서대로 처리할 수 있도록 하는 라이브러리다.
- JSON.parse를 자동으로 해주는 기능도 포함한다.

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/1'
axios.get(URL)	// promise가 리턴된다
	.then(function (result) {	// get이 끝나고 성공했다면,
    	console.log(result.data)	// get이 받아온 데이터를 출력한다.
})
```

- .then이 체이닝되어있을 때, 이후의 .then에 들어가는 파라미터는 앞의 .then의 return값이다.

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/1'
axios.get(URL)
	.then(function (result) {
    	return result.data
})
	.then(function (todo) {		// todo = result.data
    	console.log(todo)
})
```

- 아래와 같이 표현할 수도 있다.

```javascript
axios.get(URL)
	.then(result => result.data)
	.then(todo => console.log(todo))
```





### async & await

- ES8에서 등장
- Syntactic sugar로 더 쉽게 설계된 비동기 코드

```javascript
async function article() {
    const res = await axios.get(URL)
    console.log(res)
}
article()
	.catch(err => console.err(err))
```

1. async라는 키워드가 붙은 함수로 묶어준다.
2. 함수 내부의 비동기 함수들 앞에 await를 붙여준다.
3. catch는 따로 달아준다..

