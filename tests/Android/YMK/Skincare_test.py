from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.A
    @pytest.mark.S1
    def test_launcher_skincare(self, extra):
        self.app.deeplink_to_launcher() \
            .click_skincare_tile() \
            .auto_detect()\
            .screenshot("test_launcher_skincare")\
            .click_skin_diary()\
            .screenshot("test_launcher_skincare1", 3)\
            .click_avatar()\
            .delete_photo()\
            .screenshot("test_launcher_skincare2", 3)
        extra.append(extras.image('screenshot/test_launcher_skincare2.png'))
        extra.append(extras.image('screenshot/test_launcher_skincare1.png'))
        extra.append(extras.image('screenshot/test_launcher_skincare.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

