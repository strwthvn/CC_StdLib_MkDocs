# Диаграмма: Механизмы и управление

<style>
.diagram-container {
    width: 100%;
    overflow-x: auto;
    background: #1e1e1e;
    border: 1px solid #3f3f46;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}

.mermaid {
    width: 100%;
    min-width: 600px;
}
</style>

## Иерархия механизмов и блоки управления

<div class="diagram-container">

```mermaid
---
config:
  theme: dark
  themeVariables:
    background: '#1e1e1e'
    primaryColor: '#3f3f46'
    primaryTextColor: '#e4e4e7'
    primaryBorderColor: '#71717a'
    lineColor: '#a1a1aa'
    secondaryColor: '#27272a'
    tertiaryColor: '#18181b'
    classText: '#e4e4e7'
---
classDiagram
direction TB
    class FB_AbstractMechanism {
        -BOOL _xPower
        +SetPower(BOOL)
        +GetPower() BOOL
    }
    
    class FB_Mechanism {
        +Start()
        +Stop()
    }
    
    class FB_MechanismWithFeedback {
        +BOOL ixFeedback
        -E_StateFeedback _uFeedbackState
        +GetFeedbackWithoutPower() BOOL
        +GetPowerAndFeedback() BOOL
        +GetPowerWithoutFeedback() BOOL
        +GetState() E_StateFeedback
        #UpdateState()
    }
    
    class E_StateFeedback {
        Inactive
        Active
        Error_NoFeedback
        Error_UnexpectedFeedback
    }
    
    class I_Control {
        +Start()
        +Stop()
    }
    
    class FB_BasicControl {
        +I_Control ControlInterface
        -BOOL _xConditionToStart
        -BOOL _xConditionToStop
        +SetConditionToStart(BOOL)
        +SetConditionToStop(BOOL)
        +Start(BOOL)
        +Stop(BOOL)
    }
    
    class FB_FrequencyControl {
        +REAL irMaxFrequency
        +REAL irStep
        +REAL qrCurrentFrequency
        +BOOL qxTargetReached
        -REAL _rSetFrequency
        -REAL _rCurrentFrequency
        -BOOL _xInitialized
        +Calculate(rStep : REAL, xPulse : BOOL, xConditionToProceed : BOOL)
        +SetFrequencyTarget(rFrequency : REAL)
        +SetFrequencyDirect(rFrequency : REAL)
        +GetCurrentFrequency() REAL
        +GetTargetFrequency() REAL
        +Reset()
        +Hold()
    }

    FB_AbstractMechanism <|-- FB_Mechanism
    FB_Mechanism <|-- FB_MechanismWithFeedback
    FB_MechanismWithFeedback o-- E_StateFeedback
    FB_BasicControl o-- I_Control
    FB_Mechanism ..|> I_Control : implements

    <<abstract>> FB_AbstractMechanism
    <<enumeration>> E_StateFeedback
    <<interface>> I_Control
```

</div>

## Описание компонентов

### Базовые механизмы
- **FB_AbstractMechanism**: Абстрактный базовый класс для всех механизмов
  - Управляет состоянием питания устройства
  - Предоставляет базовую функциональность включения/выключения

- **FB_Mechanism**: Базовая реализация механизма
  - Реализует интерфейс `I_Control`
  - Предоставляет методы `Start()` и `Stop()`
  - Наследует управление питанием от базового класса

- **FB_MechanismWithFeedback**: Механизм с диагностикой обратной связи
  - Расширяет базовый механизм функциями диагностики
  - Контролирует соответствие команды и фактического состояния
  - Определяет состояния ошибок (нет обратной связи, неожиданная обратная связь)

### Управление
- **I_Control**: Стандартный интерфейс управления
  - Унифицирует команды `Start()` и `Stop()` для всех устройств
  - Обеспечивает полиморфизм в системах управления

- **FB_BasicControl**: Базовое управление с условиями
  - Позволяет задавать условия для запуска и остановки
  - Реализует логику блокировок и разрешений

- **FB_FrequencyControl**: Управление частотными преобразователями
  - Плавное изменение частоты с заданным шагом
  - Контроль достижения целевой частоты
  - Функции удержания и сброса

### Перечисления
- **E_StateFeedback**: Состояния обратной связи механизмов
  - `Inactive`: Механизм неактивен
  - `Active`: Механизм работает нормально
  - `Error_NoFeedback`: Ошибка - нет обратной связи при команде запуска
  - `Error_UnexpectedFeedback`: Ошибка - есть обратная связь при команде остановки

## Принципы использования

### Наследование
Все механизмы наследуют базовую функциональность управления питанием и могут быть расширены специфичными возможностями.

### Интерфейсы
Единый интерфейс `I_Control` позволяет управлять различными типами механизмов одинаково.

### Диагностика
Механизмы с обратной связью автоматически контролируют корректность выполнения команд.

---

## Связанные разделы

### Базовые механизмы
- [FB_AbstractMechanism](../mechanism/FB_AbstractMechanism.md) - Абстрактный базовый класс
- [FB_Mechanism](../mechanism/FB_Mechanism.md) - Базовая реализация механизма  
- [FB_MechanismWithFeedback](../mechanism/FB_MechanismWithFeedback.md) - Механизм с диагностикой

### Управление
- [FB_BasicControl](../control/FB_BasicControl.md) - Базовое управление с условиями
- [FB_FrequencyControl](../control/FB_FrequencyControl.md) - Управление частотными преобразователями

### Сигналы для механизмов
- [FB_SignalWithFeedback](../signal/discrete/FB_SignalWithFeedback.md) - Контроль обратной связи
- [FB_SignalWithTrigger](../signal/discrete/FB_SignalWithTrigger.md) - Детекция команд управления

### Другие диаграммы
- [Обработка сигналов](signals-diagram.md){:target="_blank"}
- [Коммуникация](communication-diagram.md){:target="_blank"}
- [Полная диаграмма](../full-diagram.md){:target="_blank"}

### Навигация
[Обзор архитектуры](../diagram.md) | [Главная](../index.md)