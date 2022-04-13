# 댓글창 만들기

### models.py

- 2개의 위치 인자가 필수적이다.
  1. model
  2. on_delete
     - 연결된 객체가 사라졌을 때 해당 객체를 어떻게 처리할 지를 정의하는 것이다.
     - CASCADE : 같이 삭제된다. 일반적으로 이 속성을 사용한다.

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
      # 이렇게 이름 지어도 테이블이 만들어질때 FK는 뒤에 _id가 붙어 article_id라는 이름이 된다.
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

- 1:N 의 관계형이므로, article은 참조하는 모델 이름의 소문자 단수형으로 만들었다. 



### forms.py

- Comment를 models에서 불러온 뒤, ModelForm으로 만들어준다.

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
```

- 댓글 내용만 작성하면 되기때문에 fields에 contents만 표시하도록 한다.



### urls.py

- 댓글을 작성하는 comment와 삭제하는 delete를 구현했다.

```python
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
```

- delete를 작성할 때, 굳이 article의 pk를 넘겨주지 않아도 되지만, url들의 통일성을 위해 저런식으로 url을 구성한다.



### views.py

- CR을 다음과 같이 만들었다.

```python
@require_POST
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # pk = comment.article_id
    # 이걸 안쓴 이유 : url의 통일성을 위해 어차피 article_pk를 넘겨주는 것이 나중을 위해서 좋기 때문에
    comment.delete()
    return redirect('articles:detail', article_pk)
```

- forms.py에 만든 CommentForm을 이용했다.
- save의 commit속성을 이용해 comment_form으로 저장한 데이터를 불러오는 함수로 save를 사용했다. 이를 통해 article의 pk와 comment의 fk를 연결할 수 있었다.
- delete를 할 때 comment의 pk를 불러와야한다는 것에 주의 (article의 pk로 헷갈릴 수 있다.)



### detail.html

- 댓글창을 detail에서만 표시되게 했다.

```django
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          {{ comment.content }}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
  <hr>
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

- delete와 create를 POST요청으로 보내기 위해 form을 통해 버튼을 만들어 줬다.
