# Примеры синтаксиса IEC 61131-3 ST

Эта страница демонстрирует подсветку синтаксиса для языка Structured Text (ST) стандарта IEC 61131-3.

## Базовый функциональный блок

```iecst
FUNCTION_BLOCK FB_BasicSignal
VAR_INPUT
    Enable : BOOL;          // Разрешение работы блока
    HardwareInput : BOOL;   // Физический вход от датчика
END_VAR

VAR_OUTPUT
    Value : BOOL;           // Обработанное значение сигнала
    IsValid : BOOL;         // Признак корректности сигнала
    ErrorCode : INT;        // Код ошибки
END_VAR

VAR
    internalState : BOOL;
    counter : INT := 0;
    timer : TON;
END_VAR

// Основная логика
IF Enable THEN
    IF HardwareInput THEN
        internalState := TRUE;
        counter := counter + 1;
    ELSE
        internalState := FALSE;
    END_IF;

    Value := internalState;
    IsValid := TRUE;
    ErrorCode := 0;
ELSE
    Value := FALSE;
    IsValid := FALSE;
    ErrorCode := -1;
END_IF;

END_FUNCTION_BLOCK
```

## Управляющие конструкции

### IF-ELSIF-ELSE

```iecst
VAR
    temperature : REAL;
    mode : INT;
END_VAR

IF temperature < 10.0 THEN
    mode := 1;  (* Режим обогрева *)
ELSIF temperature > 30.0 THEN
    mode := 2;  (* Режим охлаждения *)
ELSE
    mode := 0;  (* Нормальный режим *)
END_IF;
```

### CASE

```iecst
VAR
    state : INT;
    output : BOOL;
END_VAR

CASE state OF
    0:  // Инициализация
        output := FALSE;

    1:  // Работа
        output := TRUE;

    2, 3:  // Ошибка или останов
        output := FALSE;

ELSE
    output := FALSE;
END_CASE;
```

### Циклы FOR, WHILE, REPEAT

```iecst
VAR
    i : INT;
    sum : DINT := 0;
    array : ARRAY[1..10] OF INT;
END_VAR

// Цикл FOR
FOR i := 1 TO 10 BY 1 DO
    sum := sum + array[i];
END_FOR;

// Цикл WHILE
i := 0;
WHILE i < 10 DO
    i := i + 1;
    IF i = 5 THEN
        EXIT;  // Выход из цикла
    END_IF;
END_WHILE;

// Цикл REPEAT
i := 0;
REPEAT
    i := i + 1;
UNTIL i >= 10
END_REPEAT;
```

## Типы данных

```iecst
VAR
    // Логические
    flag : BOOL := TRUE;

    // Целочисленные
    smallInt : SINT := -128;
    normalInt : INT := 1000;
    bigInt : DINT := 2147483647;
    hugeInt : LINT;

    // Беззнаковые целые
    byteVal : BYTE := 16#FF;
    wordVal : WORD := 16#ABCD;
    dwordVal : DWORD := 16#12345678;

    // Вещественные
    floatVal : REAL := 3.14159;
    doubleVal : LREAL := 2.718281828;

    // Временные типы
    timeDelay : TIME := T#5s;
    currentDate : DATE := D#2024-01-15;
    timeOfDay : TOD := TOD#12:30:45;
    timestamp : DT := DT#2024-01-15-12:30:45;

    // Строки
    message : STRING := 'Hello, World!';
    wideName : WSTRING := "Привет";
END_VAR
```

## Числовые литералы

```iecst
VAR
    // Десятичные
    decimal : INT := 1234;

    // Шестнадцатеричные
    hexValue : WORD := 16#CAFE;
    typedHex : INT := INT#16#FF;

    // Двоичные
    binaryValue : BYTE := 2#11010110;

    // Восьмеричные
    octalValue : WORD := 8#777;

    // Вещественные с экспонентой
    scientific : REAL := 1.23E-4;
    bigNumber : REAL := 5.67E+8;
END_VAR
```

## Функция с различными операторами

```iecst
FUNCTION CalculateAverage : REAL
VAR_INPUT
    values : ARRAY[1..100] OF REAL;
    count : INT;
END_VAR

VAR
    i : INT;
    sum : REAL := 0.0;
    result : REAL;
END_VAR

// Арифметические операторы: +, -, *, /, **
FOR i := 1 TO count DO
    sum := sum + values[i];
END_FOR;

result := sum / INT_TO_REAL(count);

// Сравнение: =, <>, <, >, <=, >=
IF result >= 0.0 AND result <= 100.0 THEN
    CalculateAverage := result;
ELSE
    CalculateAverage := 0.0;
END_IF;

END_FUNCTION
```

