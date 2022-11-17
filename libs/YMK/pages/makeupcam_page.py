from libs.YMK.locators import DialogLocators, MakeupCamLocators
from libs.YMK import pages


class MakeupCam(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_bipa_agree(self):
        self.wait_element_visible(DialogLocators.BIPA_Agree)
        self.click_element(DialogLocators.BIPA_Agree)
        return self

    def click_back(self):
        self.wait_element_visible(MakeupCamLocators.Back)
        self.click_element(MakeupCamLocators.Back)
        return pages.launcher_page.Launcher(self.driver)

    def click_keycode_back(self):
        self.driver.press_keycode(4)
        return self

    def click_timer_mode(self):
        self.wait_element_visible(MakeupCamLocators.Timer_Mode)
        self.click_element(MakeupCamLocators.Timer_Mode)
        return self

    def click_detail(self):
        self.wait_element_visible(MakeupCamLocators.Detail)
        self.click_element(MakeupCamLocators.Detail)
        return self

    def click_compare(self):
        self.wait_element_visible(MakeupCamLocators.Compare)
        self.click_element(MakeupCamLocators.Compare)
        return self

    def click_reset(self):
        self.wait_element_visible(MakeupCamLocators.Reset)
        self.click_element(MakeupCamLocators.Reset)
        self.wait_element_visible(MakeupCamLocators.Remove)
        self.click_element(MakeupCamLocators.Remove)
        return self

    def panel_close(self):
        self.wait_element_visible(MakeupCamLocators.Makeup.close_button)
        self.click_element(MakeupCamLocators.Makeup.close_button)
        return self

    def click_switch_camera(self):
        self.wait_element_visible(MakeupCamLocators.Switch_Camera)
        self.click_element(MakeupCamLocators.Switch_Camera)
        return self

    def switch_to_video_mode(self):
        try:
            self.wait_element_visible(MakeupCamLocators.Photo_Mode)
            self.click_element(MakeupCamLocators.Switch_Mode)
        except:
            pass
        return self

    def switch_to_photo_mode(self):
        try:
            self.wait_element_visible(MakeupCamLocators.Video_Mode)
            self.click_element(MakeupCamLocators.Switch_Mode)
        except:
            pass
        return self

    def click_capture(self):
        self.wait_element_visible(MakeupCamLocators.Camera_Shot)
        self.click_element(MakeupCamLocators.Camera_Shot)
        try:
            self.find_element(MakeupCamLocators.PhotoPreview.Photo_Save)
            pass
        except:
            self.find_element(MakeupCamLocators.Rating_Page)
            self.driver.press_keycode(4)
        return pages.makeupcam_page.PhotoPreview(self.driver)

    def click_capture_for_timer(self):
        self.wait_element_visible(MakeupCamLocators.Camera_Shot)
        self.click_element(MakeupCamLocators.Camera_Shot)
        return self

    def check_rating_page(self):
        try:
            self.find_element(MakeupCamLocators.PhotoPreview.Photo_Save)
            pass
        except:
            self.find_element(MakeupCamLocators.Rating_Page)
            self.driver.press_keycode(4)
        return pages.makeupcam_page.PhotoPreview(self.driver)


    def click_record(self):
        self.wait_element_visible(MakeupCamLocators.Video_Rec)
        self.click_element(MakeupCamLocators.Video_Rec)
        return self

    def click_stop(self):
        self.click_element(MakeupCamLocators.Stop_Record)
        return pages.makeupcam_page.VideoPreview(self.driver)

    def switch_camera(self):
        self.wait_element_visible(MakeupCamLocators.Switch_Camera)
        self.click_element(MakeupCamLocators.Switch_Camera)
        return self

    def select_effects(self):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup_Menu_xpath, "EFFECTS")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup_Menu_id)
        return Effects(self.driver)

    def select_hair(self):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup_Menu_xpath, "HAIR")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup_Menu_id)
        return Hair(self.driver)

    def select_looks(self):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup_Menu_xpath, "LOOKS")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup_Menu_id)
        return Looks(self.driver)

    def select_makeup(self):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup_Menu_xpath, "MAKEUP")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup_Menu_id)
        return Makeup(self.driver)

    def select_reshape(self):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup_Menu_xpath, "RESHAPE")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup_Menu_id)
        return Reshape(self.driver)

    def select_brand(self, name, check=False):
        try:
            self.click_element(MakeupCamLocators.brand_menu)
            self.click_element_by_name(MakeupCamLocators.brand, name)
        except (ValueError, Exception):
            try:
                self.slidebar_to_down(MakeupCamLocators.brand_menu_view)
                self.click_element_by_name(MakeupCamLocators.brand, name)
            except(ValueError, Exception):
                if check:
                    raise
                print("Can't find the brand, skip it.")
        return self

    def slide_bar_to_top(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V)
        self.slidebar_to_top(MakeupCamLocators.SeekBar_V)
        return self

    def slide_bar_to_down(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V)
        self.slidebar_to_down(MakeupCamLocators.SeekBar_V)
        return self

    def slide_bar_to_top_vertical_1(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V_1)
        self.slidebar_to_top(MakeupCamLocators.SeekBar_V_1)
        return self

    def slide_bar_to_down_vertical_1(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V_1)
        self.slidebar_to_down(MakeupCamLocators.SeekBar_V_1)
        return self

    def slide_bar_to_top_vertical_2(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V_2)
        self.slidebar_to_top(MakeupCamLocators.SeekBar_V_2)
        return self

    def slide_bar_to_down_vertical_2(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_V_2)
        self.slidebar_to_down(MakeupCamLocators.SeekBar_V_2)
        return self

    def slide_bar_to_left(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_H)
        self.slidebar_to_left(MakeupCamLocators.SeekBar_H)
        return self

    def slide_bar_to_right(self):
        self.wait_element_visible(MakeupCamLocators.SeekBar_H)
        self.slidebar_to_right(MakeupCamLocators.SeekBar_H)
        return self

    def slide_compare_to_left(self):
        self.wait_element_visible(MakeupCamLocators.Compare_Line)
        self.slidebar_to_left(MakeupCamLocators.Compare_Line)
        return self

    def slide_compare_to_right(self):
        self.wait_element_visible(MakeupCamLocators.Compare_Line)
        self.slidebar_to_right(MakeupCamLocators.Compare_Line)
        return self

    def scroll_look_details(self):
        self.scroll_vertical(MakeupCamLocators.Looks.look_details, speed=1000)
        self.scroll_vertical(MakeupCamLocators.Looks.look_details, speed=1000)
        self.scroll_vertical(MakeupCamLocators.Looks.look_details, speed=1000)
        return self

    def click_photo_picker(self):
        self.click_element(MakeupCamLocators.Photo_Picker)
        return self

