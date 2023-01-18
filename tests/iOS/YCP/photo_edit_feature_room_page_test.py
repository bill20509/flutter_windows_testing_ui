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
    def test_tools(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_item(1)\
                .select_feature_room("Tools")

    @pytest.mark.test
    def test_brush(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_item(1)\
                .select_feature_room("Effects").select

    @pytest.mark.test
    def test_sticker(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("Download")\
                .select_photo_item(1)\
                .click_sticker()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_sticker()
    t.teardown_method()
