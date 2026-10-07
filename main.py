from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Model Data Mahasiswa
class Item(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None


# Simulasi Database
items_db = {}


# ROOT
# @app.get("/")
# async def read_root():
#    return {
#       "message": "API Mahasiswa berhasil dijalankan"
#    }


# CREATE (POST)
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):

    if item_id in items_db:
        return {
            "error": "Data mahasiswa sudah ada"
        }

    items_db[item_id] = item.model_dump()

    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "item": items_db[item_id]
    }


# READ (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):

    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    return {
        "item_id": item_id,
        "item": items_db[item_id]
    }


# UPDATE (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):

    if item_id not in items_db:
        return {
            "error": "Data mahasiswa tidak ditemukan"
        }

    items_db[item_id] = item.model_dump()

    return {
        "message": "Data mahasiswa berhasil diperbarui",
        "item": items_db[item_id]
    }


# DELETE (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):

    if item_id not in items_db:
        return {
            "error": "Data mahasiswa tidak ditemukan"
        }

    deleted_item = items_db.pop(item_id)

    return {
        "message": "Data mahasiswa berhasil dihapus",
        "deleted_item": deleted_item
    }