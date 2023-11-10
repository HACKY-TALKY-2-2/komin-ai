# Komin.AI - Dev Guideline

## See Also
- [komin-crawler](https://github.com/JayM-Oh/komin-Crawler)

## Requirements
- Python 3.11
- Docker
- OpenAI API

## Conventions

### Active Branches
- `dev` (default): 
- `feature/{description}`: 새로운 기능이 추가되는 경우에 사용
- `fix/{description}`: `dev` 브랜치로 반영하는 사소한 오류 수정 시에 사용


## Dev Guidelines

### Python Dependencies
가상환경을 활성화하고 필요한 패키지를 설치합니다.
```shell
pip install -r requirements.txt
```
`requirements.txt` 파일의 패키지 목록을 최신화하기 위해 사용하십시오
```shell
pip freeze > requirements.txt
```

### Server Startup
Docker를 활용하여 FastAPI 서버를 실행합니다.
```shell
docker build -t komin .
docker run -p 80:8000 komin
```

## Database Migration
SQLAlchemy 모델에 변경사항이 발생한 경우, 이를 위한 Alembic revision 파일을 자동 생성합니다.
자동 생성 후, 작성된 내용이 의도한 변경사항을 잘 수행하는지 검토해보는 것을 권장합니다.
```shell
make revision DESCRIPTION="Description For Revision"
```

## Deployment
`dev`, 브랜치에 새로운 push가 일어날 때마다 [GitHub Actions](.github/workflows)를 활용한 ECR 이미지 업로드를 활용한 배포가 진행됩니다.

---
# Komin.AI API Reference
[Swagger Docs](http://ec2-3-39-46-151.ap-northeast-2.compute.amazonaws.com/docs#/)