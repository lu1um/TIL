# Django와 연결하기

### 참고 코드

- vue-handsout/0518-vue-front/completed/~ 를 확인하자



### api/drf.js

- axios요청을 보낼 때 사용할 url을 함수형태로 불러오기 위해 작성해놓는다.



### Signup, login

- /src/components/AccountErrorList.vue
- /src/views/SignupView.vue, /src/views/LoginView.vue

- data에 object를 저장하고, object의 요소들을 v-model로 묶을 수 있다는 것
- account-error-list 로 오류메세지를 원하는 형태로 띄울 수 있다는 것



### Token 넘겨서 로그인 검사 통과하기

- axios의 headers에 token을 넘겨주면 된다.

```js
axios({
    url: drf.accounts.~,
    method: 'get',
    headers: <token>
})
```

- router.push({name: ~})를 통해 router의 name이 맞는 곳으로 redirect할 수 있다.



### state의 초기값

- `token: localStorage.getItem('token') || '' `와 같이 표현해, localStorage에 token이 존재할 때, 초기 메모리상의 token값을 설정할 수 있다.



### variable routing

- 주소 뒤에 variable routing된 변수에 접근할 때, `this.$route.params.<변수이름>`으로 접근할 수 있다.



### vuex의 모듈화

- module로 나누더라도, state와 getters, actions, mutations 모드 한 곳에 합쳐진다.
- 만약 `accounts.js`, `articles.js`로 나눠져있더라도, 그냥 같은 곳에 있다고 취급하고 state, getters, actions, mutations로 접근하면 된다.
- 만약 나누고 싶다면, `namespaced = true`를 export default 안에 넣어주면 된다.



### 비동기 동작으로 불러와지는 데이터 불러오기

- article을 axios로 불러올 때, 정상적으로 응답이 오지 않아도 페이지는 렌더링 되기 때문에 정상적으로 데이터가 출력되지 않을 수 있다.
- 이를 해결하기 위해 getters에 isArticle이라는 article이 빈 객체가 아님을 판단해서 article이 불러와 졌을 때 페이지가 렌더링 되도록 할 수 있다.
- `v-if="isArticle"`로 응답이 왔을 때, 렌더링 되도록 해주자.
