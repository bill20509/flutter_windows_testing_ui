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
    def test_edit_effects_portrait_candy_100(self):
        """Carl 793 test_edit_effects_portrait_candy_100_apply"""
        self.app.deeplink_to_launcher()\
            .click_photo_edit()\
            .select_album_item("a_edit")\
            .select_photo_item(6)\
            .click_effects()\
            .select_filter("Portrait")\
            .wait_time(1)\
            .select_filter_item(0)\
            .set_intensity_bar(100)\
            .click_apply()\
            .screenshot("edit_effects_portrait_candy_100_apply", wait_time=3)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_effects_portrait_candy_100()
    t.teardown_method()
