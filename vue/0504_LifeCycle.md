# Life Cycle Hook

[라이프사이클](https://kr.vuejs.org/v2/guide/instance.html#%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8)

### created

- Vue 객체가 생성되었을 때 실행될 함수



### mounted

- 태그랑 Vue가 마운트 되었을 때



### updated

- Vue의 데이터가 바뀌었을 때
- 이 경우 해당 함수에서 데이터를 조작하게되면, 무한루프에 빠지게 되므로 조심해야한다.
