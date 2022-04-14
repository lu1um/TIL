## SQLite 사용

- django-extensions를 설치
- 사용할 프로젝트의 INSTALLED_APPS에 'django_extensions'를 추가한다.
- python manage.py shell_plus로 ORM을 실행한다.



#### 튜플 추가하기

- `모델.objects.all()` : 전체 객체 조회
- `객체 = 가져온 모델()` : 선언
- `객체.인스턴스 = 내용` : 객체에 튜플 내용 저장
- `객체.save()` : 객체에 튜플의 정보가 있을 때, 이 구문을 써야 비로소 튜플이 추가가 된다.
- `모델.objects.create(필드=내용, 필드=내용, ...)` : save가 이 구문만으로도 된다.
- `객체 = 모델(필드=내용, 필드=내용, ...)` : 객체에 튜플내용을 포함해 선언함. save를 나중에 해줘야함



- save()가 되기 전에는 ID값이 주어지지 않는다. ID는 DB에서 계산되기 때문이다.



#### 튜플 조회

- `모델.objects.all()`
- `모델.objects.get(필드=내용, ...)` : 조건에 맞는 튜플을 반환해준다. 1개만 가능하므로 0개이거나 2개이상일 때 오류가 발생한다.
- `모델.objects.filter(필드=내용, ...)` : 쿼리를 적용해 쿼리셋을 반환해준다. 만약에 조건에 맞는 튜플이 하나도 없어도 빈 QuerySet을 반환해준다.
  - `필드__contains` : 필드에서 내용을 포함하는 모든 튜플 (`a__contains=123`은 123, 1234, 54123이 조회된다.)
  - `필드__gt` 등 여러 쿼리 함수가 있다.
  - [참고 DB](https://docs.Djangoproject.com/en/3.2/ref/models/querysets/)
- `모델.objects.order_by(필드)` : 필드을 기준으로 정렬된 쿼리셋을 반환해준다. 만약 `-필드`처럼 -를 붙이면 내림차순으로 정렬해준다.



#### 튜플 수정

- DB에 save된 것을 바로 수정, 삭제하는 것은 불가능하다.
- 따라서 get, all 등으로 불러와서 객체를 수정한 뒤 다시 save해주는 편이 낫다.
- `객체.delete()` : 객체의 모든 튜플 삭제. 따라서 filter를 통해 지울 튜플만 불러온 뒤, delete를 실행하면 DB에서 해당 튜플들만 삭제된다.



#### Aggregate

- 집계 함수(Avg, Sun, Max 등)을 사용할 때 써야하는 메서드

```python
User.objects.aggregate(average=Avg('balance'))
```



#### Annotate

- 새로운 필드를 만들어, 값을 집어넣는 것이다. 실제 DB에는 영향이 없고, 출력 queryset에만 영향이 있다.

```python
movies = Movie.objects.annotate(score_avg=Avg('comment__score'))
```

- 1:N으로 연결되어있는 comment의 score들의 평균값을 Movie의 새로운 필드로 만들어 붙여준다.
- 그룹화를 하고 싶다면 아래와 같이 작성한다.

```python
from django.db.models import Count

User.objects.values('country').annotate(Count('country'))
```

- country의 수가 붙고, country가 출력되게된다.
