# TeamCity REST API — Детализированные тест-кейсы

> Формат каждого тест-кейса: **Arrange → Act → Assert**
> Глобальные предусловия: сервер запущен, в системе есть агент (authorized=true, enabled=true, connected=true)
> Уточнение: endpoint'ы и шаги сверены с текущим `framework/clients/team_city_api_client.py`.

---

## Глобальные фикстуры (session scope, conftest.py)

```
TC_URL          = http://localhost:8111
ADMIN_TOKEN     = <токен системного администратора>
PROJ_ADMIN_TOKEN= <токен project admin>
DEV_TOKEN       = <токен developer>
VIEWER_TOKEN    = <токен viewer>

Проект: "TestProject" (id=TestProject)
Build Config: "HelloWorld" (id=TestProject_HelloWorld)
VCS Root: "TestRepo" (id=TestRepo) — git, ветка main
Пользователи: admin / proj_admin / developer / viewer
```

---

## SMOKE SUITE (7 тестов, P0)

---

### № 1 — Сервер доступен и отвечает

| Поле | Значение |
|---|---|
| **ID** | № 1 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/server` |

**Предусловия:**
- Docker-контейнер `teamcity-server` запущен и прошёл healthcheck
- Переменная `TC_URL` задана

**Шаги (AAA):**
```
Arrange: нет дополнительных данных
Act:     GET {TC_URL}/app/rest/server
         Header: Authorization: Bearer {ADMIN_TOKEN}
         Header: Accept: application/json
Assert:  HTTP 200
         body.version != null
         body.startTime != null
```

**Ожидаемый результат:** HTTP 200, поле `version` содержит строку вида "2025.11.x"

**Постусловия:** нет

---

### № 2 — Авторизация по Bearer-токену работает

| Поле | Значение |
|---|---|
| **ID** | № 2 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/users/current` |

**Предусловия:**
- Пользователь `admin` существует, токен `ADMIN_TOKEN` сгенерирован

**Шаги (AAA):**
```
Arrange: используем ADMIN_TOKEN
Act:     GET {TC_URL}/app/rest/users/current
         Header: Authorization: Bearer {ADMIN_TOKEN}
Assert:  HTTP 200
         body.username == "admin"
```

**Ожидаемый результат:** HTTP 200, поле `username` совпадает с именем пользователя, чей токен использован

**Постусловия:** нет

---

### № 3 — Запрос без токена возвращает 401

| Поле | Значение |
|---|---|
| **ID** | № 3 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/projects` |

**Предусловия:**
- Гостевой доступ **выключен** (настройка по умолчанию)

**Шаги (AAA):**
```
Arrange: нет токена
Act:     GET {TC_URL}/app/rest/projects
         (без заголовка Authorization)
Assert:  HTTP 401
```

**Ожидаемый результат:** HTTP 401 Unauthorized

**Постусловия:** нет

---

### № 4 — Запуск билда в очередь

| Поле | Значение |
|---|---|
| **ID** | № 4 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/buildQueue` |

**Предусловия:**
- Проект `TestProject` существует
- Build configuration `TestProject_HelloWorld` существует
- Агент авторизован и подключён

**Шаги (AAA):**
```
Arrange:
  payload = {
    "buildType": { "id": "TestProject_HelloWorld" }
  }

Act:
  POST {TC_URL}/app/rest/buildQueue
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: application/json
  Body: payload

Assert:
  HTTP 200
  body.state in ["queued", "running"]
  body.buildType.id == "TestProject_HelloWorld"

Cleanup:
  Если state == "queued": POST /app/rest/buildQueue/{id} с cancelRequest
  Если state == "running": POST /app/rest/builds/{id} с cancelRequest
```

**Ожидаемый результат:** Билд добавлен в очередь, `state == "queued"` или уже `running`

**Постусловия:** отменить билд (cleanup fixture)

---

### № 5 — Получение деталей запущенного/завершённого билда

| Поле | Значение |
|---|---|
| **ID** | № 5 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}` |

**Предусловия:**
- Создан и завершён хотя бы один билд (используем билд из № 4 или отдельный setup)
- `BUILD_ID` сохранён

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого тестового билда>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.id == build_id
  body.state in ["running", "finished"]
  body.buildType.id == "TestProject_HelloWorld"
```

**Ожидаемый результат:** HTTP 200, структура билда корректна

**Постусловия:** нет

---

### № 6 — Список проектов возвращает минимум 1 проект

| Поле | Значение |
|---|---|
| **ID** | № 6 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/projects` |

**Предусловия:**
- Проект `TestProject` создан

**Шаги (AAA):**
```
Arrange: нет дополнительных данных
Act:
  GET {TC_URL}/app/rest/projects
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count >= 1
  body.project — список, не пустой
```

**Ожидаемый результат:** HTTP 200, как минимум один проект в списке

**Постусловия:** нет

---

### № 7 — Список авторизованных агентов

| Поле | Значение |
|---|---|
| **ID** | № 7 |
| **Уровень** | Smoke |
| **Приоритет** | P0 |
| **Endpoint** | `GET /app/rest/agents` |

**Предусловия:**
- Контейнер `teamcity-agent` запущен и зарегистрирован на сервере
- Агент авторизован вручную или через API в setup

**Шаги (AAA):**
```
Arrange: нет дополнительных данных
Act:
  GET {TC_URL}/app/rest/agents?locator=authorized:true
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count >= 1
  body.agent[0].authorized == true
```

**Ожидаемый результат:** HTTP 200, минимум один авторизованный агент

**Постусловия:** нет

---

## BUILDS (12 тестов)

---

### № 8 — Отмена билда в очереди (queued)

| Поле | Значение |
|---|---|
| **ID** | № 8 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/buildQueue/{queuedBuildLocator}` |

**Предусловия:**
- Создан билд в очереди, сохранён его `id`
- Агент **недоступен** или очередь ещё не обработана (чтобы билд оставался в queued)

**Шаги (AAA):**
```
Arrange:
  # Создаём билд в очереди
  build_id = POST /app/rest/buildQueue {buildType.id: "TestProject_HelloWorld"} → body.id

  payload = {
    "comment": "Cancelled by test #8",
    "readdIntoQueue": false
  }

Act:
  POST {TC_URL}/app/rest/buildQueue/id:{build_id}
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: application/json
  Body: payload

Assert:
  HTTP 200
  body.state == "queued" (state не сменился немедленно, но cancelRequest принят)

  # Дополнительная проверка через GET:
  GET /app/rest/builds/id:{build_id}
  body.state == "finished"
  body.status == "UNKNOWN"   # отменённый билд
  body.canceledInfo != null
```

**Ожидаемый результат:** Билд отменён, `state=finished`, `canceledInfo` присутствует

**Постусловия:** нет (билд уже отменён)

---

### № 9 — Отмена запущенного билда (running)

| Поле | Значение |
|---|---|
| **ID** | № 9 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/builds/{buildLocator}` |

**Предусловия:**
- Билд запущен и находится в состоянии `running`
- Используем build config со sleep-командой чтобы агент не завершил его мгновенно

**Шаги (AAA):**
```
Arrange:
  # Запускаем билд
  build_id = POST /app/rest/buildQueue {buildType.id: "TestProject_LongRunning"} → body.id
  # Ждём state == "running" (polling)
  wait_for_state(build_id, "running", timeout=60s)

  payload = {
    "comment": "Cancelled by test TC-010b",
    "readdIntoQueue": false
  }

