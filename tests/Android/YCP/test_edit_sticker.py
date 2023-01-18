import pytest
from libs.app import App
from libs.YCP import pages
import time


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto()\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(5)\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)
        # self.app = pages.photo_edit.InstaFitPage(self.driver)
        # self.app.scr



    @pytest.mark.test
    def test_edit_sticker_mysticker_empty(self):
        #Sol
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_sticker()\
                .select_sticker_panel_item(0)\
                .screenshot("edit_sticker_mysticker_empty")

    @pytest.mark.test
    def test_edit_sticker_mysticker_add(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_sticker()\
            .select_sticker_panel_item(0)\
            .click_create_my_sticker()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_auto_cut() \
            .wait_progress_bar()\
            .click_apply()\
            .screenshot("edit_sticker_mysticker_add")


    @pytest.mark.test
    def test_edit_sticker_border(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_sticker() \
            .screenshot("edit_sticker_border_before") \
            .select_sticker_panel_item(1)\
            .select_sticker_panel_item(2)\
            .select_color_item(2)\
            .screenshot("edit_sticker_border_apply")\
            .compare_photo("edit_sticker_border_before", "edit_sticker_border_apply", "edit_sticker_border_apply_diff") \
            .click_apply()\
            .click_save()\
            .pull_photo_from_device("edit_sticker_border_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_sticker_mysticker_add()
    t.teardown_method()
