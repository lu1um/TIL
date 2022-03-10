## Model

- 직접적으로 database와 연결되어 튜플을 객체처럼 다룰 수 있게 해주는 단계



### ORM

- Object-Relational-Mapping
- SQL의 데이터를 객체로 바꿔 파이썬에서 쉽게 사용할 수 있게 해주는 중간과정이다.
- Django는 내장 ORM을 사용한다.
- 이를 통해 SQL을 모르더라도 DB를 조작할 수 있다.



### 작성법

- models.Model을 상속받는 클래스를 생성한다.

- 클래스 변수로 field를 만들어주면 된다. (Schemea만 생성)

- field의 종류는 models.CharField()와 같이 모두 미리 지정되어있다.

  ```python
  # 예시
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      
      def __str__(self):	# 나중에 get을 했을 때, 무엇이 출력될 지 선택하는것
          return self.title
  ```

- 속성

  - auto_now_add : 처음 만들어질 때 자동으로 지금의 시간을 추가
  - auto_now : 만들어질 때를 포함한 모든 수정작업이 발생했을때 자동으로 지금의 시간을 추가

  

### Migration

1. makemigrations
   - model에 작성한 모델을 django에 적용할 수 있는 migration을 생성한다.
   - migrations폴더에 model.py의 scheme을 가진 파이썬파일을 생성하게된다.
2. migrate
   - migration을 DB에 반영한다.
3. sqlmigrate
   - migration에 대한 SQL구문을 볼 수 있다.
4. showmigrations
   - 프로젝트 전체의 migration의 상태를 확인 및 migrate여부 확인



### 이미 생성된 DB의 attribute 추가

- 애초에 이런 일이 일어나지않도록 model을 처음부터 잘 구상해야한다.

- model에 추가를 한 뒤, makemigrations를 한다면 선택사항이 생긴다
  - 새로 추가된 field의 초기값이 이미 생성된 튜플들에게 존재하지 않기 때문에, 어떻게 처리할 지 알려줘야한다.
  - 주로 1입력 엔터 하면 됨



### DB API

- Django 모델 클래스에는 objects라는 Manager가 기본적으로 존재한다.
- QuerySet : DB로부터 전달받은 객체 목록이다.
