from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: Optional[str]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "クリーニングをとりに行く",
            },
            "default": {
                "title": None,
            },
        }
    )


class TaskCreateRequest(TaskBase):
    pass


class TaskCreateResponse(TaskCreateRequest):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class Task(TaskBase):
    id: int
    done: bool

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "description": {
                "done": "完了フラグ",
            },
            "example": {
                "done": False,
            },
        },
    )
