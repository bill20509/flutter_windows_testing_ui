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

    @pytest.mark.camera
    def test_pull_photo(self):
        self.app.deeplink_to_launcher()\
            .pull_photo_from_device("test", "YCP")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_pull_photo()
