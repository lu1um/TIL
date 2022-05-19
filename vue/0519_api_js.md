# api.js

### axios.create

- `import axios from 'axios'`를 받은 뒤, axios요청에 관련된 함수를 작성해놓는다.

```js
import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/v1/'
const api = axios.create({
    baseURL
})
```

- 위와 같이 작성해놓으면, 나중에 axios를 사용할 경우, url에 baseURL을 제외한 부분부터 작성하면 된다.

```js
axios({
    method: ~,
    url: 'http://127.0.0.1:8000/api/v1/signup/',
})

가 아래와 같이

api({
    method: ~,
    url: 'signup/',
})
```



### axios.interceptors.request.use((config) =>{})

- 작성된 api가 응답을 주었을 때, .then보다 먼저 실행될 함수를 설정해준다.

```js
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token')
    config.headers.Authorization = `Token ${token}`
    return config
})
```

- config를 반환해주어야 정상작동한다.
