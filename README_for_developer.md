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


# Release
GitHubのReleasesからリリースしてください。
バージョンはSemantic Versioningに従います。
リリースすると、以下の状態になります。

* ソース内のバージョン情報（`pyproject.toml`, `__version__.py`）は、https://github.com/mtkennerly/poetry-dynamic-versioning でGitHubのバージョンタグから生成されます。
* 自動でPyPIに公開されます。


# 開発フロー
* mainブランチを元にしてブランチを作成して、プルリクを作成してください。mainブランチへの直接pushすることはGitHub上で禁止しています。




# Document
### ドキュメントの作成
`$ make docs` コマンドを実行すると、`docs/_build/html/`にHTMLファイルが生成されます。

### ドキュメントの修正
`docs/*.rst`ファイルを修正してください。rstファイルは[Sphinx](https://www.sphinx-doc.org/en/master/)でビルドしています。

### ドキュメントのホスティング
ドキュメントは、https://readthedocs.org/ にホスティングしています。
masterブランチにプッシュすると、[ReadTheDocsのドキュメント](https://annowork-api-python-client.readthedocs.io/)が自動的に更新されます。

ReadTheDocsに通知するタイミングは、[GitHubのwebhook設定画面](https://github.com/kurusugawa-computer/annowork-api-python-client/settings/hooks)で設定してください。
ドキュメント生成元のブランチは、[ReadTheDocsの管理画面](https://readthedocs.org/dashboard/annowork-api-python-client/advanced/)で設定してください。

ReadTheDocsのビルド結果は https://readthedocs.org/projects/annowork-api-python-client/builds/ で確認できます。
メンテナンスする場合は、事前に管理者から招待してもらってください。






