from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Dict, Any

class QueryParams(BaseModel):
    """
    Общая модель для query-параметров TeamCity API.
    Позволяет передавать произвольные locator-строки или использовать типизированные поля.
    """
    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    locator: Optional[str] = Field(None, description="Строка локатора (например, 'count:10,start:0')")
    fields: Optional[str] = Field(None, description="Список полей через запятую")
    count: Optional[int] = Field(None, description="Количество элементов на странице")
    start: Optional[int] = Field(None, description="Смещение для пагинации")
    # дополнительные поля, специфичные для эндпоинта, можно добавить через наследование