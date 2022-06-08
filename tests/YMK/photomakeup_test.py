import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time


class TestPhotoMakeup(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YMK")\
            .create()

        self.app = YMKbase(self.driver)

    # def setup_method(self):  # run before every test
    #     # 設定device
    #     self.driver = App().set_udid("31001bb317ad43e3")\
    #         .set_platform("Android")\
    #         .set_version("6")\
    #         .set_app("YMK")\
    #         .create()
    #
    #     self.app = YMKbase(self.driver)

    @pytest.mark.YMK
    def test_case(self):
        self.app.deeplink_to_lipart().pick_photo("YouCam Makeup Sample", 4) \
            .select_texture(1).wait_loading()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