## Логические операции

```iecst
VAR
    sensor1, sensor2, sensor3 : BOOL;
    alarm : BOOL;
    enable : BOOL;
    output : BOOL;
END_VAR

// AND, OR, XOR, NOT
alarm := (sensor1 OR sensor2) AND NOT sensor3;

// Комбинированные условия
IF enable AND (sensor1 XOR sensor2) THEN
    output := TRUE;
ELSIF NOT enable OR (sensor1 AND sensor2 AND sensor3) THEN
    output := FALSE;
END_IF;
```

## Работа со структурами и указателями

```iecst
TYPE SensorData : STRUCT
    Temperature : REAL;
    Pressure : REAL;
    IsValid : BOOL;
    Timestamp : DT;
END_STRUCT
END_TYPE

VAR
    sensor : SensorData;
    pSensor : POINTER TO SensorData;
    refSensor : REFERENCE TO SensorData;
END_VAR

// Доступ к полям структуры
sensor.Temperature := 25.5;
sensor.Pressure := 101.3;
sensor.IsValid := TRUE;

// Работа с указателем
pSensor := ADR(sensor);
pSensor^.Temperature := 26.0;

// Обращение к элементам массива
VAR
    dataArray : ARRAY[1..10] OF INT;
    index : INT := 5;
END_VAR

dataArray[index] := 100;
```

## Системные переменные

```iecst
VAR
    // Системные переменные с префиксом %
    digitalInput : BOOL AT %IX0.0;      // Дискретный вход
    digitalOutput : BOOL AT %QX0.1;     // Дискретный выход
    analogInput : INT AT %IW2;          // Аналоговый вход
    analogOutput : INT AT %QW4;         // Аналоговый выход
    memoryFlag : BOOL AT %MX10.5;       // Флаг в памяти
END_VAR

digitalOutput := digitalInput;
analogOutput := analogInput;
```

## Комментарии

```iecst
// Однострочный комментарий

(*
   Многострочный комментарий
   может занимать несколько строк
*)

(*
    (* Вложенные комментарии
       также поддерживаются *)
*)

VAR
    value : INT;  // Комментарий в конце строки
END_VAR
```

## Программа с методом

```iecst
PROGRAM MainProgram
VAR
    fbSignal : FB_BasicSignal;
    sensor : BOOL;
    result : BOOL;
END_VAR

// Вызов функционального блока
fbSignal(
    Enable := TRUE,
    HardwareInput := sensor
);

result := fbSignal.Value;

// Вызов метода
IF result THEN
    ProcessData();
END_IF;

END_PROGRAM

METHOD ProcessData : BOOL
VAR
    localData : INT;
END_VAR

localData := 42;
ProcessData := TRUE;

END_METHOD
```

## ООП конструкции (CODESYS 3.5+)

```iecst
INTERFACE IControllable
    METHOD Start : BOOL
    METHOD Stop : BOOL
    METHOD GetStatus : INT
END_INTERFACE

CLASS Motor IMPLEMENTS IControllable
VAR PUBLIC
    Speed : REAL;
    IsRunning : BOOL;
END_VAR

VAR PRIVATE
    _internalState : INT;
END_VAR

METHOD PUBLIC Start : BOOL
    IsRunning := TRUE;
    _internalState := 1;
    Start := TRUE;
END_METHOD

METHOD PUBLIC Stop : BOOL
    IsRunning := FALSE;
    _internalState := 0;
    Stop := TRUE;
END_METHOD

METHOD PUBLIC GetStatus : INT
    GetStatus := _internalState;
END_METHOD

END_CLASS
```

## Перечисления и константы

```iecst
TYPE StateEnum :
(
    IDLE := 0,
    RUNNING := 1,
    ERROR := 2,
    STOPPED := 3
);
END_TYPE

VAR CONSTANT
    MAX_TEMPERATURE : REAL := 100.0;
    MIN_PRESSURE : REAL := 10.0;
    RETRY_COUNT : INT := 3;
END_VAR

VAR
    currentState : StateEnum := StateEnum.IDLE;
END_VAR

IF currentState = StateEnum.RUNNING THEN
    // Выполнение операций
END_IF;
```

---

**Примечание**: Для использования подсветки синтаксиса IEC ST укажите `iecst` в качестве языка блока кода:

    ```iecst
    // Ваш код здесь
    ```

Также поддерживаются альтернативные идентификаторы: `st`, `iec`, `structured-text`.
