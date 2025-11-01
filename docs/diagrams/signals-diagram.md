# Диаграмма: Обработка сигналов

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
    min-width: 800px;
}
</style>

## Дискретные и аналоговые сигналы

<div class="diagram-container">

```mermaid
---
config:
  theme: dark
  themeVariables:
    background: '#0d1117'
    primaryColor: '#161b22'
    primaryTextColor: '#e6edf3'
    primaryBorderColor: '#30363d'
    lineColor: '#58a6ff'
    secondaryColor: '#21262d'
    tertiaryColor: '#161b22'
    classText: '#e6edf3'
    cScale0: '#21262d'
    cScale1: '#21262d'
    cScale2: '#21262d'
---
classDiagram
direction TB
    class FB_BasicSignal {
        +BOOL ixSignal
        +GetSignal() BOOL
        +GetInvertedSignal() BOOL
    }
    
    class FB_SignalWithTrigger {
        -R_TRIG _rt_xSignal
        -F_TRIG _ft_xSignal
        +GetRtrig() BOOL
        +GetFtrig() BOOL
    }
    
    class FB_SignalWithFeedback {
        +BOOL ixFeedback
        -FB_SignalWithTrigger _inputSignalTrigger
        -BOOL _xWaitingFeedback
        -BOOL _xFeedbackReceived
        +GetReceivedFeedback() BOOL
        +GetWaitingFeedback() BOOL
        +ResetReceivedFeedback()
        +ResetWaitingFeedback()
    }
    
    class FB_SignalWithFeedbackTimer {
        +TIME tFeedbackTimeout
        -TON _ton_FeedbackTimeout
        -BOOL _xFeedbackTimeout
        +GetFeedbackTimeout() BOOL
        +GetElapsedTime() TIME
        +IsTimerRunning() BOOL
        +ResetFeedbackTimeout()
        +Reset()
    }
    
    class FB_SignalWithRattling {
        -TIME _tStabilityTime
        -UINT _nMaxTransitions
        -TIME _tDetectionWindow
        -TON _ton_StabilityFilter
        -BOOL _xOutSignal
        -BOOL _xRattlingDetected
        +GetProcessedSignal() BOOL
        +GetRattlingDetected() BOOL
        +GetTransitionCount() UINT
        +IsDetectionActive() BOOL
        +ResetRattlingError()
        +Reset()
    }
    
    class FB_BasicAnalogSignal {
        +REAL irRawValue
        -REAL _rProcessedValue
        -REAL _rMinValue
        -REAL _rMaxValue
        -BOOL _xOutOfRange
        +GetRawValue() REAL
        +GetProcessedValue() REAL
        +IsOutOfRange() BOOL
        +GetMinValue() REAL
        +GetMaxValue() REAL
        +SetRange(rMinValue : REAL, rMaxValue : REAL)
        +IsInRange(rValue : REAL) BOOL
        +ClampToRange(rValue : REAL) REAL
        +Reset()
        +ProcessRawValue()*
        #ValidateRange()
        #SetProcessedValue(rValue : REAL)
    }
    
    class FB_AnalogSignal4_20mA {
        +REAL rScaleMin
        +REAL rScaleMax
        +BOOL xEnableRangeProtection
        -REAL _rCurrentMin
        -REAL _rCurrentMax
        -BOOL _xUnderrange
        -BOOL _xOverrange
        -BOOL _xWireBreak
        -BOOL _xOverload
        +ProcessRawValue()
        +GetScaledValue() REAL
        +GetPercentValue() REAL
        +IsWireBreak() BOOL
        +IsOverload() BOOL
        +IsUnderrange() BOOL
        +IsOverrange() BOOL
        +HasError() BOOL
        +SetScaleRange(rMin : REAL, rMax : REAL)
        +Reset()
    }
    
    class FB_UniversalAnalogSignal {
        +REAL rInputMin
        +REAL rInputMax
        +REAL rScaleMin
        +REAL rScaleMax
        +BOOL xEnableRangeProtection
        +BOOL xEnableDiagnostics
        +ProcessRawValue()
        +GetScaledValue() REAL
        +GetNormalizedValue() REAL
        +GetPercentValue() REAL
        +IsUnderrange() BOOL
        +IsOverrange() BOOL
        +HasError() BOOL
        +SetInputRange(rMin : REAL, rMax : REAL)
        +SetScaleRange(rMin : REAL, rMax : REAL)
        +Reset()
    }
    
    class FB_NumericChangeDetector {
        +REAL irValue
        +BOOL qxChangeDetected
        -REAL _rPreviousValue
        -BOOL _xFirstCycle
        +GetCurrentValue() REAL
        +GetPreviousValue() REAL
        +GetValueDifference() REAL
        +IsValueIncreased() BOOL
        +IsValueDecreased() BOOL
        +Reset()
    }
    
    class FB_RangeDiagnostic_LH {
        +REAL irValue
        +REAL irSetpointL
        +REAL irSetpointLL
        +REAL irSetpointH
        +REAL irSetpointHH
        +BOOL ixEnable
        +REAL irHysteresis
        +E_AlarmSetpoints quAlarmCode
        +BOOL qxAlarmActive
        +BOOL qxWarningActive
        +BOOL qxCriticalActive
        +GetAlarmCode() E_AlarmSetpoints
        +IsNormal() BOOL
        +IsLowAlarm() BOOL
        +IsHighAlarm() BOOL
        +Reset()
    }
    
    class E_AlarmSetpoints {
        Normal
        L
        H
        LL
        HH
    }

    FB_BasicSignal <|-- FB_SignalWithTrigger
    FB_BasicSignal <|-- FB_SignalWithFeedback
    FB_SignalWithFeedback <|-- FB_SignalWithFeedbackTimer
    FB_BasicSignal <|-- FB_SignalWithRattling
    FB_BasicAnalogSignal <|-- FB_AnalogSignal4_20mA
    FB_BasicAnalogSignal <|-- FB_UniversalAnalogSignal
    FB_SignalWithFeedback o-- FB_SignalWithTrigger
    FB_RangeDiagnostic_LH o-- E_AlarmSetpoints

    <<abstract>> FB_BasicAnalogSignal
    <<enumeration>> E_AlarmSetpoints
```

