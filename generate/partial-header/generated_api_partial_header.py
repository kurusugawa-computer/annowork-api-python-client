# ruff: noqa: E501, ANN401

"""
AbstractAnnoworkApiのヘッダ部分

Note:
    このファイルはopenapi-generatorで自動生成される。詳細は generate/README.mdを参照
"""

import abc
import annoworkapi
import warnings
from typing import Any, Optional, Union
import requests


class AbstractAnnoworkApi(abc.ABC):
    """
    AnnoworkApiクラスの抽象クラス
    """

    @abc.abstractmethod
    def _request_wrapper(
        self,
        http_method: str,
        url_path: str,
        *,
        query_params: Optional[dict[str, Any]] = None,
        header_params: Optional[dict[str, Any]] = None,
        request_body: Optional[Any] = None,
        log_response_with_error: bool = True,
    ) -> Any:
        pass
