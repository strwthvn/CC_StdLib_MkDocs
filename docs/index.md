# Библиотека CC_StdLib

## Обзор

CC_StdLib - это стандартная библиотека функциональных блоков для программирования в IEC 61131-3 Structured Text. Библиотека разработана специально для использования в среде разработки **CODESYS 3.5** и предоставляет готовые компоненты для создания систем промышленной автоматизации.

## Структура библиотеки

```
CC_StdLib/
├── Сигналы (Signal)
│   ├── Дискретные сигналы
│   │   ├── FB_BasicSignal - Базовый дискретный сигнал
│   │   ├── FB_SignalWithFeedback - Сигнал с обратной связью
│   │   ├── FB_SignalWithFeedbackTimer - Сигнал с таймером обратной связи
│   │   ├── FB_SignalWithRattling - Сигнал с антидребезгом
│   │   ├── FB_SignalWithTrigger - Сигнал с триггером
│   │   └── FB_FrequencyControl - Управление частотой
│   └── Аналоговые сигналы
│       ├── FB_BasicAnalogSignal - Базовый аналоговый сигнал
│       ├── FB_AnalogSignal4_20mA - Токовая петля 4-20мА
│       ├── FB_UniversalAnalogSignal - Универсальный аналоговый вход
│       ├── FB_NumericChangeDetector - Детектор изменений
│       └── FB_RangeDiagnostic_LH - Диагностика диапазона
│
├── Механизмы (Mechanism)
│   ├── FB_AbstractMechanism - Абстрактный базовый класс
│   ├── FB_Mechanism - Основной механизм
│   └── FB_MechanismWithFeedback - Механизм с обратной связью
│
├── Управление (Control)
│   ├── FB_BasicControl - Базовое управление с условиями
│   └── FB_FrequencyControl - Плавное управление частотой
│
└── Коммуникация (Communication)
    ├── U_ByteToWord - Преобразование BYTE ↔ WORD
    ├── U_RealToWord - Преобразование REAL ↔ WORD
    ├── FC_SwapBytesInWord - Смена порядка байтов
    ├── FC_SwapBytesInWordArray - Смена байтов в массиве
    └── FC_SwapWordArrayElements - Смена элементов массива
```