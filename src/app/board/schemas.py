from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: Optional[str] = None
    id: int = None


class Subcategory(CategoryBase):
    parent_id: int = None

