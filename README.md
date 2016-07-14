# hobbycoding
카페 가서 코딩하려 하는데 혼자 하니 늘어진다.
파이썬을 좋아하는 다른 개발자들을 만나 같이 코딩하면 어떨까?
온오프믹스... Meetup사이트.. 다 복잡하다...

이럴땐 하비코딩!

## 개발환경 세팅하기
[파이썬 개발환경 세팅하기](https://milooy.wordpress.com/2015/07/31/python-set-environments/)를 참조하여 pyenv로 파이썬 `3.5.1`을 설치한다.
(파이썬 버전 확인 명령어: `python -V`)


## 의존성 관리
```shell
pip install -r requirements.txt
bower update
npm install
```

## 디비 마이그레이션
```shell
./manage.py migrate
```

## grunt돌리기
CSS를 LESS로 바꾼다
```shell
grunt
```

## 서버 띄우기
```shell
./manage.py runserver
```