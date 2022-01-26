### 01-26 class method

#### class method

- `def foo(self, ~)`처럼 클래스가 전달되어 클래스의 인스턴스에 접근 가능하다.

#### static method

- `def foo(~)`처럼 클래스정보가 전달되지 않음



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
