import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "4.uneven_skintone"
folder_name1 = "6.Red_eyes"


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
    def test_edit_background(self, extra):
        self.app.deeplink_to_background() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_background_before", wait_time=10) \
            .select_background_item(3) \
            .screenshot("test_edit_background_after", wait_time=10) \
            .compare_photo("test_edit_background_before", "test_edit_background_after", "test_edit_background_diff",
                           threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_background_save")
        extra.append(extras.image('screenshot/test_edit_background_diff.png'))
        extra.append(extras.image('savephoto/4_test_edit_background_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_background_user(self, extra):
        self.app.deeplink_to_background() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_background_user_before", wait_time=10) \
            .select_background_item(1) \
            .pick_photo(folder_name1, 1) \
            .screenshot("test_edit_background_user_after", wait_time=10) \
            .compare_photo("test_edit_background_user_before", "test_edit_background_user_after",
                           "test_edit_background_user_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_background_user_save")
        extra.append(extras.image('screenshot/test_edit_background_user_diff.png'))
        extra.append(extras.image('savephoto/4_test_edit_background_user_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_background_brush_eraser(self, extra):
        self.app.deeplink_to_background() \
            .pick_photo(folder_name, 1) \
            .select_background_item(3) \
            .screenshot("test_edit_background_brush-5_before", wait_time=10) \
            .click_brush() \
            .select_brush_size_5() \
            .tap_central() \
            .message("Brush-Brush size:5") \
            .screenshot("test_edit_background_brush-5_after", wait_time=10) \
            .click_eraser() \
            .select_brush_size_4() \
            .tap_central() \
            .message("Eraser-Brush size: 4") \
            .screenshot("test_edit_background_brush-5_eraser-4_after", wait_time=10) \
            .compare_photo("test_edit_background_brush-5_before", "test_edit_background_brush-5_after",
                           "test_edit_background_brush-5_diff", threshold=0) \
            .compare_photo("test_edit_background_brush-5_after", "test_edit_background_brush-5_eraser-4_after",
                           "test_edit_background_brush-5_eraser-4_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_background_brush-5_eraser-4_save")
        extra.append(extras.image('screenshot/test_edit_background_brush-5_eraser-4_diff.png'))
        extra.append(extras.image('screenshot/test_edit_background_brush-5_diff.png'))
        extra.append(extras.image('savephoto/4_test_edit_background_brush-5_eraser-4_save.jpg'))
    #
    # @pytest.mark.background
    # def test_edit_background_store(self, extra):
    #     self.app.deeplink_to_background() \
    #         .pick_photo(folder_name, 1) \
    #         .click_store()\
    #         .screenshot("test_edit_background_before", wait_time=10) \
    #         .
    #         .screenshot("test_edit_background_after", wait_time=10) \
    #         .compare_photo("test_edit_background_before", "test_edit_background_after", "test_edit_background_diff",
    #                        threshold=0.1) \
    #         .click_save() \
    #         .pull_photo_from_device("4_test_edit_background_store_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
