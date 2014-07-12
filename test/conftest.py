import pytest

@pytest.fixture()
def callback_mock():
    import mock
    return mock.Mock()
