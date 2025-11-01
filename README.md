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
├── docs/                           # Исходные файлы документации (Markdown)
│   ├── index.md                   # Главная страница
│   ├── getting-started.md         # Руководство по началу работы
│   ├── diagram.md                 # Архитектурные диаграммы
│   ├── Communication.md           # Документация по коммуникации
│   ├── stylesheets/               # Пользовательские CSS стили
│   │   └── github-dark.css       # GitHub Dark тема
│   ├── signal/                    # Документация сигналов
│   │   ├── discrete/             # Дискретные сигналы (FB_BasicSignal, и др.)
│   │   └── analog/               # Аналоговые сигналы (FB_AnalogSignal4_20mA, и др.)
│   ├── mechanism/                 # Документация механизмов
│   │   ├── FB_AbstractMechanism.md
│   │   ├── FB_Mechanism.md
│   │   └── FB_MechanismWithFeedback.md
│   ├── control/                   # Документация управления
│   │   ├── FB_BasicControl.md
│   │   └── FB_FrequencyControl.md
│   └── diagrams/                  # Дополнительные диаграммы
├── src/                            # Исходные файлы (дублирование для удобства)
│   └── stylesheets/               # Копия стилей для разработки
│       └── github-dark.css
├── site/                           # Собранный статический сайт (создается автоматически)
├── mkdocs.yml                      # Главная конфигурация MkDocs
├── requirements.txt                # Python зависимости
├── Dockerfile                      # Конфигурация Docker образа
├── docker-compose.yml              # Конфигурация Docker Compose
├── build.bat / serve.bat          # Скрипты для Windows
└── README.md                       # Этот файл
```

## Архитектура сайта

### Общая архитектура

Сайт построен на основе **MkDocs** - генератора статических сайтов, специализированного для документации. Архитектура состоит из нескольких ключевых компонентов:

```
┌─────────────────────────────────────────────────┐
│           Исходники (Markdown)                  │
│              docs/*.md                          │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│         MkDocs Engine                           │
│  ├─ Material Theme                              │
│  ├─ Mermaid Plugin (диаграммы)                  │
│  ├─ Search Plugin (поиск)                       │
│  └─ PyMdown Extensions (синтаксис)              │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│     Статический HTML/CSS/JS                     │
│           site/*.html                           │
└─────────────────────────────────────────────────┘
```

### Конфигурация MkDocs (mkdocs.yml)

Основной конфигурационный файл содержит:

1. **Метаданные сайта**
   - Название, описание, автор
   - Ссылки на репозиторий

2. **Настройки темы Material**
   - Цветовая схема: `slate` (темная)
   - Основной цвет: `blue grey`
   - Акцентный цвет: `blue`

3. **Функции навигации**
   - `navigation.tabs` - вкладки в верхней части
   - `navigation.instant` - AJAX-навигация без перезагрузки
   - `navigation.instant.prefetch` - предзагрузка при наведении
   - `navigation.instant.progress` - индикатор загрузки
   - `navigation.tracking` - отслеживание URL при скролле

4. **Расширения Markdown**
   - `pymdownx.highlight` - подсветка кода
   - `pymdownx.superfences` - блоки кода с поддержкой Mermaid
   - `admonition` - блоки заметок/предупреждений
   - `tables` - таблицы

5. **Плагины**
   - `search` - поиск с поддержкой русского языка
   - `mermaid2` - рендеринг диаграмм Mermaid

### Система стилей

#### Иерархия стилей

```
1. Material Theme (базовые стили)
          ↓
2. CSS переменные (:root)
          ↓
3. github-dark.css (кастомная тема)
          ↓
4. Компонентные стили
```

#### Ключевые компоненты стилей

**1. Цветовая палитра (GitHub Dark)**
```css
--github-dark-bg-primary: #0d1117     /* Основной фон */
--github-dark-bg-secondary: #161b22   /* Вторичный фон */
--github-dark-text-primary: #e6edf3   /* Основной текст */
--github-dark-accent-blue: #58a6ff    /* Акцентный цвет */
```

**2. Навигация**
- **Левая панель** (`.md-sidebar--primary`): Основная навигация по разделам
  - Ширина: `12.1rem + 70px`
  - Вложенные уровни с отступом 12px
  - Единый стиль со скругленными углами (4px)

- **Правая панель** (`.md-sidebar--secondary`): Содержание страницы
  - Sticky заголовок при скролле
  - Подсветка активного раздела

**3. Типографика**
- Основной шрифт: системный (sans-serif)
- Моноширинный: Consolas, Monaco, Courier New
- Размеры: 0.8rem (навигация), 1rem (основной текст)

### Система навигации

#### Структура навигации

```
Главная
├── Начало работы
├── Архитектура
├── Коммуникация
├── Сигналы
│   ├── Дискретные сигналы
│   │   ├── FB_BasicSignal
│   │   ├── FB_SignalWithFeedback
│   │   └── ...
│   └── Аналоговые сигналы
│       ├── FB_BasicAnalogSignal
│       └── ...
├── Механизмы
│   ├── FB_AbstractMechanism
│   └── ...
└── Управление
    └── FB_BasicControl
