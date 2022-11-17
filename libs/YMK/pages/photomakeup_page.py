import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from libs.YMK.locators import PhotoMakeupLocators, PickPhotoLocators, DialogLocators, ShareLookLocators, ResultLocators
from libs.YMK import pages
import time
from selenium.webdriver.common.by import By


class PhotoMakeup(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def pick_photo(self, folder, photo=1):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except:
                self.scroll_vertical(PickPhotoLocators.album_view, 2000)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
                self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view, 2000)
        return self

    def click_back(self):
        self.wait_element_visible(PhotoMakeupLocators.Back)
        self.click_element(PhotoMakeupLocators.Back)
        return pages.photopicker_page.PhotoPicker(self.driver)

    def check_iap_AD(self):
        try:
            self.find_element(PhotoMakeupLocators.Save)
            print("No iap & AD")
        except:
            start = time.time()
            try:
                self.find_element(PickPhotoLocators.iap)
                self.screenshot("Photo_picker_iap")
                self.driver.press_keycode(4)
                print("Close iap")
                end_iap = time.time()
                print("Check iap：%f 秒" % (end_iap - start))
            except:
                try:
                    self.find_element(PhotoMakeupLocators.Save)
                    print("No ipa & AD")
                except:
                    self.screenshot("Photo_picker_AD")
                    try:
                        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close Ad').click()
                        # self.driver.find_element(By.XPATH, '//android.widget.LinearLayout[@content-desc=\"Close Ad\"]').click()
                        print("Close video AD")
                        end_AD = time.time()
                        print("Check AD：%f 秒" % (end_AD - start))
                    except (ValueError, Exception):
                        self.driver.find_element(By.CLASS_NAME, "android.webkit.WebView")
                        for i in range(15):
                            try:
                                self.wait_element_visible(PhotoMakeupLocators.Save, 2)
                                print("Close AD")
                                end_AD = time.time()
                                print("Check AD：%f 秒" % (end_AD - start))
                                break
                            except (ValueError, Exception):
                                self.driver.press_keycode(4)
        return self

    def click_keycode_back(self):
        self.driver.press_keycode(4)
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

    def click_save(self, timeout=300):
        self.wait_element_visible(PhotoMakeupLocators.Save)
        self.click_element(PhotoMakeupLocators.Save)
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor, timeout)
        try:
            self.wait_element_invisible(PhotoMakeupLocators.Save, 5)
            return pages.result_page.Result(self.driver)
        except:
            pytest.fail("Save photo fail!")

    def check_subscription_panel(self):
        self.find_element_by_text("Subscribe Now")
        return self

    def click_detail(self):
        self.wait_element_visible(PhotoMakeupLocators.Detail)
        self.click_element(PhotoMakeupLocators.Detail)
        return self

    def click_compare(self):
        self.wait_element_visible(PhotoMakeupLocators.Compare)
        self.click_element(PhotoMakeupLocators.Compare)
        return self

    def click_finetune(self):
        self.wait_element_visible(PhotoMakeupLocators.Manual)
        self.click_element(PhotoMakeupLocators.Manual)
        return self

    # Set the value ex: 70 or "99"
    def slider_bar_set_value(self, value):
        self.wait_element_visible(PhotoMakeupLocators.slider_bar)
        self.send_keys_to_element(PhotoMakeupLocators.slider_bar, value)
        return self

    def adjust_intensity_to_top(self):
        self.wait_element_visible(PhotoMakeupLocators.slider_bar)
        self.slidebar_to_top(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_down(self):
        self.wait_element_visible(PhotoMakeupLocators.slider_bar)
        self.slidebar_to_down(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_right(self):
        self.wait_element_visible(PhotoMakeupLocators.slider_bar)
        self.slidebar_to_right(PhotoMakeupLocators.slider_bar)
        return self

    def adjust_intensity_to_left(self):
        self.wait_element_visible(PhotoMakeupLocators.slider_bar)
        self.slidebar_to_left(PhotoMakeupLocators.slider_bar)
        return self

    def waiting_cursor(self):
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor)
        return self

    def wait_animation(self):
        try:
            self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor, timeout=30)
            time.sleep(3)
        except (ValueError, Exception):
            pass
        return self

    def wait_face_animation(self):
        try:
            self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor, timeout=30)
            self.wait_element_invisible(PhotoMakeupLocators.wait_animation, timeout=30)
            time.sleep(5)
            print("wait face animation")
        except (ValueError, Exception):
            pass
        return self

    def select_brand(self, name, check=False):
        try:
            self.wait_element_visible(PhotoMakeupLocators.brand_menu, 10)
            self.click_element(PhotoMakeupLocators.brand_menu)
            for i in range(6):
                try:
                    self.click_element_by_name(PhotoMakeupLocators.brand, name)
                    break
                except (ValueError, Exception):
                    self.slidebar_to_down(PhotoMakeupLocators.brand_menu_view)
        except (ValueError, Exception):
            if check:
                raise
            print("Can't find the brand, skip it.")
        return self

    def select_looks(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Looks")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Looks(self.driver)

    def select_mouth(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Mouth")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Mouth(self.driver)

    def select_face(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Face")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Face(self.driver)

    def select_eye(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Eye")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eye(self.driver)

    def select_hair(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Hair")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Hair(self.driver)

    def select_bodytuner(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Body Tuner")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return pages.bodytuner_page.BodyTuner(self.driver)

    def select_animation(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Animation")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return pages.animation_page.Animation(self.driver)

    def select_effects(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Effects")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return pages.effects_page.Effects(self.driver)

    def select_background(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Background")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return pages.background_page.Background(self.driver)

    def select_accessories(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.feature_list, "Accessories")
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return pages.accessories_page.Accessories(self.driver)

    def add_to_favorite(self):
        self.wait_element_visible(PhotoMakeupLocators.favorite)
        self.click_element(PhotoMakeupLocators.favorite)
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor)
        self.click_element(PhotoMakeupLocators.yes)
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor)
        return self

    def click_timemachine_ad(self):
        for i in range(10):
            try:
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.click_element_by_name(PhotoMakeupLocators.category, "Time Machine")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return self

    def click_continue_to_timemachine(self):
        self.wait_element_visible(PhotoMakeupLocators.CrossPromote.leave_alert_dialog)
        self.click_element(PhotoMakeupLocators.CrossPromote.leave_alert_dialog_OK)
        self.wait_element_invisible(PhotoMakeupLocators.CrossPromote.leave_alert_dialog)
        return pages.aging_page

    def click_videoedit_ad(self):
        for i in range(10):
            try:
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.click_element_by_name(PhotoMakeupLocators.category, "Video Edit")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        self.wait_element_invisible(PhotoMakeupLocators.makeup_menu)
        return self

    def click_sticker_ad(self):
        for i in range(10):
            try:
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.click_element_by_name(PhotoMakeupLocators.category, "Sticker")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        self.wait_element_invisible(PhotoMakeupLocators.makeup_menu)
        return self

    def click_frame_ad(self):
        for i in range(10):
            try:
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.click_element_by_name(PhotoMakeupLocators.category, "Frame")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        self.wait_element_invisible(PhotoMakeupLocators.makeup_menu)
        return self

    def click_nails_ad(self):
        for i in range(10):
            try:
                self.wait_element_visible(PhotoMakeupLocators.makeup_menu)
                self.click_element_by_name(PhotoMakeupLocators.category, "Nails")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        self.wait_element_invisible(PhotoMakeupLocators.makeup_menu)
        return self


class SwitchFace(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def click_cancel(self):
        self.wait_element_visible(PhotoMakeupLocators.SwitchFace.Cancel)
        self.click_element(PhotoMakeupLocators.SwitchFace.Cancel)
        return PhotoMakeup

    def click_addface(self):
        self.wait_element_visible(PhotoMakeupLocators.SwitchFace.Add_Face)
        self.click_element(PhotoMakeupLocators.SwitchFace.Add_Face)
        return self

    def click_apply(self):
        self.wait_element_visible(PhotoMakeupLocators.SwitchFace.Apply)
        self.click_element(PhotoMakeupLocators.SwitchFace.Apply)
        return PhotoMakeup(self.driver)


class FineTune(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def click_lefteye(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Left_eye)
        self.click_element(PhotoMakeupLocators.FineTune.Left_eye)
        return self

    def click_righteye(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Right_eye)
        self.click_element(PhotoMakeupLocators.FineTune.Right_eye)
        return self

    def click_lips(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Lips)
        self.click_element(PhotoMakeupLocators.FineTune.Lips)
        return self

    def click_mouthopen(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Mouth_Open)
        self.click_element(PhotoMakeupLocators.FineTune.Mouth_Open)
        return self

    def click_apply(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Apply)
        self.click_element(PhotoMakeupLocators.FineTune.Apply)
        return PhotoMakeup(self.driver)

    def click_close(self):
        self.wait_element_visible(PhotoMakeupLocators.FineTune.Close)
        self.click_element(PhotoMakeupLocators.FineTune.Close)
        return PhotoMakeup(self.driver)


class Looks(PhotoMakeup):
    def __init__(self, driver):
        super().__init__(driver)

    def check_feature_notice(self):
        self.wait_element_visible(DialogLocators.AD_dialog)
        return self

    def skip_feature_notice(self):
        try:
            self.click_element(DialogLocators.AD_close)
        except:
            pass
        return self

    def select_look_category(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.Looks.look_category_view)
        return self

    def select_look_item(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.Looks.look_item_name, name)
                break
            except(ValueError, Exception):
                self.slidebar_to_left(PhotoMakeupLocators.Looks.look_item_view)
                self.wait_time(1)
        return self

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Looks.store)
        return pages.store_page.Look(self.driver)

    def click_heart(self):
        self.click_element(PhotoMakeupLocators.Looks.heart)
        return self

    def click_crown(self):
        self.click_element(PhotoMakeupLocators.Looks.crown)
        return self

    def long_press_look(self, name):
        self.long_press_element(PhotoMakeupLocators.Looks.look_item_name, name)
        return self

    def add_look_to_favorite(self, name):
        self.drag_and_drop_element(PhotoMakeupLocators.Looks.look_item_name, name,
                                   PhotoMakeupLocators.Looks.add_favorite)
        return self

    def remove_look_from_favorite(self, name):
        self.drag_and_drop_element(PhotoMakeupLocators.Looks.look_item_name, name,
                                   PhotoMakeupLocators.Looks.add_favorite)
        return self

    def click_look_pack(self):
        self.click_element(PhotoMakeupLocators.Looks.look_image)
        return self

    def wait_download_pack(self):
        self.wait_element_invisible(PhotoMakeupLocators.Looks.look_item_download_progress)
        return self

    def click_watermark(self,):
        el = self.driver.find_element("id", "com.cyberlink.youcammakeup:id/topToolBarExportBtn")
        button_x = el.location['x']
        print(button_x)
        button_y = el.location['y']
        width = el.size["width"]
        height = el.size["height"]
        i = 10
        while True:
            try:
                self.find_element(PickPhotoLocators.iap)
                break
            except:
                print(i, (button_x, button_y + i * height))
                TouchAction(self.driver).tap(None, button_x + 0.5 * width, button_y + i * height, 1).perform()
                i += 1
                # TouchAction(driver).tap(None, 950, 1600, 1).perform()
        return self

    def click_look_info(self,):
        self.wait_element_visible(PhotoMakeupLocators.Looks.look_info)
        self.click_element(PhotoMakeupLocators.Looks.look_info)
        return self

    def click_share_to_yc(self,):
        self.wait_element_visible(PhotoMakeupLocators.Looks.share_to_YC)
        self.click_element(PhotoMakeupLocators.Looks.share_to_YC)
        return self

    def share_look(self, title):
        self.wait_element_visible(ShareLookLocators.share)
        self.send_keys_to_element(ShareLookLocators.post_title, title)
        self.click_element(ShareLookLocators.share)
        self.wait_element_visible(ShareLookLocators.share_item_icon, 60)
        return self

    def select_look_by_number(self, number):
        self.wait_element_visible(PhotoMakeupLocators.Looks.look_view)
        self.select_element_by_number(PhotoMakeupLocators.Looks.look_view, number-1)
        return self


class Mouth(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_lipcolor(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Color")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return LipColor(self.driver)

    def select_lipreshape(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Reshape")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return LipReshape(self.driver)

    def select_smile(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Smile")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Smile(self.driver)

    def select_lipplumper(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Lip Plumper")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return LipPlumper(self.driver)

    def select_teethwhitener(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Teeth Whitener")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return WhitenTeeth(self.driver)

    def select_lipart(self):
        for i in range(10):
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
        return pages.store_page.Lipart(self.driver)

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
                self.wait_element_visible(PhotoMakeupLocators.color_content)
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
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
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Smoother")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Smoother(self.driver)

    def select_faceshape(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Face Shape")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return FaceShape(self.driver)

    def select_noseenhance(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Nose Enhance")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return NoseEnhance(self.driver)

    def select_wrinkle(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Wrinkle")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Wrinkle(self.driver)

    def select_redness(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Redness")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Redness(self.driver)

    def select_Unevenskintone(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Uneven Skintone")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return UnevenSkintone(self.driver)

    def select_pores(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Pores")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Pores(self.driver)

    def select_foundation(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Foundation")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Foundation(self.driver)

    def select_concealer(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Concealer")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Concealer(self.driver)

    def select_blush(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Blush")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Blush(self.driver)

    def select_contour(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Contour")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Contour(self.driver)

    def select_highlight(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Highlight")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Highlight(self.driver)

    def select_facepaint(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Face Paint")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return FacePaint(self.driver)

    def select_blemish(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Blemish")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Blemish(self.driver)

    def select_shineremoval(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Shine Removal")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return ShineRemoval(self.driver)

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
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.panel_view)
        return self

    def click_left(self):
        self.wait_element_visible(PhotoMakeupLocators.Face.Left)
        self.click_element(PhotoMakeupLocators.Face.Left)
        return self

    def click_overall(self):
        self.wait_element_visible(PhotoMakeupLocators.Face.Overall)
        self.click_element(PhotoMakeupLocators.Face.Overall)
        return self

    def click_right(self):
        self.wait_element_visible(PhotoMakeupLocators.Face.Right)
        self.click_element(PhotoMakeupLocators.Face.Right)
        return self


class NoseEnhance(Face):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_noseenhance_function(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.panel_view)
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

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number-1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
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
        self.wait_element_visible(PhotoMakeupLocators.tab_room_pattern)
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_pattern(self, number):
        self.wait_element_visible(PhotoMakeupLocators.pattern_grid_view)
        self.select_element_by_number(PhotoMakeupLocators.pattern_grid_view, (number - 1))
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class Contour(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_tab(self, name):
        self.wait_element_visible(PhotoMakeupLocators.tab_room_pattern)
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class Highlight(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def select_tab(self, name):
        self.wait_element_visible(PhotoMakeupLocators.tab_room_pattern)
        self.click_element_by_name(PhotoMakeupLocators.tab_room_pattern, name)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
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
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self


class Blemish(Face):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_onoff(self):
        self.wait_element_visible(PhotoMakeupLocators.Face.switch_button)
        self.click_element(PhotoMakeupLocators.Face.switch_button)
        return self


class ShineRemoval(Face):
    def __init__(self, driver):
        super().__init__(driver)


class Eye(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        
    def select_eyeliner(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eyeliner")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eyeliner(self.driver)
    
    def select_eyelashes(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eyelashes")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eyelashes(self.driver)
    
    def select_eyeshadow(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eye Shadow")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return EyeShadow(self.driver)
    
    def select_darkcircle(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Dark Circle")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return DarkCircle(self.driver)
    
    def select_eyetuner(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eye Tuner")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return EyeTuner(self.driver)
    
    def select_eyebrows(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eyebrows")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eyebrows(self.driver)
    
    def select_browreshape(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Brow Reshape")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return BrowReshape(self.driver)
    
    def select_eyecolor(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eye Color")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return EyeColor(self.driver)
    
    def select_eyebag(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eye Bag")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return EyeBag(self.driver)

    def select_brighten(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Brighten")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Brighten(self.driver)

    def select_doubleeyelid(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Double Eyelid")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return DoubleEyelid(self.driver)

    def select_redeye(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Red-Eye")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return RedEye(self.driver)

    def click_face_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)

    def click_store(self):
        self.click_element(PhotoMakeupLocators.Eye.download_store)
        return self


class Eyeliner(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_pattern(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_pattern)
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_color)
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
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self


class Eyelashes(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_eyelashes(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_eyelashes)
        self.click_element(PhotoMakeupLocators.Eye.tab_eyelashes)
        return self

    def click_mascara(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_mascara)
        self.click_element(PhotoMakeupLocators.Eye.tab_mascara)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
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

    def click_pattern(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_pattern)
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_color)
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_collection(self, text):
        count = 0
        while count < 5:
            try:
                self.click_element_by_name(PhotoMakeupLocators.Eye.eyeshadow_collection, text)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.edit_View_bottom_region)
                count += 1
        return self

    def select_palette(self, num):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.Eye.eyeshadow_palette, (num-1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_palette)
                self.scroll_horizontal(PhotoMakeupLocators.Eye.eyeshadow_palette)
                count += 1
        return self

    def select_palette_box1(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_palette_box1)
        self.click_element(PhotoMakeupLocators.Eye.eyeshadow_palette_box1)
        return self

    def click_extra(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_extra)
        self.click_element(PhotoMakeupLocators.Eye.eyeshadow_extra)
        return self

    def long_press_palette(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_palette_Area)
        self.long_press_element(PhotoMakeupLocators.Eye.eyeshadow_palette_Area)
        return self

    def delete_palette(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.delete_palette)
        self.click_element(PhotoMakeupLocators.Eye.delete_palette)
        return self

    def click_palette_colorball(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_palette_color)
        self.click_element(PhotoMakeupLocators.Eye.eyeshadow_palette_color)
        return self

    def select_palette_colorball(self, num):
        for i in range(5):
            try:
                self.select_element_by_number(PhotoMakeupLocators.Eye.eyeshadow_palette_color, (num-1))
            except(ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.Eye.eyeshadow_palette_color_view)
                self.scroll_horizontal(PhotoMakeupLocators.Eye.eyeshadow_palette_color_view)
        return self

    def click_shimmer_icon(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.shimmer_switcher)
        self.click_element(PhotoMakeupLocators.Eye.shimmer_switcher)
        return self

    def click_heart_icon(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.heart_icon)
        self.click_element(PhotoMakeupLocators.Eye.heart_icon)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_recycle_view)
                count += 1
        return self

    def click_smashbox_entry(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.smashbox_entry)
        self.click_element(PhotoMakeupLocators.Eye.smashbox_entry)
        return pages.smashbox_page.Smashbox(self.driver)

    def check_smashbox_entry_is_exist(self):
        try:
            self.wait_element_visible(PhotoMakeupLocators.Eye.smashbox_entry)
            return 1
        except(ValueError, Exception):
            return 0


class DarkCircle(Eye):
    def __init__(self, driver):
        super().__init__(driver)


class EyeTuner(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_left(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.Left)
        self.click_element(PhotoMakeupLocators.Eye.Left)
        return self

    def click_overall(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.Overall)
        self.click_element(PhotoMakeupLocators.Eye.Overall)
        return self

    def click_right(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.Right)
        self.click_element(PhotoMakeupLocators.Eye.Right)
        return self

    def select_eyetuner_function(self, name):
        self.click_element_by_name(PhotoMakeupLocators.reshape_item, name)
        return self


class Eyebrows(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def click_pattern(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_pattern)
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_color)
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def click_original(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.original_pattern)
        self.click_element(PhotoMakeupLocators.Eye.original_pattern)
        return self

    def select_pattern(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.pattern_list, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_recycle_view)
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
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def set_color_to_100(self):
        self.slidebar_to_top(PhotoMakeupLocators.Eye.color_seekbar)
        return self

    def set_color_to_0(self):
        self.slidebar_to_down(PhotoMakeupLocators.Eye.color_seekbar)
        return self

    def set_shape_to_100(self):
        self.slidebar_to_top(PhotoMakeupLocators.Eye.shape_seekbar)
        return self

    def set_shape_to_0(self):
        self.slidebar_to_down(PhotoMakeupLocators.Eye.shape_seekbar)
        return self

    def select_3D_tab(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.tab_text, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.tab_recycle_view)
        return self

    def set_position_to_together(self):
        self.slidebar_to_left(PhotoMakeupLocators.Eye.x_seekbar)
        return self

    def set_position_to_apart(self):
        self.slidebar_to_right(PhotoMakeupLocators.Eye.x_seekbar)
        return self

    def set_position_to_down(self):
        self.slidebar_to_left(PhotoMakeupLocators.Eye.y_seekbar)
        return self

    def set_position_to_up(self):
        self.slidebar_to_right(PhotoMakeupLocators.Eye.y_seekbar)
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
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_pattern)
        self.click_element(PhotoMakeupLocators.Eye.tab_pattern)
        return self

    def click_color(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.tab_color)
        self.click_element(PhotoMakeupLocators.Eye.tab_color)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def set_color_to_100(self):
        self.slidebar_to_top(PhotoMakeupLocators.Eye.color_seekbar)
        return self

    def set_color_to_0(self):
        self.slidebar_to_down(PhotoMakeupLocators.Eye.color_seekbar)
        return self

    def set_size_to_100(self):
        self.slidebar_to_top(PhotoMakeupLocators.Eye.size_seekbar)
        return self

    def set_size_to_0(self):
        self.slidebar_to_down(PhotoMakeupLocators.Eye.size_seekbar)
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
        for i in range(5):
            try:
                self.select_element_by_number(PhotoMakeupLocators.Eye.eyelid_pattern, (number-1))
                break
            except(ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.Eye.eyelid_pattern_list)
                self.scroll_horizontal(PhotoMakeupLocators.Eye.eyelid_pattern_list)
        return self


class RedEye(Eye):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_onoff(self):
        self.wait_element_visible(PhotoMakeupLocators.Eye.switch_button)
        self.click_element(PhotoMakeupLocators.Eye.switch_button)
        return self


class Hair(PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_haircolor(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Hair Color")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return HairColor(self.driver)

    def select_hairstyle(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Hair Style")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return HairStyle(self.driver)

    def click_hair_back(self):
        self.click_element(PhotoMakeupLocators.menu_back)
        return PhotoMakeup(self.driver)

    def tap_central(self):
        self.tap_element_coordinates(PhotoMakeupLocators.Hair.finetune_editroom)
        return self


class HairColor(Hair):
    def __init__(self, driver):
        super().__init__(driver)

    def select_haircolor_tab(self, name):
        self.click_element_by_name(PhotoMakeupLocators.Hair.color_tab, name)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def edit_color(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.edit_color)
        self.click_element(PhotoMakeupLocators.Hair.edit_color)
        return self

    def select_color_palette1(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.color_palette1)
        self.click_element(PhotoMakeupLocators.Hair.color_palette1)
        return self

    def select_color_palette2(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.color_palette2)
        self.click_element(PhotoMakeupLocators.Hair.color_palette2)
        return self

    def select_color_ball(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(PhotoMakeupLocators.Hair.color_ball, (number-1))
                break
            except(ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.Hair.color_ball_view)
        return self

    def click_flip_button(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.flip_button)
        self.click_element(PhotoMakeupLocators.Hair.flip_button)
        return self

    def click_finetune(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.finetune_button)
        self.click_element(PhotoMakeupLocators.Hair.finetune_button)
        return self

    def click_finetune_close(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.finetune_close)
        self.click_element(PhotoMakeupLocators.Hair.finetune_close)
        return self

    def click_finetune_apply(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.finetune_apply)
        self.click_element(PhotoMakeupLocators.Hair.finetune_apply)
        return self

    def click_brush_size1(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.brush_size1)
        self.click_element(PhotoMakeupLocators.Hair.brush_size1)
        return self

    def click_brush_size2(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.brush_size2)
        self.click_element(PhotoMakeupLocators.Hair.brush_size2)
        return self

    def click_brush_size3(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.brush_size3)
        self.click_element(PhotoMakeupLocators.Hair.brush_size3)
        return self

    def click_brush_size4(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.brush_size4)
        self.click_element(PhotoMakeupLocators.Hair.brush_size4)
        return self

    def click_brush_size5(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.brush_size5)
        self.click_element(PhotoMakeupLocators.Hair.brush_size5)
        return self

    def select_brush(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.category_view)
        self.slidebar_to_right(PhotoMakeupLocators.Hair.category_view)
        return self

    def select_eraser(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.category_view)
        self.slidebar_to_left(PhotoMakeupLocators.Hair.category_view)
        return self

    def set_coverage_to_100(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_top(PhotoMakeupLocators.Hair.coverage_seekbar)
        return self

    def set_coverage_to_0(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_down(PhotoMakeupLocators.Hair.coverage_seekbar)
        return self

    def set_blend_to_100(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_top(PhotoMakeupLocators.Hair.blend_seekbar)
        return self

    def set_blend_to_0(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_down(PhotoMakeupLocators.Hair.blend_seekbar)
        return self

    def set_shine_to_100(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_top(PhotoMakeupLocators.Hair.shine_seekbar)
        return self

    def set_shine_to_0(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_down(PhotoMakeupLocators.Hair.shine_seekbar)
        return self

    def set_color_to_100(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_top(PhotoMakeupLocators.Hair.color_seekbar)
        return self

    def set_color_to_0(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.coverage_seekbar)
        self.slidebar_to_down(PhotoMakeupLocators.Hair.color_seekbar)
        return self


class HairStyle(Hair):
    def __init__(self, driver):
        super().__init__(driver)

    def click_style(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.tab_style)
        self.click_element(PhotoMakeupLocators.Hair.tab_style)
        return self

    def select_null(self):
        self.wait_element_visible(PhotoMakeupLocators.color_content)
        self.select_element_by_number(PhotoMakeupLocators.color_content, 0)
        return self

    def select_style(self, name):
        for i in range(5):
            try:
                self.click_element_by_name(PhotoMakeupLocators.Hair.style_pattern, name)
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
        return self

    def long_press_style(self, name):
        for i in range(5):
            try:
                self.long_press_element(PhotoMakeupLocators.Hair.style_pattern, name)
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
        return self

    def click_x_button(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(PhotoMakeupLocators.Hair.x_button_on_patter, number-1)
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.pattern_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.pattern_grid_view)
        return self

    def click_color_tab(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.tab_color)
        self.click_element(PhotoMakeupLocators.Hair.tab_color)
        return self

    def select_color(self, number):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(PhotoMakeupLocators.color_content, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(PhotoMakeupLocators.color_grid_view)
                self.scroll_horizontal(PhotoMakeupLocators.color_grid_view)
                count += 1
        return self

    def click_store(self):
        self.wait_element_visible(PhotoMakeupLocators.Hair.download_store)
        self.click_element(PhotoMakeupLocators.Hair.download_store)
        return pages.store_page.Hair(self.driver)


