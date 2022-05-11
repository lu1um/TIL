# Router

### 시작하기

- vue create를 실행한 뒤, vue 폴더에서 `vue add router`를 실행해 router의 틀을 만들자.



### src/router/index.js

- routes를 수정해주면 된다.

```vue
import TheLunch from '../components/TheLunch.vue'

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunch
  },
  {
    path: '/lotto/:lottoNum',
    name: 'lotto',
    component: () => import('../components/TheLotto.vue')
  }
]
```

- path에 URL을 써주는데, variable routing이 가능하다.
  - `:변수명`을 적어주면, vue 객체로 넘어가게 된다.
  - 넘어간 변수는 `$route.params.변수명`으로 접근이 가능하다.
- name은 자주 쓰이므로 잘 정해주자.
- component는 어떤 vue파일을 연결시켜줄지 정하는 것인데, TheLunch처럼 할 수도 있고, Lazy loading으로 lotto처럼 할 수도 있다. 아래 방식이 선호된다.

