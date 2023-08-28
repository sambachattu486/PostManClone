from fastapi import FastAPI
import time
import requests
import ast
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

class URL(BaseModel):
    url:str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_html():
    html_file_path = "static/index.html"
    return FileResponse(html_file_path)

@app.get("/get",tags=["REST Client"])
async def get_body(url:str,
                   query1:Union[str,None]=None,
                   query2:Union[str,None]=None,
                   query3:Union[str,None]=None,
                   query4:Union[str,None]=None,
                   query5:Union[str,None]=None):
    string = url+"?"
    if query1:
        string+=query1+"&"
    if query2:
        string+=query2+"&"
    if query3:
        string+=query3+"&"
    if query4:
        string+=query4+"&"
    if query5:
        string+=query5+"&"
    final_url_str = string.rstrip("&")
    try:
        t1=time.time()
        response = requests.get(final_url_str,timeout=4)
        Time = round((time.time()-t1)*1000)
        size = len(response.content)/1000
        headers = response.headers
        if response.status_code==200:
            try:  
                return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":response.json()}
            except ValueError:
                return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":response.text}
        else:
            return response.status_code
    except Exception as e:
        return {"Exception Message":str(e)}
    
@app.post("/post",tags=["REST Client"])
async def post(url:str,
               request_body:str,
               query1:Union[str,None]=None,
               query2:Union[str,None]=None,
               query3:Union[str,None]=None,
               query4:Union[str,None]=None,
               query5:Union[str,None]=None):
    
    string = url+"?"
    if query1:
        string+=query1+"&"
    if query2:
        string+=query2+"&"
    if query3:
        string+=query3+"&"
    if query4:
        string+=query4+"&"
    if query5:
        string+=query5+"&"
    final_url_str = string.rstrip("&")
    payload_dict=ast.literal_eval(request_body)
    try:
        t1= time.time()
        response = requests.post(final_url_str,json=payload_dict,verify=False)
        Time = round((time.time()-t1)*1000)
        size = len(response.content)/1000
        headers = response.headers
        return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":response.json()}
    except Exception as e:
        return {"Exception message":str(e)}
    
@app.put("/put",tags=["REST Client"])
async def update(url:str,
                 body : str,
                 query1:Union[str,None]=None,
                 query2:Union[str,None]=None,
                 query3:Union[str,None]=None,
                 query4:Union[str,None]=None,
                 query5:Union[str,None]=None,):
    string = url+"?"
    if query1:
        string+=query1+"&"
    if query2:
        string+=query2+"&"
    if query3:
        string+=query3+"&"
    if query4:
        string+=query4+"&"
    if query5:
        string+=query5+"&"
    final_url_str = string.rstrip("&")
   
    payload_dict=ast.literal_eval(body)

    try:
        t1=time.time()
        response  = requests.put(final_url_str,json=payload_dict,verify=False)
        Time = round((time.time()-t1)*1000)
        size = len(response.content)/1000
        headers = response.headers
        return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":response.json()}
    except Exception as e:
        return{"Exception message="+str(e)}
    
@app.delete("/delete",tags=["REST Client"])
async def delete(url :str,
                 query1:Union[str,None]=None,
                 query2:Union[str,None]=None,
                 query3:Union[str,None]=None,
                 query4:Union[str,None]=None,
                 query5:Union[str,None]=None):
    string = url+"?"
    if query1:
        string+=query1+"&"
    if query2:
        string+=query2+"&"
    if query3:
        string+=query3+"&"
    if query4:
        string+=query4+"&"
    if query5:
        string+=query5+"&"
    final_url_str = string.rstrip("&")
    try:
        t1 = time.time()
        response = requests.delete(final_url_str,verify=False)
        Time = round((time.time()-t1)*1000)
        size = len(response.content)/1000
        headers = response.headers
        print(response.status_code)
        if response.status_code>=200 and response.status_code<=299:
            return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":{"message":"Post deleted successfully"}}
        else:
            return {"time":Time,"size":size,"status_code":response.status_code,"headers":headers,"body":{"message":"Failed to deleted"}}
    except requests.exceptions.ConnectionError as e:
        return {"Error Message":str(e)}