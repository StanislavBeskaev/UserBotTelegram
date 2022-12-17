# UserBot для Telegram
Позволяет расширять функционал Telegram и производить различные действия со своими сообщениями

## Реализованные команды
* .type: Команда для медленного набора текста. Использование: .type <Текст>. Текст будет отображаться с эффектом печатания.
* !cat: Команда для отправки котика
* !joke: Команда для отображения анекдота
* .hack: Команда для взлома пентагона(понарошку)
* .heart: Команда для рисования сердечка с указанным символом (по умолчанию *). Использование: .heart <Символ> - будет нарисовано сердечко из указанного символа, если символ не указан то будет использован символ *


# Обязательные Переменные окружения
 - TG_API_ID - id приложения в Telegram
 - TG_API_HASH - hash приложения в Telegram


# Дополнительные переменные окружения
 - TYPING_SYMBOL - символ который будет показан при печатании текста (команда .type)
 - TYPING_SYMBOL_INTERVAL - время (в секундах) в течении которого будет показан символ печатания


## Получение TG_API_ID и TG_API_HASH
 - Перейти по ссылке https://my.telegram.org/auth указать свой номер телефона, в Telegram придёт код. Авторизоваться.
 - Зайти в API development tools, заполнить необходимые поля ввода. Сохранить изменения.
 - TG_API_ID = значению в поле "App api_id"
 - TG_API_HASH = значению в поле "App api_hash"


## Добавление новой команды
В папке commands создать отдельный модуль с классом наследником от app.commands.base_command.BaseCommand. Добавить новую команды в README.
При запуске приложение само найден класс команды и будет использовать.
По аналогии с существующими командами реализовать функционал работы команды. Необходимо реализовать все абстрактные методы. 
Основной метод выполнения команды - execute