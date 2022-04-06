# Django Form

### 왜 사용하나요

- 유효성검증을 쉽게 구현할 수 있다!

- 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- 아래 세 가지 동작을 수행한다.

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리



### Form Class

- Django Form 관리 시스템의 핵심
- Form 내의 field, field배치, 디스플레이 widget, label, 초기값, 에러메세지 결정



### ModelForm으로 만들기

- Model을 통해 Form Class를 만들 수 있는 도움기능이다.

```python
# articles/forms.py

from django import forms
from .models import Article		# model을 import해준다.

class ArticleForm(forms.ModelForm):		# forms.ModelForm을 상속받는다.
    class Meta:
        model = Article			# 어떤 model을 불러온건지 이름 써주기
        fields = '__all__'		# 출력할 필드
       #fields = ['title', 'content',]
       #exclude = ['content']	제외할 필드
```

- exclude를 쓸 때는 fields를 아예 쓰지 말아야한다.



### 만들기

- 앱 디렉토리에 `forms.py`를 생성해주고, 여기에 Form Class를 생성해줘야한다.

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- model과 비슷한데, model -> form이 되었다는 것이 다르다.

```python
# articles/views.py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- 위와 같이 form을 context에 담아서 넘겨준다.

```html
</ articles/new.html />


  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성"><br>
  </form>

```

- form 변수를 출력하기만 하면, form이 알맞게 생성된다.
- `form.as_p` : p 태그로 묶어준다.
- `form.as_ul`, `form.as_table` : 각 태그로 묶어주지만, 가장 상단에 ul, table태그는 직접 작성해줘야한다.



### Widgets

- 자동으로 만들어지는 form은 디자인상 완벽하지 않으므로, widget을 사용해야한다.

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

- forms.py에서 widget을 설정하며, 파라미터 형태로 써준다. 위에선 content가 바뀌었다.
- 이를 이용해 콤보선택, 라디오선택 등을 만들 수 있다.

```python
REGION_A = 'sl'
REGION_B = 'dj'
CHOICES = [
    (REGION_A, '서울'),
    (REGION_B, '대전'),
]

region = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
```

- choices에 튜플이 담긴 리스트를 넣어주면 된다.
