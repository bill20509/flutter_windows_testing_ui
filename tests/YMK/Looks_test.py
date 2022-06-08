import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time


class TestLooks(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YMK")\
            .create()

        self.app = YMKbase(self.driver)

    @pytest.mark.looks
    def test_edit_looks(self):
        self.app.deeplink_to_photomakeup()\
            .pick_photo("YouCam Makeup Sample", 2)\
            .select_looks()\
            .select_look("Alluring")\
            .long_press_look("Alluring")\
            # .add_to_favorite("Alluring")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