```

#### Функции навигации

1. **Instant Navigation** - загрузка страниц через AJAX без полной перезагрузки
2. **Prefetch** - предзагрузка страниц при наведении на ссылку
3. **Progress Indicator** - прогресс-бар вверху при загрузке
4. **URL Tracking** - автоматическое обновление URL при скролле

### Производительность и оптимизация

#### Техники оптимизации

1. **Lazy Loading**
   - Изображения загружаются по мере необходимости
   - Mermaid диаграммы рендерятся при отображении

2. **Кэширование**
   - Статические ресурсы кэшируются браузером
   - Service Worker для offline-доступа (опционально)

3. **Минимизация**
   - HTML/CSS/JS минимизируются при сборке production
   - Неиспользуемый CSS удаляется автоматически

4. **Плавные переходы**
   - CSS анимации (fade-in 0.2-0.25s)
   - Предотвращение FOUC (Flash of Unstyled Content)

### Работа с документацией

#### Формат документации

Каждый функциональный блок документируется по следующей структуре:

```markdown
# [Название блока]

## Обзор
### Назначение
### Основные возможности

## Интерфейс
### Входные параметры
### Выходные параметры

## Логика работы
### Описание алгоритма
### Диаграммы

## Примеры использования
### Базовый пример
### Расширенный пример

## Примечания
```

#### Добавление новой документации

1. Создайте файл `.md` в соответствующей директории
2. Добавьте ссылку в `mkdocs.yml` в секцию `nav:`
3. Следуйте структуре документации выше
4. Используйте Mermaid для диаграмм

#### Поддерживаемые элементы Markdown

- Заголовки (H1-H6)
- Списки (упорядоченные/неупорядоченные)
- Таблицы
- Блоки кода с подсветкой синтаксиса
- Ссылки и изображения
- Admonitions (заметки, предупреждения)
- Mermaid диаграммы

### Docker контейнеризация

#### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
```

#### Docker Compose

Автоматически:
- Монтирует текущую директорию в `/app`
- Пробрасывает порт 8000
- Включает hot-reload при изменениях
- Автоматически перезапускается при сбоях

### Troubleshooting

#### Проблема: Фиолетовое мерцание при навигации
**Решение**: Добавлены стили для `:visited` и `:active` состояний ссылок

#### Проблема: Длинные названия обрезаются
**Решение**: Увеличена ширина левой панели, добавлен `text-overflow: ellipsis`

#### Проблема: Медленная загрузка страниц
**Решение**: Включены `navigation.instant.prefetch` и `navigation.instant.progress`

