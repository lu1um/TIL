# Django Form에 widget 적용하기

### forms.py에서 작성한다.

- 아래와 같이 field의 widget 속성의 attrs에서 class, placeholder와 같은 꾸밈속성을 작성할 수 있다.

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-dark text-light',
                'placeholder': 'Enter the title',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
```

- class에 bootstrap을 적용할 수도 있다.
- error_message등 widget과 같은 레벨에서 입력해줘야하는 속성들도 있다.



### Rendering fields manually

https://docs.djangoproject.com/en/4.0/topics/forms/

- 아래와 같이 각 form의 요소들을 나누거나 다르게 배치할 수 있다.

```django
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.label_tag }}
      {{ form.title }}
      {{ form.title.errors }}
    </div>
    <div>
      {{ form.content.label_tag }}
      {{ form.content }}
      {{ form.content.errors }}
    </div>
    <input type="submit" value="작성"><br>
  </form>
```

- 반복문을 사용할 수도 있다.

```django
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form %}
    <div>
      {{ field.label_tag }}
      {{ field }}
      {{ field.errors }}
    </div>
    {% endfor %}
    <input type="submit" value="작성"><br>
  </form>
```



