## namespace

- 다른 앱이더라도, django는 모든 템플릿을 하나의 폴더내에 있는것처럼 취급하고 다루기때문에 아래의 작업을 해주어야한다. 이를 작업하지 않으면 가장 먼저 선언된 앱의 것만 불러와진다.

1. url namespace
   - 앱 내의 코드에 `app_name = <appName>`을 추가해준다.
   - `{% url ' ' %}`등을 호출할때 `{% url '<appName>:<html>' %}`로 접근해준다.
2. templates namespace
   - 앱 내의 templates 디렉토리에 디렉토리를 한 겹 더 만들어주어 직접적으로 구분해준다.
   - app/templates/app 에 모든 html을 위치시키면 확실히 구분된다.
   - 단, 이 때 skeleton.html등의 디렉토리가 모두 바뀌므로, 이를 주의하자.
