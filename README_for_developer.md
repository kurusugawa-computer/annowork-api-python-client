# 開発者向けドキュメント


# 環境構築方法
VSCode devcontainerを使用します。

ホストで開発する場合は、uvとPython 3.12以降を用意して以下を実行します。

```bash
uv sync --locked --python 3.12
# IPythonも利用する場合
uv sync --locked --group dev
```

テスト・lint・ドキュメント用の依存関係は標準でインストールされます。
CIではPython 3.12〜3.15でテストします。
ローカルテストは `uv run pytest tests/test_local_*.py` で実行します。
依存関係を更新する場合は `uv lock --upgrade` を実行し、`uv.lock` をコミットしてください。

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
2. `make format` と `make lint` を実行する。


# Release
GitHubのReleasesからリリースしてください。
バージョンはSemantic Versioningに従います。
リリースすると、以下の状態になります。

* パッケージのバージョンは、uv-dynamic-versioning によりGitHubのバージョンタグから生成されます。`annoworkapi.__version__` はインストール済みパッケージのメタデータから取得します。
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







## シークレット検査

`make gitleaks` で現在のブランチの Git 履歴（マージ時の変更を含む）を検査します。gitleaks をインストール済みならそのコマンドを使い、未インストールなら Docker で v8.30.1 を実行します。検出値はログでマスクします。CI でも同じ検査を実行します。

コミット前の差分検査には pre-commit フックを利用できます。

```sh
uv sync --locked
uv run pre-commit install
```

Docker の接続先・認証設定は、通常利用している設定を引き継ぎます。設定ディレクトリを明示的に切り替える場合のみ、`GITLEAKS_DOCKER_CONFIG=/tmp/gitleaks-docker-config make gitleaks` のように指定してください。
