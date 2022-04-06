# Django Form - views.py 작성하기

### 유효성검사

- 유효성에 대해 is_valid() 메서드로 검사 가능하다.

```python
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return
```

- 저장하는 것 뿐만 아니라, detail 페이지를 불러오거나, 다시 new 페이지로 돌아가는 코드는 다음과 같다.

```python
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```

- 위에서 ArticleForm(request.POST, instance=article)과 같이 이미 있는 데이터가 instance로 들어있다면, save할 때 update로 자동으로 실행된다.

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```



### CREATE를 하나에서 처리하기

- 지금까지 new와 create로 따로 처리했지만, 결국 new는 GET요청이 왔을 때, create는 POST요청이 왔을 때라는 것을 제외하고 같은 기능을 위해 만들어졌다.
- request.method로 GET인지 POST인지 구분해 하나의 함수, URL에서 처리가 가능하다.

```python
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- 이렇게 처리했을 경우, html문서의 action값이 없더라도 실행된다. 하지만 써주는 것이 좋다.
  - action값이 비어있다면, 자동적으로 자신에게 요청을 보내기 때문이다.



### UPDATE를 하나에서 처리하기

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

- 주의할 점은, instance를 넘겨준다는 것이다.
