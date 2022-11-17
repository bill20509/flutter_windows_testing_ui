from libs.YMK.locators import AnimationLocators
from libs.YMK import pages


class Animation(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_animation(self):
        self.wait_element_visible(AnimationLocators.Animation_button)
        self.click_element(AnimationLocators.Animation_button)
        return self

    def adjust_seekbar_to_right(self):
        self.wait_element_visible(AnimationLocators.seekbar)
        self.slidebar_to_right(AnimationLocators.seekbar)
        return self

    def adjust_seekbar_to_left(self):
        self.wait_element_visible(AnimationLocators.seekbar)
        self.slidebar_to_left(AnimationLocators.seekbar)
        return self

    def click_effects(self):
        self.wait_element_visible(AnimationLocators.EFFECTS)
        self.click_element(AnimationLocators.EFFECTS)
        return EFFECTS(self.driver)

    def click_stickers(self):
        self.wait_element_visible(AnimationLocators.STICKERS)
        self.click_element(AnimationLocators.STICKERS)
        return STICKERS(self.driver)

    def click_take_photo(self):
        self.wait_element_visible(AnimationLocators.take_photo)
        self.click_element(AnimationLocators.take_photo)
        return self

    def click_v(self):
        self.wait_element_visible(AnimationLocators.V_button)
        self.click_element(AnimationLocators.V_button)
        return Export(self.driver)

    def click_x(self):
        self.wait_element_visible(AnimationLocators.X_button)
        self.click_element(AnimationLocators.X_button)
        return self

    def click_play_cursor(self):
        self.wait_element_visible(AnimationLocators.play_cursor)
        self.click_element(AnimationLocators.play_cursor)
        return self


class EFFECTS(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def select_xxx_category(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(AnimationLocators.category_text, name)
                break
            except (ValueError, Exception):
                self.wait_element_visible(AnimationLocators.category_text_view)
                self.scroll_horizontal(AnimationLocators.category_text_view)
        return self

    def select_n_category(self, number):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.effect_icon)
                self.select_element_by_number(AnimationLocators.effect_icon, (number-1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(AnimationLocators.effect_view)
                self.scroll_horizontal(AnimationLocators.effect_view)
        return self

    def click_eraser(self):
        self.wait_element_visible(AnimationLocators.eraser_extend_button)
        self.click_element(AnimationLocators.eraser_extend_button)
        return self

    def click_detect(self):
        self.wait_element_visible(AnimationLocators.detect_button)
        self.click_element(AnimationLocators.detect_button)
        return self

    def click_draw(self):
        self.wait_element_visible(AnimationLocators.draw_button)
        self.click_element(AnimationLocators.draw_button)
        return self

    def click_erase(self):
        self.wait_element_visible(AnimationLocators.erase_button)
        self.click_element(AnimationLocators.erase_button)
        return self

    def select_stroke(self, number):
        self.wait_element_visible(AnimationLocators.brush_view)
        self.select_element_by_number(AnimationLocators.brush_view, (number-1))
        return self

    def click_effects_v_button(self):
        self.wait_element_visible(AnimationLocators.V_button)
        self.click_element(AnimationLocators.V_button)
        return Export(self.driver)

    def click_effects_x_button(self):
        self.wait_element_visible(AnimationLocators.X_button)
        self.click_element(AnimationLocators.X_button)
        return Animation(self.driver)

    def click_undo_button(self):
        self.wait_element_visible(AnimationLocators.undo_button)
        self.click_element(AnimationLocators.undo_button)
        return self

    def click_reset_button(self):
        self.wait_element_visible(AnimationLocators.reset_button)
        self.click_element(AnimationLocators.reset_button)
        return self


class STICKERS(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def select_n_sticker(self, number):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.sticker_icon)
                self.select_element_by_number(AnimationLocators.sticker_icon, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(AnimationLocators.sticker_view)
                self.scroll_horizontal(AnimationLocators.sticker_view)
        return self

    def click_cancel_button(self):
        self.wait_element_visible(AnimationLocators.X_button)
        self.click_element(AnimationLocators.X_button)
        return Animation(self.driver)

    def click_reset_button(self):
        self.wait_element_visible(AnimationLocators.reset_button)
        self.click_element(AnimationLocators.reset_button)
        return self

    def click_stickers_v_button(self):
        self.wait_element_visible(AnimationLocators.V_button)
        self.click_element(AnimationLocators.V_button)
        return Export(self.driver)


class Export(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def click_back_button(self):
        self.wait_element_visible(AnimationLocators.Export.back_button)
        self.click_element(AnimationLocators.Export.back_button)
        return Animation(self.driver)

    def click_export_button(self):
        self.wait_element_visible(AnimationLocators.Export.Export_button)
        self.click_element(AnimationLocators.Export.Export_button)
        self.wait_time(10)
        self.wait_element_invisible(AnimationLocators.Export.alert_dialog)
        self.wait_element_invisible(AnimationLocators.Export.Export_button, timeout=480)
        return pages.result_page.Result(self.driver)

    def click_video_button(self):
        self.wait_element_visible(AnimationLocators.Export.video_button)
        self.click_element(AnimationLocators.Export.video_button)
        return Video(self.driver)

    def click_gif_button(self):
        self.wait_element_visible(AnimationLocators.Export.GIF_button)
        self.click_element(AnimationLocators.Export.GIF_button)
        return GIF(self.driver)

    def click_instagram_button(self):
        self.wait_element_visible(AnimationLocators.Export.Instagram_button)
        self.click_element(AnimationLocators.Export.Instagram_button)
        return Instagram(self.driver)

    def click_facebook_button(self):
        self.wait_element_visible(AnimationLocators.Export.Facebook_button)
        self.click_element(AnimationLocators.Export.Facebook_button)
        return Facebook(self.driver)


class Video(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_original_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_original)
        self.click_element(AnimationLocators.Export.crop_original)
        return self

    def select_16to9_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_16to9)
        self.click_element(AnimationLocators.Export.crop_16to9)
        return self

    def select_1to1_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_1to1)
        self.click_element(AnimationLocators.Export.crop_1to1)
        return self

    def select_3to4_ratio(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.crop_3to4)
                self.click_element(AnimationLocators.Export.crop_3to4)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.Export.ratio_view)
        return Video(self.driver)

    def select_9to16_ratio(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.crop_9to16)
                self.click_element(AnimationLocators.Export.crop_9to16)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.Export.ratio_view)
        return Video(self.driver)

    def select_4to3_ratio(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.crop_4to3)
                self.click_element(AnimationLocators.Export.crop_4to3)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.Export.ratio_view)
        return Video(self.driver)

    def adjust_duration_to_right(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
                self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
                break
            except (ValueError, Exception):
                self.scroll_vertical(AnimationLocators.Export.ratio_view, 500)
        return Video(self.driver)

    def adjust_duration_to_left(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
                self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
                break
            except (ValueError, Exception):
                self.scroll_vertical(AnimationLocators.Export.ratio_view, 500)
        return Video(self.driver)

    def select_720p_quality(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.quality_720p)
                self.click_element(AnimationLocators.Export.quality_720p)
                break
            except (ValueError, Exception):
                self.scroll_vertical(AnimationLocators.Export.ratio_view, 1000)
        return Video(self.driver)

    def select_1080p_quality(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.quality_1080p)
                self.click_element(AnimationLocators.Export.quality_1080p)
                break
            except (ValueError, Exception):
                self.scroll_vertical(AnimationLocators.Export.ratio_view, 1000)
        return Video(self.driver)

    def select_4k_quality(self):
        for i in range(10):
            try:
                self.wait_element_visible(AnimationLocators.Export.quality_4k)
                self.click_element(AnimationLocators.Export.quality_4k)
                break
            except (ValueError, Exception):
                self.scroll_vertical(AnimationLocators.Export.ratio_view)
        return Video(self.driver)


class GIF(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_original_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_original)
        self.click_element(AnimationLocators.Export.crop_original)
        return self

    def select_16to9_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_16to9)
        self.click_element(AnimationLocators.Export.crop_16to9)
        return self

    def select_1to1_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_1to1)
        self.click_element(AnimationLocators.Export.crop_1to1)
        return self

    def select_3to4_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_3to4)
        self.click_element(AnimationLocators.Export.crop_3to4)
        return self

    def select_9to16_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_9to16)
        self.click_element(AnimationLocators.Export.crop_9to16)
        return self


