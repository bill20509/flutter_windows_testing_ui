import pytest
from libs.app import App
import libs.YCP.pages as pages


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
        breakpoint()

    @pytest.mark.YCP
    def test_edit_crop_rotate_m90(self):
        """1"""
        self.app.deeplink_to_photo_edit()\
            .select_feature_room("Tools")\
            .select_feature_room("Crop & Rotate")\
            .rotate_m90()\
            .apply()\
            .screenshot("test_edit_crop_roate_-90.png", wait_time=1)

    @pytest.mark.YCP
    def test_edit_crop_rotate_45(self):
        """2"""
        self.app.deeplink_to_photo_edit()\
            .open_tools()\
            .select_item("Crop & Rotate")\
            .rotate_slidebar_to_45()\
            .apply()\
            .screenshot("test_edit_crop_roate_45.png", wait_time=1)

    @pytest.mark.YCP
    def test_edit_crop_rotate_flip(self):
        """3"""
        self.app.deeplink_to_photo_edit()\
            .open_tools()\
            .select_item("Crop & Rotate")\
            .rotate_flip()\
            .apply()\
            .screenshot("test_edit_crop_roate_-90.png", wait_time=1)

    @pytest.mark.YCP
    def test_edit_crop_rotate_reset(self):
        """5"""
        self.app.deeplink_to_photo_edit()\
            .open_tools()\
            .select_item("Crop & Rotate")\
            .screenshot("edit_crop_rotate_original.png", wait_time=1)\
                .rotate_m90()\
                .rotate_flip()\
                .rotate_slidebar_to_45()\
                .reset_button()\
                .screenshot("edit_crop_rotate_after_reset.png", wait_time=1)\
                .compare_photo("edit_crop_rotate_original.png", "edit_crop_rotate_after_reset.png")

    @pytest.mark.YCP
    def test_perspective_apply(self):
        """7"""
        self.app.deeplink_to_persprctive()\
                .screenshot("edit_perspective_apply.png", wait_time=1)

    @pytest.mark.YCP
    def test_edit_mirror_pattern(self):
        """8"""
        self.app.deeplink_to_mirror()\
            .click_mirror_item(1)\
            .click_apply()\
            .screenshot("edit_mirror_effect.png", wait_time=1)

    @pytest.mark.YCP
    def test_edit_mirror_offset(self):
        """9"""
        self.app.deeplink_to_mirror()\
                .click_mirror_item(2)\
                .slider_offset_value_to_0()\
                .click_apply()\
                .screenshot("edit_mirror_effect.png", wait_time=1)

    def teardown_method(self):  # quit driver when test case done
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_crop_rotate_m90()
    t.teardown_method()
