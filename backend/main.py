from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import requests
import json

# ================== APP ==================
app = FastAPI()

# ================== CORS ==================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================== DIFY CONFIG ==================
DIFY_API_KEY = "app-y8WYwZs8NhFNlrW7MdPrzZx1"   # 👉 thay bằng API key thật khi deploy
DIFY_CHAT_URL = "https://api.dify.ai/v1/chat-messages"

# ================== SCHEMA ==================
class RIASECRequest(BaseModel):
    name: str
    class_: str = Field(alias="class")   # alias tránh keyword Python
    school: str
    answers_json: List[int]

# ================== API ==================
@app.post("/run-riasec")
def run_riasec(data: RIASECRequest):

    # ===== VALIDATE =====
    if len(data.answers_json) != 50:
        raise HTTPException(
            status_code=400,
            detail="answers_json phải có đúng 50 phần tử"
        )

    # ===== PAYLOAD GỬI DIFY (CHATBOT) =====
    payload = {
        "inputs": {
            "name": data.name,
            "class": data.class_,
            "school": data.school,
            "answers_json": json.dumps(
                data.answers_json,
                ensure_ascii=False
            )
        },
        "query": (
            "Dựa trên thông tin học sinh và kết quả trắc nghiệm RIASEC, "
            "hãy phân tích và đưa ra bản tư vấn hướng nghiệp rõ ràng, "
            "phù hợp với học sinh THPT Việt Nam."
        ),
        "response_mode": "blocking",
        "user": data.name.strip() if data.name.strip() else "student"

    }

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    # ===== GỌI DIFY CHATBOT =====
    try:
        response = requests.post(
            DIFY_CHAT_URL,
            json=payload,
            headers=headers,
            timeout=90
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Lỗi kết nối Dify: {str(e)}"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    # ===== XỬ LÝ RESPONSE (SỬA LỖI 4) =====
    dify_result = response.json()
    text_output = dify_result.get("answer", "")

    return {
        "data": {
            "outputs": {
                "text": text_output
            }
        }
    }

