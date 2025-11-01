# CC_StdLib Documentation

Документация библиотеки функциональных блоков IEC ST (Structured Text).

## Описание

Этот проект представляет собой веб-документацию для библиотеки CC_StdLib, построенную с использованием MkDocs и Material Design темы. Документация включает описание архитектуры, функциональных блоков для работы с сигналами, механизмами и системами управления.

## Технологический стек

- **Python**: 3.11
- **MkDocs**: Генератор статических сайтов для документации
- **Material for MkDocs**: Современная и отзывчивая тема
- **Docker**: Контейнеризация приложения

## Основные зависимости

- `mkdocs` >= 1.5.0 - Основной генератор документации
- `mkdocs-material` >= 9.0.0 - Material Design тема
- `pymdown-extensions` >= 10.0.0 - Расширения для Markdown
- `mkdocs-mermaid2-plugin` >= 1.0.0 - Поддержка диаграмм Mermaid
- `mkdocs-git-revision-date-localized-plugin` >= 1.2.0 - Даты изменений из Git

Полный список зависимостей доступен в файле `requirements.txt`.

## Быстрый старт с Docker

### Предварительные требования

- Docker
- Docker Compose (опционально, для упрощенного запуска)

### Запуск с Docker Compose (рекомендуется)

1. Клонируйте репозиторий:
   ```bash
   git clone <repository-url>
   cd CC_StdLib_MkDocs
   ```

2. Запустите контейнер:
   ```bash
   docker-compose up
   ```

3. Откройте браузер и перейдите по адресу:
   ```
   http://localhost:8000
   ```

Для остановки контейнера используйте `Ctrl+C` или:
```bash
docker-compose down
```

### Запуск с Docker (без Docker Compose)

1. Соберите Docker образ:
   ```bash
   docker build -t cc-stdlib-docs .
   ```

2. Запустите контейнер:
   ```bash
   docker run -p 8000:8000 -v $(pwd):/app cc-stdlib-docs
   ```

3. Откройте браузер и перейдите по адресу:
   ```
   http://localhost:8000
   ```

## Локальная разработка (без Docker)

### Установка зависимостей

1. Убедитесь, что у вас установлен Python 3.11 или выше:
   ```bash
   python --version
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### Запуск локального сервера

```bash
mkdocs serve
```

Сайт будет доступен по адресу: `http://127.0.0.1:8000`

### Сборка статического сайта

```bash
mkdocs build
```

Собранный сайт будет находиться в директории `site/`.

## Структура проекта

```
CC_StdLib_MkDocs/
├── docs/                  # Исходные файлы документации
│   ├── index.md          # Главная страница
│   ├── getting-started.md
│   ├── diagram.md
│   ├── Communication.md
│   ├── signal/           # Документация сигналов
│   ├── mechanism/        # Документация механизмов
│   └── control/          # Документация управления
├── site/                  # Собранный статический сайт (создается автоматически)
├── stylesheets/          # Пользовательские CSS стили
├── mkdocs.yml            # Конфигурация MkDocs
├── requirements.txt      # Python зависимости
├── Dockerfile            # Конфигурация Docker образа
├── docker-compose.yml    # Конфигурация Docker Compose
└── README.md             # Этот файл
```

## Полезные команды

| Команда | Описание |
|---------|----------|
| `mkdocs serve` | Запуск локального dev-сервера с hot-reload |
| `mkdocs build` | Сборка статического сайта |
| `mkdocs gh-deploy` | Деплой на GitHub Pages |
| `docker-compose up` | Запуск в Docker |
| `docker-compose up -d` | Запуск в фоновом режиме |
| `docker-compose down` | Остановка контейнера |
| `docker-compose logs -f` | Просмотр логов |

## Особенности

- Поддержка русского языка
- Темная тема (Material Design)
- Подсветка синтаксиса кода
- Поддержка диаграмм Mermaid
- Поиск по документации
- Навигация с вкладками
- Адаптивный дизайн
- Копирование кода одним кликом

## Конфигурация

Основная конфигурация сайта находится в файле `mkdocs.yml`. Здесь можно изменить:
- Название сайта
- Структуру навигации
- Настройки темы
- Плагины
- Расширения Markdown
