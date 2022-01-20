# make Auto checkout by python

** 참고 문헌 **
1. https://sir.kr/so_python/273
2. https://pythondocs.net/selenium/셀레니움-wait-개념-이해하기-implicitly-wait-vs-explicitly-wait/

1. chrome 설치
2. selenium 설치
3. chromedriver 설치 - 같은 디렉토리에 넣기!

같은 폴더내의 URL.txt, PASSWORD.txt를 만들고, 클릭하기 원하는 URL, XPath, ID, 비번을 저장해놓았다.

문제점 : Path.cwd()는 현재 터미널의 작업공간 주소를 불러온다..
 -> __file__ 객체를 사용함으로 해결

로그인까지 했고, 이제 클릭만 해보자!