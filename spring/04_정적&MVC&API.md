# 정적 컨텐츠

### static에 html문서 작성하기

static에 html문서를 작성하게 되면, spring boot에서는 자동으로 GET요청에 html문서를 응답하게 된다.

만약 `src/main/resources/static/hello-static.html`문서가 존재한다면, controller에 아무런 작업을 하지 않아도 `localhost:8080/hello-static.html`요청에 해당 html 문서가 응답하게 된다.

당연하게도 hello-static에 관련된 컨트롤러가 존재한다면, 해당 컨트롤러의 응답이 우선이다.



# MVC

### Controller 만들기

컨트롤러가 있어야 MVC패턴이 시작될 수 있다. Param을 하나 받는 GET요청 컨트롤러를 만들어보았다.

```java
    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam(value = "name", defaultValue = "annonymous") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-mvc";
    }
```

name이라는 param을 받는 hello-mvc라는 요청을 처리하는 컨트롤러이다. 응답대로 hello-mvc.html이라는 템플릿을 만들어주면, name이라는 attribute를 넘겨주며 html을 응답하게된다.



# API

`@ResponseBody`라는 데코레이터를 넣으면, return의 내용이 http Body에 담겨 응답하게된다.

일단 문자열을 응답해보자.

```java
    @GetMapping("hello-api")
    @ResponseBody
    public String helloApi(@RequestParam("name") String name) {
        return "hello " + name;
    }
```

Json과 같은 데이터를 응답해보자.

1. json과 같은 형태인 class를 static으로 만들어주자.

```java
    static class Hello {
        private String name;
	
        // getter가 작성되어야 json의 키 값으로 인식된다.
        public String getName() {	
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
```

2. 만들어진 class를 리턴하는 컨트롤러를 만들어주자.

```java
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);	// setter로 Hello.name 조작
        return hello;			// class 반환, 자동으로 json으로 변환해준다.
    }
```

3. 완성!

api응답은 viewResolver대신 HttpMessageConverter가 동작해 응답하게 된다.