class Hair(MakeupCam):
    def __init__(self, driver):
        super().__init__(driver)

    def select_haircolor_tab(self, name):
        self.click_element_by_name(MakeupCamLocators.Hair.color_tab, name)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(MakeupCamLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.color_grid_view)
                count += 1
        return self

    def select_brand(self, name, check=False):
        try:
            self.click_element(MakeupCamLocators.Hair.brand_menu)
            self.click_element_by_name(MakeupCamLocators.brand, name)
        except (ValueError, Exception):
            try:
                self.slidebar_to_down(MakeupCamLocators.brand_menu_view)
                self.click_element_by_name(MakeupCamLocators.brand, name)
            except(ValueError, Exception):
                if check:
                    raise
                print("Can't find the brand, skip it.")
        return self


class Looks(MakeupCam):
    def __init__(self, driver):
        super().__init__(driver)

    def select_look_category(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Looks.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Looks.look_category_view)
        return self

    def select_look_by_number(self, number):
        self.wait_element_visible(MakeupCamLocators.Looks.look_item)
        self.select_element_by_number(MakeupCamLocators.Looks.look_item, number-1)
        self.wait_element_visible(MakeupCamLocators.Looks.info_button)
        return self

    def select_look_item(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Looks.look_item_name, name)
                try:
                    self.click_element_by_text("OK")
                    self.wait_element_visible(MakeupCamLocators.Looks.info_button)
                    break
                except:
                    self.wait_element_visible(MakeupCamLocators.Looks.info_button)
                    break
            except(ValueError, Exception):
                self.slidebar_to_left(MakeupCamLocators.Looks.look_item_view)
                self.wait_time(1)
        return self

    def select_look_download_icon(self):
        for i in range(10):
            try:
                self.find_element(MakeupCamLocators.Looks.download_icon)
                break
            except(ValueError, Exception):
                self.slidebar_to_left(MakeupCamLocators.Looks.look_item_view)
                self.wait_time(1)
        return self

    def click_in_place_download_look(self):
        self.click_element(MakeupCamLocators.Looks.download_icon)
        self.wait_element_visible(MakeupCamLocators.Looks.info_button)
        return self

    def click_premium_category(self):
        self.click_element(MakeupCamLocators.Looks.premium_category)
        self.wait_element_visible(MakeupCamLocators.Looks.look_item)
        return self

    def click_premium_pack(self):
        self.click_element(MakeupCamLocators.Looks.premium_pack)
        self.wait_element_visible(MakeupCamLocators.Looks.premium_look)
        return self

    def click_switch_button(self):
        self.click_element(MakeupCamLocators.Looks.switch_button)
        self.wait_element_visible(MakeupCamLocators.Looks.switch_button)
        return self

    def click_info_button(self):
        self.click_element(MakeupCamLocators.Looks.info_button)
        return self

    def click_favorite_icon(self):
        self.click_element(MakeupCamLocators.Looks.favorite_icon)
        return self

    def click_favorite_category(self):
        self.click_element(MakeupCamLocators.Looks.favorite_category)
        return self

    def add_look_to_favorite(self, name):
        self.drag_and_drop_element(MakeupCamLocators.Looks.look_item_name, name,
                                   MakeupCamLocators.Looks.add_favorite)
        return self

    def remove_look_from_favorite(self, name):
        self.drag_and_drop_element(MakeupCamLocators.Looks.look_item_name, name,
                                   MakeupCamLocators.Looks.add_favorite)
        return self


