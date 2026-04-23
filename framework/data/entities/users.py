from __future__ import annotations

from dataclasses import dataclass


@dataclass()
class TestUser:
    """
    Учётные данные и роль тестового пользователя TeamCity.

    Для REST: локатор пользователя чаще всего ``username:<login>``;
    назначение роли делается отдельно (``add_role_to_user``) с ``role_scope``
    (например ``_Root`` для сервера или ``p:<projectExternalId>`` для проектных ролей).
    """
    username: str
    password: str
    role_id: str
    role_scope: str
    token: str

    @property
    def locator(self) -> str:
        return f'username:{self.username}'

    def auth_headers(self, bearer_token: str) -> dict[str, str]:
        """Заголовки REST с personal access token (значение без префикса Bearer в аргументе)."""
        token = bearer_token.removeprefix('Bearer ').strip()
        return {'Authorization': f'Bearer {token}'}


# Предопределённые пользователи (создание в инстансе и выдача PAT — отдельный шаг в тестах/фикстурах)
SYSTEM_ADMIN = TestUser(
    username='Admin',
    password='Admin123',
    role_id='SYSTEM_ADMIN',
    role_scope='_Root',
    token=''

)

PROJECT_ADMIN = TestUser(
    username='proj_admin',
    password='proj_admin123',
    role_id='PROJECT_ADMIN',
    role_scope='_Root',
    token=''
)

PROJECT_DEVELOPER = TestUser(
    username='proj_developer',
    password='developer123',
    role_id='PROJECT_DEVELOPER',
    role_scope='p:<projectExternalId>',
    token=''
)

VIEWER = TestUser(
    username='proj_viewer',
    password='viewer123',
    role_id='PROJECT_VIEWER',
    role_scope='p:<projectExternalId>',
    token=''
)
