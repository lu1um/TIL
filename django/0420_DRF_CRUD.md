# DRF CRUD

### Article

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':			# 모든 글 불러오기
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':		# 글 쓰기
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':			# 글 하나 불러오기
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':	# 글 하나 지우기
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':		# 글 하나 수정하기
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
```

- method에 따른 응답을 명시적으로 하기위해 elif문을 사용한다.
- status에는 intager값이 들어가지만, 명시적으로 하기위해 status에 선언된 상수값을 사용한다. (굳이?)
  - 201 response를 발생시키기 위한 status=201과 status=status.HTTP_201_CREATED는 같은 출력을 보여준다.
- `is_valid(raise_exception=True)`에서 raise_exception=True를 통해서 valid하지 않을 때, 400 error가 자동으로 출력되게 해준다.



### Comment

- serializers.py

```python
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

- read_only_fields에 들어간 필드는 is_valid 검사에서 통과된다. 하지만 GET요청 때 읽어진다.
- 이렇게 read_only가 존재하지 않는다면, is_valid 검사 이후 foreignkey를 입력하는 기존의 방식이 동작하지 않기 때문에, 이러한 설정이 필수적이다.
- views.py

```python
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def comment_create(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- article과 거의 다를게 없지만, CREATE부분에서 save의 인자로 article=article을 넘겨주어 foreignkey를 넣어줘야한다.
