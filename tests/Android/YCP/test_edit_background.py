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
    def test_edit_add_background_highlight(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_background() \
            .click_add_background()\
            .screenshot("edit_add_background_center")


    @pytest.mark.test
    def test_edit_add_background_inplace(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_background() \
            .click_add_background()\
            .screenshot("edit_add_background_inplace_before")\
            .select_background_item(2) \
            .screenshot("edit_add_background_inplace_apply")\
            .compare_photo("edit_add_background_inplace_before", "edit_add_background_inplace_apply", "edit_add_background_inplace_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_add_background_own_photo_blur(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background()\
            .screenshot("edit_add_background_own_photo_blur_before")\
            .select_background_item(0) \
            .select_album_item("a_edit")\
            .select_photo_item(0)\
            .set_slider_bar(15)\
            .screenshot("edit_add_background_own_photo_blur_apply")\
            .compare_photo("edit_add_background_own_photo_blur_before", "edit_add_background_own_photo_blur_apply", "edit_add_background_own_photo_blur_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_add_background_ratio_apply(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background()\
            .screenshot("edit_change_background_inplace_before")\
            .select_tab('Ratio') \
            .select_ratio_item(2) \
            .select_ratio_item(4) \
            .screenshot("edit_add_background_ratio_apply")\
            .compare_photo("edit_add_background_ratio_before", "edit_add_background_ratio_apply", "edit_add_background_ratio_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_add_background_color_apply(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background() \
            .screenshot("edit_add_background_color_before") \
            .select_tab("Color") \
            .select_color_item(2) \
            .screenshot("edit_add_background_color_apply") \
            .compare_photo("edit_add_background_color_before", "edit_add_background_color_apply", "edit_add_background_color_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_color_save")


    @pytest.mark.test
    def test_edit_add_background_color_table_apply(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background() \
            .screenshot("edit_add_background_color_table_before") \
            .select_tab('Color') \
            .select_color_item(0) \
            .click_apply() \
            .screenshot("edit_add_background_color_table_apply") \
            .compare_photo("edit_add_background_color_table_before", "edit_add_background_color_table_apply",
                           "edit_add_background_color_table_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_color_table_save")


    def test_edit_add_background_color_table_favorite(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background() \
            .select_tab('Color') \
            .screenshot("edit_add_background_color_table_favorite_before") \
            .select_tool_item(0) \
            .click_add_color()\
            .screenshot("edit_add_background_color_table_favorite_apply") \
            .compare_photo("edit_add_background_color_table_favorite_before", "edit_add_background_color_table_favorite_apply",
                           "edit_add_background_color_table_favorite_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_color_table_favorite_save")


    @pytest.mark.test
    def test_edit_add_background_one_highlight(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_add_background() \
            .screenshot("edit_add_background_highlight_background") \
            .select_tab('Color') \
            .screenshot("edit_add_background_highlight_color") \



    @pytest.mark.test
    def test_edit_change_background_in_place(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(1)\
            .click_background() \
            .click_change_background()\
            .screenshot("edit_change_background_own_photo_before")\
            .select_background_item(2) \
            .screenshot("edit_change_background_own_photo_apply")\
            .compare_photo("edit_change_background_own_photo_before", "edit_change_background_own_photo_apply", "edit_change_background_own_photo_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_change_background_own_photo(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background()\
            .click_change_background()\
            .screenshot("edit_change_background_own_photo_before")\
            .select_background_item(1) \
            .select_album_item("a_edit") \
            .select_photo_item(0) \
            .screenshot("edit_change_background_own_photo_apply")\
            .compare_photo("edit_change_background_own_photo_before", "edit_change_background_own_photo_apply", "edit_change_background_own_photo_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_change_background_none(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background()\
            .click_change_background()\
            .screenshot("edit_change_background_none_before")\
            .click_forbidden() \
            .screenshot("edit_change_background_none_apply")\
            .compare_photo("edit_change_background_none_before", "edit_change_background_none_apply", "edit_change_background_none_apply_diff") \



    @pytest.mark.test
    def test_edit_change_background_feather(self):
        # Sol
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_edit") \
            .select_photo_item(3) \
            .click_background() \
            .click_change_background() \
            .screenshot("edit_change_background_feature_before") \
            .click_config_icon() \
            .click_feather()\
            .set_slider_bar(100) \
            .unfold_panel_button() \
            .screenshot("edit_change_background_feature_apply") \
            .compare_photo("edit_change_background_feature_before", "edit_change_background_feature_apply",
                          "edit_change_background_feature_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")


    @pytest.mark.test
    def test_edit_change_background_blur(self):
        # Sol
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_edit") \
            .select_photo_item(3) \
            .click_background() \
            .click_change_background() \
            .screenshot("edit_change_background_blur_before") \
            .click_config_icon() \
            .click_blur()\
            .set_slider_bar(100) \
            .unfold_panel_button() \
            .screenshot("edit_change_background_blur_apply") \
            .compare_photo("edit_change_background_blur_before", "edit_change_background_blur_apply",
                           "edit_change_background_blur_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_add_background_inplace_save")

    @pytest.mark.test
    def test_edit_change_background_color_list(self):
        # Sol
        self.app.deeplink_to_launcher() \
            .click_photo_edit() \
            .select_album_item("a_edit") \
            .select_photo_item(3) \
            .click_background() \
            .click_change_background() \
            .screenshot("edit_change_background_color_list_before") \
            .select_tab('Color') \
            .select_color_item(2) \
            .screenshot("edit_change_background_color_list_apply") \
            .compare_photo("edit_change_background_color_list_before", "edit_change_background_color_list_apply",
                           "edit_change_background_color_list_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_change_background_color_list_save")

    @pytest.mark.test
    def test_edit_change_background_one_highlight(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(3)\
            .click_background() \
            .click_change_background() \
            .screenshot("edit_add_background_highlight_background") \
            .select_tab('Color') \
            .screenshot("edit_add_background_highlight_color") \



    def teardown_method(self):  # quit driver when test case done
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_add_background_color_table_favorite()
    t.teardown_method()