Act:
  POST {TC_URL}/app/rest/builds/id:{build_id}
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  # Ждём финального состояния
  wait_for_state(build_id, "finished", timeout=30s)
  GET /app/rest/builds/id:{build_id} → body.canceledInfo != null
```

**Ожидаемый результат:** Running-билд отменён корректно

**Постусловия:** нет

---

### № 10 — Запуск custom build (параметры, ветка, агент)

| Поле | Значение |
|---|---|
| **ID** | № 10 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/buildQueue` |

**Предусловия:**
- Проект и build config существуют
- Параметр `myParam` задан в build config (или будет создан как новый)
- Известен id агента (получить заранее через GET /app/rest/agents)
- Ветка `main` существует в VCS

**Шаги (AAA):**
```
Arrange:
  agent_id = GET /app/rest/agents?locator=authorized:true → body.agent[0].id

  payload = {
    "buildType": { "id": "TestProject_HelloWorld" },
    "branchName": "main",
    "personal": false,
    "comment": { "text": "TC-011 custom build" },
    "agent": { "id": agent_id },
    "properties": {
      "property": [
        { "name": "system.myParam", "value": "test_value_011" }
      ]
    }
  }

Act:
  POST {TC_URL}/app/rest/buildQueue
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: application/json
  Body: payload

Assert:
  HTTP 200
  body.buildType.id == "TestProject_HelloWorld"
  body.branchName == "main"
  body.agent.id == agent_id

Cleanup:
  Отменить или дождаться завершения билда
```

**Ожидаемый результат:** Билд запущен с указанными параметрами

**Постусловия:** отменить билд

---

### № 11 — Скачивание артефакта сборки

| Поле | Значение |
|---|---|
| **ID** | № 11 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}/artifacts/files{path}` |

**Предусловия:**
- Завершённый успешный билд с артефактами
- Артефакт `hello.txt` опубликован в build config через artifact path
- `BUILD_ID` известен

**Шаги (AAA):**
```
Arrange:
  build_id = <id успешно завершённого билда с артефактами>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}/artifacts/files/hello.txt
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Content-Type: text/plain (или application/octet-stream)
  Body не пустой
```

**Ожидаемый результат:** Содержимое файла артефакта возвращено

**Постусловия:** нет

---

### № 12 — Статистика билда

| Поле | Значение |
|---|---|
| **ID** | № 12 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}/statistics` |

**Предусловия:**
- Завершённый билд с `BUILD_ID`

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого билда>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}/statistics/
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.property — непустой список
  Среди свойств присутствует "BuildDuration" или "SuccessRate"
```

**Ожидаемый результат:** HTTP 200, список статистических значений

**Постусловия:** нет

---

### № 13 — Фильтрация билдов по статусу и ветке

| Поле | Значение |
|---|---|
| **ID** | № 13 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds` |

**Предусловия:**
- Есть хотя бы один failed-билд в ветке `main`
- Если нет — специально завалить билд в setup (скрипт с exit code 1)

**Шаги (AAA):**
```
Arrange:
  # Убеждаемся что есть хотя бы один FAILURE билд
  # branch:(default:any) обязателен для поиска по всем веткам

Act:
  GET {TC_URL}/app/rest/builds?locator=buildType:(id:TestProject_HelloWorld),
      status:FAILURE,branch:(default:any),count:10
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Если count > 0: все body.build[i].status == "FAILURE"
  body.count <= 10
```

**Ожидаемый результат:** Список содержит только FAILURE-билды, пагинация работает

**Постусловия:** нет

---

### № 14 — Пагинация билдов (страница 1)

| Поле | Значение |
|---|---|
| **ID** | № 14 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds` |

**Предусловия:**
- Существует минимум 6 завершённых билдов

**Шаги (AAA):**
```
Arrange: нет
Act:
  GET {TC_URL}/app/rest/builds?locator=buildType:(id:TestProject_HelloWorld),
      defaultFilter:false,count:5,start:0
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count == 5
  body.build — список из 5 элементов
  body.nextHref != null (если больше 5 билдов)
```

**Ожидаемый результат:** Возвращается ровно 5 билдов, `nextHref` указывает на следующую страницу

**Постусловия:** нет

---

### № 15 — Пагинация билдов (страница 2)

| Поле | Значение |
|---|---|
| **ID** | № 15 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds` |

**Предусловия:**
- Минимум 6 завершённых билдов (те же что в № 14)

**Шаги (AAA):**
```
Arrange: нет
Act:
  GET {TC_URL}/app/rest/builds?locator=buildType:(id:TestProject_HelloWorld),
      defaultFilter:false,count:5,start:5
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.build — список с элементами, не совпадающими с № 14
  Проверяем id: set(page1_ids) ∩ set(page2_ids) == ∅
```

**Ожидаемый результат:** Страница 2 не пересекается со страницей 1

**Постусловия:** нет

---

### № 16 — Получение изменений (changes) для билда

| Поле | Значение |
|---|---|
| **ID** | № 16 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/changes` |

**Предусловия:**
- Завершённый билд с известным `BUILD_ID`
- Билд запускался на реальном VCS (должны быть изменения) или проверяем, что endpoint отвечает корректно при пустом списке

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого билда>

Act:
  GET {TC_URL}/app/rest/changes?locator=build:(id:{build_id})
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body присутствует, count >= 0
  Если count > 0: body.change[0].version != null
```

**Ожидаемый результат:** HTTP 200, список изменений (может быть пустым для первого билда)

**Постусловия:** нет

---

### № 17 — Snapshot-зависимости между билдами

| Поле | Значение |
|---|---|
| **ID** | № 17 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds?locator=snapshotDependency:(to:(id:X))` |

**Предусловия:**
- Build chain: ConfigA → ConfigB (ConfigB зависит от ConfigA через snapshot dependency)
- Оба билда завершены
- `BUILD_A_ID`, `BUILD_B_ID` известны

**Шаги (AAA):**
```
Arrange:
  build_b_id = <id билда ConfigB>

Act:
  # Получаем все билды, от которых зависит BUILD_B
  GET {TC_URL}/app/rest/builds?locator=snapshotDependency:(to:(id:{build_b_id}),
      includeInitial:true),defaultFilter:false
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  В списке присутствует build_a_id
  В списке присутствует build_b_id (includeInitial:true)
```

**Ожидаемый результат:** Зависимые билды корректно возвращены

**Постусловия:** нет

---

### № 18 — Resulting properties завершённого билда

| Поле | Значение |
|---|---|
| **ID** | № 18 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}/resulting-properties` |

**Предусловия:**
- Завершённый билд с `BUILD_ID`

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого билда>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}/resulting-properties
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.property — непустой список
  Присутствует хотя бы одно системное свойство (teamcity.build.id и т.п.)
```

**Ожидаемый результат:** Список resolved-параметров билда

**Постусловия:** нет

---

### № 19 — Запуск билда для конкретной ревизии

| Поле | Значение |
|---|---|
| **ID** | № 19 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/buildQueue` |

**Предусловия:**
- VCS Root `TestRepo` подключён к `TestProject_HelloWorld`
- Известен SHA-хэш коммита и id VCS root instance

