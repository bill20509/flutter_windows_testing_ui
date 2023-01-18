import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time
folder_name = "1.Makeup"


class Test(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_eyewear(self, extra):
        self.app.deeplink_to_eyewear() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_eyewear_before", wait_time=5) \
            .select_pattern(3) \
            .screenshot("test_edit_eyewear_after", wait_time=5) \
            .compare_photo("test_edit_eyewear_before", "test_edit_eyewear_after", "test_edit_eyewear_diff",
                           threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_eyewear_save")
        extra.append(extras.image('screenshot/test_edit_eyewear_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_eyewear_save.jpg'))

    """@pytest.mark.acc
    def test_edit_eyewear_store(self, extra):
        self.app.deeplink_to_eyewear() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_eyewear_store_before", wait_time=5) \
            .click_store() \
            .
            .screenshot("test_edit_eyewear_store_after", wait_time=5) \
            .compare_photo("test_edit_eyewear_store_before", "test_edit_eyewear_store_after",
                           "test_edit_eyewear_store_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_eyewear_store_save")"""

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_headband(self, extra):
        self.app.deeplink_to_headband() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_headband_before", wait_time=5) \
            .select_pattern(2) \
            .screenshot("test_edit_headband_after", wait_time=5) \
            .compare_photo("test_edit_headband_before", "test_edit_headband_after", "test_edit_headband_diff",
                           threshold=0) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_headband_save")
        extra.append(extras.image('screenshot/test_edit_headband_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_headband_save.jpg'))

    """@pytest.mark.acc
    def test_edit_headband_store(self, extra):
        self.app.deeplink_to_headband() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_headband_store_before", wait_time=5) \
            .click_store() \
            .
            .screenshot("test_edit_headband_store_after", wait_time=5) \
            .compare_photo("test_edit_headband_store_before", "test_edit_headband_store_after",
                           "test_edit_headband_store_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_headband_store_save")"""

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_necklace(self, extra):
        self.app.deeplink_to_necklace() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_necklace_before", wait_time=5) \
            .select_pattern(1) \
            .screenshot("test_edit_necklace_after", wait_time=5) \
            .compare_photo("test_edit_necklace_before", "test_edit_necklace_after", "test_edit_necklace_diff",
                           threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_necklace_save")
        extra.append(extras.image('screenshot/test_edit_necklace_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_necklace_save.jpg'))

    """@pytest.mark.acc
    def test_edit_necklace_store(self, extra):
        self.app.deeplink_to_necklace() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_necklace_store_before", wait_time=5) \
            .click_store() \
            .
            .screenshot("test_edit_necklace_store_after", wait_time=5) \
            .compare_photo("test_edit_necklace_store_before", "test_edit_necklace_store_after",
                           "test_edit_necklace_store_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_necklace_store_save")"""

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_earrings(self, extra):
        self.app.deeplink_to_earrings() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_earrings_before", wait_time=5) \
            .select_pattern(1) \
            .screenshot("test_edit_earrings_after", wait_time=5) \
            .compare_photo("test_edit_earrings_before", "test_edit_earrings_after", "test_edit_earrings_diff",
                           threshold=0) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_earrings_save")
        extra.append(extras.image('screenshot/test_edit_earrings_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_earrings_save.jpg'))

    """@pytest.mark.acc
    def test_edit_earrings_store(self, extra):
        self.app.deeplink_to_earrings() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_earrings_store_before", wait_time=5) \
            .click_store() \
            .
            .screenshot("test_edit_earrings_store_after", wait_time=5) \
            .compare_photo("test_edit_earrings_store_before", "test_edit_earrings_store_after",
                           "test_edit_earrings_store_diff", threshold=0) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_earrings_store_save")"""

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_hat_a_download(self, extra):
        self.app.deeplink_to_hat() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_hat_download_before", wait_time=5) \
            .select_pattern(5) \
            .screenshot("test_edit_hat_download_after", wait_time=15) \
            .compare_photo("test_edit_hat_download_before", "test_edit_hat_download_after",
                           "test_edit_hat_download_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hat_download_save")
        extra.append(extras.image('screenshot/test_edit_hat_download_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hat_download_save.jpg'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_hat_b(self, extra):
        self.app.deeplink_to_hat() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_hat_before", wait_time=5) \
            .select_pattern(2) \
            .screenshot("test_edit_hat_after", wait_time=5) \
            .compare_photo("test_edit_hat_before", "test_edit_hat_after", "test_edit_hat_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hat_save")
        extra.append(extras.image('screenshot/test_edit_hat_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hat_save.jpg'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
