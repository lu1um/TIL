# 템플릿 상속

`{% extends '<부모>' %}`가 템플릿 최상단에 작성되어야 상속받을 수 있다.

`{% block <이름> %} {% endblock <이름(안써도됨)> %}`을 통해 override할 부분을 부모에서 지정하고, 자식에서 새롭게 재정의할 수 있다.



- 보통 부모로 skeleton을 만들고, 이를 상속하는 식으로 개발을 하는데, 이러한 skeleton이 같이 templates에 가은 레벨이 있는 것은 구성상 좋지 않다.
  - 이를 해결하기위해 settings.py의 TEMPLATES의 DIRS 속성에 경로를 추가해주고, 여기에 skeleton을 놓는 것이 일반적이다.
  - project와 동일한 레벨에 templetes라는 디렉토리를 만들고, 여기에 skeleton이 존재한다면 아래와 같이 경로를 작성할 수 있다.

```python
/...
	/articles
    	/templates
        ...
    /project
    /templates  <- 이놈
    magage.py

'DIRS' : [BASE_DIR / 'templates']
```



- `{% include '<파일명>' %}`을 통해 block이 불가능한 상속 또한 가능하다. 이는 navbar, modal과 같은 요소가 너무 길어졌을 때, 따로 문서화하고 표현하고싶을 때 사용하는 문구이다.
