from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status

app = FastAPI()

class RequestModel(BaseModel):
    fileUploadId: str

@app.post("/upload")
async def uploadId (fileUploadId: RequestModel):

    # insert logic
    
    response = fileUploadId.dict()
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
