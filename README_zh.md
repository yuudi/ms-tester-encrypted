# ms-tester-encrypted

[English](./README.md) [简体中文](./README_zh.md) [русский](./README_ru.md)

## 介绍

复刻自[AutoApiSecret](https://github.com/wangziyingwen/AutoApiSecret)

使用 AES-256 加密 refresh_token

## 用法

1. 打开<https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade>，然后单击“新注册”。
1. 输入应用程序的名称，在`任何组织目录（任何 Azure AD 目录-Multitenant）和个人 Microsoft 帐户（例如 Skype，Xbox）`中选择帐户类型“帐户”，在“重定向 URI”中选择 `Web`，然后键入 `http://localhost:53682/`，然后点击注册。复制并保留应用名称下的“应用（客户端）ID”，以备后用。
1. 在“管理”下，选择“证书和机密”，然后单击“新客户机密”。复制并保留该秘密以供以后使用。
1. 在“管理”下，选择“API 权限”，单击“添加权限”，然后选择“ Microsoft Graph”，然后选择“授权权限”。
1. 搜索并选择以下权限：`Files.Read.All Files.ReadWrite.All Sites.Read.All Sites.ReadWrite.All User.Read.All User.ReadWrite.All Directory.Read.All Directory.ReadWrite.All Mail.Read Mail.ReadWrite MailboxSettings.Read MailboxSettings.ReadWrite`。选择后，点击底部的“添加权限”。
1. 在你的 Windows 电脑上下载[这个脚本](https://github.com/yuudi/ms-tester-encrypted/raw/v1.0/init.ps1)，右键选择`用 powershell 执行`，输入刚刚获得的 `client id` 和 `client secret`，按照提示完成授权，获得 `refresh_token`。（如果脚本被禁止，请以管理员身份打开 powershell 执行 `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`）
1. 单击<https://github.com/yuudi/ms-tester-encrypted/generate>，这将帮助您创建 github 仓库，公开或私人仓库均可。
1. 进入仓库设置，单击 `secrets`，单击 `New secret`，在 `Name` 中输入 `AES_KEY`，在 `Value` 中输入一个密码。（您无需记住它，使用随机字符串即可）
1. 重复上一步添加机密，Name 与 Value 分别为： `CLIENT_ID`->您的 client id，`CLIENT_SECRET`->您的 client secret，`REFRESH_TOKEN`->刚刚脚本获取的 refresh_token。
1. 转到仓库 actions，启用 actions 开始定时任务，您也可以单击 `Run workflow` 来手动触发它。
