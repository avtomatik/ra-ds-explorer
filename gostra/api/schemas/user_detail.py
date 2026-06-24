from pydantic import Field

from gostra.api.schemas.user_list import User


class UserDetail(User):
    creator_id: str = Field(validation_alias="creatorId")
    creator_name: str = Field(validation_alias="creatorName")
    creator_login: str = Field(validation_alias="creatorLogin")

    distinguished_name: str = Field(validation_alias="distinguishedName")
    folder: str
