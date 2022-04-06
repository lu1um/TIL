# Django Bootstrap v5

### widget을 안써도 된다

- `pip install django-bootstrap-v5`로 설치한 뒤, settings.py에 INTSALLED_APPS에 `'bootstrap5'`를 등록해준다.

- 쓸 html문서의 상단에 `{% load bootstrap5 %}`를 써준다.
- `{{ form }}` 대신 `{% bootstrap_form form %}`을 써주면 bootstrap이 적용된 form이 출력된다.
