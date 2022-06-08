import pytest
from libs.app import App
from libs.YCP import pages
import time


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_udid("R5CR5122ACA")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(10)\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)

    @pytest.mark.test
    def test_beautify(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(1)\
                .click_beautify()

    @pytest.mark.test
    def test_edit(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(1)\
                .click_edit()

    @pytest.mark.test
    def test_share(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(1)\
                .click_share()

    @pytest.mark.test
    def test_delete(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(1)\
                .click_delete()\
                .click_dialog_cancel()

    @pytest.mark.test
    def test_delete(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(1)\
                .click_delete()\
                .click_dialog_delete()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_makeupcam()
    t.teardown_method()
