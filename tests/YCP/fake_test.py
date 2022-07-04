import pytest
import time


class Test(object):

    def setup_method(self):  # run before every test
        print('setup')

    def test_1(self):
        assert 1 == 2

    def test_2(self):
        assert 1 == 1

    def test_3(self):
        assert 1 == 1

    def teardown_method(self):  # quit driver when test case done
        time.sleep(1)
        print('quit')


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.teardown_method()
