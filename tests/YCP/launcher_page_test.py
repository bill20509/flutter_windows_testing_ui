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
    def test_settings(self):
        self.app.deeplink_to_launcher()\
            .click_settings()

    @pytest.mark.test
    def test_crown(self):
        self.app.deeplink_to_launcher()\
            .click_premium()

    @pytest.mark.test
    def test_app_logo(self):
        self.app.deeplink_to_launcher()\
            .click_app_logo()

    @pytest.mark.test
    def test_camera(self):
        self.app.click_camera()

    @pytest.mark.test
    def test_photo_edit(self):
        self.app.deeplink_to_launcher()\
            .click_photo_edit()

    @pytest.mark.test
    def test_beautify(self):
        self.app.deeplink_to_launcher()\
            .click_beautify()

    @pytest.mark.test
    def test_collage(self):
        self.app.deeplink_to_launcher()\
            .click_collage()

    @pytest.mark.test
    def test_discovery(self):
        self.app.deeplink_to_launcher()\
            .click_discovery()

    @pytest.mark.test
    def test_store(self):
        self.app.deeplink_to_launcher()\
            .click_store()

    @pytest.mark.test
    def test_how_to_see_all(self):
        self.app.deeplink_to_launcher()\
            .click_how_to_see_all()

    @pytest.mark.test
    def test_trending_see_all(self):
        self.app.deeplink_to_launcher()\
            .click_trending_see_all()

    @pytest.mark.test
    def test_photo_challenge_see_all(self):
        self.app.deeplink_to_launcher()\
            .click_photo_challenge_see_all()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_makeupcam()
    t.teardown_method()
