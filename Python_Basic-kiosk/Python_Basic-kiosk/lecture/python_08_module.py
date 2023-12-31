#   라이브러리(Libarary), 패키지(Package), 모듈(Moudle)
# - 라이브러리 >= 패키지 >= 모듈

# 1. 라이브러리: 여러 패키지와 모듈의 묶음
# 2. 패키지: 특정 기능과 관련된 여러 모듈의 묶음
# 3. 모듈: 이미 작성된 프로그램(일반적으로 한 파일을 의미)

# ** 모듈의 종류
# 1. 내부 모듈 : 파이썬을 설치 하면 기본적으로 제공
# 2. 외부 모듈 : 다른 개발자가 개발 해놓은 모듈
# 3. 사용자 정의 모듈 : 직접 개발해서 사용하는 모듈

# 1. import
# ex) import requests
#   -> "requests" 라이브러리 전체 호출 (1,000개)
#   -> requests.get()


#   2.from ~ import
#    es) form requests import get, put, ...
#    -> "requests" 라이브러리 내에서 "get" 모듈만 호출
#    -> get()

#   3.as(Alias:별명)
#    ex) import requests as req
#    -> "requests" 모듈 전체 호출, 그리고 "req"라는 별명 붙이기
#    -> req.get()