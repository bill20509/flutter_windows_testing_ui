import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "3.Bodytuner"


class Test(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_removal_apply(self, extra):
        self.app.deeplink_to_removal() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .check_alert_dialog() \
            .screenshot("test_edit_removal_apply_before", wait_time=5) \
            .draw_on_photo(0.45, 0.2, 0.45, 0.8) \
            .draw_on_photo(0.5, 0.2, 0.5, 0.8) \
            .draw_on_photo(0.55, 0.2, 0.55, 0.8) \
            .screenshot("test_edit_removal_apply_draw", wait_time=5) \
            .click_apply() \
            .screenshot("test_edit_removal_apply_after", wait_time=5) \
            .compare_photo("test_edit_removal_apply_before", "test_edit_removal_apply_after",
                           "test_edit_removal_apply_diff", threshold=0.1) \
            .compose_gif("test_edit_removal_apply_results",
                         "screenshot/test_edit_removal_apply_before.png",
                         "screenshot/test_edit_removal_apply_draw.png",
                         "screenshot/test_edit_removal_apply_after.png",
                         "screenshot/test_edit_removal_apply_diff.png", speed=1) \
            .message("GIF order = before + draw + after + diff") \
            .click_v() \
            .check_noface_dialog() \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_removal_apply_save")
        extra.append(extras.image('savephoto/3_test_edit_removal_apply_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_removal_apply_results.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_removal_erase(self, extra):
        self.app.deeplink_to_removal() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .check_alert_dialog() \
            .screenshot("test_edit_removal_erase_before", wait_time=5) \
            .draw_on_photo(0.45, 0.2, 0.45, 0.8) \
            .draw_on_photo(0.5, 0.2, 0.5, 0.8) \
            .draw_on_photo(0.55, 0.2, 0.55, 0.8) \
            .screenshot("test_edit_removal_erase_draw", wait_time=5) \
            .click_eraser() \
            .draw_on_photo(0.1, 0.2, 0.8, 0.8) \
            .draw_on_photo(0.15, 0.2, 0.85, 0.8) \
            .draw_on_photo(0.2, 0.2, 0.9, 0.8) \
            .screenshot("test_edit_removal_erase_draw_erase", wait_time=5) \
            .click_apply() \
            .screenshot("test_edit_removal_erase_after", wait_time=5) \
            .compare_photo("test_edit_removal_erase_before", "test_edit_removal_erase_after",
                           "test_edit_removal_erase_diff", threshold=0.1) \
            .compose_gif("test_edit_removal_erase_results",
                         "screenshot/test_edit_removal_erase_before.png",
                         "screenshot/test_edit_removal_erase_draw.png",
                         "screenshot/test_edit_removal_erase_draw_erase.png",
                         "screenshot/test_edit_removal_erase_after.png",
                         "screenshot/test_edit_removal_erase_diff.png", speed=1) \
            .message("GIF order = before + draw + erase + after + diff") \
            .click_v() \
            .check_noface_dialog() \
            .click_save() \
            .message("Photo Saved!") \
            .pull_photo_from_device("3_test_edit_removal_erase_save")
        extra.append(extras.image('savephoto/3_test_edit_removal_erase_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_removal_erase_results.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_removal_undo_redo(self, extra):
        self.app.deeplink_to_removal() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .check_alert_dialog() \
            .draw_on_photo(0.4, 0.1, 0.4, 0.9) \
            .draw_on_photo(0.5, 0.1, 0.5, 0.9) \
            .draw_on_photo(0.6, 0.1, 0.6, 0.9) \
            .screenshot("test_edit_removal_undo_redo_A_before", wait_time=5) \
            .click_undo() \
            .screenshot("test_edit_removal_undo_redo_A_1", wait_time=5) \
            .click_undo() \
            .screenshot("test_edit_removal_undo_redo_A_2", wait_time=5) \
            .click_redo() \
            .screenshot("test_edit_removal_undo_redo_A_3", wait_time=5) \
            .compose_gif("test_edit_removal_undo_redo_A_steps",
                         "screenshot/test_edit_removal_undo_redo_A_before.png",
                         "screenshot/test_edit_removal_undo_redo_A_1.png",
                         "screenshot/test_edit_removal_undo_redo_A_2.png",
                         "screenshot/test_edit_removal_undo_redo_A_3.png",
                         "screenshot/test_edit_removal_undo_redo_A_3.png", speed=2) \
            .click_redo() \
            .click_apply() \
            .screenshot("test_edit_removal_undo_redo_B_before", wait_time=5) \
            .click_undo() \
            .screenshot("test_edit_removal_undo_redo_B_1", wait_time=5) \
            .click_redo() \
            .screenshot("test_edit_removal_undo_redo_B_2", wait_time=5) \
            .compose_gif("test_edit_removal_undo_redo_B_steps",
                         "screenshot/test_edit_removal_undo_redo_B_before.png",
                         "screenshot/test_edit_removal_undo_redo_B_1.png",
                         "screenshot/test_edit_removal_undo_redo_B_2.png",
                         "screenshot/test_edit_removal_undo_redo_B_2.png", speed=2) \
            .message("This Case Does Not Save Photo!") \
            .message("GIF order A = Undo/Redo drawing") \
            .message("GIF order B = Undo/Redo apply step")
        extra.append(extras.image('screenshot/test_edit_removal_undo_redo_B_steps.gif'))
        extra.append(extras.image('screenshot/test_edit_removal_undo_redo_A_steps.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
