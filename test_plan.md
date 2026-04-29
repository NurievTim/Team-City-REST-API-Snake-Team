**TEST PLAN**

**TeamCity REST API — Test Automation**

*Апрель 2026 · Верифицирована по Swagger TC.json*

| Дата       | Апрель 2026                |
|:-----------|:---------------------------|
| Продукт    | JetBrains TeamCity 2025.11 |
| API версия | REST API 2025.11           |
| Горизонт   | 1 месяц / 4 недели         |

#  **1\. Бизнес-контекст и цели**

## **1.1 Baseline → Target метрики**

| Метрика             | Baseline         | Target (месяц)        |
|:--------------------|:-----------------|:----------------------|
| Время регрессии     | \~8 ч (вручную)  | \< 20 мин             |
| Частота запуска     | 1 раз / 2 недели | Каждый push / nightly |
| Покрытие эндпоинтов | \~30%            | ≥ 70%                 |
| Участие человека    | 8 ч / 2 недели   | 0 ч (разбор только)   |

## **1.2 ROI-оценка**

* Ручная регрессия: 8 ч × 2 раза/мес × $50/ч \= $800/месяц

* Разработка фреймворка: \~80 ч (одноразово)

* Поддержка: \~2 ч/неделю

* Точка окупаемости: 4–5 месяцев (с учётом prevention дефектов)

# **2\. Deliverables (6 артефактов)**

* ✓ Набор автотестов (71 тест-кейс): 7 smoke, 48 integration, 11 E2E, 5 quality

* ✓ CI/CD пайплайн (GitHub Actions): smoke @ push, full nightly, pytest-xdist

* ✓ Allure-отчёт с трендами: история, severity, timeline, flakiness

* ✓ Документация: README (10 мин setup)

* ✓ ROI-отчёт: baseline vs actual, покрытие


# **3\. Скоуп тестирования**

## **3.1 In Scope (12 модулей)**

* Build \+ BuildQueue (P0): trigger, cancel, custom params, statistics, artifacts, pin, tags

* Project \+ BuildType (P0): CRUD, copy, paused, parameters, steps, triggers, VCS roots

* Authentication (P0): Bearer token, 401/403, token lifecycle, 2FA

* Agent \+ AgentPool (P1): list, enabledInfo, authorizedInfo, pools CRUD

* User \+ Group \+ Role (P1): CRUD, roles/{roleId}/{scope}, tokens

* REST Locators (P1): pagination, lookupLimit, nested, $help, branch:\<any\>, Base64

* VCS Root \+ VersionedSettings (P1): CRUD, config sync, commitHook, status

* RBAC (P1): 4 роли × основные операции (матрикс 4×7)

* Test \+ Mute \+ Investigation (P1): occurrences, mute/unmute, assign investigations

* Server \+ Audit (P2): globalSettings, authSettings, backup, audit records

* Artifact Dependencies E2E (P1): конфигурация, download, checksum

* VCS Triggers (P1): триггер конфигурация (не само срабатывание, оно @slow)

## **3.2 Out of Scope**

* UI-тестирование (Web UI) — отдельный проект

* Performance / load testing

## **3.3 Пирамида тестирования (71 тест)**

| Уровень     | Кол-во | %    |
|:------------|:-------|:-----|
| Unit        | 8      | 11%  |
| Integration | 52     | 73%  |
| E2E         | 11     | 16%  |
| ИТОГО       | 71     | 100% |


# **4\. Тест-кейсы (71 шт.)**

## **4.1 Smoke Suite (7 тестов, P0)**

| ID  | Endpoint                            | Expected Result                |
|:----|:------------------------------------|:-------------------------------|
| № 1 | GET /server                         | HTTP 200, version присутствует |
| № 2 | GET /users/current \+ Bearer token  | HTTP 200, username совпадает   |
| № 3 | GET /projects без токена            | HTTP 401 Unauthorized          |
| № 4 | POST /buildQueue {buildType.id}     | HTTP 200, state=queued         |
| № 5 | GET /builds/{id}                    | HTTP 200, state=running        |finished |
| № 6 | GET /projects                       | HTTP 200, count \>= 1          |
| № 7 | GET /agents?locator=authorized:true | HTTP 200, ≥1 агент             |

## **4.2 Builds (12 тестов)**

* № 8: POST /buildQueue/{queuedBuildLocator} — отмена queued-билда

* № 9: POST /builds/{buildLocator} — отмена running-билда (новый endpoint)

* № 10: Запуск custom build с параметрами (personal, branchName, agent)

* № 11: GET /artifacts/files{path} — скачивание артефакта

* № 12: GET /statistics — статистика билда

* № 13: GET /builds?locator=status:FAILURE,branch:(default:any) — фильтр (branch обязателен\!)

* № 14: GET /builds?locator=count:5,start:0 — pagination, страница 1

* № 15: GET /builds?locator=count:5,start:5 — pagination, страница 2

* № 16: GET /changes?locator=build:(id:X) — изменения для билда

