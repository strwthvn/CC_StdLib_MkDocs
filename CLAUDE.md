# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a MkDocs-based documentation site for CC_StdLib, a library of IEC 61131-3 Structured Text functional blocks for CODESYS 3.5 industrial automation systems. The documentation is written in Russian and covers discrete/analog signals, mechanisms, and control systems.

## Essential Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start development server with hot-reload (recommended)
mkdocs serve

# Access at http://127.0.0.1:8000
```

### Docker Development
```bash
# Start with Docker Compose (recommended)
docker-compose up

# Stop Docker Compose
docker-compose down

# Build and run manually
docker build -t cc-stdlib-docs .
docker run -p 8000:8000 -v $(pwd):/app cc-stdlib-docs
```

### Building and Testing
```bash
# Build static site (output in site/)
mkdocs build

# Build with strict mode (fails on warnings, useful for validation)
mkdocs build --strict

# Build with verbose output (useful for link checking)
mkdocs build --strict --verbose
```

### Deployment
```bash
# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Project Architecture

### MkDocs Configuration Flow

The site build process follows this pipeline:
1. **Source**: Markdown files in `docs/` directory
2. **Processing**: MkDocs engine applies Material theme + plugins (Mermaid, search)
3. **Extensions**: PyMdown Extensions add syntax highlighting and Markdown features
4. **Output**: Static HTML/CSS/JS in `site/` directory

Key configuration in `mkdocs.yml:1-97`:
- Theme: Material for MkDocs with slate (dark) color scheme
- Language: Russian (`ru`)
- Navigation features: instant loading, prefetch, tabs, progress indicator
- Plugins: Russian search, Mermaid diagrams

### Navigation System

The site uses a hierarchical navigation structure defined in `mkdocs.yml:38-63`:
- **Главная** → Main landing page
- **Сигналы** (Signals) → Discrete and analog signal functional blocks
- **Механизмы** (Mechanisms) → Abstract and concrete mechanism implementations
- **Управление** (Control) → Control system functional blocks
- **Коммуникация** → Data conversion utilities

Navigation features enable:
- **Instant navigation**: AJAX page loading without full refresh
- **Prefetch**: Pre-loads pages on hover for faster transitions
- **URL tracking**: Auto-updates URL during scroll

### Custom Styling

The project uses a custom GitHub Dark theme in `docs/stylesheets/github-dark.css`.

Key customizations:
- GitHub-inspired dark color palette with CSS variables
- Left sidebar (`.md-sidebar--primary`): Main navigation, width ~12.1rem + 70px
- Right sidebar (`.md-sidebar--secondary`): Page table of contents with sticky header
- Nested navigation with 12px indentation per level
- Fade-in animations (0.2-0.25s) for smooth transitions

Important: The CSS file contains extensive styling that maintains consistency. When modifying styles, preserve the variable-based color system defined in `:root`.

### Documentation Structure

Each functional block follows this template:
```markdown
# [Block Name]

## Обзор (Overview)
### Назначение (Purpose)
### Основные возможности (Key Features)

## Интерфейс (Interface)
### Входные параметры (Input Parameters)
### Выходные параметры (Output Parameters)

## Логика работы (Logic)
### Описание алгоритма (Algorithm Description)
### Диаграммы (Diagrams - using Mermaid)

## Примеры использования (Usage Examples)
### Базовый пример (Basic Example)
### Расширенный пример (Advanced Example)

## Примечания (Notes)
```

## Adding New Documentation

1. Create `.md` file in appropriate `docs/` subdirectory:
   - `docs/signal/discrete/` - Discrete signals
   - `docs/signal/analog/` - Analog signals
   - `docs/mechanism/` - Mechanisms
   - `docs/control/` - Control systems

2. Add entry to navigation in `mkdocs.yml:38-63` under the appropriate section

3. Use Mermaid for diagrams:
   ````markdown
   ```mermaid
   graph TD
       A[Start] --> B[Process]
   ```
   ````

4. Preview changes with `mkdocs serve` before committing

## Content Language

All documentation content is in **Russian**. When adding or modifying documentation:
- Use Russian for all text content
- Technical terms may remain in English (e.g., "CODESYS", "IEC 61131-3")
- Code examples use Structured Text (IEC ST) syntax
- Comments in code examples should be in Russian

## Markdown Extensions

Available features (configured in `mkdocs.yml:66-86`):
- **Code blocks**: Syntax highlighting with line numbers
- **Mermaid diagrams**: Use `mermaid` code fence
- **Admonitions**: Note/warning/info boxes
- **Tables**: Standard Markdown tables
- **Tabbed content**: Multi-tab content blocks
- **Code annotations**: Inline code comments

## Performance Considerations

The site implements several optimizations:
- **Instant navigation**: Reduces full page reloads
- **Prefetch**: Pre-loads pages on link hover
- **Progress indicator**: Shows loading state for better UX
- **Lazy loading**: Mermaid diagrams render on display

When adding large diagrams or images, consider:
- Using Mermaid over static images when possible
- Optimizing image sizes before adding
- Testing page load times with `mkdocs serve`

## Docker Workflow

The Docker setup mounts the current directory into the container, enabling hot-reload during development. Changes to markdown files or configuration are immediately reflected without rebuilding the container.

For production deployment, consider using a multi-stage build with nginx (see README.md:512-525 for example).

## Common Issues

**Navigation links showing purple flash**: Fixed via `:visited` and `:active` styles in github-dark.css

**Long navigation labels truncated**: Sidebar width is already increased; use shorter labels if possible

**Styles not applying**: Verify `extra_css` path in mkdocs.yml points to `stylesheets/github-dark.css`

**Search not working in Russian**: Search plugin is configured with `lang: ru` in mkdocs.yml:91

## Dependencies

Core dependencies in `requirements.txt`:
- `mkdocs` >= 1.5.0
- `mkdocs-material` >= 9.0.0
- `pymdown-extensions` >= 10.0.0
- `mkdocs-mermaid2-plugin` >= 1.0.0
- `mkdocs-git-revision-date-localized-plugin` >= 1.2.0

When updating dependencies, test thoroughly with `mkdocs build --strict` to catch breaking changes.
