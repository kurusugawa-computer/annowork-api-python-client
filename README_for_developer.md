# 開発者向けドキュメント


# 環境構築方法
VSCode devcontainerを使用します。

## requirement
* ホスト側に以下の環境変数が設定されていること
    * `ANNOWORK_USER_ID`：AnnoworkにログインするときのユーザID
    * `ANNOWORK_PASSWORD`：Annoworkにログインするときのパスワード





# ソースコードの生成方法

## 環境
* Docker
    * OpenAPI Generator
* bash

## 事前準備
1. GitHubのアクセストークンを取得する。

## 作業手順
1. `generate/generate.sh --download --github_token ${GITHUB_TOKEN}`コマンドを実行して、pythonソースコードを生成する
2. バージョンを上げる
    * `annoworkcli/__version__.py`
    * `pyproject.toml`



# リリース
## 事前準備
以下のコマンドを実行する。ユーザ名とパスワードを求められたら、PyPIのユーザ名とパスワードを入力する。

```
$ make publish
```



## WebAPIドキュメントの閲覧方法
TODO

