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
            .click_brush()\
            .draw_on_photo(0.1, 0.5, 0.8, 0.5)\
            .draw_on_photo(0.0, 0.9, 1, 0.9)\
            .draw_on_photo(0.0, 0.2, 1, 0.4)\
            .draw_on_photo(0.3, 0.3, 0.5, 0.2)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.draw_horizontal()