class Effects(MakeupCam):
    def __init__(self, driver):
        super().__init__(driver)

    def select_premium_pack(self):
        for i in range(10):
            try:
                self.click_element(MakeupCamLocators.Effects.premium_pack)
                break
            except(ValueError, Exception):
                self.slidebar_to_left(MakeupCamLocators.Effects.effect_grid_area)
                self.wait_time(1)
        return self

    def click_premium_effect(self):
        self.click_element(MakeupCamLocators.Effects.effect)
        self.wait_element_visible(MakeupCamLocators.Effects.premium_effect)
        return self


class Makeup(MakeupCam):
    def __init__(self, driver):
        super().__init__(driver)

    def select_feature_list(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup.feature_list, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup.makeup_menu)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(MakeupCamLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.color_grid_view)
                count += 1
        return self

    def select_palette(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(MakeupCamLocators.palette, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.color_grid_view)
                count += 1
        return self

    def select_color_tab(self, name):
        self.click_element_by_name(MakeupCamLocators.Makeup.color_tab, name)
        return self

    def click_premium_lip(self):
        self.click_element(MakeupCamLocators.Makeup.crown_icon)
        self.wait_element_visible(MakeupCamLocators.Makeup.premium_lip)
        return self

    def click_smashbox_entry(self):
        self.wait_element_visible(MakeupCamLocators.Makeup.smashbox_entry)
        self.click_element(MakeupCamLocators.Makeup.smashbox_entry)
        return pages.smashbox_page.Smashbox(self.driver)

    def check_smashbox_entry_is_exist(self):
        try:
            self.wait_element_visible(MakeupCamLocators.Makeup.smashbox_entry)
            return 1
        except(ValueError, Exception):
            return 0

    def select_pattern(self, number):
        self.select_element_by_number(MakeupCamLocators.Makeup.template_button, number)
        return self

    def click_none_button(self):
        self.click_element(MakeupCamLocators.Makeup.none_button)
        return self

    def click_shimmer_button(self):
        self.click_element(MakeupCamLocators.Makeup.shimmer_switcher)
        return self

    def select_lip_art_pattern(self, number):
        self.select_element_by_number(MakeupCamLocators.Makeup.lip_art_pattern, (number-1))
        return self

    def select_texture(self, name):
        count = 0
        while count < 5:
            try:
                self.click_element_by_name(MakeupCamLocators.Makeup.pattern_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Makeup.pattern_grid_view)
                count += 1
        return self


class Reshape(MakeupCam):
    def __init__(self, driver):
        super().__init__(driver)

    def select_feature_list(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(MakeupCamLocators.Reshape.feature_list, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(MakeupCamLocators.Reshape.retouch_menu)
        return self


class PhotoPreview(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_photo_retake(self):
        self.wait_element_visible(MakeupCamLocators.PhotoPreview.Photo_Retake)
        self.click_element(MakeupCamLocators.PhotoPreview.Photo_Retake)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def click_photo_edit(self):
        self.wait_element_visible(MakeupCamLocators.PhotoPreview.Photo_Edit)
        self.click_element(MakeupCamLocators.PhotoPreview.Photo_Edit)
        return self

    def click_photo_save(self):
        self.wait_element_visible(MakeupCamLocators.PhotoPreview.Photo_Save)
        self.click_element(MakeupCamLocators.PhotoPreview.Photo_Save)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def click_photo_frame(self):
        self.wait_element_visible(MakeupCamLocators.PhotoPreview.Photo_Frame)
        self.click_element(MakeupCamLocators.PhotoPreview.Photo_Frame)
        return self

    def click_photo_share(self):
        self.wait_element_visible(MakeupCamLocators.PhotoPreview.Photo_Share)
        self.click_element(MakeupCamLocators.PhotoPreview.Photo_Share)
        return self


class VideoPreview(pages.YMK_base.YMKbase):
    def click_video_edit(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Video_Edit)
        self.click_element(MakeupCamLocators.VideoPreview.Video_Edit)
        return self

    def wait_video_play(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Video_Play)
        return self

    def click_video_save(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Video_Save)
        self.click_element(MakeupCamLocators.VideoPreview.Video_Save)
        return pages.result_page.Result(self.driver)

    def click_video_retake(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Video_Retake)
        self.click_element(MakeupCamLocators.VideoPreview.Video_Retake)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def click_video_volume(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Volume_Switcher)
        self.click_element(MakeupCamLocators.VideoPreview.Volume_Switcher)
        return self

    def click_remove_watermark(self):
        self.wait_element_visible(MakeupCamLocators.VideoPreview.Remove_Watermark)
        self.click_element(MakeupCamLocators.VideoPreview.Remove_Watermark)
        return self

    def check_watermark_iap(self):
        self.find_element(MakeupCamLocators.VideoPreview.IAP)
        return self
