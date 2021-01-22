# ms-tester-encrypted

[English](./README.md) [简体中文](./README_zh.md) [русский](./README_ru.md)

## Intruction

forked from [AutoApiSecret](https://github.com/wangziyingwen/AutoApiSecret)

encrypt refresh_token with aes-256

## Usage

1. Open <https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade> and then click `New registration`.
1. Enter a name for your app, choose account type `Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)`, select `Web` in `Redirect URI`, then type `http://localhost:53682/` and click Register. Copy and keep the `Application (client) ID` under the app name for later use.
1. Under `manage` select `Certificates & secrets`, click `New client secret`. Copy and keep that secret for later use.
1. Under `manage` select `API permissions`, click `Add a permission` and select `Microsoft Graph` then select `delegated permissions`.
1. Search and select the following permissions: `Files.Read.All Files.ReadWrite.All Sites.Read.All Sites.ReadWrite.All User.Read.All User.ReadWrite.All Directory.Read.All Directory.ReadWrite.All Mail.Read Mail.ReadWrite MailboxSettings.Read MailboxSettings.ReadWrite`. Once selected click `Add permissions` at the bottom.
1. Download [this script](https://github.com/yuudi/ms-tester-encrypted/raw/v1.0/init.ps1) on your Windows computer and run it, enter your `client id` and `client secret`, and follow the instruction. (if the script is forbidden, execute in powershell as administrator `Start-Process -Wait -Verb RunAs powershell.exe -Args "-executionpolicy bypass -command Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`)
1. Click <https://github.com/yuudi/ms-tester-encrypted/generate>, this will help you create a github repositories.
1. Go to repositories settings, click `secrets`, click `New secret`, enter `AES_KEY` in `Name`, enter any password in `Value`. (you don't need to remember it, just use a random string)
1. Repeat the previous step, add `CLIENT_ID` -> your client id, `CLIENT_SECRET` -> your client secret, `REFRESH_TOKEN` -> the refresh_token we get just now.
1. Go to repositories actions, enable the actions, and enjoy the tester, you can click `Run workflow` to manual trigger it.
