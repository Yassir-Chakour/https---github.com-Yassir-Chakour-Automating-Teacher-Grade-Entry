from fastapi import FastAPI, Request

api = FastAPI()

@api.post("/sync-grades")
async def sync_grades(request: Request):
    data = await request.json()
    print(f"📥 Received data for class: {data.get('class_name')}")

    return {"status": "success", "message": "Grades sync started"}
