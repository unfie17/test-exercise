# Документация API для сервиса BIN verifier

## Описание

Сервис предоставляет информацию о банковской карте по её BIN (Bank Identification Number). Сайт позволяет пользователям вводить BIN и получать соответствующие данные, хранящиеся в CSV файле. Если введенный BIN корректен и существует в базе, пользователь увидит информацию о карте. Если BIN неверный или неизвестный, будет отображено сообщение об ошибке.

## Эндпоинты

### 1. Проверка работоспособности сервера

**Метод:** `GET`

**URL:** `/ping`

**Ответ:**
```json
"pong" 
```

### 2. Получение информации по BIN

**Метод:** `POST`

**URL:** `/get-info`

**Тело запроса:**
```json
{
    "bin_number": "111100"
} 
```

**Ответ(успешный запрос):**
```json
{
    "data": {
        "bin": "111100",
        "brand": "PRIVATE LABEL",
        "type": "DEBIT",
        "category": "",
        "issuer": "",
        "alpha_2": "US",
        "alpha_3": "USA",
        "country": "United States",
        "latitude": "37.0902",
        "longitude": "-95.7129",
        "bank_phone": "",
        "bank_url": ""
    }
} 
```

**Ошибки:**

**400 Bad Request:**

Причина: Пустое тело запроса.

Ответ: `{"detail": "Empty request body"}`

Причина: Отсутствие поля bin_number в запросе.

Ответ: `{"detail": "No 'bin_number' field in request"}`

Причина: Поле bin_number не является строкой.

Ответ: `{"detail": "BIN number should be string"}`

Причина: Поле bin_number пустое.

Ответ: `{"detail": "BIN number can't be empty"}`

Причина: Поле bin_number содержит не только цифры.

Ответ: `{"detail": "BIN number should contain only digits"}`

Причина: Длина bin_number меньше 6 символов.

Ответ: `{"detail": "BIN number's length can't be less than 6"}`

Причина: Длина bin_number больше 8 символов.

Ответ: `{"detail": "BIN number's length can't be greater than 8"}`

**404 Not Found:**

Причина: Неизвестный BIN.

Ответ: `{"detail": "Unknown BIN"}`