#### Проблема: Стили не применяются
**Решение**: Проверьте путь к CSS в `mkdocs.yml`:
```yaml
extra_css:
  - stylesheets/github-dark.css
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

## Расширение функциональности

### Добавление новых плагинов

1. Добавьте плагин в `requirements.txt`:
   ```
   mkdocs-plugin-name>=version
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Добавьте плагин в `mkdocs.yml`:
   ```yaml
   plugins:
     - search
     - plugin-name
   ```

### Изменение темы

Кастомные стили находятся в `docs/stylesheets/github-dark.css`. Основные элементы для настройки:

- **Цвета**: CSS переменные в `:root`
- **Навигация**: `.md-sidebar--primary`, `.md-sidebar--secondary`
- **Контент**: `.md-typeset`, `.md-content`
- **Код**: `.highlight`, `.md-code`

### Добавление custom JavaScript

Создайте файл `docs/javascripts/custom.js` и добавьте в `mkdocs.yml`:
```yaml
extra_javascript:
  - javascripts/custom.js
```

## Разработка

### Структура разработки

Рекомендуемый workflow:

1. Создайте новую ветку для изменений:
   ```bash
   git checkout -b feature/new-documentation
   ```

2. Внесите изменения в Markdown файлы или стили

3. Запустите локальный сервер для предварительного просмотра:
   ```bash
   mkdocs serve
   ```

4. Проверьте изменения в браузере

5. Создайте коммит и push:
   ```bash
   git add .
   git commit -m "Описание изменений"
   git push origin feature/new-documentation
   ```

### Pre-commit хуки (опционально)

Для автоматической проверки перед коммитом:

```bash
pip install pre-commit
pre-commit install
```

### Тестирование

Проверка корректности конфигурации:
```bash
mkdocs build --strict
```

Проверка всех ссылок:
```bash
mkdocs build --strict --verbose
```

## Деплой

### GitHub Pages

```bash
mkdocs gh-deploy
```

Автоматически:
- Собирает сайт
- Создает ветку `gh-pages`
- Публикует на GitHub Pages

### Ручной деплой

1. Соберите сайт:
   ```bash
   mkdocs build
   ```

2. Загрузите содержимое `site/` на веб-сервер

### Docker Production

Для production используйте отдельный Dockerfile с оптимизацией:

```dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdocs build

FROM nginx:alpine
COPY --from=builder /app/site /usr/share/nginx/html
EXPOSE 80
```

## Мониторинг и аналитика

### Google Analytics (опционально)

Добавьте в `mkdocs.yml`:
```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

### Метрики сайта

MkDocs Material поддерживает отслеживание:
- Просмотров страниц
- Поисковых запросов
- Времени на странице

## Часто задаваемые вопросы (FAQ)

**Q: Как изменить порт для локального сервера?**  
A: Используйте флаг `-a`:
```bash
mkdocs serve -a localhost:8080
```

**Q: Как добавить кастомный favicon?**  
A: Добавьте в `mkdocs.yml`:
```yaml
theme:
  favicon: images/favicon.ico
```

**Q: Как включить темную/светлую тему переключение?**  
A: Добавьте в `mkdocs.yml`:
```yaml
theme:
  palette:
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Переключить на темную тему
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Переключить на светлую тему
```

**Q: Поддерживает ли MkDocs i18n (мультиязычность)?**  
A: Да, используйте плагин `mkdocs-static-i18n`:
```bash
pip install mkdocs-static-i18n
```

## Ресурсы и ссылки

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [Mermaid Documentation](https://mermaid.js.org/)

## Changelog

### v1.0.0 (2025-01-XX)
- Первый релиз документации
- Темная тема GitHub Dark
- Унифицированная навигация
- Оптимизация производительности
- Instant navigation с prefetch

## Лицензия

Информация о лицензии доступна в репозитории проекта.

## Команда

CC_StdLib Team

## Контакты и поддержка

Для вопросов и предложений:
- Создайте Issue в репозитории
- Отправьте Pull Request с улучшениями
- Свяжитесь с командой разработки
