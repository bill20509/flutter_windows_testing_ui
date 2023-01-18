import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
from pytest_html import extras


class Test(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S2
    def test_delete_photo(self, extra):
        self.app.deeplink_to_launcher() \
            .click_photomakeup_button()\
            .pick_album("YouCam Makeup")\
            .screenshot("test_delete_photo_before", 3)\
            .delete_photos() \
            .waiting_cursor()\
            .screenshot("test_delete_photo_after", 3)
        extra.append(extras.image('screenshot/test_delete_photo_after.png'))
        extra.append(extras.image('screenshot/test_delete_photo_before.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_ycv_video(self, extra):
        self.app.deeplink_to_makeupcam() \
            .switch_to_video_mode()\
            .click_record()\
            .click_stop()\
            .click_video_save()\
            .click_home()\
            .click_photomakeup_button()\
            .pick_album("YouCam Makeup")\
            .screenshot("test_ycv_video_before", 3)\
            .pick_photo()\
            .screenshot("test_ycv_video_after", 3)
        extra.append(extras.image('screenshot/test_ycv_video_after.png'))
        extra.append(extras.image('screenshot/test_ycv_video_before.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
