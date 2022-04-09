# Decorator

### 알맞는 오류를 출력해주자

- get_object_or_404() : model에 요청을 보낼때 사용한다.

```python
from django.shortcuts import get_object_or_404

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
```

- 만약 존재하지 않는 pk라면 404 error가 출력되게된다.



### Decorator

- 클래스 메서드의 데코레이터처럼 사용한다.
- `@require_http_methods(['???', '???', ...])` : 특정한 method 요청만 허용
- `@require_POST` : POST method 요청만 허용
- `@require_safe` : GET method 요청만 허용

```python
from django.views.decorators.http import require_POST, require_safe, require_http_methods
```

