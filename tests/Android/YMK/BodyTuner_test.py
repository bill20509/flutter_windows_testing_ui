import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "3.Bodytuner"


class Test(object):
    def setup_method(self):  # run before every test
        # 設定device
        # self.driver = App().set_udid("R58M788DFJP") \
        #    .set_platform("Android") \
        #    .set_version("9") \
        #    .set_app("YMK") \
        #    .create()
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_a_tutorial(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .wait_time(wait=3) \
            .check_tutorial() \
            .screenshot("test_edit_bodytuner_tips_enhancer", wait_time=3) \
            .message("Enhancer tutorial checked!") \
            .click_tutorial_ok() \
            .select_tool("Slim") \
            .wait_time(wait=3) \
            .check_tutorial() \
            .screenshot("test_edit_bodytuner_tips_slim", wait_time=3) \
            .message("Slim tutorial checked!") \
            .click_tutorial_ok() \
            .select_tool("Protect") \
            .wait_time(wait=3) \
            .check_tutorial() \
            .screenshot("test_edit_bodytuner_tips_protect", wait_time=3) \
            .message("Protect tutorial checked!") \
            .click_tutorial_ok() \
            .message("This Case Does Not Save Photo!")
        extra.append(extras.image('screenshot/test_edit_bodytuner_tips_protect.png'))
        extra.append(extras.image('screenshot/test_edit_bodytuner_tips_slim.png'))
        extra.append(extras.image('screenshot/test_edit_bodytuner_tips_enhancer.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_enhancer(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Enhancer") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_enhancer_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .message("Enhancer applied = 100") \
            .screenshot("test_edit_bodytuner_enhancer", wait_time=3) \
            .compare_photo("test_edit_bodytuner_enhancer_before", "test_edit_bodytuner_enhancer",
                           "test_edit_bodytuner_enhancer_diff", threshold=0.4) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_enhancer_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_enhancer", "test_edit_bodytuner_enhancer_leaveroom",
                           "test_edit_bodytuner_enhancer_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_enhancer_save") \
            .compose_gif("test_edit_bodytuner_enhancer_compare",
                         "screenshot/test_edit_bodytuner_enhancer_diff.png",
                         "screenshot/test_edit_bodytuner_enhancer.png",
                         "screenshot/test_edit_bodytuner_enhancer_before.png", speed=2) \
            .message("GIF order = before + enhancer + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_enhancer_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_enhancer_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_enhancer_minus(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Enhancer") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_enhancer_minus_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .message("Enhancer applied = -100") \
            .screenshot("test_edit_bodytuner_enhancer_minus", wait_time=3) \
            .compare_photo("test_edit_bodytuner_enhancer_minus_before", "test_edit_bodytuner_enhancer_minus",
                           "test_edit_bodytuner_enhancer_minus_diff", threshold=0.4) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_enhancer_minus_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_enhancer_minus", "test_edit_bodytuner_enhancer_minus_leaveroom",
                           "test_edit_bodytuner_enhancer_minus_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_enhancer_minus_save") \
            .compose_gif("test_edit_bodytuner_enhancer_minus_compare",
                         "screenshot/test_edit_bodytuner_enhancer_minus_diff.png",
                         "screenshot/test_edit_bodytuner_enhancer_minus.png",
                         "screenshot/test_edit_bodytuner_enhancer_minus_before.png", speed=2) \
            .message("GIF order = before + enhancer minus + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_enhancer_minus_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_enhancer_minus_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_slim(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Slim") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_slim_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .message("Slim applied = -100") \
            .screenshot("test_edit_bodytuner_slim", wait_time=3) \
            .compare_photo("test_edit_bodytuner_slim_before", "test_edit_bodytuner_slim",
                           "test_edit_bodytuner_slim_diff", threshold=0.4) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_slim_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_slim", "test_edit_bodytuner_slim_leaveroom",
                           "test_edit_bodytuner_slim_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_slim_save") \
            .compose_gif("test_edit_bodytuner_slim_compare",
                         "screenshot/test_edit_bodytuner_slim_diff.png",
                         "screenshot/test_edit_bodytuner_slim.png",
                         "screenshot/test_edit_bodytuner_slim_before.png", speed=2) \
            .message("GIF order = before + slim + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_slim_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_slim_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_slim_plus(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Slim") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_slim_plus_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .message("Slim applied = 100") \
            .screenshot("test_edit_bodytuner_slim_plus", wait_time=3) \
            .compare_photo("test_edit_bodytuner_slim_plus_before", "test_edit_bodytuner_slim_plus",
                           "test_edit_bodytuner_slim_plus_diff", threshold=0.4) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_slim_plus_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_slim_plus", "test_edit_bodytuner_slim_plus_leaveroom",
                           "test_edit_bodytuner_slim_plus_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_slim_plus_save") \
            .compose_gif("test_edit_bodytuner_slim_plus_compare",
                         "screenshot/test_edit_bodytuner_slim_plus_diff.png",
                         "screenshot/test_edit_bodytuner_slim_plus.png",
                         "screenshot/test_edit_bodytuner_slim_plus_before.png", speed=2) \
            .message("GIF order = before + slim plus + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_slim_plus_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_slim_plus_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_waist(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Waist") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_waist_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .message("Auto waist applied = -100") \
            .screenshot("test_edit_bodytuner_waist", wait_time=5) \
            .compare_photo("test_edit_bodytuner_waist_before", "test_edit_bodytuner_waist",
                           "test_edit_bodytuner_waist_diff", threshold=0.1) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_waist_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_waist", "test_edit_bodytuner_waist_leaveroom",
                           "test_edit_bodytuner_waist_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_waist_save") \
            .compose_gif("test_edit_bodytuner_waist_compare",
                         "screenshot/test_edit_bodytuner_waist_diff.png",
                         "screenshot/test_edit_bodytuner_waist.png",
                         "screenshot/test_edit_bodytuner_waist_before.png", speed=2) \
            .message("GIF order = before + waist + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_waist_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_waist_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_waist_plus(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Waist") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_waist_plus_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .message("Auto waist applied = 100") \
            .screenshot("test_edit_bodytuner_waist_plus", wait_time=3) \
            .compare_photo("test_edit_bodytuner_waist_plus_before", "test_edit_bodytuner_waist_plus",
                           "test_edit_bodytuner_waist_plus_diff", threshold=0.1) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_waist_plus_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_waist_plus", "test_edit_bodytuner_waist_plus_leaveroom",
                           "test_edit_bodytuner_waist_plus_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_waist_plus_save") \
            .compose_gif("test_edit_bodytuner_waist_plus_compare",
                         "screenshot/test_edit_bodytuner_waist_plus_diff.png",
                         "screenshot/test_edit_bodytuner_waist_plus.png",
                         "screenshot/test_edit_bodytuner_waist_plus_before.png", speed=2) \
            .message("GIF order = before + waist plus + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_waist_plus_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_waist_plus_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_arms(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Arms") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_arms_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .message("Auto arms applied = -100") \
            .screenshot("test_edit_bodytuner_arms", wait_time=5) \
            .compare_photo("test_edit_bodytuner_arms_before", "test_edit_bodytuner_arms",
                           "test_edit_bodytuner_arms_diff", threshold=0) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_arms_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_arms", "test_edit_bodytuner_arms_leaveroom",
                           "test_edit_bodytuner_arms_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_arms_save") \
            .compose_gif("test_edit_bodytuner_arms_compare",
                         "screenshot/test_edit_bodytuner_arms_diff.png",
                         "screenshot/test_edit_bodytuner_arms.png",
                         "screenshot/test_edit_bodytuner_arms_before.png", speed=2) \
            .message("GIF order = before + arms + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_arms_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_arms_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_arms_plus(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Arms") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_arms_plus_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .message("Auto arms applied = 100") \
            .screenshot("test_edit_bodytuner_arms_plus", wait_time=5) \
            .compare_photo("test_edit_bodytuner_arms_plus_before", "test_edit_bodytuner_arms_plus",
                           "test_edit_bodytuner_arms_plus_diff", threshold=0) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_arms_plus_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_arms_plus", "test_edit_bodytuner_arms_plus_leaveroom",
                           "test_edit_bodytuner_arms_plus_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_arms_plus_save") \
            .compose_gif("test_edit_bodytuner_arms_plus_compare",
                         "screenshot/test_edit_bodytuner_arms_plus_diff.png",
                         "screenshot/test_edit_bodytuner_arms_plus.png",
                         "screenshot/test_edit_bodytuner_arms_plus_before.png", speed=2) \
            .message("GIF order = before + arms plus + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_arms_plus_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_arms_plus_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_legs(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Legs") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_legs_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .message("Auto legs applied = -100") \
            .screenshot("test_edit_bodytuner_legs", wait_time=5) \
            .compare_photo("test_edit_bodytuner_legs_before", "test_edit_bodytuner_legs",
                           "test_edit_bodytuner_legs_diff", threshold=0.1) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_legs_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_legs", "test_edit_bodytuner_legs_leaveroom",
                           "test_edit_bodytuner_legs_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_legs_save") \
            .compose_gif("test_edit_bodytuner_legs_compare",
                         "screenshot/test_edit_bodytuner_legs_diff.png",
                         "screenshot/test_edit_bodytuner_legs.png",
                         "screenshot/test_edit_bodytuner_legs_before.png", speed=2) \
            .message("GIF order = before + legs + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_legs_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_legs_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_legs_plus(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Legs") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_legs_plus_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .message("Auto legs applied = 100") \
            .screenshot("test_edit_bodytuner_legs_plus", wait_time=5) \
            .compare_photo("test_edit_bodytuner_legs_plus_before", "test_edit_bodytuner_legs_plus",
                           "test_edit_bodytuner_legs_plus_diff", threshold=0.1) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_legs_plus_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_legs_plus", "test_edit_bodytuner_legs_plus_leaveroom",
                           "test_edit_bodytuner_legs_plus_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_arms_plus_save") \
            .compose_gif("test_edit_bodytuner_legs_plus_compare",
                         "screenshot/test_edit_bodytuner_legs_plus_diff.png",
                         "screenshot/test_edit_bodytuner_legs_plus.png",
                         "screenshot/test_edit_bodytuner_legs_plus_before.png", speed=2) \
            .message("GIF order = before + legs plus + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_legs_plus_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_arms_plus_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_bodytuner_protect(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Enhancer") \
            .waiting_cursor() \
            .adjust_intensity_to_right() \
            .message("Enhancer applied = 100") \
            .screenshot("test_edit_bodytuner_protect_before", wait_time=3) \
            .click_undo() \
            .message("Undo enhancer!") \
            .select_tool("Protect") \
            .click_detect() \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_protect_detect", wait_time=3) \
            .message("Protect applied!") \
            .click_v() \
            .message("Clicked V!") \
            .select_tool("Enhancer") \
            .adjust_intensity_to_right() \
            .message("Enhancer applied!") \
            .screenshot("test_edit_bodytuner_protect", wait_time=3) \
            .compare_photo("test_edit_bodytuner_protect_before", "test_edit_bodytuner_protect",
                           "test_edit_bodytuner_protect_diff", threshold=0) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_protect_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_protect", "test_edit_bodytuner_protect_leaveroom",
                           "test_edit_bodytuner_protect_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_protect_save") \
            .compose_gif("test_edit_bodytuner_protect_compare",
                         "screenshot/test_edit_bodytuner_protect_diff.png",
                         "screenshot/test_edit_bodytuner_protect.png",
                         "screenshot/test_edit_bodytuner_protect_before.png", speed=2) \
            .message("GIF order = before + protect + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_protect_compare.gif'))
        extra.append(extras.image('screenshot/test_edit_bodytuner_protect_detect.png'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_protect_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_bodytuner_undo(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Enhancer") \
            .waiting_cursor() \
            .adjust_intensity_to_right() \
            .message("Enhancer applied = 100") \
            .screenshot("test_edit_bodytuner_undo_before", wait_time=3) \
            .click_undo() \
            .message("Undo enhancer!") \
            .screenshot("test_edit_bodytuner_undo", wait_time=3) \
            .compare_photo("test_edit_bodytuner_undo_before", "test_edit_bodytuner_undo",
                           "test_edit_bodytuner_undo_diff", threshold=0.4) \
            .click_redo() \
            .message("Redo enhancer!") \
            .screenshot("test_edit_bodytuner_undo_redo", wait_time=3) \
            .compare_photo("test_edit_bodytuner_undo", "test_edit_bodytuner_undo_redo",
                           "test_edit_bodytuner_undo_redo_diff", threshold=0.4) \
            .click_v() \
            .message("Clicked V!") \
            .screenshot("test_edit_bodytuner_undo_redo_leaveroom", wait_time=3) \
            .compare_photo("test_edit_bodytuner_undo_redo", "test_edit_bodytuner_undo_redo_leaveroom",
                           "test_edit_bodytuner_undo_redo_leaveroom_diff", threshold=0.9) \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_bodytuner_undo_redo_save") \
            .compose_gif("test_edit_bodytuner_undo_redo_compare",
                         "screenshot/test_edit_bodytuner_undo_before.png",
                         "screenshot/test_edit_bodytuner_undo.png",
                         "screenshot/test_edit_bodytuner_undo_redo.png",
                         "screenshot/test_edit_bodytuner_undo_redo_diff.png", speed=2) \
            .message("GIF order = enhancer + undo enhancer + redo enhancer + diff")
        extra.append(extras.image('screenshot/test_edit_bodytuner_undo_redo_compare.gif'))
        extra.append(extras.image('savephoto/3_test_edit_bodytuner_undo_redo_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_bodytuner_protect_undo(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Protect") \
            .click_detect() \
            .message("Protect applied!") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_protect_undo_before", wait_time=3) \
            .click_undo() \
            .screenshot("test_edit_bodytuner_protect_undo", wait_time=3) \
            .message("Undo protect!") \
            .compare_photo("test_edit_bodytuner_protect_undo_before", "test_edit_bodytuner_protect_undo",
                           "test_edit_bodytuner_protect_undo_diff", threshold=0.2) \
            .click_redo() \
            .screenshot("test_edit_bodytuner_protect_undo_redo", wait_time=3) \
            .message("Redo protect!") \
            .compare_photo("test_edit_bodytuner_protect_undo", "test_edit_bodytuner_protect_undo_redo",
                           "test_edit_bodytuner_protect_undo_redo_diff", threshold=0.2) \
            .compose_gif("test_edit_bodytuner_protect_undo_redo_compare",
                         "screenshot/test_edit_bodytuner_protect_undo_before.png",
                         "screenshot/test_edit_bodytuner_protect_undo.png",
                         "screenshot/test_edit_bodytuner_protect_undo_redo.png", speed=2) \
            .message("This Case Does Not Save Photo!") \
            .message("GIF order = before + undo + undo_redo")
        extra.append(extras.image('screenshot/test_edit_bodytuner_protect_undo_redo_compare.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_bodytuner_protect_reset(self, extra):
        self.app.deeplink_to_bodytuner() \
            .pick_photo(folder_name, 1) \
            .select_tool("Protect") \
            .click_detect() \
            .message("Protect applied!") \
            .waiting_cursor() \
            .screenshot("test_edit_bodytuner_protect_reset_before", wait_time=3) \
            .click_clear() \
            .screenshot("test_edit_bodytuner_protect_reset", wait_time=3) \
            .message("Reset protect!") \
            .compare_photo("test_edit_bodytuner_protect_reset_before", "test_edit_bodytuner_protect_reset",
                           "test_edit_bodytuner_protect_reset_diff", threshold=0.2) \
            .compose_gif("test_edit_bodytuner_protect_reset_compare",
                         "screenshot/test_edit_bodytuner_protect_reset_before.png",
                         "screenshot/test_edit_bodytuner_protect_reset.png", speed=2) \
            .message("This Case Does Not Save Photo!") \
            .message("GIF order = before + reset")
        extra.append(extras.image('screenshot/test_edit_bodytuner_protect_reset_compare.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
