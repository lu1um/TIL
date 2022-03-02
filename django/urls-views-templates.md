## URLS.py -> Views.py -> templates

1. 위와 같은 순서대로 작성해나가자!
1. url 요청을 받았을 때 어떻게 할지가 urlpatterns 리스트안에 작성되어있다.



[django document](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

# DTL(Django Template Language)

`{{ key }}`와 같이 딕셔너리를 render의 세번째 인자로 보내준 경우에 HTML에서 사용할 수 있다.

```python
def greeting(request):
    name = {
        'name': 'Alice',
    }
    context = {
        'info': name,
    }
    return render(request, 'greeting.html', context)
```

위와 같이 되어있다면, `{{ info.name }}`을 html문서내에 위치시키면, Alice가 나올것이다.

- Filter

`{{ key|length }}`와 같이 미리 지정된 필터들로 변수를 조작할 수 있다.

`{{ key|join:'<string>' }}` 처럼 인자를 받는 필터도 있다.

`{{ forloop.counter }}`와 같이 미리 지정된 이름을 갖는 필터도 있다. loop가 몇 번 진행됐는지 알 수 있는 필터



- Tag

반복, 논리를 HTML안에 구현할 수 있다.

**실제로 파이썬이 구동되는 것이 아니므로**, 파이썬 문법과 다른 부분이 존재한다.

`{% tag %}`와 같이 표현되고, 종료태그가 필요한 if문과 같은 tag도 존재한다.

```html
{% for food in foods %}
	<li>{{ food }} </li>
{% endfor %}
```

`{% empty %}`for문 안에서 만약 iterable이 비어있다면, 이 tag아래가 실행된다! if문 없이도 이런 tag를 사용해 편하게 만들 수 있다.
