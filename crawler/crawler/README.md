# komin-Crawler
channelTalk Hackerton-HACKYTOKY 2nd Team16

## newsDB.py
1. **초기화 (`__init__` 메소드)**:
    - 데이터베이스 연결을 설정합니다 (`sqlite3.connect`).
    - 데이터베이스 파일 이름(`google_news.db`)과 테이블 이름(`google_news`, `keyword`)을 정의합니다.
    - `google_news` 테이블과 `keyword` 테이블에 사용될 컬럼과 데이터 타입을 지정합니다.

2. **소멸자 (`__del__` 메소드)**:
    - 인스턴스가 삭제될 때 데이터베이스 연결을 닫습니다 (`stop` 메소드 호출).

3. **`stop` 메소드**:
    - 데이터베이스 연결을 안전하게 닫습니다.

4. **Google News 테이블 관련 메소드**:
    - `queryCreateGoogleNewsTable`: 주어진 키워드에 맞는 Google News 테이블을 생성합니다.
    - `queryInsertGoogleNewsTable`: Google News 데이터를 테이블에 삽입합니다.
    - `queryDeleteAllGoogleNewsTable`: 주어진 키워드에 해당하는 Google News 테이블을 삭제합니다.
    - `querySelectAllGoogleNewsTable`: 주어진 키워드에 해당하는 Google News 테이블의 모든 데이터를 조회합니다.

5. **키워드 테이블 관련 메소드**:
    - `queryCreateKeywordTable`: 키워드를 저장할 테이블을 생성합니다.
    - `queryInsertKeywordTable`: 키워드 데이터를 테이블에 삽입합니다.
    - `queryDeleteKeywordTable`: 주어진 키워드를 키워드 테이블에서 삭제합니다.
    - `querySelectAllKeywordTable`: 키워드 테이블의 모든 데이터를 조회합니다.

## get_google_news.py
1. **모듈 임포트**: 
    - `apscheduler`는 Python에서 스케줄러 기능을 제공하는 라이브러리입니다. `BackgroundScheduler`는 백그라운드에서 작업을 스케줄링하며, `JobLookupError`는 스케줄러 관련 에러 처리에 사용됩니다.
    - `requests`는 HTTP 요청을 보내는 데 사용됩니다.
    - `datetime`와 `maya`는 날짜와 시간을 다루는 데 사용됩니다.
    - `feedparser`는 RSS 피드를 파싱하는 데 사용됩니다.
    - `db_google_news`는 데이터베이스 작업을 위한 사용자 정의 모듈로 보입니다.

2. **GoogleNewsCron 클래스**:
    - `__init__`: 클래스가 인스턴스화될 때 호출됩니다. 스케줄러를 초기화하고 데이터베이스 매니저 인스턴스를 생성합니다.
    - `__del__`: 클래스 인스턴스가 삭제될 때 호출되며, `stop` 메소드를 호출하여 스케줄러를 중단합니다.
    - `exec`: 지정된 국가와 키워드로 Google News RSS 피드를 조회합니다. 조회 성공 시, 받아온 데이터를 파싱하여 데이터베이스에 저장합니다.
    - `run`: 크롤링 작업을 시작합니다. 'once', 'interval', 'cron' 모드에 따라 다른 스케줄링 옵션을 사용합니다.
    - `stop`: 스케줄러와 데이터베이스 연결을 중단합니다.

3. **메인 기능**:
    - Google News의 RSS 피드를 이용하여 지정된 키워드에 대한 뉴스를 가져옵니다.
    - 가져온 뉴스 데이터는 `feedparser`를 통해 파싱되고, `maya`를 사용해 시간을 서울 시간대로 변환합니다.
    - 파싱된 데이터는 `dbManager` 객체(데이터베이스 관리 클래스의 인스턴스)를 통해 데이터베이스에 저장됩니다.
    - 스케줄러는 주어진 모드('once', 'interval', 'cron')에 따라 주기적으로 `exec` 메소드를 실행합니다.
