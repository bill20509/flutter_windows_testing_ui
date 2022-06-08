import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
# py.test --capture=no YMK_Test.py


class TestYMK(object):

    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YMK")\
            .create()

        self.app = YMKbase(self.driver)

    @pytest.mark.test
    def test_function(self):
        self.app.deeplink_to_facepaint()\
            .pick_photo("YouCam Makeup", 1)\
            .screenshot("test_edit_lipcolor_intensity_before", 3)\
            .select_pattern(3)\
            .screenshot("test_edit_lipcolor_intensity_after", 3)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
