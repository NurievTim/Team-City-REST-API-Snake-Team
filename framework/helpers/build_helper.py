import time

import pytest


def wait_for_build_state(
    client,
    headers: dict,
    build_id: int | str,
    target_state: str,
    timeout: float = 5,
    poll_interval: float = 0.3,
) -> dict:
    """
    Опрашивает `GET /app/rest/builds/id:{build_id}` до тех пор, пока поле `state`
    в теле ответа не станет равным `target_state`, либо пока не истечёт `timeout`.

    :param client: HTTP-клиент TeamCity (ожидается метод `get_build`).
    :param headers: Заголовки для авторизованного запроса (как в фикстурах `admin_headers` / read).
    :param build_id: Числовой id билда из ответа `buildQueue` или `builds`.
    :param target_state: Ожидаемое значение `state` в JSON (например, ``"queued"``, ``"running"``, ``"finished"``).
    :param timeout: Максимальное время ожидания в секундах.
    :param poll_interval: Интервал между опросами в секундах.
    """
    deadline = time.monotonic() + timeout
    last_body: dict | None = None
    while time.monotonic() < deadline:
        resp = client.get_build(
            build_locator=f"id:{build_id}",
            headers=headers,
            check_status=None,
        )
        if resp.status_code == 200:
            last_body = resp.json()
            if last_body.get("state") == target_state:
                return last_body
        time.sleep(poll_interval)
    pytest.fail(
        f"Build id:{build_id} не перешёл в state={target_state!r} за {timeout}s "
        f"(последний ответ: {last_body})"
    )