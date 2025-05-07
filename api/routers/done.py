from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.done as done_crud
import api.cruds.task as task_crud
from api.supabase_client import get_supabase_client
from supabase import Client

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    supabase_client: Client = Depends(get_supabase_client),
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task.done:
        raise HTTPException(status_code=400, detail="Done already exists")

    return await done_crud.create_done(db, task_id)


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done not found")

    return await done_crud.delete_done(db, original=done)
