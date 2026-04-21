# 🐍 TeamCity Tests — SnakeTeam

Проект автоматизированного API-тестирования **TeamCity** на Python.  
Разработан командой **SnakeTeam**.

---

## 🛠 Стек технологий

| Инструмент | Назначение |
|---|---|
| Python 3.11+ | Основной язык |
| pytest | Фреймворк для тестов |
| requests | HTTP-клиент для API |
| pydantic | Валидация моделей данных |
| faker + rstr | Генерация случайных тестовых данных |
| allure-pytest | Отчёты о прогоне тестов |
| pytest-xdist | Параллельный запуск тестов |
| softest | Мягкие ассерты |
| ruff | Линтер / форматтер |

---

## 📁 Структура проекта

```
TeamCity_Tests_SnakeTeam/
├── framework/
│   ├── clients/
│   │   ├── base_http_api_client.py                     # Базовый HTTP-клиент
│   │   ├── team_city_api_client.py                     # Методы TeamCity REST API
│   │   └── log_to_allure.py                            # Attach request/response в Allure
│   ├── checkers/
│   │   └── check.py                                    # Проверки статусов и JSON-схем
│   ├── data/
│   │   ├── entities/
│   │   │   └── team_city_api_handler_info.py           # Описания API handlers
│   │   ├── fixtures/
│   │   │   └── api_fixtures.py                         # Дополнительные pytest-фикстуры
│   │   ├── models/
│   │   │   ├── team_city_api_models.py
│   │   │   ├── team_city_api_headers_models.py
│   │   │   └── team_city_api_query_models.py
│   │   └── constants.py                                # Базовые константы
│   ├── helpers/
│   │   └── helper.py                                   # Хэлперы для подготовки данных
│   └── reporting/                                      # Хэлперы для репортинга
├── tests/
│   ├── agents/                                         # Тесты сервиса agents
│   ├── builds/                                         # Тесты сервиса builds
│   ├── projects/                                       # Тесты сервиса projects
│   ├── RBAC/                                           # Тесты ролевых моделей
│   ├── VCS/                                            # Тесты сервиса VCS
│   └── E2E/                                            # E2E тесты
├── conftest.py                                         # Общие фикстуры pytest
├── test_plan.md                                        # План покрытия и тест-кейсов
├── requirements.txt                                    # Зависимости
├── ruff.toml                                           # Конфиг линтера
└── .gitignore
```

---

## ⚙️ Установка проекта (шаг за шагом)

### 1. Клонировать репозиторий

```bash
git clone https://github.com/GLskill/TeamCity_Tests_SnakeTeam.git
cd TeamCity_Tests_SnakeTeam
```

### 2. Убедиться, что Python 3.11+ установлен

```bash
python --version
# должно быть Python 3.11.x или выше
```

Если Python не установлен — скачай с [python.org](https://www.python.org/downloads/).

### 3. Создать и активировать виртуальное окружение

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

> ✅ Ты должен увидеть `(.venv)` в начале строки терминала — значит, окружение активно.

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

