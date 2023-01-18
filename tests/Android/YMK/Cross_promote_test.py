import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "1.Makeup"


class Test(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_promote_timemachine(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_timemachine_ad() \
            .screenshot("test_edit_promote_timemachine_alert_dialog", wait_time=10) \
            .message("TimeMachine clicked, show dialog before entering!") \
            .click_continue_to_timemachine()
        self.app.screenshot("test_edit_promote_timemachine", wait_time=10)
        extra.append(extras.image('screenshot/test_edit_promote_timemachine.png'))
        extra.append(extras.image('screenshot/test_edit_promote_timemachine_alert_dialog.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_promote_videoedit(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_videoedit_ad() \
            .screenshot("test_edit_promote_VideoEdit_YCV", wait_time=10) \
            .message("VideoEdit AD button clicked, enter/install YCV!")
        extra.append(extras.image('screenshot/test_edit_promote_VideoEdit_YCV.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_promote_sticker(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_sticker_ad() \
            .screenshot("test_edit_promote_Sticker_YCP", wait_time=10) \
            .message("Sticker AD button clicked, enter/install YCP!")
        extra.append(extras.image('screenshot/test_edit_promote_Sticker_YCP.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_promote_frame(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_frame_ad() \
            .screenshot("test_edit_promote_Frame_YCP", wait_time=10) \
            .message("Frame AD button clicked, enter/install YCP!")
        extra.append(extras.image('screenshot/test_edit_promote_Frame_YCP.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_promote_nails(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_nails_ad() \
            .screenshot("test_edit_promote_Nails_YCN", wait_time=10) \
            .message("Nails AD button clicked, enter/install YCN!")
        extra.append(extras.image('screenshot/test_edit_promote_Nails_YCN.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
