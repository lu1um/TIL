## SQLite

- INSERT, SELECT, UPDATE, DELETE 가 CRUD에 해당하는 명령어다.



#### DROP

- `DROP TABLE ~` : ~ 테이블을 삭제한다.



#### CREATE

- `CREATE TABLE ~ ( __ ??? attribute, ...);` : 테이블을 생성하는 명령어다.
  - ??? : 자료형을 지정하며, 만약 PRIMARY KEY라면 무조건 INTEGER여야 생성된다.
  - attribute : NOT NULL, PRIMARY KEY등 부여해줄 속성을 작성한다.



#### INSERT

- `INSERT INTO ~ (__, ...) VALUES (???, ...)`; : 필드를 명시하고 데이터를 삽입하는 방법. 만약 PRIMARY KEY를 지정했다면 이 구문을 통해 PRIMARY KEY는 자동으로 입력되고, 나머지 필드만 입력할 수 있기 때문에 주로 이 구문을 사용한다.
- `INSERT INTO ~ VALUES (???, ...), (???, ...), ...;` : 필드 순서대로 값들이 추가된다.



#### SELECT

- `SELECT __ FROM ~` : ~ 테이블에서 __ field를 조회한다. 보통 *로 모든 필드를 조회하며, PRIMARY KEY가 특별히 지정되지 않았을 때 생성되는 rowid라는 PRIMARY KEY는 *로 조회되지 않으므로, 아래와 같이 불러줘야 조회가능하다.

  `SELECT rowid, * FROM tables`

- SELECT는 clause, 절과 함께 사용되므로 SQL문 중에 가장 복잡하게 사용 가능하다.

  - LIMIT : 반환되는 행 수를 제한. OFFSET과 같이 사용할 수도 있다.
  - WHERE : 조건을 지정할 수 있다.
  - DISTINCT : 중복 행을 제거하는 명령이다. 이 절은 `SELECT DISTINCT`처럼 바로 뒤에 써있어야한다.

  `SELECT __ FROM ~ LIMIT 5 OFFSET 2` : 3번째 튜플부터(OFFSET) 5개 조회(LIMIT)

  `SELECT __ FROM ~ WHERE address = '서울'` : address의 값이 서울인 튜플만 불러오기



#### DELETE

- `DELETE FROM ~ WHERE 조건` : 테이블 내에서 조건에 부합한 요소를 지운다.
- 기본적으로 PK에 AUTOINCREMENT가 적용되어있다면, INSERT를 수행했을 때 DELETE된 PK위치에 다시 추가되지 않는다. 중요한 설정이라고 한다. 



#### UPDATE

- `UPDATE ~ SET __=???, __=???, ... WHERE 조건` : 테이블 내에서 조건에 부합한 튜플의 필드들에 값을 지정해준 값으로 수정해준다.

