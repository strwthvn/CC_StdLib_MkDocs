# Запуск CC_StdLib Documentation в Docker

Этот документ содержит инструкции по запуску документации CC_StdLib в Docker контейнере в среде WSL.

## Предварительные требования

- Docker установлен и запущен в WSL
- Docker Compose установлен
- Git для клонирования репозитория

## Быстрый запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/strwthvn/CC_StdLib_MkDocs.git
cd CC_StdLib_MkDocs
```

### 2. Запуск с помощью Docker Compose (рекомендуется)

```bash
docker-compose up -d
```

Это запустит контейнер в фоновом режиме. Сайт будет доступен по адресу: `http://localhost:8000`

### 3. Альтернативный запуск через Docker

```bash
# Сборка образа
docker build -t cc-stdlib-docs .

# Запуск контейнера
docker run -d -p 8000:8000 -v $(pwd):/app --name cc-stdlib-docs cc-stdlib-docs
```

## Управление контейнером

### Просмотр логов
```bash
docker-compose logs -f
```

### Остановка контейнера
```bash
docker-compose down
```

### Перезапуск контейнера
```bash
docker-compose restart
```

### Остановка и удаление контейнера
```bash
docker-compose down -v
```

## Разработка

При использовании Docker Compose с volume mapping, все изменения в файлах документации будут автоматически отображаться на сайте благодаря функции live reload MkDocs.

### Редактирование документации
1. Отредактируйте файлы `.md` в папке `docs/`
2. Сохраните изменения
3. Обновите страницу в браузере - изменения появятся автоматически

## Доступ к сайту

После успешного запуска, документация будет доступна по адресу:
- **Локально**: http://localhost:8000
- **В сети WSL**: http://[WSL-IP]:8000

Чтобы узнать IP адрес WSL, выполните в WSL:
```bash
ip addr show eth0
```

## Устранение неполадок

### Порт уже занят
Если порт 8000 уже используется, измените порт в `docker-compose.yml`:
```yaml
ports:
  - "8080:8000"  # Использовать порт 8080 вместо 8000
```

### Проблемы с правами доступа
Если возникают проблемы с правами доступа к файлам:
```bash
sudo chown -R $USER:$USER .
```

### Контейнер не запускается
Проверьте логи:
```bash
docker-compose logs
```

Убедитесь, что Docker запущен:
```bash
docker --version
docker-compose --version
```

## Структура проекта

```
CC_StdLib_MkDocs/
├── docs/                 # Документация в формате Markdown
├── src/                  # Дополнительные ресурсы
├── mkdocs.yml           # Конфигурация MkDocs
├── requirements.txt     # Python зависимости
├── Dockerfile          # Конфигурация Docker образа
├── docker-compose.yml  # Конфигурация Docker Compose
├── .dockerignore       # Исключения для Docker
└── DOCKER_SETUP.md     # Эта инструкция
```

## Дополнительные команды

### Вход в контейнер для отладки
```bash
docker-compose exec mkdocs bash
```

### Принудительная пересборка образа
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Очистка Docker ресурсов
```bash
# Остановка всех контейнеров
docker stop $(docker ps -aq)

# Удаление неиспользуемых образов
docker image prune -f

# Полная очистка системы Docker
docker system prune -af
```