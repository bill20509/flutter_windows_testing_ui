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

    @pytest.mark.camera
    def test_edit_template_apply_inplace(self): 
        # Riley 1.apply inplace item
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_template()\
                .screenshot("edit_template_apply_inplace_after",3)\
                .click_apply()\
                .screenshot("edit_template_apply_inplace_lobby",3)\
                .click_save()\
                .pull_photo_from_device("edit_template_apply_inplace_save")

    @pytest.mark.camera
    def test_edit_template_original_ratio(self): 
        # Riley 5.origin ratio
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_template()\
                .select_tab("Ratio")\
                .screenshot("edit_edit_template_original_ratio_before",3)\
                .select_ratio_item(0)\
                .screenshot("edit_edit_template_original_ratio_after",3)\
                .compare_photo("edit_edit_template_original_ratio_before", "edit_edit_template_original_ratio_after", "edit_edit_template_original_ratio_diff")\
                .click_apply()\
                .click_save()\
                .pull_photo_from_device("edit_edit_template_original_ratio_save")

    @pytest.mark.camera
    def test_edit_template_different_ratio(self): 
        # Riley 6.different ratio
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_template()\
                .select_tab("Ratio")\
                .screenshot("edit_template_different_ratio_before",3)\
                .select_ratio_item(3)\
                .screenshot("edit_template_different_ratio_after",3)\
                .compare_photo("edit_template_different_ratio_before", "edit_template_different_ratio_after", "edit_template_different_ratio_diff")\
                .click_apply()\
                .click_save()\
                .pull_photo_from_device("edit_template_different_ratio_save")

    @pytest.mark.camera
    def test_edit_template_change_dialog_popup(self): 
        # Riley 52.change dialog popup
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_template()\
                .select_tab("Background")\
                .select_background_item(3)\
                .click_apply()\
                .screenshot("edit_template_change_dialog_popup",3)\



    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_template_change_dialog_popup()
    t.teardown_method()
