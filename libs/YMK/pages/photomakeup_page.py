from libs.YMK.locators import PhotoMakeupLocators, PickPhotoLocators, MakeupCamLocators, ResultLocators
from libs.YMK import pages
import sys


class PhotoMakeup(pages.YMK_base.YMKbase):
    def __init__(self, driver):
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

    def click_back(self):
        self.click_element(PhotoMakeupLocators.Back)
        return self

    def click_switchface(self):
        self.click_element(PhotoMakeupLocators.Switch_Face)
        return SwitchFace(self.driver)

    def click_undo(self):
        self.click_element(PhotoMakeupLocators.Undo)
        return self

    def click_redo(self):
        self.click_element(PhotoMakeupLocators.Redo)
        return self

    def click_save(self, timeout=60):
        self.click_element(PhotoMakeupLocators.Save)
        self.wait_element_visible(ResultLocators.share_page_view, timeout)
        print("Saved")
        return pages.result_page.Result(self.driver)

    def click_detail(self):
        self.click_element(PhotoMakeupLocators.Detail)
        return self

    def click_compare(self):
        self.click_element(PhotoMakeupLocators.Compare)
        return self

    def click_finetune(self):
        self.click_element(PhotoMakeupLocators.Manual)
        return self

    # Set the value ex: 70 or "99"
    def slider_bar_set_value(self, value):
        self.send_keys_to_element(PhotoMakeupLocators.slider_bar, value)
        return self

    def adjust_intensity_to_top(self):
        self.slidebar_to_top(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_down(self):
        self.sliderbar_to_down(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_right(self):
        self.slidebar_to_right(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_left(self):
        self.slidebar_to_left(PhotoMakeupLocators.slider_bar)
        return self

    def waiting_cursor(self):
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor)
        return self

    def wait_animation(self):
        try:
            self.wait_element_visible(PhotoMakeupLocators.waiting_cursor, timeout=30)
        except (ValueError, Exception):
            pass
        return self

    def select_looks(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Looks")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Looks(self.driver)

    def select_mouth(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Mouth")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Mouth(self.driver)

    def select_face(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Face")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Face(self.driver)

    def select_eye(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Eye")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eye(self.driver)

    # def select_feature(self, name):
    #     while True:
    #         try:
    #             self.click_element_by_name(PhotoMakeupLocators.category, name)
    #             link_page = self.str_to_class(name)
    #             print(link_page)
    #             print(PhotoMakeup)
    #             break
    #         except (ValueError, Exception):
    #             self.scroll_horizontal(PhotoMakeupLocators.pattern_view)
    #     return link_page(self.driver)
    #
    # def select_category(self, name):
    #     while True:
    #         try:
    #             self.click_element_by_name(PhotoMakeupLocators.category, name)
    #             link_page = self.str_to_class(name)
    #             break
    #         except (ValueError, Exception):
    #             self.scroll_horizontal(PhotoMakeupLocators.pattern_view)
    #     return link_page(self.driver)
    #
    # def str_to_class(self, name):
    #     return getattr(sys.modules[__name__], str(name).replace(' ', ''))


class SwitchFace(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def click_cancel(self):
        self.click_element(PhotoMakeupLocators.SwitchFace.Cancel)
        return PhotoMakeup

    def click_addface(self):
        self.click_element(PhotoMakeupLocators.SwitchFace.Add_Face)
        return self

    def click_apply(self):
        self.click_element(PhotoMakeupLocators.SwitchFace.Apply)
        return PhotoMakeup(self.driver)


class FineTune(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def click_lefteye(self):
        self.click_element(PhotoMakeupLocators.FineTune.Left_eye)
        return self

    def click_righteye(self):
        self.click_element(PhotoMakeupLocators.FineTune.Right_eye)
        return self

    def click_lips(self):
        self.click_element(PhotoMakeupLocators.FineTune.Lips)
        return self

    def click_mouthopen(self):
        self.click_element(PhotoMakeupLocators.FineTune.Mouth_Open)
        return self

    def click_apply(self):
        self.click_element(PhotoMakeupLocators.FineTune.Apply)
        return PhotoMakeup(self.driver)

    def click_close(self):
        self.click_element(PhotoMakeupLocators.FineTune.Close)
        return PhotoMakeup(self.driver)


class Looks(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def skip_feature_notice(self):
        try:
            self.click_element(MakeupCamLocators.AD_close)
        except:
            pass
        return self

    def select_look(self, name):
        self.click_element_by_name(PhotoMakeupLocators.Looks.look_item_name, name)
        return self

    def select_look_category(self, name):
        count = 0
        while count < 5:
            try:
                self.click_element_by_name(PhotoMakeupLocators.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.tab_recycle_view)
                count += 1
        return self

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Looks.store)
        return pages.store_page.Store(self.driver)

    def click_heart(self):
        self.click_element(PhotoMakeupLocators.Looks.heart)
        return self

    def click_crown(self):
        self.click_element(PhotoMakeupLocators.Looks.crown)
        return self

    def long_press_look(self, name):
        self.long_press_element(PhotoMakeupLocators.Looks.look_item_name, name)

    def add_to_favorite(self, name):
        self.drag_and_drop_element(PhotoMakeupLocators.Looks.look_item_name, name, PhotoMakeupLocators.Looks.add_favorite)
        return self

    def remove_from_favorite(self, name):
        self.drag_and_drop_element(PhotoMakeupLocators.Looks.look_item_name, name, PhotoMakeupLocators.Looks.add_favorite)
        return self


class Mouth(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_lipcolor(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Color")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.category)
        return LipColor(self.driver)

    def select_lipreshape(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Reshape")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.category)
        return LipReshape(self.driver)

    def select_smile(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Smile")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.category)
        return Smile(self.driver)

    def select_lipplumper(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Plumper")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.category)
        return LipPlumper(self.driver)

    def select_teethwhitener(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Teeth Whitener")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.category)
        return WhitenTeeth(self.driver)

    def select_lipart(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Art")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return LipArt(self.driver)

    def click_mouth_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)


class LipColor(Mouth):
    def __init__(self, driver):
        super().__init__(driver)

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Mouth.download_store)
        return pages.store_page.Store(self.driver)

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def select_texture(self, name):
        count = 0
        while count < 5:
            try:
                self.click_element_by_name(PhotoMakeupLocators.pattern_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
                count += 1
        return self

    def select_tab(self, name):
        count = 0
        while count < 5:
            try:
                self.click_element_by_name(PhotoMakeupLocators.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.tab_recycle_view)
                count += 1
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class LipReshape(Mouth):
    def __init__(self, driver):
        super().__init__(driver)

    def select_lipreshape_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class Smile(Mouth):
    def __init__(self, driver):
        super().__init__(driver)


class LipPlumper(Mouth):
    def __init__(self, driver):
        super().__init__(driver)

    def select_lipplumper_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class WhitenTeeth(Mouth):
    def __init__(self, driver):
        super().__init__(driver)


class LipArt(Mouth):
    def __init__(self, driver):
        super().__init__(driver)

    def select_null(self):
        self.select_element_by_number(PhotoMakeupLocators.color_content, 0)
        return self

    def select_lipart_pattern(self, number=1):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Mouth.download_store)
        return pages.store_page.Store(self.driver)


class Face(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_smoother(self):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Smoother")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
        return Smoother(self.driver)

    def click_face_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)


class Smoother(Face):
    def __init__(self, driver):
        super().__init__(driver)


class FaceShape(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_faceshape_function(self, name):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.panel_view)
        return self

    def click_left(self):
        self.click_element(PhotoMakeupLocators.Face.Left)
        return self

    def click_overall(self):
        self.click_element(PhotoMakeupLocators.Face.Overall)
        return self

    def click_right(self):
        self.click_element(PhotoMakeupLocators.Face.Right)
        return self


class NoseEnhance(Face):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_noseenhance_function(self, name):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.panel_view)
        return self


class Wrinkle(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_wrinkle_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class Redness(Face):
    def __init__(self, driver):
        super().__init__(driver)


class UnevenSkintone(Face):
    def __init__(self, driver):
        super().__init__(driver)


class Pores(Face):
    def __init__(self, driver):
        super().__init__(driver)


class Foundation(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class Concealer(Face):
    def __init__(self, driver):
        super().__init__(driver)


class Blush(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_tab(self, name):
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def select_pattern(self, number):
        self.select_element_by_number(PhotoMakeupLocators.pattern_grid_view, (number - 1))
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class Contour(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_tab(self, name):
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class Highlight(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_tab(self, name):
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class FacePaint(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Face.download_store)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class Blemish(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_onoff(self):
        self.click_element(PhotoMakeupLocators.Face.switch_button)
        return self


class ShineRemoval(Face):
    def __init__(self, driver):
        super().__init__(driver)


class Eye(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_face_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)


class Eyeliner(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def click_pattern(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class Eyelashes(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def click_eyelashes(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_eyelashes)
        return self

    def click_mascara(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_mascara)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class EyeShadow(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        try:
            self.click_element(PhotoMakeupLocators.brand_menu)
            self.click_element_by_name(PhotoMakeupLocators.brand, name)
        except (ValueError, Exception):
            print("Can't find the brand, skip it.")
        return self

    def click_pattern(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class DarkCircle(Eye):
    def __init__(self, driver):
        super().__init__(driver)


class EyeTuner(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_left(self):
        self.click_element(PhotoMakeupLocators.Eye.Left)
        return self

    def click_overall(self):
        self.click_element(PhotoMakeupLocators.Eye.Overall)
        return self

    def click_right(self):
        self.click_element(PhotoMakeupLocators.Eye.Right)
        return self

    def select_eyetuner_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class Eyebrows(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        self.click_element(PhotoMakeupLocators.brand_menu)
        self.click_element_by_name(PhotoMakeupLocators.brand, name)
        return self

    def click_pattern(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class BrowReshape(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_browsreshape_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class EyeColor(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_pattern(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class EyeBag(Eye):
    def __init__(self, driver):
        super().__init__(driver)


class Brighten(Eye):
    def __init__(self, driver):
        super().__init__(driver)


class DoubleEyelid(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def select_pattern(self, number):
        self.select_element_by_number(PhotoMakeupLocators.Eye.eyelid_pattern, number)
        return self


class RedEye(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_onoff(self):
        self.click_element(PhotoMakeupLocators.Eye.switch_button)
        return self


class Hair(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_hair_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)


class HairColor(Hair):
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, name):
        self.click_element(PhotoMakeupLocators.brand_menu)
        self.click_element_by_name(PhotoMakeupLocators.brand, name)
        return self

    def select_tab(self, name):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.tab_recycle_view)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class HairStyle(Hair):
    def __init__(self, driver):
        super().__init__(driver)

    def click_style(self):
        self.click_element(PhotoMakeupLocators.Hair.tab_style)
        return self

    # TODO: not done
    def select_style(self, name):
        while True:
            try:
                self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
        return self

    def click_color(self):
        self.click_element(PhotoMakeupLocators.Hair.tab_color)
        return self

    def select_null(self):
        self.select_element_by_number(PhotoMakeupLocators.color_content, 0)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Hair.download_store)
        return self
