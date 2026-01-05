# backend/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, create_engine, Session, select
import uvicorn
import uuid
import shutil
import os
from typing import List, Optional
from datetime import datetime
from PIL import Image

# ---- Config ----
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
DB_FILE = "backend/data.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

# ---- DB models ----
from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gtin: str
    name: str
    brand: Optional[str] = None
    calories_per_100g: Optional[float] = None
    nutrients_json: Optional[str] = None
    last_updated: Optional[datetime] = None

# ---- Pydantic models (API) ----
class ScanResult(BaseModel):
    ingredients: List[str]
    portions_estimate: str
    confidence: float
    notes: Optional[str] = None

class TrendItem(BaseModel):
    id: str
    title: str
    summary: str
    health_flag: Optional[str] = None  # e.g., "ok", "watch", "danger"

# ---- App init ----
app = FastAPI(title="Optioun POC API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(DATABASE_URL, echo=False)
SQLModel.metadata.create_all(engine)

# seed mock product(s) if none
with Session(engine) as s:
    q = s.exec(select(Product)).all()
    if not q:
        p = Product(
            gtin="0001112223334",
            name="Mock Vollkornbrot 500g",
            brand="OptiounBrand",
            calories_per_100g=250.0,
            nutrients_json='{"fat":5.0, "protein":9.0, "carbs":45.0}',
            last_updated=datetime.utcnow()
        )
        s.add(p)
        s.commit()

# ---- Endpoints ----

@app.post("/scan", response_model=ScanResult)
async def scan_image(file: UploadFile = File(...)):
    """
    Mock scan endpoint:
    - saves uploaded image
    - heuristically derives ingredients from filename (until you plug ML)
    - returns portions estimate + confidence
    """
    # save file
    file_ext = os.path.splitext(file.filename)[1] or ".jpg"
    uid = uuid.uuid4().hex
    saved_path = os.path.join(UPLOAD_DIR, f"{uid}{file_ext}")
    with open(saved_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # attempt to open with PIL (just to validate image)
    try:
        img = Image.open(saved_path)
        img.verify()
    except Exception:
        # not a valid image? remove and error
        os.remove(saved_path)
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid image")

    # Heuristic: split filename by underscores/commas to fake ingredients
    fname = file.filename.lower()
    tokens = [t.strip() for t in fname.replace(".jpg", "").replace(".jpeg", "").replace(".png", "").replace("-", " ").replace("_", " ").split() if len(t.strip())>2]
    # keep only likely food words by naive list (this is mock)
    common_food_words = {"salat","brot","tomate","käse","eier","ei","hähnchen","chicken","reis","nudeln","pasta","pizza","avocado","banane","apfel","fisch","lachs","tofu","kartoffel","pommes","suppe","reis"}
    ingredients = []
    for t in tokens:
        if t in common_food_words:
            ingredients.append(t)
    # fallback: provide generic tags
    if not ingredients:
        ingredients = ["unknown_dish", "water", "salt"]

    # mock portion estimate & confidence
    portions = "1 portion" if "small" in fname or "single" in fname else "2 portions" if "large" in fname or "family" in fname else "1 portion"
    confidence = 0.86 if any(t in common_food_words for t in tokens) else 0.45

    notes = "This is a mock result. Replace with ML-based vision model in production."

    return ScanResult(ingredients=ingredients, portions_estimate=portions, confidence=confidence, notes=notes)

@app.get("/product/{gtin}")
def product_lookup(gtin: str):
    """
    Returns product data for given GTIN (mock DB)
    """
    with Session(engine) as s:
        q = s.exec(select(Product).where(Product.gtin == gtin)).first()
        if not q:
            raise HTTPException(status_code=404, detail="Product not found in mock DB")
        return {
            "gtin": q.gtin,
            "name": q.name,
            "brand": q.brand,
            "calories_per_100g": q.calories_per_100g,
            "nutrients": q.nutrients_json,
            "last_updated": q.last_updated.isoformat() if q.last_updated else None
        }

@app.get("/trends", response_model=List[TrendItem])
def get_trends():
    """
    Mock trends feed: later replace with trend detection (TikTok/IG scraping + verification)
    """
    items = [
        TrendItem(id="t1", title="Avocado Smash", summary="High engagement recipe. Try a lighter oil.", health_flag="ok"),
        TrendItem(id="t2", title="Extreme Juice Cleanse", summary="Short-term weight loss claims — lacks evidence.", health_flag="watch"),
    ]
    return items

@app.post("/community/post")
def create_post(content: dict):
    """
    Placeholder: receive community post, run light moderation (mock).
    """
    text = content.get("text","")
    if "kill" in text.lower() or "suicide" in text.lower():
        return JSONResponse(status_code=400, content={"detail":"Disallowed content"})
    # In prod: run moderation model & persist
    return {"status":"ok", "id": uuid.uuid4().hex, "text": text}

@app.get("/health")
def health():
    return {"status":"ok", "uptime": datetime.utcnow().isoformat()}

# ---- Static file serving for demo UI (optional) ----
@app.get("/")
def index():
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path, media_type="text/html")
    return {"info": "Start backend and open frontend/index.html in your browser."}

# ---- Run (only if invoked directly) ----
if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
