# Substituting a custom User model

### User 모델을 만들어놓자

- User를 나중에 바꾸려면 정말 힘들다.

1. accounts를 만들 때, accounts/models.py에 다음과 같이 써놓고 시작하자.

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

2. 그리고 settings.py에서 아래 속성을 입력하자.

```python
AUTH_USER_MODEL = 'accounts.User'
```

3. accounts/admin.py에 User를 register하자.

```python
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- 만약 이미 User를 썼다면, 초기화하자.

1. db.sqlite3 파일 삭제
2. migrations 디렉토리의 숫자가 붙은 파일들 모두 삭제
3. makemigrations, migrate진행



### 안되는게 생긴다

- 회원가입, 회원정보수정이 안됨
  - Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
  - 내장 User 모델을 사용하도록 라이브러리가 지정되어있기 때문에, 커스텀 User 모델로 바꿔줘야한다.
- 그대로 상속받아서 Meta만 바꿔주면 된다!

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model() # User
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

- creationForm의 Meta처럼 원래 Meta를 상속받아 fields를 유지하고, 더할 수도 있다.
- `from .models import User`처럼 User를 직접참조하지 않는 것이 권장된다.
