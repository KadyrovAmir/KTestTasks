from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from schemas import Data

router = APIRouter()
db = {}
transactions = []


@router.get("/select/")
async def get_data() -> list[Data]:
    return [
        Data(id=key, value=value)
        for key, value in db.items()
    ]


@router.post("/insert/")
async def insert_data(value: Annotated[str, Body(embed=True)]) -> None:
    new_id = max(db) + 1 if db else 1
    db[new_id] = value


@router.delete("/delete/{item_id}")
async def delete_data(item_id: int) -> None:
    db.pop(item_id, None)


@router.post("/begin")
async def begin_transaction() -> None:
    transactions.append(db.copy())


@router.post("/commit")
async def commit_transaction() -> None:
    if not transactions:
        raise HTTPException(status_code=404)

    transactions.pop()


@router.post("/rollback")
async def rollback_transaction() -> None:
    global db
    if not transactions:
        raise HTTPException(status_code=404)

    db = transactions.pop()
