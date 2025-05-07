from typing import Optional

from supabase import Client


async def get_done(supabase_client: Client, task_id: int) -> Optional[bool]:
    result = supabase_client.table("task").select("*").eq("id", task_id).execute()
    if result.data:
        task = result.data[0]
        return task["done"]
    return None


async def create_done(supabase_client: Client, task_id: int) -> None:
    supabase_client.table("task").update({"done": True}).eq("id", task_id).execute()


async def delete_done(supabase_client: Client, task_id: int) -> None:
    supabase_client.table("task").update({"done": False}).eq("id", task_id).execute()
