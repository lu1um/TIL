# 반응형으로 만들어보자

## CSS

[youtube](https://www.youtube.com/watch?v=67stn7Pu7s4)



### button

```css
button,
button:focus {
    cursor: pointer;
}
```

- 커서를 button위에 올렸을 때, 커서가 손가락으로 바뀐다.



### line clamp

- 창이 작아져서 텍스트가 일정 줄 이상 되었을 때, ...으로 나타내는 것!

```css
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
```

- 위 4개 속성을 넣어주고, 숫자를 최대 표시 줄 수로 설정해주면 된다.



### calc

- 변수를 연산하여 사용하고 싶을 때 쓰는 것이다.

```css
:root {
	--padding: 12px;
}

h1 {
    margin-bottom: calc(var(--padding) / 2);
}
```

- 위와 같이 padding을 12px의 반인 6px을 줄 수 있다.



### flex

- flex: 증가너비 감소너비 기본너비;

```css
flex: 1 1 35% 
```



### 크기에 반응하는 반응형

```css
@media screen and (min-width:768px) {
  .infoAndUpNext {
    flex-direction: row;
    margin: var(--padding) 0;
    justify-content: center;
  }
}
```

- 768px 이상일 때 위의 속성이 적용된다.



### transform, transition

- transform : 자기 자신의 좌표에서 위치를 바꾸거나, 회전할 때 사용
- transition : 애니메이션을 만들어준다. 빙글빙글 돌아가는 애니메이션을 만들어봤다.

```css
.info .metadata .titleAndButton .moreBtn {
  height: 100%;
  transition: transform 300ms ease-in-out;
}
```

- transform할 때 빙글빙글 돌아간다.