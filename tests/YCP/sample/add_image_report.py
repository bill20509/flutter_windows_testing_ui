import pytest
from pytest_html import extras


class Test(object):

    def setup_method(self):  # run before every test
        pass

    @pytest.mark.camera
    def test_1(self, extra):
        assert 1 == 1
        print('this is message')
        extra.append(extras.image('screenshot/1.jpg'))
        extra.append(extras.image('screenshot/2.jpg'))
        extra.append(extras.image('screenshot/3.jpg'))

    def teardown_method(self):  # quit driver when test case done
        pass


if __name__ == "__main__":
    pass
