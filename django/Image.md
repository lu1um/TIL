# Image

### ImageField

- 이미지 업로드에 사용되는 모델 필드이다. FileField의 자식 클래스이다.
- 이미지 자체를 갖는 것이 아니라, 이미지의 주소인 Text를 가지고 있다.
- 기본 max_length는 100이지만, 변경 가능하다.
- **Pillow** 라는 라이브러리가 반드시 설치되어있어야한다!



### ImageField 작성하기

- upload_to, storage 라는 속성이 있다.

- `blank=True` : 빈 값이 허용되도록, 즉 이미지를 업로드 하지 않아도 되도록 model을 설정한 것

  - `null=True` : blank일 때 빈 문자열이 아닌 NULL이 저장되는 것인데, **문자열 기반 필드에는 쓰지말자.**

- `upload_to='images/'` : images라는 경로에 실제 이미지가 저장된다는 뜻이다.

  - strftime : %Y, %H 처럼 시간을 나타내는 문자열을 뜻하는 것이다. 찾아보자
  - upload_to에 strftime형식이 포함될 수 있다. 따라서 날짜형태로 올린다면 정리하기 좋다.

  ```python
  upload_to='uploads/%Y/%m/%d/'
  ```

  - 위처럼 쓰면 uploads 디렉토리에 연/월/일 폴더에 저장된다.
  - 함수를 사용해 pk값을 넣을 수도 있다.

  ```python
  def articles_image_path(instance, filename):
      return f'image_{instance.pk}/{filename}'
  
  upload_to=articles_image_path
  ```

  - 함수의 파라미터와 리턴 형태는 고정적이다.

- upload_to에 지정한 디렉토리를 settings.py의 MEDIA_ROOT, MEDIA_URL에 설정해주자.

- 또, urls.py에 urlpatterns를 수정해야한다.

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  

### CREATE

- create.html의 form에 enctype속성을 부여해줘야한다. 
- `enctype="multipart/form-data"`
- input중 type이 file인 것이 있을 경우, 반드시 적용해줘야하는 속성이다.



- views.py에 form을 만들 때, request.FILES를 두 번째 인자로 넘겨주면 된다.

  ```python
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
         	...
  ```



### READ

- 넘겨준 DB의 field.url로 url기반으로 출력해준다.

  ```django
  <img src="{{ article.image.url }}">
  ```

- image가 없을 때도 오류가 나지 않기 위해서 if문을 포함해주자

  ```django
  {% if article.image %}
    <img src="{{ article.image.url }}">
  {% endif %}
  ```

  

### 이미지 Resizing

[참고 링크](https://github.com/matthewwithanm/django-imagekit)

- 사진이 너무 크면 서버에 부담이 가기때문에 resizing을 고려해야한다.

- django-imagekit 라이브러리를 설치해야한다.

- INSTALLED_APPS에 'imagekit'을 등록하면 준비 끝

- 원본을 저장하지 않고, 썸네일형태로 저장하는 방법

  ```python
  # models.py
  
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Models):
      ...
      image = ProcessedImageField(
          blank=True,
          upload_to='images/',
          processors=[Thumbnail(200, 300)],	# width, height
          format='JPEG',
          options={'quality': 60},	# 품질 %
      )
  ```

