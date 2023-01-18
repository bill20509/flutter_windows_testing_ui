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
    def test_edit_frame_download_apply_single(self): 
        # Riley 1.apply inplace item (improve when have time)
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_frame()\
                .scroll_frame_list()\
                .scroll_frame_list()\
                .scroll_frame_list()\
                .scroll_frame_list()\
                .scroll_frame_list()\
                .select_single_frame_item(0)\
                .select_single_frame_item(0)\
                .screenshot("edit_frame_download_apply_single_after",3)\
                .click_apply()\
                .screenshot("edit_frame_download_apply_single_lobby",3)\
                .click_save()\
                .pull_photo_from_device("edit_frame_download_apply_single_save")


    @pytest.mark.camera
    def test_edit_frame_watermark_removal(self): 
        # Riley 2.remove watermark
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_frame()\
                .select_frame_item("Spring")\
                .select_frame_item("Spring 01")\
                .screenshot("edit_frame_watermark_removal_after",3)\
                .click_apply()\
                .screenshot("edit_frame_watermark_removal_lobby",3)\
                .click_save()\
                .pull_photo_from_device("edit_frame_watermark_removal_save")

    @pytest.mark.camera
    def test_edit_frame_apply(self): 
        # Riley 3.frame apply
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_frame()\
                .screenshot("edit_frame_apply_before", 3)\
                .select_frame_item("Spring")\
                .select_frame_item("Spring 01")\
                .screenshot("edit_frame_apply_after",3)\
                .compare_photo("edit_frame_apply_before", "edit_frame_apply_after", "edit_frame_apply_diff")\
                .click_apply()\
                .screenshot("edit_frame_apply_lobby",3)\
                .click_save()\
                .pull_photo_from_device("edit_frame_apply_save")


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_frame_download_apply_single()
    t.teardown_method()