</div>

## Описание компонентов

### Дискретные сигналы
- **FB_BasicSignal**: Базовый функциональный блок для работы с булевыми сигналами
- **FB_SignalWithTrigger**: Расширяет базовый сигнал детекцией фронтов (R_TRIG, F_TRIG)
- **FB_SignalWithFeedback**: Добавляет контроль обратной связи к базовому сигналу
- **FB_SignalWithFeedbackTimer**: Расширяет обратную связь таймаутом ожидания
- **FB_SignalWithRattling**: Фильтрация дребезга контактов с настраиваемыми параметрами

### Аналоговые сигналы
- **FB_BasicAnalogSignal**: Абстрактный базовый класс для обработки аналоговых сигналов
- **FB_AnalogSignal4_20mA**: Специализированный блок для токовой петли 4-20мА с диагностикой
- **FB_UniversalAnalogSignal**: Универсальный блок для различных типов аналоговых входов

### Диагностика сигналов
- **FB_NumericChangeDetector**: Обнаружение и анализ изменений числовых значений
- **FB_RangeDiagnostic_LH**: Четырехуровневая система контроля параметров (L, LL, H, HH)
- **E_AlarmSetpoints**: Перечисление уровней аварий и предупреждений

---

## Связанные разделы

### Дискретные сигналы
- [FB_BasicSignal](../signal/discrete/FB_BasicSignal.md) - Базовый дискретный сигнал
- [FB_SignalWithFeedback](../signal/discrete/FB_SignalWithFeedback.md) - Контроль обратной связи
- [FB_SignalWithFeedbackTimer](../signal/discrete/FB_SignalWithFeedbackTimer.md) - Таймаут обратной связи

### Аналоговые сигналы  
- [FB_BasicAnalogSignal](../signal/analog/FB_BasicAnalogSignal.md) - Базовый аналоговый сигнал
- [FB_AnalogSignal4_20mA](../signal/analog/FB_AnalogSignal4_20mA.md) - Токовая петля 4-20мА
- [FB_UniversalAnalogSignal](../signal/analog/FB_UniversalAnalogSignal.md) - Универсальный аналоговый вход

### Диагностика
- [FB_NumericChangeDetector](../signal/analog/FB_NumericChangeDetector.md) - Детекция изменений значений
- [FB_RangeDiagnostic_LH](../signal/analog/FB_RangeDiagnostic_LH.md) - Контроль уставок

### Другие диаграммы
- [Механизмы и управление](mechanisms-diagram.md){:target="_blank"}
- [Коммуникация](communication-diagram.md){:target="_blank"}
- [Полная диаграмма](../full-diagram.md){:target="_blank"}

### Навигация
[Обзор архитектуры](../diagram.md) | [Главная](../index.md)