**Шаги (AAA):**
```
Arrange:
  # Получить последний коммит из VCS root instance
  vcs_instance_id = GET /app/rest/vcs-root-instances?locator=vcsRoot:(id:TestRepo) → body.vcsRootInstance[0].id
  commit_sha = <известный SHA из git-истории>

  payload = {
    "buildType": { "id": "TestProject_HelloWorld" },
    "branchName": "main",
    "revisions": {
      "revision": [
        {
          "version": commit_sha,
          "vcsBranchName": "refs/heads/main",
          "vcs-root-instance": { "vcs-root-id": "TestRepo" }
        }
      ]
    }
  }

Act:
  POST {TC_URL}/app/rest/buildQueue
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.revisions.revision[0].version == commit_sha

Cleanup:
  Отменить билд
```

**Ожидаемый результат:** Билд запущен на указанной ревизии

**Постусловия:** отменить билд

---

## PROJECTS & BUILD CONFIGURATIONS (10 тестов)

---

### № 20 — Создание проекта

| Поле | Значение |
|---|---|
| **ID** | № 20 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/projects` |

**Предусловия:**
- Нет проекта с id `AutoTest_TC020`

**Шаги (AAA):**
```
Arrange:
  payload = {
    "parentProject": { "locator": "id:_Root" },
    "name": "AutoTest TC020",
    "id": "AutoTest_TC020",
    "copyAllAssociatedSettings": false
  }

Act:
  POST {TC_URL}/app/rest/projects
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.id == "AutoTest_TC020"
  body.name == "AutoTest TC020"
  body.parentProjectId == "_Root"

Cleanup:
  DELETE /app/rest/projects/id:AutoTest_TC020
```

**Ожидаемый результат:** Проект создан с корректными атрибутами

**Постусловия:** удалить проект `AutoTest_TC020`

---

### № 21 — Удаление проекта

| Поле | Значение |
|---|---|
| **ID** | № 21 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `DELETE /app/rest/projects/{projectLocator}` |

**Предусловия:**
- Существует проект `AutoTest_TC021` (создать в setup)

**Шаги (AAA):**
```
Arrange:
  # Создаём проект
  POST /app/rest/projects {id: "AutoTest_TC021", name: "AutoTest TC021", parentProject: {locator: "id:_Root"}}

Act:
  DELETE {TC_URL}/app/rest/projects/id:AutoTest_TC021
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 204 (No Content)

  # Проверяем что проект больше не существует
  GET /app/rest/projects/id:AutoTest_TC021 → HTTP 404
```

**Ожидаемый результат:** Проект удалён, повторный GET возвращает 404

**Постусловия:** нет (проект удалён в шаге Act)

---

### № 22 — Создание build configuration

| Поле | Значение |
|---|---|
| **ID** | № 22 |
| **Уровень** | Integration |
| **Приоритет** | P0 |
| **Endpoint** | `POST /app/rest/buildTypes` |

**Предусловия:**
- Проект `TestProject` существует

**Шаги (AAA):**
```
Arrange:
  payload = {
    "id": "TestProject_TC022Config",
    "name": "TC022 Config",
    "project": { "id": "TestProject" },
    "steps": {
      "step": [
        {
          "name": "echo step",
          "type": "simpleRunner",
          "properties": {
            "property": [
              { "name": "script.content", "value": "echo 'Hello TC022'" }
            ]
          }
        }
      ]
    }
  }

Act:
  POST {TC_URL}/app/rest/buildTypes
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.id == "TestProject_TC022Config"
  body.project.id == "TestProject"

Cleanup:
  DELETE /app/rest/buildTypes/id:TestProject_TC022Config
```

**Ожидаемый результат:** Build configuration создана

**Постусловия:** удалить build config

---

### № 23 — Копирование build configuration

| Поле | Значение |
|---|---|
| **ID** | № 23 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/projects/{projectLocator}/buildTypes` |

**Предусловия:**
- Существует `TestProject_HelloWorld`

**Шаги (AAA):**
```
Arrange:
  payload = {
    "sourceBuildTypeLocator": "id:TestProject_HelloWorld",
    "name": "HelloWorld Copy TC023",
    "id": "TestProject_HelloWorldCopyTC023",
    "copyAllAssociatedSettings": true
  }

Act:
  POST {TC_URL}/app/rest/projects/id:TestProject/buildTypes
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.id == "TestProject_HelloWorldCopyTC023"
  body.project.id == "TestProject"

Cleanup:
  DELETE /app/rest/buildTypes/id:TestProject_HelloWorldCopyTC023
```

**Ожидаемый результат:** Копия создана в том же проекте

**Постусловия:** удалить копию

---

### № 24 — Приостановка build configuration (paused)

| Поле | Значение |
|---|---|
| **ID** | № 24 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/buildTypes/{buildTypeLocator}/paused` |

**Предусловия:**
- Существует `TestProject_HelloWorld`, она **не** в paused-состоянии

**Шаги (AAA):**
```
Arrange:
  # Убеждаемся что конфиг не на паузе
  GET /app/rest/buildTypes/id:TestProject_HelloWorld/paused → "false"

Act:
  PUT {TC_URL}/app/rest/buildTypes/id:TestProject_HelloWorld/paused
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: text/plain
  Body: "true"

Assert:
  HTTP 200

  # Проверяем статус
  GET /app/rest/buildTypes/id:TestProject_HelloWorld/paused → body == "true"

Cleanup:
  PUT /app/rest/buildTypes/id:TestProject_HelloWorld/paused → Body: "false"
```

**Ожидаемый результат:** Build config приостановлена

**Постусловия:** снять паузу

---

### № 25 — Изменение параметра build configuration

| Поле | Значение |
|---|---|
| **ID** | № 25 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/buildTypes/{buildTypeLocator}/parameters/{name}` |

**Предусловия:**
- `TestProject_HelloWorld` существует
- Параметр `myTestParam` существует (создать в setup если нет)

**Шаги (AAA):**
```
Arrange:
  # Создаём параметр если не существует
  POST /app/rest/buildTypes/id:TestProject_HelloWorld/parameters
  Body: { "name": "myTestParam", "value": "old_value" }

Act:
  PUT {TC_URL}/app/rest/buildTypes/id:TestProject_HelloWorld/parameters/myTestParam
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: text/plain
  Body: "new_value_025"

Assert:
  HTTP 200

  GET /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/myTestParam
  body.value == "new_value_025"

Cleanup:
  DELETE /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/myTestParam
```

**Ожидаемый результат:** Значение параметра обновлено

**Постусловия:** удалить параметр

---

### № 26 — Создание VCS Root

| Поле | Значение |
|---|---|
| **ID** | № 26 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/vcs-roots` |

**Предусловия:**
- Проект `TestProject` существует
- Нет VCS Root с id `TestProject_TC026Root`

**Шаги (AAA):**
```
Arrange:
  payload = {
    "id": "TestProject_TC026Root",
    "name": "TC026 Test Root",
    "vcsName": "jetbrains.git",
    "project": { "id": "TestProject" },
    "properties": {
      "property": [
        { "name": "authMethod", "value": "ANONYMOUS" },
        { "name": "branch",     "value": "refs/heads/main" },
        { "name": "url",        "value": "https://github.com/JetBrains/teamcity-rest.git" }
      ]
    }
  }

Act:
  POST {TC_URL}/app/rest/vcs-roots
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.id == "TestProject_TC026Root"
  body.vcsName == "jetbrains.git"

Cleanup:
  DELETE /app/rest/vcs-roots/id:TestProject_TC026Root
