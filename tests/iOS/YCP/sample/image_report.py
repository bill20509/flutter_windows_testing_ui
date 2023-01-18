import pytest
from pytest_html import extras


def test_1(extra):
    assert 1 == 1
    print('this is message')
    extra.append(extras.image('screenshot/1.jpg'))
    extra.append(extras.image('screenshot/2.jpg'))
    extra.append(extras.image('screenshot/3.jpg'))
