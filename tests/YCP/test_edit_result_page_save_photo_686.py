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
    def test_edit_result_page_continue_editing(self):
        """Carl 686 test_result_page_continue_editing"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_beautify")\
            .select_photo_item(0)\
            .click_save() \
            .click_continue_editing() \
            .screenshot("edit_result_page_continue_editing", wait_time=3)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_result_page_continue_editing()
    t.teardown_method()