```

**Ожидаемый результат:** VCS Root создан

**Постусловия:** удалить VCS Root

---

### № 27 — Архивация проекта

| Поле | Значение |
|---|---|
| **ID** | № 27 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/projects/{projectLocator}/archived` |

**Предусловия:**
- Существует проект `AutoTest_TC027` (создать в setup)

**Шаги (AAA):**
```
Arrange:
  POST /app/rest/projects {id:"AutoTest_TC027", name:"AutoTest TC027", parentProject:{locator:"id:_Root"}}

Act:
  PUT {TC_URL}/app/rest/projects/id:AutoTest_TC027/archived
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Header: Content-Type: text/plain
  Body: "true"

Assert:
  HTTP 200
  GET /app/rest/projects/id:AutoTest_TC027 → body.archived == true

Cleanup:
  PUT /app/rest/projects/id:AutoTest_TC027/archived → "false"
  DELETE /app/rest/projects/id:AutoTest_TC027
```

**Ожидаемый результат:** Проект заархивирован

**Постусловия:** разархивировать и удалить проект

---

### № 28 — Перемещение build configuration в другой проект

| Поле | Значение |
|---|---|
| **ID** | № 28 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/buildTypes/{buildTypeLocator}/move` |

**Предусловия:**
- Существует `TestProject_TC028Config` (создать в setup)
- Существует целевой проект `AutoTest_TC028Target`

**Шаги (AAA):**
```
Arrange:
  # Создаём исходный проект и конфиг
  POST /app/rest/projects {id:"AutoTest_TC028Src", name:"TC028 Src"}
  POST /app/rest/buildTypes {id:"AutoTest_TC028Src_Config", name:"Config028", project:{id:"AutoTest_TC028Src"}}

  # Создаём целевой проект
  POST /app/rest/projects {id:"AutoTest_TC028Target", name:"TC028 Target"}

Act:
  POST {TC_URL}/app/rest/buildTypes/id:AutoTest_TC028Src_Config/move?targetProjectId=AutoTest_TC028Target
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  # Проверяем что конфиг теперь принадлежит целевому проекту
  GET /app/rest/buildTypes/id:AutoTest_TC028Src_Config → body.project.id == "AutoTest_TC028Target"

Cleanup:
  DELETE /app/rest/buildTypes/id:AutoTest_TC028Src_Config
  DELETE /app/rest/projects/id:AutoTest_TC028Target
  DELETE /app/rest/projects/id:AutoTest_TC028Src
```

**Ожидаемый результат:** Build config перемещена в целевой проект

**Постусловия:** удалить созданные ресурсы

---

### № 29 — Рекурсивный поиск build configs через affectedProject

| Поле | Значение |
|---|---|
| **ID** | № 29 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/buildTypes?locator=affectedProject:{id}` |

**Предусловия:**
- Проект `TestProject` содержит подпроекты с build configs
- `TestProject_Sub` — подпроект, содержит `TestProject_Sub_Config`

**Шаги (AAA):**
```
Arrange:
  # Создаём подпроект и конфиг в нём
  POST /app/rest/projects {id:"TestProject_Sub029", name:"Sub029", parentProject:{locator:"id:TestProject"}}
  POST /app/rest/buildTypes {id:"TestProject_Sub029_Config", name:"SubConfig", project:{id:"TestProject_Sub029"}}

Act:
  GET {TC_URL}/app/rest/buildTypes?locator=affectedProject:(id:TestProject)
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  В списке присутствует "TestProject_Sub029_Config"
  В списке присутствует "TestProject_HelloWorld"

Cleanup:
  DELETE /app/rest/buildTypes/id:TestProject_Sub029_Config
  DELETE /app/rest/projects/id:TestProject_Sub029
```

**Ожидаемый результат:** Рекурсивный поиск возвращает конфиги из подпроектов

**Постусловия:** удалить подпроект и конфиг

---

## AGENTS & USERS (12 тестов)

---

### № 30 — Фильтрация агентов (connected + authorized)

| Поле | Значение |
|---|---|
| **ID** | № 30 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/agents` |

**Предусловия:**
- Минимум один агент connected=true и authorized=true

**Шаги (AAA):**
```
Arrange: нет
Act:
  GET {TC_URL}/app/rest/agents?locator=connected:true,authorized:true
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count >= 1
  Все body.agent[i].connected == true
  Все body.agent[i].authorized == true
```

**Ожидаемый результат:** Список только connected+authorized агентов

**Постусловия:** нет

---

### № 31 — Отключение агента с комментарием

| Поле | Значение |
|---|---|
| **ID** | № 31 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/agents/{agentLocator}/enabledInfo` |

**Предусловия:**
- Агент с `AGENT_ID` авторизован и включён (enabled=true)

**Шаги (AAA):**
```
Arrange:
  agent_id = GET /app/rest/agents?locator=authorized:true → body.agent[0].id

  payload = {
    "status": false,
    "comment": { "text": "Disabled by TC-031 test" }
  }

Act:
  PUT {TC_URL}/app/rest/agents/id:{agent_id}/enabledInfo
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  GET /app/rest/agents/id:{agent_id} → body.enabled == false

Cleanup:
  PUT /app/rest/agents/id:{agent_id}/enabledInfo → { "status": true }
```

**Ожидаемый результат:** Агент отключён

**Постусловия:** включить агент обратно

---

### № 32 — Создание пула агентов

| Поле | Значение |
|---|---|
| **ID** | № 32 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/agentPools` |

**Предусловия:**
- Нет пула с именем "TC032 Test Pool"

**Шаги (AAA):**
```
Arrange:
  payload = { "name": "TC032 Test Pool" }

Act:
  POST {TC_URL}/app/rest/agentPools
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.name == "TC032 Test Pool"
  body.id != null

Cleanup:
  DELETE /app/rest/agentPools/id:{pool_id}
```

**Ожидаемый результат:** Пул создан с корректным именем

**Постусловия:** удалить пул

---

### № 33 — Создание пользователя

| Поле | Значение |
|---|---|
| **ID** | № 33 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/users` |

**Предусловия:**
- Нет пользователя с username `tc_test_033`

**Шаги (AAA):**
```
Arrange:
  payload = {
    "username": "tc_test_033",
    "password": "Passw0rd033!",
    "email": "tc033@test.local",
    "name": "Test User 033"
  }

Act:
  POST {TC_URL}/app/rest/users
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.username == "tc_test_033"
  body.email == "tc033@test.local"
  body.id != null

Cleanup:
  DELETE /app/rest/users/id:{user_id}
```

**Ожидаемый результат:** Пользователь создан

**Постусловия:** удалить пользователя

---

### № 34 — Добавление роли пользователю

| Поле | Значение |
|---|---|
| **ID** | № 34 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/users/{userLocator}/roles/{roleId}/{scope}` |

**Предусловия:**
- Существует пользователь `tc_test_034` (создать в setup)
- У пользователя нет роли `PROJECT_VIEWER` в проекте `TestProject`

**Шаги (AAA):**
```
Arrange:
  # Создаём тестового пользователя
  user = POST /app/rest/users {username:"tc_test_034", password:"Passw0rd034!", email:"tc034@test.local"}
  user_id = user.id

Act:
  PUT {TC_URL}/app/rest/users/id:{user_id}/roles/PROJECT_VIEWER/p:TestProject
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  GET /app/rest/users/id:{user_id}/roles → список содержит роль {roleId:"PROJECT_VIEWER", scope:"p:TestProject"}

