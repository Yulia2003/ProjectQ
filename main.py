from fastapi import FastAPI
import uvicorn
from db.base import database
from endpoints import users, auth, publik

app = FastAPI(title="ProjectQ")


app.include_router(users.router, prefix="/users", tags=["users"]) 
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(publik.router, prefix="/publik", tags=["publik"])

@app.get("/")
def read_root():
  return {"Hello": "World"}



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)