class Instagram(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_feed_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_feed)
        self.click_element(AnimationLocators.Export.crop_feed)
        return self

    def select_story_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_story)
        self.click_element(AnimationLocators.Export.crop_story)
        return self

    def select_4to5_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_4to5)
        self.click_element(AnimationLocators.Export.crop_4to5)
        return self

    def adjust_duration_to_right(self):
        self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
        self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
        return self

    def adjust_duration_to_left(self):
        self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
        self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
        return self

    def select_720p_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_720p)
        self.click_element(AnimationLocators.Export.quality_720p)
        return self

    def select_1080p_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_1080p)
        self.click_element(AnimationLocators.Export.quality_1080p)
        return self

    def select_4k_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_4k)
        self.click_element(AnimationLocators.Export.quality_4k)
        return self


class Facebook(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_cover_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_cover)
        self.click_element(AnimationLocators.Export.crop_cover)
        return self

    def select_profile_ratio(self):
        self.wait_element_visible(AnimationLocators.Export.crop_profile)
        self.click_element(AnimationLocators.Export.crop_profile)
        return self

    def adjust_duration_to_right(self):
        self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
        self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
        return self

    def adjust_duration_to_left(self):
        self.wait_element_visible(AnimationLocators.Export.duration_seekbar)
        self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
        return self

    def select_720p_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_720p)
        self.click_element(AnimationLocators.Export.quality_720p)
        return self

    def select_1080p_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_1080p)
        self.click_element(AnimationLocators.Export.quality_1080p)
        return self

    def select_4k_quality(self):
        self.wait_element_visible(AnimationLocators.Export.quality_4k)
        self.click_element(AnimationLocators.Export.quality_4k)
        return self
