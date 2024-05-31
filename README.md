# RU
> [!CAUTION]
> Защищено [MIT лиценизей](https://github.com/mbutskpy/mbutsks-reminder/blob/main/LICENSE)

## Что делает этот бот?
Если у Вас бывает такое, что Вы захотели что-то сделать, но не можете подойти к компьютеру, а когда можете, забываете, то этот бот для Вас.
Он пришлет Вам push-уведомление при включении

## Как добавить этого бота себе?
* Клонируйте репозиторий
* Пропишите в консоль `pip install -r requirements.txt`
* Зайдите в оффициальный бот Telegram [BotFather](https://t.me/BotFather). Отправьте ему команду `/newbot` и по инструкции от него создайте бота.
* Скопируйте API ключ, который BotFather отправил Вам.
* Через команду /mybots по желанию можно изменить бота
* Создайте файл config.py
* Напишите в него `TOKEN=""` в кавычки укажите Ваш токен
* В main.py в списке `allowed_id` впишите все идентификаторы пользователей, которые могут писать Вам напоминания
* Создайте .exe файл для `main.py` через pyinstaller, auto-py-to-exe или другой удобный Вам инструмент
* Добавьте этот .exe в авто загрузку
> [!NOTE]
> auto-py-to-exe имеет GUI интерфейс, а pyinstaller работает в консоли. Функционал полностью одинаковый. Выбор за Вами

> [!WARNING]
> Оставьте флаги `--windowed`, `--onefile` и `--hidden-import plyer.platforms.win.notification` в pyinstaller, либо для auto-py-to-exe нажмите кнопки `One file` и `Window Based`, также напишите `plyer.platforms.win.notification в pyinstaller` в `Advanced-"hiden-import"`. Это надо для правильной работы приложения. 
> Система Windows думает, что все приложения без консоли - вирусы. На момент создания exe файла выключите Windows Defender. Если Вы мне не доверяете, можете не выключать Windows Defender, но не ставьте флаг `--windowed` в pyinstaller, либо нажмите `Console Based` в auto-py-to exe, однако живите с этой проклятой консолькой :trollface: . Выбор за Вами

## Как пользоваться ботом?
* Напишите боту сообщение, которое он должен будет Вам отправить в качестве push-уведомления при включении компьютера
* Включите компьютер
* push-уведомление должно прийти Вам. В противном случае, вы сделали что-то не так



# EN
> [!CAUTION]
> Protected by [MIT licence](https://github.com/mbutskpy/mbutsks-reminder/blob/main/LICENSE)

## What does this bot do?
If you have a situation where you want to do something but can't get to your computer, and when you can, you forget, then this bot is for you.
It will send you a push notification when you switch it on

## How do I add this bot to myself?
* Clone the repository
* Write `pip install -r requirements.txt` into the terminal
* Go to the official Telegram bot [BotFather](https://t.me/BotFather). Send him the command /`newbot `and follow his instructions to create a bot.
* Copy the API key that BotFather sent you.
* Through the /mybots command, you can change the bot at will
* Create a config.py file
* Write `TOKEN=""` in it ` specify your token in quotes
* In main.py, in the `allowed_id` list, type all the IDs of users who can write reminders to you
* Create an .exe file for `main.py` via pyinstaller, auto-py-to-exe or another tool you are comfortable with
* Add this .exe to auto download
> [!NOTE]
> auto-py-to-exe has a GUI interface, while pyinstaller works in the console. The functionality is completely the same. The choice is yours

> [!WARNING]
> Leave the flags `--windowed`, `--onefile` and `--hidden-import plyer.platforms.win.notification` in pyinstaller, or for auto-py-to-exe, click the buttons `One file` и `Window Based`, also write `plyer.platforms.win.notification в pyinstaller` in `Advanced-"hiden-import"`. This is necessary for the application to work properly.
> The Windows system thinks that all applications without a console are viruses. Switch off Windows Defender at the time of creation .exe file. If you don't trust me, you can keep Windows Defender switched off, but don't tick the flag `--windowed` in pyinstaller, or press `Console Based` in auto-py-to exe, but live with the damn console :trollface: . The choice is yours

## How to use the bot?
* Write a message for the bot to send you as a push notification when you turn on your computer
* Switch on the computer
* push notification should come to you. Otherwise, you have done something wrong
