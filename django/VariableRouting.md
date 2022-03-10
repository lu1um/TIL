## Variable Routing

- views에서 request외에 인자를 더 받는 것을 variable routing이라고 한다.
- 이를 위해서 html파일에서도 `{% url 'url' variable %}`형태로 variable또한 넘겨줘야한다.
- 또한 urls.py에서도 `path('<type:field>/')`와 같이 `<>`로 묶어줘 variable routing을 활용한다.
- 이를 통해 get, filter등 variable을 활용해 제목을 클릭하면 내용이 보이는 등의 기능을 구현할 수 있다.
