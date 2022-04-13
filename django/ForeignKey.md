# Foreign Key

### 외래 키, 외부 키

- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응되도록, pk를 가리킨다.
- 꼭 pk일 필요는 없지만, 유일한 값이여야 하기때문에 주로 pk이다.



### models.ForeignKey()

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



### 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 참조 무결성
  - FK(Foreign Key) 값이 특정 테이블의 유일한 값인 PK를 참조하는 것



### FK 작성하기

- `comment.article_id = article.pk` : 필드에 직접 넣는 방법
- `comment.article = article` : pk를 포함한 article 객체가 불러져있을 때, pk를 자동으로 FK에 넣는 방법



### 참조, 역참조

- 참조는 comment에서 article을 참조할 때, 이는 **comment.article**로 접근이 쉽다.
- 역참조는 article에서 comment를 참조할 때, **article.comment_set**이 자동으로 생성되어, 접근할 수 있다.
