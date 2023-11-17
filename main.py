# main.py
from fastapi import FastAPI, HTTPException, UploadFile, File
import json
from minio import Minio
from minio.datatypes import Object
from etl_process import CustomJSONEncoder, ETLProcess, CodeContext
import asyncio

app = FastAPI()

minioClient = Minio("YOUR_MINIO_ENDPOINT", access_key="YOUR_ACCESS_KEY", secret_key="YOUR_SECRET_KEY")

@app.post("/process_code/")
async def process_code(file: UploadFile = File(...)):
    content = await file.read()

    try:
        # Deserialize JSON to get code snippet and surrounding text
        data = json.loads(content, cls=CustomJSONEncoder)
        code_snippet = data['code']
        surrounding_text = data['text']

        etl_process = ETLProcess(code_snippet, surrounding_text)
        await asyncio.run(etl_process.run())

        return {"status": "success", "processed_data": etl_process.combined_data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