* № 17: GET /builds?locator=snapshotDependency:(from:(id:A)) — зависимость

* № 18: GET /builds/{id}/resulting-properties — параметры завершённого билда

* № 19: POST /buildQueue с revisions\[{version:SHA,...}\] — конкретная ревизия

## **4.3 Projects (10 тестов)**

* № 20: POST /projects — создание проекта

* № 21: DELETE /projects/{id} → GET — удаление (HTTP 2xx, no body)

* № 22: POST /buildTypes — создание конфигурации

* № 23: POST /projects/{id}/buildTypes с copyAllAssociatedSettings:true — копирование

* № 24: PUT /buildTypes/{id}/paused — приостановка

* № 25: PUT /buildTypes/{id}/parameters/{name} → GET — изменение параметра

* № 26: POST /vcs-roots — создание VCS root

* № 27: PUT /projects/{id}/archived — архивация проекта

* № 28: POST /buildTypes/{id}/move?targetProjectId — перемещение конфигурации

* № 29: GET /buildTypes?locator=affectedProject:{id} — рекурсивный поиск

## **4.4 Agents & Users (12 тестов)**

* № 30: GET /agents?locator=connected:true,authorized:true — фильтр

* № 31: PUT /agents/{id}/enabledInfo {status:false,comment} — отключение

* № 32: POST /agentPools — создание пула

* № 33: POST /users — создание пользователя

* № 34: PUT /users/{id}/roles/{roleId}/{scope} — добавление роли (с scope\!)

* № 35: DELETE /users/{id} → GET — удаление пользователя

* № 36: POST /users/{id}/tokens/{name} — создание токена

* № 37: GET /agentPools/{id}/agents — агенты в пуле

* № 38: PUT /agents/{id}/authorizedInfo {status:true} — авторизация

* № 39: GET /users/current — текущий пользователь

* № 40: GET /userGroups — системные группы

* № 41: DELETE /users/{id}/tokens/{name} — удаление токена

## **4.5 E2E (11 тестов)**

* № 42: Полный цикл проекта (create → VCS → buildType → trigger → artifact → delete)

* № 43: Build Chain с reuse bildo

* № 44: Agent offline → bildo waits → online → finished

* № 45: Versioned Settings sync

* № 46: Investigation assign/delete

* № 47: Bildo для конкретной ревизии (revisions\[{version:SHA}\])

* № 48: Custom build params override

* № 49: Artifact dependency между сборками

* № 50: Download archived artifacts (wildcard)

* № 51: Artifact metadata

* № 52: Pin/unpin build

## **4.6 Edge Cases (9 тестов)**

* № 53: Истёкший токен → 401

* № 54: Несуществующий проект → 404 (не 500\)

* № 55: GET /$help → список dimensions

* № 56: lookupLimit 5000 → корректный ответ

* № 57: 5 конкурентных buildQueue → все в очереди

* № 58: Неверный locator → 400 (не 500\)

* № 59: Дублирующийся project ID → 400 (не 500\)

* № 60: Base64url encoding в locator

* № 61: Идемпотентность PUT


## **4.7 RBAC (8 тестов, P1)**

| Операция        | ADMIN | PROJ\_ADMIN | DEVELOPER | VIEWER |
|:----------------|:------|:------------|:----------|:-------|
| Trigger build   | ✓     | ✓           | ✓         | ✗      |
| Delete project  | ✓     | ✗           | ✗         | ✗      |
| Create user     | ✓     | ✗           | ✗         | ✗      |
| Create VCS root | ✓     | ✓           | ✗         | ✗      |
| GET /builds     | ✓     | ✓           | ✓         | ✓      |
| Personal build  | ✓     | ✓           | ✓         | ✗      |
| Delete agent    | ✓     | ✗           | ✗         | ✗      |

* № 62: PROJECT\_ADMIN создаёт VCS root в своём проекте

* № 63: PROJECT\_ADMIN пытается DELETE /agents (системный) → 403

* № 64: DEVELOPER пытается PUT /buildTypes/{id}/triggers → 403

* № 65: DEVELOPER запускает personal build → 200

* № 66: Гостевой доступ ON: GET /projects без токена → 200 (public только)

* № 67: Гостевой доступ OFF: GET /projects без токена → 401

* № 68: ADMIN отзывает роль → пользователь теряет доступ → 403

* № 69: VIEWER пытается POST /buildQueue → 403

## **4.8 VCS & Triggers (4 теста, P1)**

* № 70: GET /buildTypes/{id}/triggers — проверяем конфигурацию trigg'ера (не срабатывание)

* № 71: POST /buildQueue с branchName → GET resulting-properties проверка

* № 72: GET /vcs-root-instances?locator=vcsRoot:(id:X) → фильтр

## **4.9 Tests, Mutes, Investigations (5 тестов, P1)**

* № 73: POST /builds/{id}/tags — добавление тага

* № 74: GET /investigations?locator=assignee:(username:X) — фильтр

* № 75: POST /mutes — muting теста

