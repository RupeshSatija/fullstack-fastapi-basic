import os

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


@app.get("/image/{animal}")
async def get_animal_image(animal: str):
    valid_animals = ["cat", "dog", "elephant"]
    if animal not in valid_animals:
        raise HTTPException(status_code=404, detail="Animal not found")

    image_path = f"static/{animal}.jpg"
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(image_path)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    file_size = os.path.getsize(file_path)
    return {
        "filename": file.filename,
        "size": file_size,
        "content_type": file.content_type,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
