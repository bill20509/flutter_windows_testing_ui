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
    def test_edit_text_apply(self):
        # Sol
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit") \
            .select_photo_item(1) \
            .screenshot("edit_text_before") \
            .click_text()\
            .screenshot("edit_text_apply")\
            .compare_photo("edit_text_before", "edit_text_apply", "edit_text_apply_diff") \
            .click_apply() \
            .click_save() \
            .pull_photo_from_device("edit_text_apply_save")



    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_text_apply()
    t.teardown_method()
