from fastapi impprt FastAPI

app = FastAPI()

@app.post("/generate")
async def text_generation_pipeline():
	print("generated text")
