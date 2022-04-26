# javascript 라이브러리

### Lodash

- 사용할 html에 lodash cdn을 넣어준다.

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

- _ 라는 object의 메서드를 사용하는 식으로 쓴다.

```html
_.sample([1, 2, 3, 4]) // 랜덤으로 나옴
_.range(5) // [0, 1, 2, 3, 4]
const new = _.cloneDeep(original) // deepcopy
```