Cleanup:
  DELETE /app/rest/users/id:{user_id}
```

**Ожидаемый результат:** Роль добавлена с корректным scope

**Постусловия:** удалить пользователя

---

### № 35 — Удаление пользователя

| Поле | Значение |
|---|---|
| **ID** | № 35 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `DELETE /app/rest/users/{userLocator}` |

**Предусловия:**
- Существует пользователь `tc_test_035` (создать в setup)

**Шаги (AAA):**
```
Arrange:
  user = POST /app/rest/users {username:"tc_test_035", password:"Passw0rd035!", email:"tc035@test.local"}
  user_id = user.id

Act:
  DELETE {TC_URL}/app/rest/users/id:{user_id}
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 204

  # Проверяем что пользователь удалён
  GET /app/rest/users/id:{user_id} → HTTP 404
```

**Ожидаемый результат:** Пользователь удалён, повторный GET возвращает 404

**Постусловия:** нет

---

### № 36 — Создание access token для пользователя

| Поле | Значение |
|---|---|
| **ID** | № 36 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/users/{userLocator}/tokens/{tokenName}` |

**Предусловия:**
- Существует пользователь `developer` (из глобальных фикстур)
- Нет токена с именем `tc_036_token`

**Шаги (AAA):**
```
Arrange:
  dev_user_id = GET /app/rest/users/username:developer → body.id

Act:
  POST {TC_URL}/app/rest/users/id:{dev_user_id}/tokens/tc_036_token
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.name == "tc_036_token"
  body.value != null   # сам токен виден только при создании!

Cleanup:
  DELETE /app/rest/users/id:{dev_user_id}/tokens/tc_036_token
```

**Ожидаемый результат:** Токен создан, значение возвращено в ответе

**Постусловия:** удалить токен

---

### № 37 — Список агентов в пуле

| Поле | Значение |
|---|---|
| **ID** | № 37 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/agentPools/{agentPoolLocator}/agents` |

**Предусловия:**
- Существует пул `Default` (всегда есть)
- Хотя бы один агент в пуле

**Шаги (AAA):**
```
Arrange:
  # Получаем id дефолтного пула
  pool_id = GET /app/rest/agentPools?locator=name:Default → body.agentPool[0].id

Act:
  GET {TC_URL}/app/rest/agentPools/id:{pool_id}/agents
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count >= 0   # может быть пустым, но ответ корректный
```

**Ожидаемый результат:** Список агентов пула возвращён

**Постусловия:** нет

---

### № 38 — Авторизация агента

| Поле | Значение |
|---|---|
| **ID** | № 38 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `PUT /app/rest/agents/{agentLocator}/authorizedInfo` |

**Предусловия:**
- Существует неавторизованный агент (зарегистрирован но не authorized)
- В реальных тестах: используем второй агент-контейнер или unauthorized-состояние из setup

**Шаги (AAA):**
```
Arrange:
  # Получаем id неавторизованного агента
  agent_id = GET /app/rest/agents?locator=authorized:false → body.agent[0].id

  payload = {
    "status": true,
    "comment": { "text": "Authorized by TC-038 test" }
  }

Act:
  PUT {TC_URL}/app/rest/agents/id:{agent_id}/authorizedInfo
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  GET /app/rest/agents/id:{agent_id} → body.authorized == true

Cleanup:
  PUT /app/rest/agents/id:{agent_id}/authorizedInfo → { "status": false }
```

**Ожидаемый результат:** Агент авторизован

**Постусловия:** снять авторизацию (если используем реальный агент)

---

### № 39 — Получение текущего пользователя

| Поле | Значение |
|---|---|
| **ID** | № 39 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/users/current` |

**Предусловия:**
- Токены для всех ролей заданы в .env

**Шаги (AAA):**
```
Arrange: используем DEVELOPER_TOKEN

Act:
  GET {TC_URL}/app/rest/users/current
  Header: Authorization: Bearer {DEV_TOKEN}

Assert:
  HTTP 200
  body.username == "developer"
```

**Ожидаемый результат:** Возвращён пользователь, соответствующий токену

**Постусловия:** нет

---

### № 40 — Получение списка групп пользователей

| Поле | Значение |
|---|---|
| **ID** | № 40 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/userGroups` |

**Предусловия:** нет

**Шаги (AAA):**
```
Arrange: нет
Act:
  GET {TC_URL}/app/rest/userGroups
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.group — список
  Присутствует системная группа "ALL_USERS_GROUP"
```

**Ожидаемый результат:** Список групп возвращён

**Постусловия:** нет

---

### № 41 — Удаление access token пользователя

| Поле | Значение |
|---|---|
| **ID** | № 41 |
| **Уровень** | Integration |
| **Приоритет** | P1 |
| **Endpoint** | `DELETE /app/rest/users/{userLocator}/tokens/{tokenName}` |

**Предусловия:**
- Создан токен `tc_039c_token` у пользователя `developer`

**Шаги (AAA):**
```
Arrange:
  dev_id = GET /app/rest/users/username:developer → body.id
  POST /app/rest/users/id:{dev_id}/tokens/tc_039c_token  # создаём токен

Act:
  DELETE {TC_URL}/app/rest/users/id:{dev_id}/tokens/tc_039c_token
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 204
  GET /app/rest/users/id:{dev_id}/tokens → в списке нет "tc_039c_token"
```

**Ожидаемый результат:** Токен удалён

**Постусловия:** нет

---

## E2E ТЕСТЫ (11 тестов)

---

### № 42 — Полный lifecycle проекта

| Поле | Значение |
|---|---|
| **ID** | № 42 |
| **Уровень** | E2E |
| **Приоритет** | P0 |

**Сценарий:** Создание проекта → VCS Root → Build Config → Запуск → Скачивание артефакта → Удаление всего

**Предусловия:**
- Доступен git-репозиторий (публичный)
- Агент запущен

**Шаги (AAA):**
```
Arrange:
  prefix = "E2E_TC040"

Step 1: Создать проект
  POST /app/rest/projects {id:"{prefix}", name:"E2E TC040", parentProject:{locator:"id:_Root"}}

Step 2: Создать VCS Root
  POST /app/rest/vcs-roots {
    id:"{prefix}_Root", name:"E2E Root",
    vcsName:"jetbrains.git",
    project:{id:"{prefix}"},
    properties:[{name:"url", value:"https://github.com/JetBrains/teamcity-rest.git"},
                {name:"branch", value:"refs/heads/main"},
                {name:"authMethod", value:"ANONYMOUS"}]
  }

Step 3: Создать Build Config с артефактом
  POST /app/rest/buildTypes {
    id:"{prefix}_Build", name:"E2E Build",
    project:{id:"{prefix}"},
    steps:[{type:"simpleRunner",
            properties:[{name:"script.content", value:"echo 'artifact' > build_output.txt"}]}],
    settings:[{name:"artifactRules", value:"build_output.txt"}]
  }

Step 4: Привязать VCS Root к конфигу
  POST /app/rest/buildTypes/{prefix}_Build/vcs-root-entries
  { "id":"{prefix}_Root", "vcs-root":{"id":"{prefix}_Root"} }

Step 5: Запустить билд
  build_id = POST /app/rest/buildQueue {buildType:{id:"{prefix}_Build"}} → body.id
  wait_for_state(build_id, "finished", timeout=120s)

