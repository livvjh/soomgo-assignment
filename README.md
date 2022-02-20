# ****Getting Started****
### Project Setup
```markdown
1. $ git clone https://deploy.addcampus.com/career-wallet/career-wallet.git
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
.
├── 📁 backend
│   ├── 📁 _api_cms         # cms api (사용 x)
│   ├── 📁 _api_web         # web api 
│   ├── 📁 _common          # 공통
│   ├── 📁 account          # 유저
│   ├── 📁 addy             # 애디 연동
│   ├── 📁 company          # 회사
│   ├── 📁 recruit          # 채용 공고
│   └── 📁 resume           # 이력서
├── 📁 config
│   ├── 📁 authorization    # 인증 
│   ├── 📁 common           # 공통 모듈
│   ├── 📁 settings         # settings.py 
│   ├── 📄 urls.py          # root urls
│   └── 📄 wsgi.py          # wsgi
├── 📄 eb-deploy.sh         # 배포 스크립트
├── 📁 frontend             # 프론트엔드 앱
│   ├── 📁 cms              # 사용 x 
│   ├── 📁 templates        # 빌드 후 index.html
│   └── 📁 web              # front react app
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 README.md            # 프로젝트 문서
└── 📄 todo-list.py         # 작업 목록
```


# DB ERD
> 공사중 👷🏼


# Test Guide
### 테스트 명령
- `$ python manage.py test --settings='config.settings_test' --verbosity 3`
### 커버리지 테스트
- `$ coverage run manage.py test`
### 커버리지 리포트
- `$ coverage report -m`