* № 76: GET /testOccurrences?locator=build:(id:Z) — результаты тестов

* № 77: GET /problemOccurrences — проблемы в билде

# **5\. Окружение**

## **5.1 Инфраструктура**

* TeamCity Server: docker pull jetbrains/teamcity-server:2025.11 (ЗАФИКСИРОВАНО, не latest)

* TeamCity Agent: docker pull jetbrains/teamcity-agent:2025.11

* Docker Compose: tc-server \+ tc-agent; health check на /app/rest/server

* CI: GitHub Actions Ubuntu 22.04; pytest-xdist (параллель)

* Python: 3.11+; httpx, pytest, allure-pytest

* .env: TC\_URL, TC\_ADMIN\_TOKEN, TC\_PROJECT\_ADMIN\_TOKEN, TC\_DEVELOPER\_TOKEN, TC\_VIEWER\_TOKEN

## **5.2 Предусловия (Неделя 1\)**

* GET /app/rest/server → HTTP 200

* ≥1 агент: authorized=true, enabled=true, connected=true

* 4 тестовых пользователя с ролями (в conftest.py, session scope):

  * admin: SYSTEM\_ADMIN (scope:g)

  * proj\_admin: PROJECT\_ADMIN (scope:p:TestProject)

  * developer: PROJECT\_DEVELOPER (scope:p:TestProject)

  * viewer: PROJECT\_VIEWER (scope:p:TestProject)

* Проект TestProject с build config HelloWorld

* Git VCS Root для дефолтных тестов

# **6\. Риски и митигация**

| Риск                         | Вероятность | Mitigation                                    |
|:-----------------------------|:------------|:----------------------------------------------|
| Baseline недоступен          | Высокая     | Замер вручную неделя 1                        |
| Flaky тесты (race condition) | Высокая     | wait\_for\_build\_state() polling, no sleep() |
| Docker нестабилен            | Средняя     | health-check retry; conftest isolation        |
| RBAC требует инфры           | Средняя     | 4 токена в .env; fixture session scope        |
| Время на E2E                 | Средняя     | P0/P1 приоритетны; E2E после smoke            |
|                              |             |                                               |
| Нет реального бага           | Средняя     | Edge cases исторически содержат дефекты       |
| Rate limiting                | Низкая      | pytest-xdist \-n 4; retry на 429              |
|                              |             |                                               |


# **8\. Метрики и отчётность**

## **8.1 Метрики качества**

| Метрика                | Целевое значение | Инструмент              |
|:-----------------------|:-----------------|:------------------------|
| Pass rate (smoke)      | \>= 100%         | Allure / GitHub Actions |
| Pass rate (regression) | \>= 95%          | Allure Trends           |
| Flaky test rate        | \< 5% за 7 дней  | Allure Retries          |
| Время полной регрессии | \< 22 мин        | GitHub Actions logs     |
| API endpoint coverage  | \>= 80% (P0+P1)  | Coverage report         |
| RBAC coverage          | 4 роли × 7 ops   | Allure Suite            |

## **8.2 Definition of Done для теста**

1. Уникальный ID и привязка к пирамиде

2. Структура AAA: Arrange → Act → Assert

3. Атомарность: одна проверка; если две — два теста

4. Стабильность: зелёный 20 раз подряд

5. Независимость: не зависит от других тестов

6. Endpoint соответствует Swagger (operationId, HTTP-метод, response code)

7. Ролевое покрытие: если RBAC применимо — проверена ≥2 ролями

# **9\. Архитектура Фреймворка** 


|                                                                                             1 — Target System (Layer 0) JetBrains TeamCity в Docker · REST API /app/rest/\* · тестовый проект с билдом и пользователями                                                                                             |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                    2 — HTTP Client (**Layer 1**) Единый клиент для всех запросов · авторизация по токену · автоматический retry                                                                                                     |
| 3 — Fixtures & Config (**Layer 2**) Готовые пользователи для тестов (admin, developer, viewer) · создание и удаление ресурсов · ожидание состояния билда conftest.py · auth fixtures: admin · dev · viewer · scope=session · resource fixtures: project · buildType · vcs\_root · agent · wait\_for\_build\_state() |
|                                                                                                       4 — Test Layer (**Layer 3**) tests/smoke/ · tests/builds/ · tests/rbac/ · tests/e2e/ · tests/edge+vcs/                                                                                                        |
|                                                                                      5 — Reporting (**Layer 4**) Allure Reports · severity · timeline · history · @allure.step · flakiness \<5% · pytest-xdist · parallel \-n4                                                                                      |
|                                                                                    6 — Infrastructure (**Layer 5**) docker-compose.yml · tc-server:2025.11  · .env / secrets · TC\_URL · TC\_ADMIN\_TOKEN · healthcheck · retry                                                                                     |
|                                                                                                       7 — CI/CD Pipeline (**Layer 6**) Smoke при каждом push · регрессия ночью · Allure отчёт на GitHub Pages                                                                                                       |