### 01-20

#### selenium

- 우선 driver를 선언함으로 크롬창을 띄울 수 있다.

  ```python
  from selenium.webdriver import Chrome
  
  driver = Chrome(<chromedriver.exe 가 있는 디렉토리>)
  ```

- URL열기
  - `driver.get(<URL>)`
  - 열릴 때 까지 대기 : `driver.implicitly_wait(<최대 대기시간>)`
- 텍스트 입력
  - `txtbox = driver.find_element_by_xpath(<xpath>)`이후 `txtbox.send_keys(<txt>)`로 텍스트 박스에 text 입력가능
- 클릭
  - `driver.find_element_by_xpath(<xpath>).click()`으로 클릭!

- 최소화, 최대화

  - `driver.minimize_window()`
  - `driver.maximize_window()`

  

