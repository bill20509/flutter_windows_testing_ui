import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time


class TestBodyTuner(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("R58M788DFJP")\
            .set_platform("Android")\
            .set_version("9")\
            .set_app("YMK")\
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.bodytuner
    def test_edit_bodytuner_enhancer(self):
        self.app.deeplink_to_bodytuner()\
            .pick_photo("YouCam Makeup Sample", 8)\
            .select_tool("Enhancer")\
            .waiting_cursor()\
            .screenshot("test_edit_bodytuner_enhancer_before", 3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_bodytuner_enhancer", 3)\
            .compare_photo("test_edit_bodytuner_enhancer_before", "test_edit_bodytuner_enhancer", "test_edit_bodytuner_enhancer_diff")\
            .click_v() \
            .screenshot("test_edit_bodytuner_enhancer_leaveroom", 2) \
            .compare_photo("test_edit_bodytuner_enhancer", "test_edit_bodytuner_enhancer_leaveroom",
                           "test_edit_bodytuner_enhancer_leaveroom_diff") \
            .click_save()\
            .pull_photo_from_device("test_edit_bodytuner_enhancer_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_enhancer_minus(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Enhancer") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_enhancer_minus_before", 3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_bodytuner_enhancer_minus", 3) \
            .compare_photo("test_edit_bodytuner_enhancer_minus_before", "test_edit_bodytuner_enhancer_minus",
                           "test_edit_bodytuner_enhancer_minus_diff") \
            .click_v() \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_enhancer_minus_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_slim(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Slim") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_slim_before", 3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_bodytuner_slim", 3) \
            .compare_photo("test_edit_bodytuner_slim_before", "test_edit_bodytuner_slim",
                           "test_edit_bodytuner_slim_diff") \
            .click_v() \
            .screenshot("test_edit_bodytuner_slim_leaveroom", 2) \
            .compare_photo("test_edit_bodytuner_slim", "test_edit_bodytuner_slim_leaveroom",
                           "test_edit_bodytuner_slim_leaveroom_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_slim_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_slim_plus(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Slim") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_slim_plus_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_bodytuner_slim_plus", 3) \
            .compare_photo("test_edit_bodytuner_slim_plus_before", "test_edit_bodytuner_slim_plus",
                           "test_edit_bodytuner_slim_plus_diff") \
            .click_v() \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_slim_plus_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_waist(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Waist") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_waist_before", 3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_bodytuner_waist", 5) \
            .compare_photo("test_edit_bodytuner_waist_before", "test_edit_bodytuner_waist",
                           "test_edit_bodytuner_waist_diff") \
            .click_v() \
            .screenshot("test_edit_bodytuner_waist_leaveroom", 2) \
            .compare_photo("test_edit_bodytuner_waist", "test_edit_bodytuner_waist_leaveroom", "test_edit_bodytuner_waist_leaveroom_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_waist_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_waist_plus(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Waist") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_waist_plus_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_bodytuner_waist_plus", 5) \
            .compare_photo("test_edit_bodytuner_waist_plus_before", "test_edit_bodytuner_waist_plus",
                           "test_edit_bodytuner_waist_plus_diff") \
            .click_v() \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_waist_plus_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_arms(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Arms") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_arms_before", 3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_bodytuner_arms", 5) \
            .compare_photo("test_edit_bodytuner_arms_before", "test_edit_bodytuner_arms",
                           "test_edit_bodytuner_arms_diff") \
            .click_v() \
            .screenshot("test_edit_bodytuner_arms_leaveroom", 2) \
            .compare_photo("test_edit_bodytuner_arms", "test_edit_bodytuner_arms_leaveroom", "test_edit_bodytuner_arms_leaveroom_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_arms_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_arms_plus(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Arms") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_arms_plus_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_bodytuner_arms_plus", 5) \
            .compare_photo("test_edit_bodytuner_arms_plus_before", "test_edit_bodytuner_arms_plus",
                           "test_edit_bodytuner_arms_plus_diff") \
            .click_v() \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_arms_plus_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_legs(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Legs") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_legs_before", 3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_bodytuner_legs", 5) \
            .compare_photo("test_edit_bodytuner_legs_before", "test_edit_bodytuner_legs",
                           "test_edit_bodytuner_legs_diff") \
            .click_v() \
            .screenshot("test_edit_bodytuner_legs_leaveroom", 2) \
            .compare_photo("test_edit_bodytuner_legs", "test_edit_bodytuner_legs_leaveroom", "test_edit_bodytuner_legs_leaveroom_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_legs_save")

    @pytest.mark.bodytuner
    def test_edit_bodytuner_legs_plus(self):
        self.app.deeplink_to_bodytuner() \
            .pick_photo("YouCam Makeup Sample", 8) \
            .select_tool("Legs") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_legs_plus_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_bodytuner_legs_plus", 5) \
            .compare_photo("test_edit_bodytuner_legs_plus_before", "test_edit_bodytuner_legs_plus",
                           "test_edit_bodytuner_legs_plus_diff") \
            .click_v() \
            .click_save() \
            .pull_photo_from_device("test_edit_bodytuner_arms_plus_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
