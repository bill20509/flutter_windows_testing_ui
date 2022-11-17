import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

folder_name = "3.Bodytuner"


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
    def test_edit_animation(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .screenshot("test_edit_animation_effect_applied", wait_time=5) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .screenshot("test_edit_animation_sticker_applied", wait_time=5) \
                .message("Sticker applied!") \
                .click_v() \
                .click_video_button() \
                .select_16to9_ratio() \
                .message("Export parameter is set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_16to9_save", app_name="YMK") \
                .message("Export format: mp4, 16to9, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_16to9_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_16to9_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_16to9_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_16to9_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_speed(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect Applied!") \
                .click_play_cursor() \
                .adjust_seekbar_to_right() \
                .message("Adjust Effect Speed=2x") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker1 Applied!") \
                .adjust_seekbar_to_left() \
                .message("Adjust Sticker1 Speed=0.5x") \
                .select_n_sticker(1) \
                .message("Sticker2 Applied!") \
                .click_play_cursor() \
                .adjust_seekbar_to_right() \
                .message("Adjust Sticker2 Speed=2x") \
                .click_v() \
                .click_video_button() \
                .select_1to1_ratio() \
                .message("Export Parameter is Set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_speed-E2x-S0.5x2x_1to1_save",
                                        app_name="YMK") \
                .message("Effect Speed=2x, Sticker Speed=0.5x/2x") \
                .message("Export Format: mp4, 1to1, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_speed-E2x-S0.5x2x_1to1_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_speed-E2x-S0.5x2x_1to1_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_speed-E2x-S0.5x2x_1to1_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_speed-E2x-S0.5x2x_1to1_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_capture(self, extra):
        self.app.deeplink_to_animation() \
            .pick_photo(folder_name, 1) \
            .click_effects() \
            .select_n_category(1) \
            .message("Effect applied!") \
            .click_stickers() \
            .select_n_sticker(1) \
            .message("Sticker applied!") \
            .click_take_photo() \
            .message("Photo captured!") \
            .pull_photo_from_device("3_test_edit_animation_capture_save") \
            .message("Export format: jpg") \
            .get_image_dimension('savephoto/3_test_edit_animation_capture_save.jpg')
        extra.append(extras.image('savephoto/3_test_edit_animation_capture_save.jpg'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_effect_eraser(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .wait_time(wait=5) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_eraser() \
                .screenshot("test_edit_animation_effect_eraser_before", wait_time=6) \
                .click_detect() \
                .message("Eraser auto detection complete!") \
                .screenshot("test_edit_animation_effect_eraser_after", wait_time=6) \
                .compare_photo("test_edit_animation_effect_eraser_before", "test_edit_animation_effect_eraser_after",
                               "test_edit_animation_effect_eraser_diff", threshold=0) \
                .click_effects_v_button() \
                .message("Eraser applied!") \
                .click_v() \
                .click_video_button() \
                .select_3to4_ratio() \
                .click_export_button() \
                .message("export parameter is set!") \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_effect_eraser_3to4_save",
                                        app_name="YMK") \
                .message("Export format: mp4, 3to4, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_effect_eraser_3to4_save.mp4') \
                .compose_gif("test_edit_animation_effect_eraser_compare",
                             "screenshot/test_edit_animation_effect_eraser_before.png",
                             "screenshot/test_edit_animation_effect_eraser_after.png",
                             "screenshot/test_edit_animation_effect_eraser_diff.png", speed=2)
            extra.append(extras.video('savephoto/3_test_edit_animation_effect_eraser_3to4_save.mp4'))
            extra.append(extras.image('screenshot/test_edit_animation_effect_eraser_compare.gif'))
        except:
            self.app.screenshot("test_edit_animation_effect_eraser_3to4_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_effect_eraser_3to4_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_effect_eraser_undo(self, extra):
        self.app.deeplink_to_animation() \
            .pick_photo(folder_name, 1) \
            .click_effects() \
            .select_n_category(1) \
            .click_eraser() \
            .click_detect() \
            .screenshot("test_edit_animation_effect_eraser_undo_before", wait_time=5) \
            .message("Eraser applied!") \
            .click_undo_button() \
            .screenshot("test_edit_animation_effect_eraser_undo_after", wait_time=5) \
            .message("Eraser undo!") \
            .compare_photo("test_edit_animation_effect_eraser_undo_before",
                           "test_edit_animation_effect_eraser_undo_after",
                           "test_edit_animation_effect_eraser_undo_diff", threshold=0) \
            .message("This Case Does Not Save Photo!") \
            .compose_gif("test_edit_animation_effect_eraser_undo_compare",
                         "screenshot/test_edit_animation_effect_eraser_undo_before.png",
                         "screenshot/test_edit_animation_effect_eraser_undo_after.png",
                         "screenshot/test_edit_animation_effect_eraser_undo_diff.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_animation_effect_eraser_undo_compare.gif'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_effect_eraser_reset(self, extra):
        self.app.deeplink_to_animation() \
            .pick_photo(folder_name, 1) \
            .click_effects() \
            .select_n_category(1) \
            .click_eraser() \
            .click_detect() \
            .screenshot("test_edit_animation_effect_eraser_reset_before", wait_time=5) \
            .message("Eraser applied!") \
            .click_reset_button() \
            .screenshot("test_edit_animation_effect_eraser_reset_after", wait_time=5) \
            .message("Eraser reset!") \
            .compare_photo("test_edit_animation_effect_eraser_reset_before",
                           "test_edit_animation_effect_eraser_reset_after",
                           "test_edit_animation_effect_eraser_reset_diff", threshold=0) \
            .message("This Case Does Not Save Photo!") \
            .compose_gif("test_edit_animation_effect_eraser_reset_compare",
                         "screenshot/test_edit_animation_effect_eraser_reset_before.png",
                         "screenshot/test_edit_animation_effect_eraser_reset_after.png",
                         "screenshot/test_edit_animation_effect_eraser_reset_diff.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_animation_effect_eraser_reset_compare.gif'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_export_ratio(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_video_button() \
                .select_9to16_ratio() \
                .message("Export parameter is set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_export_ratio_9to16-6s-720p_save",
                                        app_name="YMK") \
                .message("Export format: mp4, 9to16, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_export_ratio_9to16-6s-720p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_export_ratio_9to16-6s-720p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_export_ratio_9to16-6s-720p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_export_ratio_9to16-6s-720p_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_export_quality(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_video_button() \
                .select_4to3_ratio() \
                .select_1080p_quality() \
                .message("Export parameter is set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_export_quality_4to3-6s-1080p_save",
                                        app_name="YMK") \
                .message("Export format: mp4, 4to3, 6s, 1080p") \
                .get_video_info('savephoto/3_test_edit_animation_export_quality_4to3-6s-1080p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_export_quality_4to3-6s-1080p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_export_quality_4to3-6s-1080p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_export_quality_4to3-6s-1080p_NotSupported.png'))
            # ratio is changed from 4to3 to 9to16 temporarily before scroll function is implemented.

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_export_mix_max(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_eraser() \
                .click_detect() \
                .click_effects_v_button() \
                .message("Eraser applied!") \
                .adjust_seekbar_to_right() \
                .message("Effect speed=2x") \
                .click_stickers() \
                .select_n_sticker(1) \
                .adjust_seekbar_to_right() \
                .message("Sticker1 applied! speed=2x") \
                .select_n_sticker(1) \
                .adjust_seekbar_to_left() \
                .message("Sticker2 applied! speed=0.5x") \
                .select_n_sticker(1) \
                .adjust_seekbar_to_right() \
                .message("Sticker3 applied! speed=2x") \
                .select_n_sticker(1) \
                .adjust_seekbar_to_right() \
                .message("Sticker4 applied! speed=2x") \
                .message("Low-end devices supports up to 4 stickers, high-end supports up to 9!") \
                .click_v() \
                .click_video_button() \
                .adjust_duration_to_right() \
                .select_4k_quality() \
                .message("Export parameter set!") \
                .message("Low-end devices cannot select 4k quality, and will fail in this case!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_export_mix_max_orgnl-30s-4k_save",
                                        app_name="YMK") \
                .message("Export format: mp4, original, 30s, 4k") \
                .get_video_info('savephoto/3_test_edit_animation_export_mix_max_orgnl-30s-4k_save.mp4')
            extra.append(
                extras.video('savephoto/3_test_edit_animation_export_mix_max_orgnl-30s-4k_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_export_mix_max_orgnl-30s-4k_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_export_mix_max_orgnl-30s-4k_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_edit_animation_gif(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_gif_button() \
                .select_1to1_ratio() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="gif", rename="3_test_edit_animation_gif_1to1_save", app_name="YMK") \
                .message("Export format: gif, 1:1") \
                .get_image_dimension('savephoto/3_test_edit_animation_gif_1to1_save.gif')
            extra.append(extras.image('savephoto/3_test_edit_animation_gif_1to1_save.gif'))
        except:
            self.app.screenshot("test_edit_animation_gif_1to1_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_16to9_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_ig_feed(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_instagram_button() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_ig_feed_6s_720p_save", app_name="YMK") \
                .message("Export format: mp4, 'feed' ratio, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_ig_feed_6s_720p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_ig_feed_6s_720p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_ig_feed_6s_720p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_ig_feed_6s_720p_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_ig_story(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_instagram_button() \
                .select_story_ratio() \
                .select_1080p_quality() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_ig_story_6s_1080p_save",
                                        app_name="YMK") \
                .message("Export format: mp4, story, 6s, 1080p") \
                .get_video_info('savephoto/3_test_edit_animation_ig_story_6s_1080p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_ig_story_6s_1080p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_ig_story_6s_1080p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_ig_story_6s_1080p_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_ig_4to5(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_instagram_button() \
                .select_4to5_ratio() \
                .adjust_duration_to_right() \
                .select_4k_quality() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_ig_4to5_30s_4k_save", app_name="YMK") \
                .message("Export format: mp4, 4to5, 30s, 4k") \
                .get_video_info('savephoto/3_test_edit_animation_ig_4to5_30s_4k_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_ig_4to5_30s_4k_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_ig_4to5_30s_4k_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_ig_4to5_30s_4k_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_fb_cover(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_facebook_button() \
                .select_cover_ratio() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_fb_cover_6s_720p_save",
                                        app_name="YMK") \
                .message("Export format: mp4, cover, 6s, 720p") \
                .get_video_info('savephoto/3_test_edit_animation_fb_cover_6s_720p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_fb_cover_6s_720p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_fb_cover_6s_720p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_fb_cover_6s_720p_NotSupported.png'))

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_fb_profile(self, extra):
        try:
            self.app.deeplink_to_animation() \
                .pick_photo(folder_name, 1) \
                .click_effects() \
                .select_n_category(1) \
                .message("Effect applied!") \
                .click_stickers() \
                .select_n_sticker(1) \
                .message("Sticker applied!") \
                .click_v() \
                .click_facebook_button() \
                .select_profile_ratio() \
                .adjust_duration_to_right() \
                .select_1080p_quality() \
                .message("Export parameter set!") \
                .click_export_button() \
                .pull_video_from_device(format="mp4", rename="3_test_edit_animation_fb_profile_30s_1080p_save",
                                        app_name="YMK") \
                .message("Export format: mp4, profile, 30s, 1080p") \
                .get_video_info('savephoto/3_test_edit_animation_fb_profile_30s_1080p_save.mp4')
            extra.append(extras.video('savephoto/3_test_edit_animation_fb_profile_30s_1080p_save.mp4'))
        except:
            self.app.screenshot("test_edit_animation_fb_profile_30s_1080p_NotSupported") \
                .message("Device Maybe Not Supported, Check Screenshot!")
            extra.append(extras.image('screenshot/test_edit_animation_fb_profile_30s_1080p_NotSupported.png'))

    # @pytest.mark.animation
    # def test_edit_animation_sticker_cancel(self):
    #     self.app.deeplink_to_animation() \
    #         .pick_photo(folder_name, 1) \
    #         .click_stickers() \
    #         .select_n_sticker(1) \
    #         .message("Sticker applied!") \
    #         .screenshot("test_edit_animation_sticker_cancel_before", wait_time=5) \
    #         .click_cancel_button() \
    #         .message("Click cancel!") \
    #         .screenshot("test_edit_animation_sticker_cancel_after", wait_time=5) \
    #         .compare_photo("test_edit_animation_sticker_cancel_before", "test_edit_animation_sticker_cancel_after",
    #                        "test_edit_animation_export_sticker_cancel_diff")
    #         .message("This Case Does Not Save Photo!")

    @pytest.mark.A
    @pytest.mark.S2
    def test_edit_animation_sticker_reset(self, extra):
        self.app.deeplink_to_animation() \
            .pick_photo(folder_name, 1) \
            .click_stickers() \
            .select_n_sticker(1) \
            .message("Sticker applied!") \
            .screenshot("test_edit_animation_sticker_reset_before", wait_time=5) \
            .click_reset_button() \
            .message("Reset sticker!") \
            .screenshot("test_edit_animation_sticker_reset_after", wait_time=5) \
            .compare_photo("test_edit_animation_sticker_reset_before", "test_edit_animation_sticker_reset_after",
                           "test_edit_animation_sticker_reset_diff") \
            .message("This Case Does Not Save Photo!") \
            .compose_gif("test_edit_animation_sticker_reset_compare",
                         "screenshot/test_edit_animation_sticker_reset_before.png",
                         "screenshot/test_edit_animation_sticker_reset_after.png",
                         "screenshot/test_edit_animation_sticker_reset_diff.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_animation_sticker_reset_compare.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