Step 6: Проверить успех
  GET /app/rest/builds/id:{build_id} → body.status == "SUCCESS"

Step 7: Скачать артефакт
  GET /app/rest/builds/id:{build_id}/artifacts/files/build_output.txt → HTTP 200

Assert:
  Все шаги выполнены без ошибок
  Артефакт доступен для скачивания

Cleanup:
  DELETE /app/rest/buildTypes/id:{prefix}_Build
  DELETE /app/rest/vcs-roots/id:{prefix}_Root
  DELETE /app/rest/projects/id:{prefix}
```

**Ожидаемый результат:** Полный lifecycle выполнен успешно

---

### № 43 — Build Chain с reuse билда

| Поле | Значение |
|---|---|
| **ID** | № 43 |
| **Уровень** | E2E |
| **Приоритет** | P1 |

**Сценарий:** Создать chain ConfigA→ConfigB, запустить ConfigB с reuse существующего ConfigA

**Предусловия:**
- Существуют конфиги ConfigA и ConfigB со snapshot dependency
- Завершённый успешный билд ConfigA с `CONF_A_BUILD_ID`

**Шаги (AAA):**
```
Arrange:
  conf_a_build_id = <id завершённого успешного билда ConfigA>

  payload = {
    "buildType": { "id": "TestProject_ConfigB" },
    "snapshot-dependencies": {
      "count": 1,
      "build": [{ "id": conf_a_build_id, "buildTypeId": "TestProject_ConfigA" }]
    }
  }

Act:
  build_b_id = POST /app/rest/buildQueue → payload → body.id
  wait_for_state(build_b_id, "finished", timeout=120s)

Assert:
  HTTP 200 на запуске
  GET /app/rest/builds/id:{build_b_id} → body.status == "SUCCESS"
  Билд ConfigA НЕ был перезапущен (проверяем что нет нового билда с startDate > timestamp)
```

**Ожидаемый результат:** ConfigB завершился, reuse ConfigA сработал

**Постусловия:** нет

---

### № 44 — Агент offline → билд ждёт → online → finished

| Поле | Значение |
|---|---|
| **ID** | № 44 |
| **Уровень** | E2E |
| **Приоритет** | P1 |

**Сценарий:** Поставить билд в очередь при отключённом агенте, затем включить агент и дождаться выполнения

**Предусловия:**
- Есть второй агент-контейнер, которым можно управлять (start/stop)

**Шаги (AAA):**
```
Arrange:
  # Отключаем агент через API
  agent_id = GET /app/rest/agents?locator=name:agent2 → body.agent[0].id
  PUT /app/rest/agents/id:{agent_id}/enabledInfo → { "status": false }

Step 1: Запускаем билд
  build_id = POST /app/rest/buildQueue {buildType:{id:"TestProject_HelloWorld"}} → body.id
  # Ждём что билд в queued-состоянии (агент недоступен)
  sleep(5s)
  GET /app/rest/builds/id:{build_id} → body.state == "queued"

Step 2: Включаем агент обратно
  PUT /app/rest/agents/id:{agent_id}/enabledInfo → { "status": true }

Step 3: Ждём завершения
  wait_for_state(build_id, "finished", timeout=120s)

Assert:
  GET /app/rest/builds/id:{build_id} → body.status == "SUCCESS"
```

**Ожидаемый результат:** Билд дождался агента и выполнился

---

### № 45 — Versioned Settings sync

| Поле | Значение |
|---|---|
| **ID** | № 45 |
| **Уровень** | E2E |
| **Приоритет** | P1 |
| **Endpoint** | `POST /app/rest/projects/{locator}/versionedSettings/checkForChanges` |

**Предусловия:**
- Проект с включёнными версионными настройками
- VCS Root с `.teamcity` директорией

**Шаги (AAA):**
```
Arrange:
  project_id = "TestProjectVersioned"

Act:
  POST {TC_URL}/app/rest/projects/id:{project_id}/versionedSettings/checkForChanges
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200 или 202

  # Проверяем статус синхронизации
  GET /app/rest/projects/id:{project_id}/versionedSettings/status → body не пустой
```

**Ожидаемый результат:** Проверка изменений инициирована

---

### № 46 — Assign и удаление Investigation

| Поле | Значение |
|---|---|
| **ID** | № 46 |
| **Уровень** | E2E |
| **Приоритет** | P1 |

**Предусловия:**
- Существует FAILURE-билд, породивший build problem
- Пользователь `developer` существует

**Шаги (AAA):**
```
Arrange:
  payload = {
    "scope": { "buildType": { "id": "TestProject_HelloWorld" } },
    "state": "TAKEN",
    "assignee": { "username": "developer" },
    "resolution": { "type": "whenFixed" },
    "target": { "anyProblem": true }
  }

Step 1: Создаём investigation
  POST /app/rest/investigations → payload → investigation_id = body.id

Assert_1:
  HTTP 200
  body.assignee.username == "developer"
  body.state == "TAKEN"

Step 2: Удаляем investigation
  DELETE /app/rest/investigations/id:{investigation_id}

Assert_2:
  HTTP 204
  GET /app/rest/investigations/{investigation_id} → HTTP 404
```

**Ожидаемый результат:** Investigation создан и удалён

---

### № 47 — Билд на конкретной ревизии (E2E)

> Детали см. в № 19 (Integration). Разница — E2E проверяет весь сайд-эффект: что билд действительно собрал код из нужной ревизии.

---

### № 48 — Override параметров при запуске

| Поле | Значение |
|---|---|
| **ID** | № 48 |
| **Уровень** | E2E |
| **Приоритет** | P1 |

**Сценарий:** Запустить билд с переопределённым параметром, проверить что билд использовал новое значение в resulting-properties

**Шаги (AAA):**
```
Arrange:
  payload = {
    "buildType": { "id": "TestProject_HelloWorld" },
    "properties": {
      "property": [{ "name": "env.CUSTOM_VAR", "value": "override_value_047" }]
    }
  }

Act:
  build_id = POST /app/rest/buildQueue → payload → body.id
  wait_for_state(build_id, "finished", timeout=120s)

Assert:
  GET /app/rest/builds/id:{build_id}/resulting-properties
  В списке есть property с name=="env.CUSTOM_VAR" и value=="override_value_047"
```

---

### № 49 — Artifact dependency между сборками (E2E)

**Предусловия:**
- ConfigA публикует артефакт, ConfigB скачивает его через artifact dependency

**Шаги (AAA):**
```
Arrange:
  # Запустить ConfigA, дождаться артефакта
  build_a_id = POST /app/rest/buildQueue {buildType:{id:"ConfigA"}} → body.id
  wait_for_state(build_a_id, "finished", timeout=120s)

Act:
  # Запустить ConfigB (использует артефакт ConfigA)
  build_b_id = POST /app/rest/buildQueue {buildType:{id:"ConfigB"}} → body.id
  wait_for_state(build_b_id, "finished", timeout=120s)

Assert:
  GET /app/rest/builds/id:{build_b_id} → body.status == "SUCCESS"
  # Проверяем что артефактная зависимость разрешена
  GET /app/rest/builds?locator=artifactDependency:(to:(id:{build_b_id})) → содержит build_a_id
```

---

### № 50 — Скачивание архивированных артефактов (wildcard)

| Поле | Значение |
|---|---|
| **ID** | № 50 |
| **Уровень** | E2E |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}/artifacts/archived{path}?locator=pattern:{wildcard}` |

