import pytest

from libs.YCP.locator import ePhotoPickerPage, eStickerPage, eMainPhotoPage, eColorPickerPanel, eEffectPage, \
    eRemovalPage, eMainPhotoEraserPage, eToolsCropRotatePage, eCutOutPage, eAdjustPage, eEditFeatureRoom, eBrushPage
from libs.YCP.pages.photo_edit import EffectsPage
from libs.app import App
from libs.YCP import pages
import time


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto()\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(2)\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)

    @pytest.mark.camera
    def test_edit_add_photo_add_10_photos(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel()\
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(0)\
            .select_photo_item(1)\
            .select_photo_item(2)\
            .select_photo_item(3)\
            .select_photo_item(4)\
            .select_photo_item(5)\
            .select_photo_item(6)\
            .select_photo_item(7)\
            .select_photo_item(8)\
            .select_photo_item(9)\
            .select_photo_item(10)\
            .screenshot('edit_add_photo_add_to_limitation', 1)\
            .click_v()\
            .screenshot('edit_add_photo_add_10_photos', 3)

    @pytest.mark.camera
    def test_edit_add_photo_add_more_photo(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit') \
            .select_photo_item(1)\
            .click_v()\
            .click_add_more()\
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(0)\
            .click_v()\
            .screenshot('edit_add_photo_add_more_photo', 1)

    @pytest.mark.camera
    def test_edit_add_photo_add_more_text(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_add_more()\
            .click_add_text()\
            .screenshot('edit_add_photo_add_more_text', 1)

    @pytest.mark.camera
    def test_edit_add_photo_add_more_stickers(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_add_more()\
            .click_add_stickers() \
            .select_sticker_panel_item(2) \
            .wait_progress_bar() \
            .wait_time(1) \
            .select_sticker_panel_item(2) \
            .screenshot('edit_add_photo_add_more_stickers', 1)

    @pytest.mark.camera
    def test_edit_add_photo_opacity(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_opacity()\
            .set_slider_bar(50)\
            .screenshot('edit_add_photo_opacity', 1)

    @pytest.mark.camera
    def test_edit_add_photo_border_color(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_border()\
            .select_color_item(2) \
            .set_intensity_value(100) \
            .screenshot('edit_add_photo_border_color', 1)

    @pytest.mark.camera
    def test_edit_add_photo_border_add_color(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_border()\
            .select_tool_item(1)\
            .click_add_color()\
            .screenshot('edit_add_photo_border_add_color', 1)

    @pytest.mark.camera
    def test_edit_add_photo_border_with_other_features(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo()\
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_border()\
            .select_color_item(2)\
            .set_intensity_value(100)\
            .click_opacity()\
            .set_slider_bar(50)\
            .click_blender()\
            .select_blender_tab('SCREEN')\
            .click_adjust()\
            .set_intensity_value(200)\
            .click_apply()\
            .screenshot('edit_add_photo_border_with_other_features', 1)

    @pytest.mark.camera
    def test_edit_add_photo_blender(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_blender()\
            .screenshot('edit_add_photo_blender_normal', 1)\
            .select_blender_tab('MULTIPLY')\
            .screenshot('edit_add_photo_blender_multiply', 1)\
            .select_blender_tab('SCREEN') \
            .screenshot('edit_add_photo_blender_screen', 1)\
            .select_blender_tab('OVERLAY') \
            .screenshot('edit_add_photo_blender_overlay', 1)\
            .select_blender_tab('SOFT LIGHT')\
            .screenshot('edit_add_photo_blender_soft_light', 1)\
            .select_blender_tab('HARD LIGHT') \
            .screenshot('edit_add_photo_blender_hard_light', 1)

    @pytest.mark.camera
    def test_edit_add_photo_effect_original(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_effects()\
            .screenshot('edit_add_photo_effect_original', 1)

    @pytest.mark.camera
    def test_edit_add_photo_effect_apply(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_effects() \
            .select_filter_item(1) \
            .select_filter('Auto Tone')\
            .set_intensity_bar(75)\
            .click_apply()\
            .screenshot('edit_add_photo_effect_apply', 1)

    @pytest.mark.camera
    def test_edit_add_photo_eraser_slider_bar(self):
        # Josh Can't swipe
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_eraser() \
            .select_dot_item(4)\
            .screenshot('edit_add_photo_eraser_slider_bar', 1)

    @pytest.mark.camera
    def test_edit_add_photo_eraser_auto_detect(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel()\
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_eraser() \
            .click_auto_detect()\
            .wait_progress_bar()\
            .click_apply()\
            .screenshot('edit_add_photo_eraser_auto_detect', 1)

    @pytest.mark.camera
    def test_edit_add_photo_eraser_undo_reset(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_eraser() \
            .click_auto_detect()\
            .wait_progress_bar()\
            .screenshot('edit_add_photo_eraser_undo_reset_before', 1)\
            .click_eraser_undo()\
            .screenshot('edit_add_photo_eraser_undo_after', 1)\
            .compare_photo('edit_add_photo_eraser_undo_reset_before', 'edit_add_photo_eraser_undo_after',
                           'edit_add_photo_eraser_undo')\
            .click_auto_detect()\
            .wait_progress_bar()\
            .click_reset()\
            .screenshot('edit_add_photo_eraser_reset_after', 1) \
            .compare_photo('edit_add_photo_eraser_undo_reset_before', 'edit_add_photo_eraser_reset_after',
                           'edit_add_photo_eraser_reset')

    @pytest.mark.camera
    def test_edit_add_photo_corp_with_other_features(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_eraser() \
            .click_auto_detect()\
            .wait_progress_bar()\
            .click_add_photo_apply()\
            .click_crop_and_rotate()\
            .screenshot('edit_add_photo_corp_with_other_features', 1)

    @pytest.mark.camera
    def test_edit_add_photo_corp_flip_rotate(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_crop_and_rotate()\
            .click_image_2x3()\
            .click_image_mirror()\
            .click_image_rotate()\
            .click_apply()\
            .screenshot('edit_add_photo_corp_flip_rotate', 1)

    @pytest.mark.camera
    def test_edit_add_photo_corp_reset(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_crop_and_rotate()\
            .click_image_2x3()\
            .click_image_mirror()\
            .click_image_rotate()\
            .screenshot('edit_add_photo_corp_reset_before', 1)\
            .click_crop_reset()\
            .screenshot('edit_add_photo_corp_reset_after', 1)\
            .compare_photo('edit_add_photo_corp_reset_before', 'edit_add_photo_corp_reset_after',
                           'edit_add_photo_corp_reset')

    @pytest.mark.camera
    def test_edit_add_photo_cutout_auto_detect(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_cutout() \
            .click_auto_detect()\
            .wait_progress_bar()\
            .click_apply()\
            .screenshot('edit_add_photo_cutout_auto_detect', 1)

    @pytest.mark.camera
    def test_edit_add_photo_cutout_undo_reset(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_cutout() \
            .click_auto_detect() \
            .wait_progress_bar() \
            .screenshot('edit_add_photo_cutout_undo_reset_before', 1)\
            .click_undo()\
            .screenshot('edit_add_photo_cutout_undo_after', 1)\
            .compare_photo('edit_add_photo_cutout_undo_reset_before', 'edit_add_photo_cutout_undo_after',
                           'edit_add_photo_cutout_undo')\
            .click_auto_detect()\
            .wait_progress_bar()\
            .click_reset()\
            .screenshot('edit_add_photo_cutout_reset_after', 1) \
            .compare_photo('edit_add_photo_cutout_undo_reset_before', 'edit_add_photo_cutout_reset_after',
                           'edit_add_photo_cutout_reset')

    @pytest.mark.camera
    def test_edit_add_photo_adjust(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit') \
            .select_photo_item(1) \
            .click_v() \
            .click_adjust()\
            .set_intensity_value(150)\
            .select_feature('Contrast')\
            .set_intensity_value(200)\
            .select_feature('Brightness') \
            .set_intensity_value(200)\
            .select_feature('Highlights') \
            .set_intensity_value(200)\
            .select_feature('Shadows') \
            .set_intensity_value(200)\
            .select_feature('Light') \
            .set_intensity_value(200)\
            .select_feature('Dark') \
            .set_intensity_value(200)\
            .select_feature('Saturation') \
            .set_intensity_value(200)\
            .select_feature('Temperature') \
            .set_intensity_value(200)\
            .select_feature('Tint') \
            .set_intensity_value(200)\
            .select_feature('Sharpen') \
            .set_intensity_value(200)\
            .click_apply()\
            .screenshot('edit_add_photo_adjust', 1)

    @pytest.mark.camera
    def test_edit_add_photo_duplicate(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_duplicate()\
            .screenshot('edit_add_photo_duplicate', 1)\
            .click_undo() \
            .screenshot('edit_add_photo_duplicate_undo', 1) \
            .click_redo() \
            .screenshot('edit_add_photo_duplicate_redo', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_opacity(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_opacity() \
            .set_slider_bar(50) \
            .screenshot('edit_add_photo_sticker_opacity', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_border(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_border()\
            .select_color_item(2) \
            .set_intensity_value(100) \
            .screenshot('edit_add_photo_sticker_border', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_border_add_color(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_border()\
            .select_tool_item(1)\
            .click_add_color()\
            .screenshot('edit_add_photo_sticker_border_add_color', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_blender(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_blender() \
            .select_blender_tab('SCREEN') \
            .screenshot('edit_add_photo_sticker_blender', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_effect(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_effects() \
            .select_filter_item(1) \
            .select_filter('Auto Tone') \
            .set_intensity_bar(75) \
            .screenshot('edit_add_photo_sticker_effect', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_crop(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_crop_and_rotate()\
            .click_image_2x3()\
            .click_image_mirror()\
            .click_image_rotate()\
            .click_apply()\
            .screenshot('edit_add_photo_sticker_crop', 1)

    @pytest.mark.camera
    def test_edit_add_photo_sticker_adjust(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1) \
            .click_v() \
            .click_add_more()\
            .click_add_stickers()\
            .select_sticker_panel_item(2)\
            .wait_progress_bar()\
            .wait_time(1)\
            .select_sticker_panel_item(2)\
            .select_sticker_panel_item(3)\
            .click_undo() \
            .click_adjust()\
            .set_intensity_value(150)\
            .select_feature('Contrast')\
            .set_intensity_value(200)\
            .click_apply()\
            .screenshot('edit_add_photo_sticker_adjust', 1)

    @pytest.mark.camera
    def test_edit_add_photo_layer(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(0)\
            .select_photo_item(1)\
            .select_photo_item(2)\
            .select_photo_item(3)\
            .select_photo_item(4)\
            .select_photo_item(5)\
            .select_photo_item(6)\
            .select_photo_item(7)\
            .select_photo_item(8)\
            .select_photo_item(9)\
            .click_v() \
            .screenshot('edit_add_photo_layer_original', 3)\
            .click_layer_down()\
            .screenshot('edit_add_photo_layer_down_button', 1)\
            .compare_photo('edit_add_photo_layer_original', 'edit_add_photo_layer_down_button',
                           'edit_add_photo_layer_down')\
            .click_layer_up()\
            .screenshot('edit_add_photo_layer_up_button', 1) \
            .compare_photo('edit_add_photo_layer_down_button', 'edit_add_photo_layer_up_button',
                           'edit_add_photo_layer_up')

    @pytest.mark.camera
    def test_edit_add_photo_x(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_opacity()\
            .set_slider_bar(50)\
            .click_add_photo_close()\
            .click_dialog_yes()\
            .screenshot('edit_add_photo_x_no', 1) \
            .click_add_photo_close()\
            .click_dialog_no()\
            .screenshot('edit_add_photo_x_yes', 1)

    @pytest.mark.camera
    def test_edit_add_photo_v(self):
        # Josh
        self.app.deeplink_to_photo_edit() \
            .wait_loading_panel() \
            .click_add_photo() \
            .select_album_item('a_edit')\
            .select_photo_item(1)\
            .click_v()\
            .click_opacity()\
            .set_slider_bar(50)\
            .click_add_photo_apply()\
            .click_dialog_no()\
            .screenshot('edit_add_photo_v_later', 1)\
            .click_add_photo_apply()\
            .click_dialog_yes()\
            .screenshot('edit_add_photo_v_yes', 1)\
            .click_save()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_add_photo_add_more_stickers()

