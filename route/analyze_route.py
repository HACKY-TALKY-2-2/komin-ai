import os

import openai
from fastapi import APIRouter, Depends
from data.database import get_db
from data.models import Entity, News
from starlette import status
from sqlalchemy.orm import Session
import openai
import os
from entity.dashboard_entity import Dashboard, EntityCreate, News
import pandas as pd


router = APIRouter(prefix='/analyze')


openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(prompt, model="gpt-4-1106-preview"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content
@router.get("/industrial", summary='')
def get_industrial_summary(query: str):
    result = generate_response("""
- 최근 {0}의 동향과 이슈를 정리하시오. 추가적인 설명 없이 목록화하여 정리하시오.
- 예시는 아래와 같습니다, 예시의 형식을 참고하여 && && 기호 사이에 정리하시오
인터넷 검색을 사용하여도 좋고, 아래의 $$ $$사이에 정리된 참고 자료를 요약해도 좋다

&&
1) 최근 "새팜"이라는 회사가 유망하여 부각 중
2) 직불금이 큰 이슈로 성장 중
&&

$$
{1}
$$
""".format(query, "."))

    return {
        "result": result
    }


@router.get("/finance", summary='')
def get_finance_data(query: str):
    result = generate_response("""
- 당신은 친절한 금융 전문가입니다. 당신이 답할 금융 초보의 질문은 %% %% 사이에 있습니다..
- 답변을 친절히 작성하여 && && 기호 사이에 정리하시오.
대답 외에 다른 말을 작성하지 마십시오
%%
%%
""".format(query, "."))

    return {
        "result": result
    }


@router.get("/news", summary='')
def get_daily_news():

    result = generate_response("""
- $$ $$ 기호 안의 뉴스 내용을 요약하여 && && 기호 사이에 정리하시오.
- 각각의 뉴스마다 해당 사건이 금융계에 미칠 영향을 예상하여 추가하십시오
대답 외에 다른 말을 작성하지 마십시오
%%
{0}
%%
""".format('\n'.join(pd.read_csv('crawler/google_news_채널톡_ko.csv')['title'].to_list()[:15])
))

    return {
        "result": result
    }