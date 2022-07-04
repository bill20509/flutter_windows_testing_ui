from libs.YMK.locators import PickPhotoLocators, AnimationLocators
from libs.YMK import pages


class Animation(pages.YMK_base.YMKbase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Select folder and photo (folder name, photo number)
    def pick_photo(self, folder, photo=1):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.album_view)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view)
        return self

    def click_animation(self):
        self.click_element(AnimationLocators.Animation_button)
        return self

    def adjust_seekbar_to_right(self):
        self.slidebar_to_right(AnimationLocators.seekbar)
        return self

    def adjust_seekbar_to_left(self):
        self.slidebar_to_left(AnimationLocators.seekbar)
        return self

    def click_effects(self):
        self.click_element(AnimationLocators.EFFECTS)
        return EFFECTS(self.driver)

    def click_stickers(self):
        self.click_element(AnimationLocators.STICKERS)
        return STICKERS(self.driver)

    def click_take_photo(self):
        self.click_element(AnimationLocators.take_photo)
        return self

    def click_v(self):
        self.click_element(AnimationLocators.V_button)
        return self

    def click_x(self):
        self.click_element(AnimationLocators.X_button)
        return self

    def click_play_cursor(self):
        self.click_element(AnimationLocators.play_cursor)
        return self


class EFFECTS(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def select_xxx_category(self, name):
        for i in range(10):
            try:
                self.select_element_by_number(AnimationLocators.category_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.category_text_view)
        return self

    def select_n_category(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AnimationLocators.effect_view, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.effect_view)
        return self

    def click_eraser(self):
        self.click_element(AnimationLocators.eraser_extend_button)
        return self

    def click_detect(self):
        self.click_element(AnimationLocators.detect_button)
        return self

    def click_draw(self):
        self.click_element(AnimationLocators.draw_button)
        return self

    def click_erase(self):
        self.click_element(AnimationLocators.erase_button)
        return self

    def select_stroke(self, number):
        self.select_element_by_number(AnimationLocators.brush_view, (number-1))
        return self

    def click_effects_v_button(self):
        self.click_element(AnimationLocators.V_button)
        return Export(self.driver)

    def click_effects_x_button(self):
        self.click_element(AnimationLocators.X_button)
        return Animation(self.driver)

    def click_undo_button(self):
        self.click_element(AnimationLocators.undo_button)
        return self

    def click_reset_button(self):
        self.click_element(AnimationLocators.reset_button)
        return self


class STICKERS(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def select_n_sticker(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AnimationLocators.stickers, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AnimationLocators.sticker_view)
        return self

    def click_cancel_button(self):
        self.click_element(AnimationLocators.X_button)
        return Animation(self.driver)

    def click_reset_button(self):
        self.click_element(AnimationLocators.reset_button)
        return self

    def click_stickers_v_button(self):
        self.click_element(AnimationLocators.V_button)
        return Export(self.driver)


class Export(Animation):
    def __init__(self, driver):
        super().__init__(driver)

    def click_back_button(self):
        self.click_element(AnimationLocators.Export.back_button)
        return Animation(self.driver)

    def click_export_button(self):
        self.click_element(AnimationLocators.Export.Export_button)
        return pages.result_page.Result(self.driver)

    def click_video_button(self):
        self.click_element(AnimationLocators.Export.video_button)
        return Video(self.driver)

    def click_gif_button(self):
        self.click_element(AnimationLocators.Export.GIF_button)
        return GIF(self.driver)

    def click_instagram_button(self):
        self.click_element(AnimationLocators.Export.Instagram_button)
        return Instagram(self.driver)

    def click_facebook_button(self):
        self.click_element(AnimationLocators.Export.Facebook_button)
        return Facebook(self.driver)


class Video(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_original_ratio(self):
        self.click_element(AnimationLocators.Export.crop_original)
        return self

    def select_16to9_ratio(self):
        self.click_element(AnimationLocators.Export.crop_16to9)
        return self

    def select_1to1_ratio(self):
        self.click_element(AnimationLocators.Export.crop_1to1)
        return self

    def select_3to4_ratio(self):
        self.click_element(AnimationLocators.Export.crop_3to4)
        return self

    def select_9to16_ratio(self):
        self.click_element(AnimationLocators.Export.crop_9to16)
        return self

    def select_4to3_ratio(self):
        self.click_element(AnimationLocators.Export.crop_4to3)
        return self

    def adjust_duration_to_right(self):
        self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
        return self

    def adjust_duration_to_left(self):
        self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
        return self

    def select_720p_quality(self):
        self.click_element(AnimationLocators.Export.quality_720p)
        return self

    def select_1080p_quality(self):
        self.click_element(AnimationLocators.Export.quality_1080p)
        return self

    def select_4k_quality(self):
        self.click_element(AnimationLocators.Export.quality_4k)
        return self


class GIF(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_original_ratio(self):
        self.click_element(AnimationLocators.Export.crop_original)
        return self

    def select_16to9_ratio(self):
        self.click_element(AnimationLocators.Export.crop_16to9)
        return self

    def select_1to1_ratio(self):
        self.click_element(AnimationLocators.Export.crop_1to1)
        return self

    def select_3to4_ratio(self):
        self.click_element(AnimationLocators.Export.crop_3to4)
        return self

    def select_9to16_ratio(self):
        self.click_element(AnimationLocators.Export.crop_9to16)
        return self


class Instagram(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_feed_ratio(self):
        self.click_element(AnimationLocators.Export.crop_feed)
        return self

    def select_story_ratio(self):
        self.click_element(AnimationLocators.Export.crop_story)
        return self

    def select_4to5_ratio(self):
        self.click_element(AnimationLocators.Export.crop_4to5)
        return self

    def adjust_duration_to_right(self):
        self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
        return self

    def adjust_duration_to_left(self):
        self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
        return self

    def select_720p_quality(self):
        self.click_element(AnimationLocators.Export.quality_720p)
        return self

    def select_1080p_quality(self):
        self.click_element(AnimationLocators.Export.quality_1080p)
        return self

    def select_4k_quality(self):
        self.click_element(AnimationLocators.Export.quality_4k)
        return self


class Facebook(Export):
    def __init__(self, driver):
        super().__init__(driver)

    def select_cover_ratio(self):
        self.click_element(AnimationLocators.Export.crop_cover)
        return self

    def select_profile_ratio(self):
        self.click_element(AnimationLocators.Export.crop_profile)
        return self

    def adjust_duration_to_right(self):
        self.slidebar_to_right(AnimationLocators.Export.duration_seekbar)
        return self

    def adjust_duration_to_left(self):
        self.slidebar_to_left(AnimationLocators.Export.duration_seekbar)
        return self

    def select_720p_quality(self):
        self.click_element(AnimationLocators.Export.quality_720p)
        return self

    def select_1080p_quality(self):
        self.click_element(AnimationLocators.Export.quality_1080p)
        return self

    def select_4k_quality(self):
        self.click_element(AnimationLocators.Export.quality_4k)
        return self
