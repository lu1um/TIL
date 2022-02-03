### 01-27 class method

class method, static method, instance method가 있다. 평소 쓰던건 instance method

#### class method

- 클래스 변수에 먼저 접근하는 것으로, 매개변수로 cls가 넘겨지고, 데코레이터가 존재한다. 상속이 되었을 때 해당 클래스를 먼저 참조하고, 없다면 부모클래스의 클래스 변수를 참조한다.

  ```python
  class Person:
      species = human
      
      @classmethod
      def person_cls(cls):
          return cls.species
    
  class Male(Person)
  	pass
  ```

  

#### static method

- `def foo(~)`처럼 클래스정보가 전달되지 않는다. 데코레이터가 필요하다.

  ```python
  class Person:
      ~
      
      @staticmethod
      def foo():
          return ~
  ```



#### instance method

- 보통의 메서드로 첫 번째 인자로 self를 받는 메서드



#### class namespace

```python
class Person:
    species = 'human'
    
    def __init__(self, name):
        self.name = name
```

- 위와 같이 정의했을 때, `self.species`는 class namespace에 속한다.
- `self.name`은 instance에 속한다.

- 만약 Person으로 두 객체를 만들었고, `Person.species = 'dog'`로 변경하면, 두 객체 모두 변화하는 효과를 얻을 수 있다.



#### isinstance(instance, class)

- instance가 class의 인스턴스나 서브클래스일 경우 True반환, 아닐경우 False를 반환한다.



#### issubclass(subclass, class)

- subclass가 class를 상속했다면 True를 반환한다. 상속관계가 아닐경우 False
