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
    def test_edit_instafit_ratio(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_instafit()\
            .screenshot("edit_instafit_ratio_before") \
            .select_ratio_item(4) \
            .screenshot("edit_instafit_ratio_apply")\
            .compare_photo("edit_instafit_ratio_before", "edit_instafit_ratio_apply", "edit_instafit_ratio_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_instafit_ratio_save")


    @pytest.mark.test
    def test_edit_instafit_color_apply(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .click_instafit()\
            .screenshot("edit_instafit_color_before")\
            .select_tab("Color") \
            .select_color_item(2) \
            .screenshot("edit_instafit_color_apply")\
            .compare_photo("edit_instafit_color_before", "edit_instafit_color_apply", "edit_instafit_color_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_instafit_color_save")

    @pytest.mark.test
    def test_edit_instafit_color_add_favorite(self):
        # Sol
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_edit") \
            .select_photo_item(1) \
            .click_instafit() \
            .select_tab("Color") \
            .screenshot("edit_instafit_color_add_favorite_before") \
            .select_color_item(2) \
            .long_press_element(3) \
            .screenshot("edit_instafit_color_add_favorite_apply") \
            .compare_photo("edit_instafit_color_add_favorite_before", "edit_instafit_color_add_favorite_apply", "edit_instafit_color_add_favorite_applydiff") \


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_instafit_color_apply()
    t.teardown_method()
