import os
import asyncio
from PIL import Image
from io import BytesIO
import base64
from pathlib import Path

genai.configure(api_key=os.getenv("API_KEY"))
vision_model = genai.GenerativeModel('gemini-pro')
text_model = genai.GenerativeModel('gemini-pro-vision')

with open(f"{Path.cwd()}/image_context_prompt.txt","r") as text_prompt:
	image_context_prompt = text_prompt

async def generate_image_context(image):
	response = vision_model.generate_content([image_context_prompt,image])
	response.resolve()
	return response.text

async def generate_text(text_prompt):
	pass
