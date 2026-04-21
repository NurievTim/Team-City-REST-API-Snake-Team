from pydantic import BaseModel, ConfigDict, Optional, HttpUrl, Field

class TeamCityHeaders(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    location: Optional[HttpUrl] = Field(None, alias="Location")
    next_href: Optional[HttpUrl] = Field(None, alias="Next-Href")
    prev_href: Optional[HttpUrl] = Field(None, alias="Prev-Href")
    total_count: Optional[int] = Field(None, alias="X-Total-Count")