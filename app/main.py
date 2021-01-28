from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from Operations.set_data import SetData

app = FastAPI()


class MySum(BaseModel):
    data: List[dict] = []


@app.get("/ping")
def ping():
    return {"response": "Pong"}


@app.post('/perfect_sum')
def my_sum(mysum: MySum):
    my_data = dict(mysum)
    set_data = SetData(my_data['data'])
    my_data = set_data.execute_operation()
    return {"response": my_data}
