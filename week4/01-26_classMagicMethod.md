### 01-26 class_magic method

#### magic method

- `__init__`, `__del__`으로 생성, 파괴시 실행될 인스턴스
- `__len__` : `len(<class>)`를 했을 때 호출될 인스턴스를 리턴하는 함수.
- `__str__` : `print(<class>)`를 했을 때 호출될  인스턴스 리턴

- `__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__` : 비교 인스턴스로 관례상 bool값을 리턴한다.
