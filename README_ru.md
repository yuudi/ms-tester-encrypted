# ms-tester-encrypted

[English](./README.md) [简体中文](./README_zh.md) [русский](./README_ru.md)

## Инструкция

разветвлен из [AutoApiSecret](https://github.com/wangziyingwen/AutoApiSecret)

зашифровать refresh_token с помощью aes-256

## Применение

1. Откройте <https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade> и нажмите «Новая регистрация».
1. Введите имя для своего приложения, выберите тип учетной записи «Учетные записи в любом каталоге организации (любой каталог Azure AD - Multitenant) и личные учетные записи Microsoft (например, Skype, Xbox)», выберите «Интернет» в «URI перенаправления», затем введите `http://localhost:53682/` и нажмите Зарегистрироваться. Скопируйте и сохраните идентификатор приложения (клиента) под именем приложения для дальнейшего использования.
1. В разделе «Управление» выберите «Сертификаты и секреты», нажмите «Новый секрет клиента». Скопируйте и сохраните этот секрет для дальнейшего использования.
1. В разделе «управление» выберите «Разрешения API», нажмите «Добавить разрешение» и выберите «Microsoft Graph», затем выберите «делегированные разрешения».
1. Найдите и выберите следующие разрешения: `Files.Read.All Files.ReadWrite.All Sites.Read.All Sites.ReadWrite.All User.Read.All User.ReadWrite.All Directory.Read.All Directory.ReadWrite.All Mail.Read Mail.ReadWrite MailboxSettings.Read MailboxSettings.ReadWrite`. После выбора нажмите «Добавить разрешения» внизу.
1. Загрузите [этот скрипт](https://github.com/yuudi/ms-tester-encrypted/raw/v1.0/init.ps1) на свой компьютер с Windows и запустите его, введите свой идентификатор клиента и секрет клиента, следуйте инструкциям. (если сценарий запрещен, выполнить в PowerShell от имени администратора `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`)
1. Щелкните <https://github.com/yuudi/ms-tester-encrypted/generate>, это поможет вам создать репозитории github.
1. Перейдите в настройки репозитория, нажмите `secrets`, нажмите `New secret`, введите `AES_KEY` в `Name`, введите любой пароль в `Value`. (запоминать не нужно, просто используйте случайную строку)
1. Повторите предыдущий шаг, добавьте `CLIENT_ID` -> ваш идентификатор клиента, `CLIENT_SECRET` -> секрет вашего клиента, `REFRESH_TOKEN` -> refresh_token, который мы получили только что.
1. Заходим в `actions` репозитория, включаем `actions`. Вы можете нажать `Run workflow`, чтобы запустить его вручную.
