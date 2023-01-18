import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from libs.YMK.locators import ResultLocators, PhotoMakeupLocators, LauncherLocators, PickPhotoLocators, MakeupCamLocators
import time
from pytest_html import extras

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
    def test_live_makeup_foundation(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Foundation ") \
            .select_brand("PERFECT") \
            .click_none_button() \
            .screenshot("test_live_makeup_foundation_before") \
            .select_color(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_foundation_color_1") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_foundation_intensity_100") \
            .select_color(2) \
            .wait_time(2) \
            .screenshot("test_live_makeup_foundation_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_foundation") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_foundation_video") \
            .compose_gif("test_live_makeup_foundation_color", 'screenshot/test_live_makeup_foundation_before.png'
                         , 'screenshot/test_live_makeup_foundation_color_1.png'
                         , 'screenshot/test_live_makeup_foundation_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_foundation_intensity", 'screenshot/test_live_makeup_foundation_before.png'
                         , 'screenshot/test_live_makeup_foundation_color_1.png'
                         , 'screenshot/test_live_makeup_foundation_intensity_100.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_foundation_video.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_foundation.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_foundation_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_foundation_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_blush(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Blush ") \
            .select_brand("PERFECT") \
            .click_none_button() \
            .screenshot("test_live_makeup_blush_before") \
            .select_color(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_blush_color_1") \
            .select_color(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_blush_color_2") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_blush_intensity_100") \
            .select_pattern(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_blush_pattern_1") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_blush") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_blush") \
            .compose_gif("test_live_makeup_blush_color", 'screenshot/test_live_makeup_blush_before.png'
                         , 'screenshot/test_live_makeup_blush_color_1.png'
                         , 'screenshot/test_live_makeup_blush_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_blush_intensity", 'screenshot/test_live_makeup_blush_before.png'
                         , 'screenshot/test_live_makeup_blush_color_2.png'
                         , 'screenshot/test_live_makeup_blush_intensity_100.png', speed=1) \
            .compose_gif("test_live_makeup_blush_pattern", 'screenshot/test_live_makeup_blush_before.png'
                         , 'screenshot/test_live_makeup_blush_intensity_100.png'
                         , 'screenshot/test_live_makeup_blush_pattern_1.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_blush.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_blush.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_blush_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_blush_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_blush_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_eyeliner(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Eyeliner ") \
            .select_brand("PERFECT") \
            .click_none_button() \
            .screenshot("test_live_makeup_eyeliner_before") \
            .select_color(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeliner_color_1") \
            .select_pattern(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeliner_pattern_1") \
            .select_color(5) \
            .select_color(6) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeliner_color_2") \
            .slide_bar_to_down() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeliner_intensity_0") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeliner_intensity_100") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_eyeliner") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_eyeliner") \
            .compose_gif("test_live_makeup_eyeliner_color", 'screenshot/test_live_makeup_eyeliner_before.png'
                         , 'screenshot/test_live_makeup_eyeliner_pattern_1.png'
                         , 'screenshot/test_live_makeup_eyeliner_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_eyeliner_intensity", 'screenshot/test_live_makeup_eyeliner_before.png'
                         , 'screenshot/test_live_makeup_eyeliner_intensity_0.png'
                         , 'screenshot/test_live_makeup_eyeliner_color_2.png'
                         , 'screenshot/test_live_makeup_eyeliner_intensity_100.png', speed=1) \
            .compose_gif("test_live_makeup_eyeliner_pattern", 'screenshot/test_live_makeup_eyeliner_before.png'
                         , 'screenshot/test_live_makeup_eyeliner_color_1.png'
                         , 'screenshot/test_live_makeup_eyeliner_pattern_1.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_eyeliner.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_eyeliner.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_eyeliner_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyeliner_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyeliner_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_eyelashes(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Eyelashes ") \
            .select_brand("PERFECT") \
            .click_none_button() \
            .screenshot("test_live_makeup_eyelashes_before") \
            .select_color(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyelashes_color_1") \
            .select_color(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyelashes_color_2") \
            .slide_bar_to_down() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyelashes_intensity_0") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyelashes_intensity_100") \
            .select_pattern(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyelashes_pattern_1") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_eyelashes") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_eyelashes") \
            .compose_gif("test_live_makeup_eyelashes_color", 'screenshot/test_live_makeup_eyelashes_before.png'
                         , 'screenshot/test_live_makeup_eyelashes_color_1.png'
                         , 'screenshot/test_live_makeup_eyelashes_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_eyelashes_intensity", 'screenshot/test_live_makeup_eyelashes_before.png'
                         , 'screenshot/test_live_makeup_eyelashes_intensity_0.png'
                         , 'screenshot/test_live_makeup_eyelashes_color_2.png'
                         , 'screenshot/test_live_makeup_eyelashes_intensity_100.png', speed=1) \
            .compose_gif("test_live_makeup_eyelashes_pattern", 'screenshot/test_live_makeup_eyelashes_before.png'
                         , 'screenshot/test_live_makeup_eyelashes_intensity_100.png'
                         , 'screenshot/test_live_makeup_eyelashes_pattern_1.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_eyelashes.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_eyelashes.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_eyelashes_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyelashes_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyelashes_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_eyebrows(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Eyebrows ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_before") \
            .select_color(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_color_1") \
            .slide_bar_to_top_vertical_1() \
            .screenshot("test_live_makeup_eyebrows_intensity_100") \
            .select_color(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_color_2") \
            .select_pattern(3) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_pattern_1") \
            .slide_bar_to_down_vertical_2() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_shape_0") \
            .slide_bar_to_top_vertical_2() \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyebrows_shape_100") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_eyebrows") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_eyebrows") \
            .compose_gif("test_live_makeup_eyebrows_color", 'screenshot/test_live_makeup_eyebrows_before.png'
                         , 'screenshot/test_live_makeup_eyebrows_color_1.png'
                         , 'screenshot/test_live_makeup_eyebrows_intensity_100.png'
                         , 'screenshot/test_live_makeup_eyebrows_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_eyebrows_pattern", 'screenshot/test_live_makeup_eyebrows_before.png'
                         , 'screenshot/test_live_makeup_eyebrows_color_2.png'
                         , 'screenshot/test_live_makeup_eyebrows_pattern_1.png', speed=1) \
            .compose_gif("test_live_makeup_eyebrows_shape", 'screenshot/test_live_makeup_eyebrows_before.png'
                         , 'screenshot/test_live_makeup_eyebrows_shape_0.png'
                         , 'screenshot/test_live_makeup_eyebrows_shape_100.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_eyebrows.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_eyebrows.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_eyebrows_shape.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyebrows_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyebrows_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_eyeshadow(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Eye Shadow ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeshadow_before") \
            .select_palette(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeshadow_palette_1") \
            .select_palette(2) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eyeshadow_palette_2") \
            .click_shimmer_button() \
            .wait_time(5) \
            .screenshot("test_live_makeup_eyeshadow_shimmer_1") \
            .click_shimmer_button() \
            .wait_time(5) \
            .screenshot("test_live_makeup_eyeshadow_shimmer_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_eyeshadow") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_eyeshadow") \
            .compose_gif("test_live_makeup_eyeshadow_palette", 'screenshot/test_live_makeup_eyeshadow_before.png'
                         , 'screenshot/test_live_makeup_eyeshadow_palette_1.png'
                         , 'screenshot/test_live_makeup_eyeshadow_palette_2.png', speed=1) \
            .compose_gif("test_live_makeup_eyeshadow_shimmer", 'screenshot/test_live_makeup_eyeshadow_before.png'
                         , 'screenshot/test_live_makeup_eyeshadow_shimmer_1.png'
                         , 'screenshot/test_live_makeup_eyeshadow_shimmer_2.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_eyeshadow.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_eyeshadow.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_eyeshadow_shimmer.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eyeshadow_palette.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_lip_art(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Lip Color ") \
            .select_brand("PERFECT") \
            .click_element_by_text("LIP ART") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_art_before") \
            .select_lip_art_pattern(1) \
            .wait_time(5) \
            .screenshot("test_live_makeup_lip_art_pattern_1") \
            .select_lip_art_pattern(2) \
            .wait_time(5) \
            .screenshot("test_live_makeup_lip_art_pattern_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_lip_art") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_lip_art") \
            .compose_gif("test_live_makeup_lip_art", 'screenshot/test_live_makeup_lip_art_before.png'
                         , 'screenshot/test_live_makeup_lip_art_pattern_1.png'
                         , 'screenshot/test_live_makeup_lip_art_pattern_2.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_lip_art.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_lip_art.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_art.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_lip_single_color(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Lip Color ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_before") \
            .select_color(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_1") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_intensity") \
            .select_color(2) \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_lip_single_color") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_lip_single_color") \
            .compose_gif("test_live_makeup_lip_single_color", 'screenshot/test_live_makeup_lip_single_color_before.png'
                         , 'screenshot/test_live_makeup_lip_single_color_intensity.png'
                         , 'screenshot/test_live_makeup_lip_single_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_lip_single_color_intensity", 'screenshot/test_live_makeup_lip_single_color_before.png'
                         , 'screenshot/test_live_makeup_lip_single_color_1.png'
                         , 'screenshot/test_live_makeup_lip_single_color_intensity.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_lip_single_color.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_lip_single_color.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_single_color_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_single_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_lip_color_effect(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Lip Color ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_color_before") \
            .click_element_by_text("2 COLORS") \
            .select_color(1) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_2_color_1") \
            .select_color(2) \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_2_color_2") \
            .click_element_by_text("OMBRE") \
            .select_color(1) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_ombre_color_1") \
            .select_color(2) \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_ombre_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_lip_color_effect") \
            .compose_gif("test_live_makeup_lip_2_color", 'screenshot/test_live_makeup_lip_color_before.png'
                         , 'screenshot/test_live_makeup_lip_2_color_1.png'
                         , 'screenshot/test_live_makeup_lip_2_color_2.png', speed=1) \
            .compose_gif("test_live_makeup_lip_ombre_color", 'screenshot/test_live_makeup_lip_color_before.png'
                         , 'screenshot/test_live_makeup_lip_ombre_color_1.png'
                         , 'screenshot/test_live_makeup_lip_ombre_color_2.png', speed=1)
        extra.append(extras.image('savephoto/test_live_makeup_lip_color_effect.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_ombre_color.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_2_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_lip_single_color_texture(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Lip Color ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .select_color(1) \
            .wait_time(2) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Sheer") \
            .select_texture("Matte") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Matte") \
            .select_texture("Gloss") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Gloss") \
            .select_texture("Satin") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Satin") \
            .select_texture("Shimmer") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Shimmer") \
            .select_texture("Metallic") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Metallic") \
            .select_texture("Holographic") \
            .wait_time(2) \
            .screenshot("test_live_makeup_lip_single_color_Holographic") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_lip_single_color_texture") \
            .compose_gif("test_live_makeup_lip_single_color_texture", 'screenshot/test_live_makeup_lip_single_color_Sheer.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Matte.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Gloss.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Satin.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Shimmer.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Metallic.png'
                         , 'screenshot/test_live_makeup_lip_single_color_Holographic.png', speed=1)
        extra.append(extras.image('savephoto/test_live_makeup_lip_single_color_texture.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_lip_single_color_texture.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_eye_color(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Eye Color ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_eye_color_before") \
            .select_pattern(3) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eye_pattern_1") \
            .select_pattern(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eye_pattern_2") \
            .select_color(5) \
            .wait_time(2) \
            .screenshot("test_live_makeup_eye_pattern_2_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_eye_color") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_eye_color") \
            .compose_gif("test_live_makeup_eye_pattern", 'screenshot/test_live_makeup_eye_color_before.png'
                         , 'screenshot/test_live_makeup_eye_pattern_2.png'
                         , 'screenshot/test_live_makeup_eye_pattern_1.png', speed=1) \
            .compose_gif("test_live_makeup_eye_pattern_color", 'screenshot/test_live_makeup_eye_color_before.png'
                         , 'screenshot/test_live_makeup_eye_pattern_2.png'
                         , 'screenshot/test_live_makeup_eye_pattern_2_color_2.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_eye_color.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_eye_color.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_eye_pattern_color.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_eye_pattern.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_contour(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Contour ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_contour_before") \
            .select_pattern(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_contour_pattern_1") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_contour_pattern_1_intensity_100") \
            .select_pattern(3) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_contour_pattern_2") \
            .select_palette(2) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_contour_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_contour") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_contour") \
            .compose_gif("test_live_makeup_contour_intensity", 'screenshot/test_live_makeup_contour_before.png'
                         , 'screenshot/test_live_makeup_contour_pattern_1.png'
                         , 'screenshot/test_live_makeup_contour_pattern_1_intensity_100.png', speed=1) \
            .compose_gif("test_live_makeup_contour_pattern", 'screenshot/test_live_makeup_contour_before.png'
                         , 'screenshot/test_live_makeup_contour_pattern_1_intensity_100.png'
                         , 'screenshot/test_live_makeup_contour_pattern_2.png', speed=1) \
            .compose_gif("test_live_makeup_contour_color", 'screenshot/test_live_makeup_contour_before.png'
                         , 'screenshot/test_live_makeup_contour_pattern_2.png'
                         , 'screenshot/test_live_makeup_contour_color_2.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_contour.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_contour.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_contour_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_contour_intensity.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_contour_color.gif'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_live_makeup_highlight(self, extra):
        self.app.deeplink_to_makeupcam() \
            .select_makeup() \
            .select_feature_list(" Highlight ") \
            .select_brand("PERFECT") \
            .wait_time(2) \
            .screenshot("test_live_makeup_highlight_before") \
            .select_pattern(1) \
            .wait_time(2) \
            .screenshot("test_live_makeup_highlight_pattern_1") \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_highlight_pattern_1_intensity_100") \
            .select_pattern(3) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_highlight_pattern_2") \
            .select_palette(3) \
            .slide_bar_to_top() \
            .wait_time(2) \
            .screenshot("test_live_makeup_highlight_color_2") \
            .click_capture() \
            .click_photo_save() \
            .pull_photo_from_device("test_live_makeup_highlight") \
            .panel_close() \
            .switch_to_video_mode() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .pull_video_from_device("mp4", "test_live_makeup_highlight") \
            .compose_gif("test_live_makeup_highlight_intensity", 'screenshot/test_live_makeup_highlight_before.png'
                         , 'screenshot/test_live_makeup_highlight_pattern_1.png'
                         , 'screenshot/test_live_makeup_highlight_pattern_1_intensity_100.png', speed=1) \
            .compose_gif("test_live_makeup_highlight_pattern", 'screenshot/test_live_makeup_highlight_before.png'
                         , 'screenshot/test_live_makeup_highlight_pattern_1_intensity_100.png'
                         , 'screenshot/test_live_makeup_highlight_pattern_2.png', speed=1) \
            .compose_gif("test_live_makeup_highlight_color", 'screenshot/test_live_makeup_highlight_before.png'
                         , 'screenshot/test_live_makeup_highlight_pattern_2.png'
                         , 'screenshot/test_live_makeup_highlight_color_2.png', speed=1)
        extra.append(extras.video('savephoto/test_live_makeup_highlight.mp4'))
        extra.append(extras.image('savephoto/test_live_makeup_highlight.jpg'))
        extra.append(extras.image('screenshot/test_live_makeup_highlight_color.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_highlight_pattern.gif'))
        extra.append(extras.image('screenshot/test_live_makeup_highlight_intensity.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_live_makeup_foundation()
    # t.teardown_method()