
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

RESULT = {
    "A": {
        "text": "Report job-c6dddbf: café\nReady ✔",
        "complete": True,
        "error": None
    },
    "B": {
        "text": "Partial job-c6dddbf",
        "complete": False,
        "error": None
    },
    "C": {
        "text": "Draft job-c6dddbf",
        "complete": False,
        "error": "model unloaded"
    }
}


@app.get("/")
async def get_result():
    return JSONResponse(content=RESULT)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
