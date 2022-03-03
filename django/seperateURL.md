## URL을 다른 문서에 따로 작성하기

1. 프로젝트의 urls.py에 아래와 같이 작성하여, 다른 폴더의 urls.py를 불러올 수 있다.

```python
path('~', include('articles.urls'))
```

- articles의 urls.py를 불러오는 모습
- include는 django.urls의 메서드이므로, 헤더 또한 바꿔주자

```python
from django.urls import path, include
```



