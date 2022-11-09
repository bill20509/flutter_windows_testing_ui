import pytest
import time


class Test(object):

    def setup_method(self):  # run before every test
        print('setup')

    @pytest.mark.fake
    def test_1(self):
        assert 1 == 2

    @pytest.mark.fake
    def test_2(self):
        assert 1 == 1

    @pytest.mark.fake
    def test_3(self):
        assert 1 == 1

    @pytest.mark.fake
    def test_4(self):
        assert 1 == 3

    def test_5(self):
        assert 1 == 3

    def test_6(self):
        assert 1 == 3

    def test_7(self):
        assert 1 == 3

    def test_8(self):
        assert 1 == 3

    def test_9(self):
        assert 1 == 3

    def test_10(self):
        assert 1 == 3

    def test_11(self):
        assert 1 == 3

    def test_12(self):
        assert 1 == 3

    def test_13(self):
        assert 1 == 3

    def test_14(self):
        assert 1 == 3

    def test_15(self):
        assert 1 == 3

    def test_16(self):
        assert 1 == 3

    def test_17(self):
        assert 1 == 3

    def test_18(self):
        assert 1 == 3

    def test_19(self):
        assert 1 == 3

    def test_20(self):
        assert 1 == 3

    def test_21(self):
        assert 1 == 3

    def test_22(self):
        assert 1 == 3

    def teardown_method(self):  # quit driver when test case don
        print('quit')


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.teardown_method()
