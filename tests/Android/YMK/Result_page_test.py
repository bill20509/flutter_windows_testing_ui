import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from libs.YMK.locators import ResultLocators
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
    @pytest.mark.S2
    def test_edit_result_to_ycp(self, extra):
        try:
            self.app.deeplink_to_photomakeup() \
                .pick_photo(folder_name, 1) \
                .waiting_cursor() \
                .click_save() \
                .pull_photo_from_device("1_test_edit_result_to_ycp_SavedPhoto") \
                .show_result_page() \
                .find_ycp_card() \
                .click_to_ycp() \
                .message("Clicked CREATE button, enter YCP!") \
                .ycp_permission_allow() \
                .ycp_bipa_agree() \
                .screenshot("test_edit_result_to_ycp", wait_time=5) \
                .message("Check if photo is carried over!")
            extra.append(extras.image('screenshot/test_edit_result_to_ycp.png'))
            extra.append(extras.image('savephoto/1_test_edit_result_to_ycp_SavedPhoto.jpg'))
        except (ValueError, Exception):
            self.app.screenshot("test_edit_result_to_ycp_NotInstalled", wait_time=5) \
                .message("YCP not installed!") \
                .wait_element_visible(ResultLocators.create_with_ycp) \
                .click_element(ResultLocators.create_with_ycp) \
                .wait_element_invisible(ResultLocators.result_page_view) \
                .screenshot("test_edit_result_to_ycp_NotInstalled_LeaveApp", wait_time=5) \
                .message("Open app panel!") \
                .wait_element_visible(ResultLocators.open_with_panel) \
                .click_element_by_name(ResultLocators.open_with_app, "Google Play Store") \
                .wait_element_invisible(ResultLocators.open_with_panel) \
                .screenshot("test_edit_result_to_ycp_NotInstalled_PlayStore", wait_time=5) \
                .message("Enter Play Store!") \
                .compose_gif("test_edit_result_to_ycp_Installation",
                             "screenshot/test_edit_result_to_ycp_NotInstalled.png",
                             "screenshot/test_edit_result_to_ycp_NotInstalled_LeaveApp.png",
                             "screenshot/test_edit_result_to_ycp_NotInstalled_PlayStore.png", speed=1) \
                .message("GIF order = NotInstalled + LeaveApp + Playstore")
            extra.append(extras.image('screenshot/test_edit_result_to_ycp_Installation.gif'))
            #  Proceed to store if exception happens.

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_result_to_ycn(self, extra):
        try:
            self.app.deeplink_to_photomakeup() \
                .pick_photo(folder_name, 1) \
                .waiting_cursor() \
                .click_save() \
                .show_result_page() \
                .find_ycn_card() \
                .click_to_ycn() \
                .message("Clicked CREATE button, enter YCN!") \
                .screenshot("test_edit_result_to_ycn", wait_time=5) \
                .message("Check if YCN is launched!")
            extra.append(extras.image('screenshot/test_edit_result_to_ycn.png'))
        except (ValueError, Exception):
            self.app.screenshot("test_edit_result_to_ycn_NotInstalled", wait_time=5) \
                .message("YCN not installed!") \
                .wait_element_visible(ResultLocators.create_with_ycn) \
                .click_element(ResultLocators.create_with_ycn) \
                .wait_element_invisible(ResultLocators.result_page_view) \
                .screenshot("test_edit_result_to_ycn_NotInstalled_LeaveApp", wait_time=5) \
                .message("Open app panel!") \
                .wait_element_visible(ResultLocators.open_with_panel) \
                .click_element_by_name(ResultLocators.open_with_app, "Google Play Store") \
                .wait_element_invisible(ResultLocators.open_with_panel) \
                .screenshot("test_edit_result_to_ycn_NotInstalled_PlayStore", wait_time=5) \
                .message("Enter Play Store!") \
                .compose_gif("test_edit_result_to_ycn_Installation",
                             "screenshot/test_edit_result_to_ycn_NotInstalled.png",
                             "screenshot/test_edit_result_to_ycn_NotInstalled_LeaveApp.png",
                             "screenshot/test_edit_result_to_ycn_NotInstalled_PlayStore.png", speed=1) \
                .message("GIF order = NotInstalled + LeaveApp + Playstore")
            extra.append(extras.image('screenshot/test_edit_result_to_ycn_Installation.gif'))
            #  Proceed to store if exception happens.

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_result_collage(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_save() \
            .show_result_page() \
            .find_collage_card() \
            .click_to_collage() \
            .screenshot("test_edit_result_collage_page", wait_time=5) \
            .click_collage_share() \
            .message("Clicked SHARE to insure collage is saved!") \
            .pull_photo_from_device("1_test_edit_result_collage_SavedCollage")
        extra.append(extras.image('savephoto/1_test_edit_result_collage_SavedCollage.jpg'))
        extra.append(extras.image('screenshot/test_edit_result_collage_page.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
