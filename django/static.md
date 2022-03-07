## static

- 이미지와 같이 정적인 파일들은 한 곳에 모아두고 관리하게된다.
- app/static/app/ 에 존재시킨다.
- 이를 불러오기 위해선 두 가지 태그가 필요하다.
  - `{% load static %}`으로 tag를 불러온다. static은 built-in tag가 아니다!
  - `{% static 'app/~.jpg' %}`와 같이 static태그로 불러와준다.
- 당연하게도, settings.py의 STATICFILES_DIRS에 경로를 추가함으로 위의 기본 경로외에 경로도 추가해줄 수 있다.



### STATIC_URL

- 기본적으로 '/static/'으로 지정되어있으며, static파일들이 모여있는 URL이다.
- app/static/ 에 존재하는 파일들을 모아주는데, 별도의 경로를 추가하는 상수도 존재한다.
  - `STATICFILES_DIR = []`에 작성함으로 추가할 수 있다. 이는 기본적으로 작성이 안되어있다.



### STATIC_ROOT

- 기본적으로 작성되있지 않지만, 개발이 끝나고 배포환경에서 작성해주는 것이 권장되는 속성이다.
- 정적파일을 수집해놓는 디렉토리의 절대경로로, `python manage.py collectstatic`을 실행했을 때 이 경로에 모든 정적 파일이 이 곳에 모아진다.
- settings.py의 DEBUG가 True라면 이 속성은 작동하지 않는다.
