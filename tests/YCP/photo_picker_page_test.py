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
    def test_select_photo_item(self):
        launcher_page = self.app.deeplink_to_launcher()
        launcher_page.click_photo_edit()\
            .select_album_item(1)\
            .select_photo_item(1)
        self.driver.back()
        launcher_page.click_app_logo()

    @pytest.mark.test
    def test_delete_photo(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .click_delete()\
            # .select_photo_item(1)\
        # .select_photo_item(2)\
        # .click_delete_photo()

    @pytest.mark.test
    def test_photo_maginfier(self):
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item(1)\
                .select_photo_magnifier_icon(2)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_makeupcam()
    t.teardown_method()
