# Soomgo 과제 
## 기능
- 어드민 계정으로 상품 등록
- 일반 유저로 상품 구매
- 구매한 상품 상세 보기
- 구매한 상품 목록 보기


# ****Getting Started****
### Project Setup
```markdown
1. $ git@github.com:live-jh/soomgo-assignment.git
2. $ pip install virtualenv
3. $ virtualenv venv
4. $ source venv/bin/activate
5. config/settings/common/env.json 파일 옮기기 (있는 사람에게 요청)
6. 환경 변수 DJANGO_SETTINGS_MODULE=config.settings
7. $ pip install -r requirements.txt
8. $ python manage.py runserver
```

# Project Information

### backend

- Python 3.8
- PostgreSQL 13
- Django 4.0

### document
- swagger

### version control
- Git & Gitlab

# Project Structure

```markdown
🚀 PROJECT
├── 📄 README.md
├── 📁 account
│   ├── 📄 __init__.py
│   ├── 📄 account_serializers.py
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📁 migrations
│   ├── 📄 models.py
│   ├── 📄 tests.py
│   ├── 📄 urls.py
│   └── 📄 views.py
├── 📁 config
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py
│   ├── 📁 common
│   │   ├── 📄 env.json                 # 환경변수
│   │   ├── 📄 exception_handler.py     # 커스텀 에러 핸들러
│   │   ├── 📄 library_classes.py       # 함수 라이브러리
│   │   └── 📄 response_code.py         # 상수 응답 코드
│   ├── 📄 settings.py                  # 프로젝트 세팅
│   ├── 📄 settings_test.py             # 테스트 세팅
│   ├── 📄 test_runner.py               # 테스트 러너
│   ├── 📄 urls.py
│   ├── 📄 utils                       
│   │   └── 📄 swagger_parameters.py    # 스웨거 openapi 함수
│   └── 📄 wsgi.py
├── 📄 manage.py
├── 📁 product
│   ├── __init__.py
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📁 migrations
│   ├── 📄 models.py
│   ├── 📄 product_serializers.py
│   ├── 📄 tests.py
│   ├── 📄 urls.py
│   └── 📄 views.py
├── 📄 requirements.txt
└── 📁 templates
```


# DB ERD
![soomgo](https://user-images.githubusercontent.com/48043799/155637276-60166ca4-458d-4dd3-9e32-b1de6c4d5dbe.png)



# Test Guide
### 테스트 명령
- `$ python manage.py test --verbosity 3`
### 커버리지 테스트
- `$ coverage run manage.py test`
### 커버리지 리포트
- `$ coverage report`


