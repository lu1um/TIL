# TypeScript

## 설치

- node.js가 깔려있고, npm이 활용 가능할 때

```shell
sudo npm install -g typescript
```



## 생성 파일

- `tsconfig.json` : 타입스크립트를 `tsc -w`로 변환하는 설정들이 담긴다.
  - `target` : 어떤 버전으로 작성할지, esnext로 하면 최신 문법으로 작성된다.
  - `module` : 어떤 문법으로 작성할 지 
- `~.ts` : typescript가 작성되는 소스파일
-  typescript는 웹페이지가 읽지 않는다. 따라서 js로 변환해주어야하는데, 이는 콘솔에 아래 명령어를 입력하고, 실행해놓으면 자동으로 변환해준다. 이를 컴파일한다고 표현한다.

```shell
tsc -w
```

