# node.js 에서 Vue 사용하기

### 시작하기

- `vue create my-app-name`

- `npm run serve` 로 서버를 실행한다.



### 주의사항

- 문법에 굉장히 깐깐하고, 정해지지 않은대로 하면 웬만하면 오류가 발생한다.
  - import를 하고 사용하지 않으면 오류발생
  - vue파일의 이름등은 2개의 Capital이 포함되어야한다. (두 단어 권장)
  - template 하위에는 하나의 div만 존재해야 한다. div의 자손이 몇명인지는 상관없다.
  - data는 객체 자체가 들어가지 않고, 객체를 반환하는 함수로 선언해줘야한다.



### ~.vue

- src/App.vue가 가장 중요한 main 뷰 파일이다.
- 아래와 같이 3개의 구성요소가 있다. html의 ! tab 처럼 vue tab으로 생성한다.

```vue
<template>
  <div>
      
  </div>
</template>

<script>
import ~ from './components/~.vue'    
    
export default {

}
</script>

<style>

</style>
```



### script

- 내부에 vue 객체의 내용이 들어간다.

  - name : 표시되는 이름, 중요하진 않지만 알아볼 수 있게 작성한다.
  - components : tag로 사용할 vue파일들을 포함시킨다. 미리 import가 되어있어야한다.
  - data : 변수들이 들어간다. 주의사항과 같이 객체를 반환하는 함수의 형태로 작성해줘야한다.

  ```vue
  data () {
  	return {
  		firstData: 1,
  		secondData: 2,
  	}
  }
  ```

  - methods : 메서드가 들어간다.
  - created, mounted.. : 이하 vue와 같다.



### template

- div안에 여러개의 자손을 만들어도 된다.
- components에서 선언되었다면, kebab-case로 사용하거나, CamelCase로 사용할 수 있다.

```vue
<template>
	<div>
        <AboutView />
        <about-view></about-view>
    </div>
</template>
<script>
...
components: {
    AboutView,
}
</script>
```



### app -> component : props

- app의 태그에서 보낸 prop을 component에서 캐치해서 활용할 수 있다.

```vue
// App.vue
<template>
	<div>
        <AboutView :my-message="someData"/>
    </div>
</template>

<script>
    ...
    data () {
        return {
            someData: "this is message"
        }
    }
```

```vue
// AboutView.vue
<template>
<div>
  <h1>{{ myMessage }}</h1>
</div>
</template>

<script>
export default {
  name: 'TheAbout',
  props: {
    myMessage: String,
  },
```

- tag안에서 my-message는 myMessage와 같이 CamelCase, kebab-case 모두 상관없다.
- props안의 key값은 CamelCase만 가능하다. -이 포함되면 빼기 연산자로 인식하기때문



### components -> app : $emit

- `$emit`을 활용해서 app으로 이벤트를 전송하는 식으로 데이터를 보낼 수 있다.

```vue
// App.vue
<template>
  <div id="app">
    <about @child-input-change="onBoss"></about>
  </div>
</template>

<script>
import About from './components/TheAbout.vue'

export default {
  name: 'App',
  components: {
    About,
  },
  methods: {
    onBoss (event) {
      console.log(event)
    }
  },
}
</script>
```

- emit이 오면 methods의 onBoss가 실행되어, 넘겨져온 event를 콘솔에 출력한다는 뜻이다.

```vue
// AboutView.vue
<template>
<div>
  <input 
    type="text"
    v-model="childInputData"
    @keyup.enter="childInputEnter"
  >
</div>
</template>

<script>
export default {
  name: 'TheAbout',
  data: function () {
    return {
      childInputData: '',
    }
  },
  methods: {
    childInputEnter () {
      console.log('Enter!!', this.childInputData)
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
```

- 엔터를 누르면 childInputEnter 메서드가 실행되는데, 이 메서드에 $emit이 포함되어있다.
- 첫 인자가 emit 요청의 이름이고, 두 번째 부터 event에 넘길 인자를 여러개 넣을 수 있다. 여러개여도 리스트에 담아 한 개만 넘기는 것을 권장한다.
