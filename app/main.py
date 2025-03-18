from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root_read():
    return {"messages": "hello world"} 