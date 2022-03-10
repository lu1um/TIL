## POST

- form에 method="POST"를 사용해 내용을 숨겨 전송할 수 있다.
- 이를 위해선 views에서도 POST.get으로 정보를 조회한다.
- 또한 CSRF Token을 사용해야 정상적으로 전달이 된다.



### CSRF

- form 태그 안에 `{% csrf_token %}`을 첫 줄에 넣기만 하면 된다.
