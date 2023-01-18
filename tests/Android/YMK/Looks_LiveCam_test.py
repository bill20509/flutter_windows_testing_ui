import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from libs.YMK.locators import ResultLocators, PhotoMakeupLocators, LauncherLocators, PickPhotoLocators, MakeupCamLocators
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

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_with_background(self, extra):
        self.app.deeplink_to_makeupcam() \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_no_effect") \
            .select_looks() \
            .select_look_category(" Background ") \
            .select_look_by_number(3) \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_look_with_background") \
            .select_looks() \
            .click_switch_button() \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_look_switch_background")
        extra.append(extras.image('savephoto/test_live_look_switch_background.jpg'))
        extra.append(extras.image('savephoto/test_live_look_with_background.jpg'))
        extra.append(extras.image('savephoto/test_live_no_effect.jpg'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_in_place_download(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .select_look_category(" Daily ") \
            .select_look_download_icon() \
            .screenshot("in_place_download_look") \
            .click_in_place_download_look() \
            .screenshot("apply_in_place_download_look")
        extra.append(extras.image('screenshot/apply_in_place_download_look.png'))
        extra.append(extras.image('screenshot/in_place_download_look.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_info(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .click_element_by_text("Alluring") \
            .screenshot("test_live_look_info_with_creator") \
            .wait_time() \
            .screenshot("test_live_look_info_hide_creator") \
            .click_info_button() \
            .screenshot("test_live_look_info_list") \
            .compose_gif("test_live_look_info", 'screenshot/test_live_look_info_with_creator.png'
                     , 'screenshot/test_live_look_info_hide_creator.png'
                     , 'screenshot/test_live_look_info_list.png', speed=1)
        extra.append(extras.image('screenshot/test_live_look_info.gif'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_live_look_info_item(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .select_look_by_number(1) \
            .click_info_button() \
            .click_element_by_text("View Profile") \
            .wait_time(3)\
            .screenshot("test_live_look_info_item_profile") \
            .click_keycode_back() \
            .click_element_by_text("Learn More About This Look") \
            .wait_time(3) \
            .screenshot("test_live_look_info_item_learn_more") \
            .click_keycode_back() \
            .click_element_by_text("Copy Link") \
            .wait_time(3) \
            .screenshot("test_live_look_info_item_copy_link") \
            .click_element_by_text("See More Looks") \
            .wait_time(3) \
            .screenshot("test_live_look_info_item_more_look") \
            .click_keycode_back()
        extra.append(extras.image('screenshot/test_live_look_info_item_more_look.png'))
        extra.append(extras.image('screenshot/test_live_look_info_item_copy_link.png'))
        extra.append(extras.image('screenshot/test_live_look_info_item_learn_more.png'))
        extra.append(extras.image('screenshot/test_live_look_info_item_profile.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_with_accessories(self, extra):
        self.app.deeplink_to_makeupcam() \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_no_effect") \
            .select_looks() \
            .click_premium_category() \
            .select_look_item("Baddie Love") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_look_3_accessories")
        extra.append(extras.image('savephoto/test_live_look_3_accessories.jpg'))
        extra.append(extras.image('savephoto/test_live_no_effect.jpg'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_with_reshape(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .select_look_category(" Celebrity ") \
            .screenshot("test_live_look_reshape_before") \
            .select_look_item("Becca Bowen") \
            .screenshot("test_live_look_reshape_after") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_look_reshape") \
            .click_detail() \
            .scroll_look_details() \
            .screenshot("test_live_look_reshape") \
            .compose_gif("test_live_look_reshape", 'screenshot/test_live_look_reshape_before.png'
                         , 'screenshot/test_live_look_reshape_after.png', speed=1)
        extra.append(extras.image('savephoto/test_live_look_reshape.jpg'))
        extra.append(extras.image('screenshot/test_live_look_reshape.gif'))
        extra.append(extras.image('screenshot/test_live_look_reshape.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_with_hair_color(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .click_premium_category() \
            .select_look_item("Baddie Love") \
            .click_compare() \
            .screenshot("test_live_look_with_hair_color") \
            .slide_compare_to_left() \
            .screenshot("test_live_look_with_hair_color_compare") \
            .click_capture() \
            .click_photo_save() \
            .click_reset() \
            .screenshot("test_live_look_with_hair_color_reset") \
            .screenshot("test_live_look_with_hair_color_reset_2") \
            .pull_photo_from_device("test_live_look_with_hair_color") \
            .compose_gif("test_live_look_with_hair_color_compare", 'screenshot/test_live_look_with_hair_color.png'
                         , 'screenshot/test_live_look_with_hair_color_compare.png', speed=1) \
            .compose_gif("test_live_look_with_hair_color_reset", 'screenshot/test_live_look_with_hair_color_reset.png'
                         , 'screenshot/test_live_look_with_hair_color_reset_2.png', speed=1)
        extra.append(extras.image('savephoto/test_live_look_with_hair_color.jpg'))
        extra.append(extras.image('screenshot/test_live_look_with_hair_color_reset.gif'))
        extra.append(extras.image('screenshot/test_live_look_with_hair_color_compare.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_look_favorite(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_looks() \
            .select_look_item("Alluring") \
            .add_look_to_favorite("Alluring") \
            .click_favorite_icon() \
            .screenshot("test_live_look_favorite_add") \
            .remove_look_from_favorite("Alluring") \
            .screenshot("test_live_look_favorite_remove")
        extra.append(extras.image('screenshot/test_live_look_favorite_add.png'))
        extra.append(extras.image('screenshot/test_live_look_favorite_remove.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_function_test(self, extra):
        self.app.deeplink_to_makeupcam() \
            .wait_time(2) \
            .screenshot("front_camera") \
            .click_switch_camera() \
            .wait_time(2) \
            .screenshot("rear_camera") \
            .click_switch_camera() \
            .wait_time(2) \
            .click_element_by_text("Alluring") \
            .wait_time(2) \
            .screenshot("test_live_look") \
            .wait_time(2) \
            .click_timer_mode() \
            .click_timer_mode() \
            .wait_time(2) \
            .click_capture_for_timer() \
            .screenshot("timer_3") \
            .wait_time(1) \
            .screenshot("timer_2") \
            .wait_time(1) \
            .screenshot("timer_1") \
            .check_rating_page() \
            .click_photo_save() \
            .wait_time(3) \
            .click_timer_mode() \
            .click_timer_mode() \
            .wait_time(2) \
            .screenshot("timer_off") \
            .wait_time(2)  \
            .click_reset() \
            .screenshot("test_live_makeup_SKU_reset") \
            .wait_time(2) \
            .screenshot("test_live_makeup_SKU_reset_2") \
            .slide_bar_to_down() \
            .wait_time(2) \
            .screenshot("Exposure_bar_0") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("Exposure_bar_100") \
            .compose_gif("timer_mode", 'screenshot/timer_off.png'
                         , 'screenshot/timer_3.png'
                         , 'screenshot/timer_2.png'
                         , 'screenshot/timer_1.png', speed=1) \
            .compose_gif("SKU_reset", 'screenshot/test_live_look.png'
                         , 'screenshot/test_live_makeup_SKU_reset.png'
                         , 'screenshot/test_live_makeup_SKU_reset_2.png', speed=1) \
            .compose_gif("switch_camera", 'screenshot/front_camera.png'
                         , 'screenshot/rear_camera.png', speed=1) \
            .compose_gif("Exposure_bar", 'screenshot/Exposure_bar_0.png'
                         , 'screenshot/front_camera.png'
                         , 'screenshot/Exposure_bar_100.png', speed=1)
        extra.append(extras.image('screenshot/Exposure_bar.gif'))
        extra.append(extras.image('screenshot/SKU_reset.gif'))
        extra.append(extras.image('screenshot/timer_mode.gif'))
        extra.append(extras.image('screenshot/switch_camera.gif'))


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_live_look_background()
    # t.teardown_method()