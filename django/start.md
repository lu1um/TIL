## Django 시작하기

1. vscode에 django, excelviewer 익스텐션 깔기
2. venv 가상환경에서 작업
   - python -m venv venv로 가상환경 생성
   - source venv/Scripts/activate로 가상환경 실행 (activate로 설정해놨음)
3. django-admin startproject <이름> . 으로 프로젝트 생성
4. python manage.py runserver로 서버 실행 확인!
5. python manage.py startapp <앱 이름>으로 앱 생성
6. 프로젝트 내의 settings.py의 INSTALLED_APPS에 앱이름을 추가해 등록해준다.
   - 반드시 앱을 생성한 후 등록해야한다! 등록하고 생성하면 안됨

