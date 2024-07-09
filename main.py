from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/voices/')
async def save_voice(temp):
    import pdb;pdb.set_trace()
    return {"item_id": item_id, "q": q}
