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
    def draw_horizontal(self):
        self.app.deeplink_to_photo_edit()\
            .wait_loading_panel()\
            .click_effects()\
            .click_animation_tab()\
            .select_animation_item(0)\
            .wait_progress_bar()\
            .click_erase_panel()\
            .draw_on_photo(0.3, 0.3, 0.5, 0.2)\
            .click_paint()\
            .click_erase()\


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.draw_horizontal()