**Предусловия:**
- Завершённый билд с несколькими .txt артефактами

**Шаги (AAA):**
```
Arrange:
  build_id = <id билда с несколькими .txt файлами>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}/artifacts/archived/?locator=pattern:*.txt
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Content-Type: application/zip
  Размер ответа > 0
```

**Ожидаемый результат:** ZIP-архив со всеми txt-артефактами

---

### № 51 — Метаданные артефакта

| Поле | Значение |
|---|---|
| **ID** | № 51 |
| **Уровень** | E2E |
| **Приоритет** | P1 |
| **Endpoint** | `GET /app/rest/builds/{buildLocator}/artifacts/metadata{path}` |

**Шаги (AAA):**
```
Arrange:
  build_id = <id билда с артефактом hello.txt>

Act:
  GET {TC_URL}/app/rest/builds/id:{build_id}/artifacts/metadata/hello.txt
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.name == "hello.txt"
  body.size >= 0
  body.modificationTime != null
```

---

### № 52 — Pin/unpin билда

| Поле | Значение |
|---|---|
| **ID** | № 52 |
| **Уровень** | E2E |
| **Приоритет** | P1 |
| **Endpoint** | `GET/PUT /app/rest/builds/{buildLocator}/pinInfo` |

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого билда>

Step 1: Пинуем
  PUT {TC_URL}/app/rest/builds/id:{build_id}/pinInfo
  Header: Content-Type: application/json
  Body: { "status": true }

Assert_1:
  GET /app/rest/builds/id:{build_id}/pinInfo → body.status == true

Step 2: Анпинуем
  PUT {TC_URL}/app/rest/builds/id:{build_id}/pinInfo
  Header: Content-Type: application/json
  Body: { "status": false }

Assert_2:
  GET /app/rest/builds/id:{build_id}/pinInfo → body.status == false
```

---

## EDGE CASES (9 тестов)

---

### № 53 — Истёкший/невалидный токен → 401

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/projects
  Header: Authorization: Bearer invalid_fake_token_12345

Assert:
  HTTP 401
```

---

### № 54 — Несуществующий проект → 404 (не 500)

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/projects/id:NonExistentProject999
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 404
  НЕ 500
```

---

### № 55 — $help возвращает список dimensions

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/$help
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 400 (TeamCity возвращает 400 с описанием)
  body содержит список поддерживаемых dimensions
  Упоминаются: "buildType", "status", "branch", "id"
```

---

### № 56 — lookupLimit не превышает 5000 по умолчанию

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/builds?locator=start:4999,count:1
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count <= 1
  (Не выбрасывает 500, корректно обрабатывает граничное значение)
```

---

### № 57 — 5 конкурентных POST /app/rest/buildQueue

**Шаги (AAA):**
```
Act:
  Одновременно (async) отправляем 5 запросов:
  POST /app/rest/buildQueue {buildType:{id:"TestProject_HelloWorld"}}

Assert:
  Все 5 ответов: HTTP 200
  Все 5 body.state in ["queued", "running"]
  5 уникальных body.id

Cleanup:
  Отменить все 5 билдов
```

---

### № 58 — Невалидный locator → 400 (не 500)

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/builds?locator=invalidDimension:(garbage:value)
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 400
  НЕ 500
  body содержит сообщение об ошибке
```

---

### № 59 — Дублирующийся project ID → 400 (не 500)

**Шаги (AAA):**
```
Arrange:
  # TestProject уже существует
  payload = { "id": "TestProject", "name": "Duplicate", parentProject:{locator:"id:_Root"} }

Act:
  POST {TC_URL}/app/rest/projects
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 400
  НЕ 500
```

---

### № 60 — Base64url encoding в locator

**Шаги (AAA):**
```
Arrange:
  # Кодируем "TestProject" в base64url
  import base64
  encoded = base64.urlsafe_b64encode(b"TestProject").decode()  # "VGVzdFByb2plY3Q="

Act:
  GET {TC_URL}/app/rest/projects/id:($base64:{encoded})
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.id == "TestProject"
  Результат совпадает с GET /app/rest/projects/id:TestProject
```

---

### № 61 — Идемпотентность PUT параметра

**Шаги (AAA):**
```
Arrange:
  # Создаём параметр
  POST /app/rest/buildTypes/id:TestProject_HelloWorld/parameters
  { "name": "idempotentParam", "value": "v1" }

Act:
  # Отправляем PUT дважды с одним значением
  PUT /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/idempotentParam → "v2"
  PUT /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/idempotentParam → "v2"

Assert:
  Оба PUT: HTTP 200
  GET /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/idempotentParam → value == "v2"

Cleanup:
  DELETE /app/rest/buildTypes/id:TestProject_HelloWorld/parameters/idempotentParam
```

---

## RBAC (8 тестов)

---

### № 62 — PROJECT_ADMIN создаёт VCS Root в своём проекте

**Шаги (AAA):**
```
Act:
  POST {TC_URL}/app/rest/vcs-roots
  Header: Authorization: Bearer {PROJ_ADMIN_TOKEN}
  Body: { "id":"PA_TC060_Root", "name":"PA Root", "vcsName":"jetbrains.git",
          "project":{"id":"TestProject"},
          "properties":[{name:"url",value:"https://github.com/test/repo.git"},
                        {name:"branch",value:"refs/heads/main"},
                        {name:"authMethod",value:"ANONYMOUS"}] }

Assert:
  HTTP 200

Cleanup:
  DELETE /app/rest/vcs-roots/id:PA_TC060_Root (с ADMIN токеном)
```

---

### № 63 — PROJECT_ADMIN пытается удалить агента → 403

**Шаги (AAA):**
```
Arrange:
  agent_id = GET /app/rest/agents?locator=authorized:true → body.agent[0].id

Act:
  DELETE {TC_URL}/app/rest/agents/id:{agent_id}
  Header: Authorization: Bearer {PROJ_ADMIN_TOKEN}

Assert:
  HTTP 403
  Агент НЕ удалён: GET /app/rest/agents/id:{agent_id} → HTTP 200
```

---

### № 64 — DEVELOPER пытается изменить триггеры → 403

**Шаги (AAA):**
```
Act:
  POST {TC_URL}/app/rest/buildTypes/id:TestProject_HelloWorld/triggers
  Header: Authorization: Bearer {DEV_TOKEN}
  Body: { "type": "vcsTrigger", "properties": {"property":[{name:"branchFilter",value:"+:*"}]} }

Assert:
  HTTP 403
```

---

### № 65 — DEVELOPER запускает personal build → 200

**Шаги (AAA):**
```
Act:
  build_id = POST {TC_URL}/app/rest/buildQueue
  Header: Authorization: Bearer {DEV_TOKEN}
  Body: { "buildType":{"id":"TestProject_HelloWorld"}, "personal": true }

Assert:
  HTTP 200
  body.personal == true

Cleanup:
  Отменить билд
```

---

### № 66 — Guest доступ ON: GET /app/rest/projects без токена → 200

**Шаги (AAA):**
```
Arrange:
  PUT /app/rest/server/authSettings → включить allowGuest:true (с ADMIN токеном)

Act:
  GET {TC_URL}/guestAuth/app/rest/projects
  (без Authorization заголовка)

Assert:
  HTTP 200

Cleanup:
  PUT /app/rest/server/authSettings → allowGuest:false
```

---

### № 67 — Guest доступ OFF: GET /app/rest/projects без токена → 401

