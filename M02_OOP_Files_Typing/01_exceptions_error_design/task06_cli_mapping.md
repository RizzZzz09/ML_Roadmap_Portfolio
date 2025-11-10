# Task 06 — CLI/UX Mapping

| Исключение          | Сообщение для пользователя                 | Exit Code | Log Level |
|---------------------|--------------------------------------------|-----------|-----------|
| PaymentInvalidValue | Невозможно интерпретировать сумму оплаты.  | 2         | warning   |
| MinAmountViolation  | Сумма меньше минимально допустимой.        | 3         | error     |
| ConfigFileNotFound  | Файл конфигурации не найден.               | 2         | error     |
| ConfigInvalidJSON   | Файл конфигурации повреждён или невалиден. | 2         | error     |
| ConfigMissingField  | В конфигурации отсутствует требуемый ключ. | 2         | warning   |
| ConfigInvalidField  | Значение поля конфигурации некорректно.    | 2         | warning   |
