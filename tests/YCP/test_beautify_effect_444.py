import pytest
from libs.app import App
from libs.YCP import pages
import time


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto()\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(10)\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)
        """breakpoint()"""

    @pytest.mark.test
    def test_beautify_effects_apply(self):
        """Carl 444 test_beautify_effects_original_apply"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_beautify")\
            .select_photo_item(0)\
            .click_beautify_tab() \
            .screenshot("beautify_effects_original_apply_before", wait_time=3)\
            .click_effects()\
            .click_apply() \
            .screenshot("beautify_effects_original_apply_after", wait_time=3)\
            .compare_photo("beautify_effects_original_apply_before", "beautify_effects_original_apply_after", "beautify_effects_original_apply_diff")

    @pytest.mark.test
    def test_beautify_effects_animation_forbid(self):
        """Carl 468 469 test_beautify_effects_animation_forbid_preview, test_beaufify_effects_animation_preview"""
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_beautify") \
            .select_photo_item(0) \
            .click_beautify_tab() \
            .click_effects() \
            .click_animation_tab() \
            .select_animation_category("Sparkle") \
            .select_animation_item(1) \
            .select_animation_item(3) \
            .screenshot("beautify_effects_animation_forbid_before", wait_time=3) \
            .click_forbidden() \
            .screenshot("beautify_effects_animation_forbid_after", wait_time=3) \
            .compare_photo("beautify_effects_animation_forbid_before", "beautify_effects_animation_forbid_after",
                           "beautify_effects_animation_forbid_diff") \
            .click_apply() \
            .screenshot("beautify_effects_appply_to_lobby", wait_time=3)


    @pytest.mark.test
    def test_beautify_effects_animation_sparkle_config(self):
        """Carl 470 test_beaufify_effects_animation_sparkle_config"""
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_beautify") \
            .select_photo_item(0) \
            .click_beautify_tab() \
            .click_effects() \
            .click_animation_tab() \
            .select_animation_category("Sparkle") \
            .select_animation_item(3) \
            .select_animation_item(2) \
            .set_feature_value("Quantity", 100) \
            .set_feature_value("Size", 100) \
            .set_feature_value("Opacity", 100) \
            .set_feature_value("Random", 100) \
            .screenshot("beautify_effects_animation_sparkle_config", wait_time=1) \
            .click_apply()


    @pytest.mark.test
    def test_beautify_effects_animation_speed(self):
        """Carl 471 test_beaufify_effects_animation_speed"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_beautify")\
            .select_photo_item(0)\
            .click_beautify_tab() \
            .click_effects()\
            .click_animation_tab()\
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .screenshot("beautify_effects_animation_hot01_speed_x1", wait_time=3) \
            .set_speed_bar(0.5) \
            .screenshot("beautify_effects_animation_hot01_speed_x0.5", wait_time=3) \
            .set_speed_bar(2) \
            .screenshot("beautify_effects_animation_hot01_speed_x2", wait_time=3)


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_beautify_effects_apply()
    t.teardown_method()
