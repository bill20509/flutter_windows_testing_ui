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

    @pytest.mark.picker
    def test_photo_picker_back(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .click_back() \
                .screenshot("test_photo_picker_back", 1)


    @pytest.mark.picker
    def test_photo_picker_single_view(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_magnifier_icon(2)\
                .screenshot("test_photo_picker_single_view",1)

    @pytest.mark.picker
    def test_feature_i_removal(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_removal()\
                .click_i()\

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_photo_picker_back()
    t.test_photo_picker_single_view()
    t.test_feature_i_removal()
    t.teardown_method()
