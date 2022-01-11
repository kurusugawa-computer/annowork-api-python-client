import logging


def pytest_addoption(parser):
    parser.addoption("--print_log_annoworkapi", action="store_true", default=False, help="annoworkapiモジュールのログを表示する。")


def pytest_cmdline_main(config):
    if config.getoption("--print_log_annoworkapi"):
        logging_formatter = "%(levelname)s : %(asctime)s : %(name)s : %(funcName)s : %(message)s"
        logging.basicConfig(format=logging_formatter)
        logging.getLogger("annoworkapi").setLevel(level=logging.DEBUG)
