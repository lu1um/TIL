## Admin

- model을 통해 migration파일이 작성되면 admin 정보를 저장할 공간이 만들어진 것이다.
- `python manage.py createsuperuser`를 통해 admin을 생성할 수 있다.



#### admin.py

- 아래와 같이 작성하면 admin 페이지에 해당 DB가 표시되게 된다.

  ```python
  from django.contrib import admin
  from .models import <클래스명>
  
  admin.site.register(<클래스명>)
  ```

- 클래스명은 모델에서 작성한 클래스 이름이다.

![image-20220308144826731](admin%EB%90%98%EA%B8%B0.assets/image-20220308144826731.png)

- 오른쪽은 `__str__`에서 반환된 내용이 제목으로 표시된다.

  - 아래와 같이 ModelAdmin을 이용해 두 번째 인자로 register를 호출할 경우, 표시를 다른 방법으로 바꿀 수 있다.

  ```python
  from django.contrib import admin
  from .models import *
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('title', 'content')
  
  admin.site.register(Article, ArticleAdmin)
  ```

![image-20220308145100993](admin%EB%90%98%EA%B8%B0.assets/image-20220308145100993.png)

