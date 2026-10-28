import os
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

macbook_client = genai.Client(api_key=os.getenv("APPLE_AI_API_KEY"))

class AppleRecipeSchema(BaseModel):
    device_dish: str
    mac_ingredients: list[str]
    ios_steps: list[str]
    watchos_time: int

siri_prompt = "ขอเมนูอาหารทำในหอพักง่ายๆ อ้างอิงจากราคาวัตถุดิบปัจจุบัน"

response = macbook_client.models.generate_content(
    model="gemini-2.5-flash",
    contents=siri_prompt,
    config=types.GenerateContentConfig(
        system_instruction="คุณคือผู้ช่วยอัจฉริยะ Apple Intelligence เชี่ยวชาญการแนะนำอาหารสไตล์มินิมอล",
        tools=[{"google_search": {}}],
        response_mime_type="application/json",
        response_schema=AppleRecipeSchema,
        temperature=0.7,
    ),
)

print(response.text)
