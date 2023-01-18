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
    def test_edit_animation_effects_preview(self):
        """Carl 799 test_edit_animation_effects_preview"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .select_animation_category("Sparkle") \
            .select_animation_item(3) \
            .wait_progress_bar()\
            .screenshot("edit_animation_effects_preview", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_effects_speed_preview(self):
        """Carl 801 test_edit_animation_effects_speed_preview"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .wait_progress_bar() \
            .screenshot("edit_animation_effects_speed_preview_x1", wait_time=3) \
            .set_speed_bar(0.5) \
            .screenshot("edit_animation_effects_speed_preview_x0.5", wait_time=3) \
            .set_speed_bar(2) \
            .screenshot("edit_animation_effects_speed_preview_x2", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_stickers_tab(self):
        """Carl 817 test_edit_animation_stickers_tab"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .wait_progress_bar() \
            .click_stickers_tab()\
            .screenshot("edit_animation_effects_to_stickers_tab", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_stickers_preview(self):
        """Carl 823 test_edit_animation_stickers_preview"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .click_stickers_tab() \
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .wait_progress_bar() \
            .screenshot("edit_animation_stickers_preview", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_stickers_speed_preview(self):
        """Carl 824 test_edit_animation_stickers_speed_preview"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .click_stickers_tab() \
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .wait_progress_bar() \
            .screenshot("edit_animation_stickers_speed_preview_x1", wait_time=3) \
            .select_animation_item(1) \
            .wait_progress_bar() \
            .set_speed_bar(0.5) \
            .screenshot("edit_animation_stickers_speed_preview_x0.5", wait_time=3) \
            .select_animation_item(4) \
            .wait_progress_bar() \
            .set_speed_bar(2) \
            .screenshot("edit_animation_stickers_speed_preview_x2", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_stickers_to_effects_tab(self):
        """Carl 843 test_edit_animation_stickers_to_effects_tab"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_animation()\
            .click_stickers_tab() \
            .select_animation_category("Hot") \
            .select_animation_item(0) \
            .wait_progress_bar() \
            .click_effects_tab()\
            .screenshot("edit_animation_stickers_to_effects_tab", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_wraparounds_forbidden(self):
        """Carl 851 test_edit_animation_wraparounds_forbidden"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_animation()\
            .click_wraparounds_tab()\
            .screenshot("edit_animation_wraparounds_forbidden", wait_time=3)

    @pytest.mark.test
    def test_edit_animation_wraparounds_no_person(self):
        """Carl 853 test_edit_animation_wraparounds_no_person"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_animation()\
            .click_wraparounds_tab()\
            .screenshot("edit_animation_wraparounds_no_person", wait_time=3)


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_animation_wraparounds_forbidden()
    t.teardown_method()
