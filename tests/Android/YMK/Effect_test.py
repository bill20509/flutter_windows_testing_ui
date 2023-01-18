import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "1.Makeup"


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
    @pytest.mark.S1
    def test_edit_effect(self, extra):
        self.app.deeplink_to_effect() \
            .pick_photo(folder_name, 1) \
            .select_collection(2) \
            .select_effect(1) \
            .message("Effect selected!") \
            .adjust_intensity_to_down() \
            .screenshot("test_edit_effect_0", wait_time=5) \
            .message("Intensity set = 0") \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_effect_100", wait_time=5) \
            .message("Intensity set = 100") \
            .compare_photo("test_edit_effect_0", "test_edit_effect_100",
                           "test_edit_effect_0to100_diff", threshold=0) \
            .click_save() \
            .message("Photo saved!") \
            .pull_photo_from_device("1_test_edit_effect_100_save") \
            .compose_gif("test_edit_effect_compare",
                         "screenshot/test_edit_effect_0.png",
                         "screenshot/test_edit_effect_100.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_effect_compare.gif'))
        extra.append(extras.image('savephoto/1_test_edit_effect_100_save.jpg'))

    # @pytest.mark.effect
    # def test_edit_effect_store(self, extra):
    #     self.app.deeplink_to_effect() \
    #         .pick_photo(folder_name, 1) \
    #         .click_store() \
    #         .click_summer_pack() \
    #         .click_effect_pack_download() \
    #         .screenshot("test_edit_effect_intensity_100", wait_time=5) \
    #         .adjust_intensity_to_down() \
    #         .screenshot("test_edit_effect_intensity_0", wait_time=5) \
    #         .compare_photo("test_edit_effect_intensity_100", "test_edit_effect_intensity_0",
    #                        "test_edit_effect_intensity_100to0_diff", threshold=0) \
    #         .click_save() \
    #         .pull_photo_from_device("1_test_edit_effect_intensity_0_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
