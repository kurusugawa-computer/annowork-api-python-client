"""
resource.pyのテストコード
"""

import os

import pytest

from annoworkapi.exceptions import CredentialsNotFoundError
from annoworkapi.resource import Resource, build, build_from_env

# プロジェクトトップに移動する
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../")


class Test__build_from_env:
    def test_環境変数の認証情報を元にインスタンスが作成される(self):
        os.environ["ANNOWORK_USER_ID"] = "FOO"
        os.environ["ANNOWORK_PASSWORD"] = "BAR"
        actual = build_from_env()
        assert isinstance(actual, Resource)

    def test_環境変数に認証情報がない場合はCredentialsNotFoundErrorが発生する(self):
        os.environ.pop("ANNOWORK_USER_ID", None)
        os.environ.pop("ANNOWORK_PASSWORD", None)
        with pytest.raises(CredentialsNotFoundError):
            build_from_env()


# `.netrc`ファイルを事前に準備するのが難しいので、テストしない
# class Test__build_from_netrc:
#     pass


class Test__build:
    def test_引数に認証情報を指定する(self):
        actual = build(login_user_id="FOO", login_password="BAR")
        assert isinstance(actual, Resource)

    def test_引数にユーザーIDのみ指定するとValueErrorが発生する(self):
        with pytest.raises(ValueError):
            build(login_user_id="FOO")

    def test_引数にパスワードのみ指定するとValueErrorが発生する(self):
        with pytest.raises(ValueError):
            build(login_password="FOO")

    def test_引数に認証情報を指定しないと環境変数から認証情報を読み込む(self):
        os.environ["ANNOWORK_USER_ID"] = "FOO"
        os.environ["ANNOWORK_PASSWORD"] = "BAR"
        actual = build()
        assert isinstance(actual, Resource)