**Шаги (AAA):**
```
Arrange:
  Убеждаемся что guest доступ выключен
  PUT /app/rest/server/authSettings → allowGuest:false

Act:
  GET {TC_URL}/app/rest/projects
  (без Authorization заголовка)

Assert:
  HTTP 401
```

---

### № 68 — Отзыв роли лишает доступа

**Шаги (AAA):**
```
Arrange:
  # Создаём тестового пользователя с ролью VIEWER
  user_id = POST /app/rest/users {username:"tc_065_user", password:"P@ssw0rd065"} → body.id
  PUT /app/rest/users/id:{user_id}/roles/PROJECT_VIEWER/p:TestProject
  user_token = POST /app/rest/users/id:{user_id}/tokens/tc065 → body.value

  # Проверяем что доступ есть
  GET /app/rest/projects Header:Bearer {user_token} → HTTP 200

Act:
  # Отзываем роль
  DELETE /app/rest/users/id:{user_id}/roles/PROJECT_VIEWER/p:TestProject

Assert:
  # Доступ закрыт
  GET /app/rest/projects/id:TestProject Header:Bearer {user_token} → HTTP 403

Cleanup:
  DELETE /app/rest/users/id:{user_id}
```

---

### № 69 — VIEWER пытается запустить билд → 403

**Шаги (AAA):**
```
Act:
  POST {TC_URL}/app/rest/buildQueue
  Header: Authorization: Bearer {VIEWER_TOKEN}
  Body: { "buildType": { "id": "TestProject_HelloWorld" } }

Assert:
  HTTP 403
```

---

## VCS & TRIGGERS (4 теста)

---

### № 70 — Получение конфигурации триггеров

| Поле | Значение |
|---|---|
| **ID** | № 70 |
| **Endpoint** | `GET /app/rest/buildTypes/{id}/triggers` |

**Шаги (AAA):**
```
Arrange:
  # Убеждаемся что в TestProject_HelloWorld есть VCS trigger
  # (добавить в setup если нет)

Act:
  GET {TC_URL}/app/rest/buildTypes/id:TestProject_HelloWorld/triggers
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.trigger — список
  Если добавлен VCS trigger: body.trigger[0].type == "vcsTrigger"
```

---

### № 71 — Запуск в ветке и проверка resulting-properties

**Шаги (AAA):**
```
Arrange:
  payload = {
    "buildType": { "id": "TestProject_HelloWorld" },
    "branchName": "main"
  }

Act:
  build_id = POST /app/rest/buildQueue → payload → body.id
  wait_for_state(build_id, "finished", timeout=120s)

Assert:
  GET /app/rest/builds/id:{build_id}/resulting-properties
  → содержит "teamcity.build.branch" == "main"
```

---

### № 72 — Фильтр VCS root instances по VCS Root

**Шаги (AAA):**
```
Act:
  GET {TC_URL}/app/rest/vcs-root-instances?locator=vcsRoot:(id:TestRepo)
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Все body.vcsRootInstance[i].vcsRoot.id == "TestRepo"
```

---

## TESTS, MUTES, INVESTIGATIONS (5 тестов)

---

### № 73 — Добавление тега к билду

| Поле | Значение |
|---|---|
| **Endpoint** | `POST /app/rest/builds/{buildLocator}/tags` |

**Шаги (AAA):**
```
Arrange:
  build_id = <id завершённого билда>
  payload = { "tag": [{"name": "tc070-tag"}, {"name": "regression"}] }

Act:
  POST {TC_URL}/app/rest/builds/id:{build_id}/tags
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  GET /app/rest/builds/id:{build_id}/tags → содержит "tc070-tag" и "regression"

Cleanup:
  PUT /app/rest/builds/id:{build_id}/tags → { "tag": [] }  # очищаем
```

---

### № 74 — Фильтрация investigations по assignee

**Шаги (AAA):**
```
Arrange:
  # Создаём investigation для developer
  POST /app/rest/investigations { scope:{buildType:{id:"TestProject_HelloWorld"}},
    state:"TAKEN", assignee:{username:"developer"},
    resolution:{type:"whenFixed"}, target:{anyProblem:true} }

Act:
  GET {TC_URL}/app/rest/investigations?locator=assignee:(username:developer)
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Все body.investigation[i].assignee.username == "developer"
```

---

### № 75 — Muting теста

**Шаги (AAA):**
```
Arrange:
  # Нужен тест с известным именем, который фейлится
  # Имя теста: "com.example.FailingTest.testSomething"
  payload = {
    "scope": { "project": { "id": "TestProject" } },
    "target": { "tests": { "test": [{"name": "com.example.FailingTest.testSomething"}] } },
    "resolution": { "type": "whenFixed" }
  }

Act:
  POST {TC_URL}/app/rest/mutes
  Header: Authorization: Bearer {ADMIN_TOKEN}
  Body: payload

Assert:
  HTTP 200
  body.target.tests.test[0].name == "com.example.FailingTest.testSomething"
  mute_id = body.id

Cleanup:
  DELETE /app/rest/mutes/id:{mute_id}
```

---

### № 76 — Результаты тестов для билда

**Шаги (AAA):**
```
Arrange:
  # Нужен билд с тест-результатами (build config с pytest/junit runner)
  build_id = <id билда, который запускал тесты>

Act:
  GET {TC_URL}/app/rest/testOccurrences?locator=build:(id:{build_id})
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  body.count >= 0
  Если count > 0: body.testOccurrence[0].status in ["SUCCESS", "FAILURE", "IGNORED"]
```

---

### № 77 — Build problems в билде

**Шаги (AAA):**
```
Arrange:
  # Нужен билд со статусом FAILURE (есть build problem)
  failed_build_id = <id failed билда>

Act:
  GET {TC_URL}/app/rest/problemOccurrences?locator=build:(id:{failed_build_id})
  Header: Authorization: Bearer {ADMIN_TOKEN}

Assert:
  HTTP 200
  Если билд failed: body.count >= 1
  body.problemOccurrence[0].type != null
```

---

## Приложение: Утилиты для тестов (Python/pytest)

```python
import time
import httpx

def wait_for_build_state(
    base_url: str,
    build_id: int,
    target_state: str,
    token: str,
    timeout: int = 120,
    poll_interval: int = 3
) -> dict:
    """
    Polling хелпер — ждёт пока билд перейдёт в нужное состояние.
    Никаких time.sleep без таймаута.
    """
    deadline = time.time() + timeout
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    while time.time() < deadline:
        resp = httpx.get(f"{base_url}/app/rest/builds/id:{build_id}", headers=headers)
        data = resp.json()
        if data.get("state") == target_state:
            return data
        time.sleep(poll_interval)

    raise TimeoutError(f"Build {build_id} did not reach state '{target_state}' within {timeout}s")


def cancel_build(base_url: str, build_id: int, token: str) -> None:
    """Cleanup-утилита для отмены билда."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"comment": "Cancelled by test cleanup", "readdIntoQueue": False}

    # Сначала пробуем как queued
    httpx.post(f"{base_url}/app/rest/buildQueue/id:{build_id}",
               json=payload, headers=headers)
    # Потом как running
    httpx.post(f"{base_url}/app/rest/builds/id:{build_id}",
               json=payload, headers=headers)
```

---

*Документ содержит 77 тест-кейсов (нумерация № 1–77, как в test_plan.md). Версия 1.1 · Апрель 2026*