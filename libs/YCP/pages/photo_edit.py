from libs.YCP import pages
from libs.YCP.locator import *


class feature:
    pass


class ColorPickerPanel(pages.YCP_base.YCPBase):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_color_list(self):
        self.scroll_horizontal(eColorPickerPanel.color_list)
        return self

    def click_color_picker_show_tab(self):
        self.click_element(eColorPickerPanel.color_picker_show_tab)
        return self

    def click_color_picker_hide_tab(self):
        self.click_element(eColorPickerPanel.color_picker_hide_tab)
        return self

    def click_dripper(self):
        self.click_element(eColorPickerPanel.dripper)
        return self

    def click_add_color(self):
        self.click_element(eColorPickerPanel.add_color)
        return self

    def select_color_item(self, num: int):
        self.select_element_by_number(eColorPickerPanel.color_item, num)
        return self

    def select_tool_item(self, num: int):
        self.select_element_by_number(eColorPickerPanel.tool_item, num)
        return self


class RatioPanel(pages.YCP_base.YCPBase):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_ratio_list(self):
        self.scroll_horizontal(eRatioPanel.ratio_list)
        return self

    def select_ratio_item(self, num: int):
        self.select_element_by_number(eRatioPanel.ratio_item, num)
        return self


class BackgroundPanel(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_blur(self):
        self.click_element(eBackgroundPanel.blur_button)
        return self

    def click_feather(self):
        self.click_element(eBackgroundPanel.feather_button)
        return self

    def click_config_icon(self):
        self.click_element(eBackgroundPanel.config_icon)
        return self

    def click_forbidden(self):
        self.click_element(eBackgroundPanel.forbidden_button)
        return self

    def scroll_background_list(self):
        self.click_element(eBackgroundPanel.background_list)
        return self

    def click_store(self):
        self.click_element(eBackgroundPanel.store_button)
        return pages.store.StorePage(self.driver)

    def click_library_icon(self):
        self.click_element(eBackgroundPanel.library_icon)
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def select_background_item(self, num: int):
        self.select_element_by_number(eBackgroundPanel.background_item, num)
        return self

    def set_slider_bar(self, num: int):
        self.send_keys_to_element(seek_bar, num)
        return self


class MainPhotoPage(ColorPickerPanel):
    def __init__(self, driver):
        super().__init__(driver)

    def click_adjust(self):
        self.click_element_in_list(
            eMainPhotoPage.adjust_button, eMainPhotoPage.tools_list)
        return AdjustPage(self.driver)

    def click_cutout(self):
        self.click_element_in_list(
            eMainPhotoPage.cutout_button, eMainPhotoPage.tools_list)
        return CutOutPage(self.driver)

    def click_crop_and_rotate(self):
        self.click_element_in_list(
            eMainPhotoPage.crop_and_rotate, eMainPhotoPage.tools_list)
        return ToolsCropRotatePage(self.driver)

    def click_effects(self):
        self.click_element_in_list(
            eMainPhotoPage.effects_button, eMainPhotoPage.tools_list)
        return EffectPage(self.dirver)

    def click_eraser(self):
        self.click_element_in_list(
            eMainPhotoPage.eraser_button, eMainPhotoPage.tools_list)
        return MainPhotoEraserPage(self.driver)

    def click_blender(self):
        self.click_element(eMainPhotoPage.blender_button)
        return self

    def click_border(self):
        self.click_element(eMainPhotoPage.border_button)
        return self

    def click_opacity(self):
        self.click_element(eMainPhotoPage.opacity_button)
        return self

    def scroll_blender_list(self):
        self.scroll_horizontal(eMainPhotoPage.blender_list)
        return self

    def scroll_tools_list(self):
        self.scroll_horizontal(eMainPhotoPage.tools_list)
        return self

    def set_slider_bar(self, value: int):
        self.send_keys_to_element(eMainPhotoPage.effect_bar, value)
        return self

    def select_blender_tab(self, blender_mode: str):
        assert blender_mode in ['NORMAL', 'MUTIPLY',
                                'SCREEN', 'OVERLAY', 'SOFT LIGHT', 'HARD LIGHT']
        self.click_element_in_list(blender_mode, eMainPhotoPage.blender_list)
        return self


class PhotoEditTemplate(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_undo(self):
        self.click_element(ePhotoEditTemplate.undo_button)
        return self

    def click_redo(self):
        self.click_element(ePhotoEditTemplate.redo_button)
        return self

    def click_crown_icon(self):
        self.click_element(ePhotoEditTemplate.crown_icon_button)
        return self

    def click_save(self):
        self.click_element(ePhotoEditTemplate.save_button)
        return pages.result.ResultPage(self.driver)

    def click_beautify_tab(self):
        self.click_element(ePhotoEditTemplate.beautify_tab_button)
        return PhotoEditPage(self.driver)

    def click_edit_tab(self):
        self.click_element(ePhotoEditTemplate.edit_tab_button)
        return PhotoBeautifyPage(self.driver)

    def click_compare(self):
        self.click_element(ePhotoEditTemplate.compare_button)
        return self


class EditFeatureRoom(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_close(self):
        self.click_element(eEditFeatureRoom.close_button)
        return PhotoEditPage(self.driver)

    def click_apply(self):
        self.click_element(eEditFeatureRoom.apply_button)
        return PhotoEditPage(self.driver)


class BeautifyFeatureRoom(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_close(self):
        self.click_element(eEditFeatureRoom.close_button)
        return PhotoEditPage(self.driver)

    def click_apply(self):
        self.click_element(eEditFeatureRoom.apply_button)
        return PhotoEditPage(self.driver)


class PhotoBeautifyPage(PhotoEditTemplate):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_back(self):
        pass

    def click_save(self):
        pass

    def click_effects(self):
        pass

    def click_smooth(self):
        pass

    def click_face_shaper(self):
        pass

    def click_body_tuner(self):
        pass


class PhotoEditPage(PhotoEditTemplate):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_feature_room(self, feature_name: str):
        self.click_element_by_text(feature_name)
        return self

    def click_overlays(self):
        self.click_element_in_list(
            ePhotoEditPage.overlays_button, ePhotoEditPage.feature_room)
        return OverlaysPage(self.driver)

    def click_brush(self):
        self.click_element_in_list(
            ePhotoEditPage.brush_button, ePhotoEditPage.feature_room)
        return BrushPage(self.driver)

    def click_text(self):
        self.click_element_in_list(
            ePhotoEditPage.text_button, ePhotoEditPage.feature_room)
        return TextPage(self.driver)

    def click_template(self):
        self.click_element_in_list(
            ePhotoEditPage.template_button, ePhotoEditPage.feature_room)
        return TemplatePage(self.driver)

    def click_add_photo(self):
        self.click_element_in_list(
            ePhotoEditPage.add_photo_button, ePhotoEditPage.feature_room)
        return AddPhotoPage(self.driver)

    def click_background(self):
        self.click_element_in_list(
            ePhotoEditPage.background_button, ePhotoEditPage.feature_room)
        return BackgroundPage(self.driver)

    def click_frame(self):
        self.click_element_in_list(
            ePhotoEditPage.frame_button, ePhotoEditPage.feature_room)
        return FramePage(self.driver)

    def click_instafit(self):
        self.click_element_in_list(
            ePhotoEditPage.instafit_button, ePhotoEditPage.feature_room)
        return InstaFitPage(self.driver)

    def click_sticker(self):
        self.click_element_in_list(
            ePhotoEditPage.sticker_button, ePhotoEditPage.feature_room)
        return StickerPage(self.driver)

    def click_magic_brush(self):
        self.click_element_in_list(
            ePhotoEditPage.magic_brush_button, ePhotoEditPage.feature_room)
        return MagicBrushPage(self.driver)

    def click_adjust(self):
        self.click_element_in_list(
            ePhotoEditPage.adjust_button, ePhotoEditPage.feature_room)
        return AdjustPage(self.driver)

    def click_removal(self):
        self.click_element_in_list(
            ePhotoEditPage.removal_button, ePhotoEditPage.feature_room)
        return RemovalPage(self.driver)

    def click_animation(self):
        self.click_element_in_list(
            ePhotoEditPage.animation_button, ePhotoEditPage.feature_room)
        return AnimationPage(self.driver)

    def click_effects(self):
        self.click_element_in_list(
            ePhotoEditPage.effects_button, ePhotoEditPage.feature_room)
        return EffectPage(self.driver)

    def click_tools(self):
        self.click_element_in_list(
            ePhotoEditPage.tools_button, ePhotoEditPage.feature_room)
        return ToolsPanel(self.driver)

    def click_premium(self):
        self.click_element_in_list(
            ePhotoEditPage.premium_button, ePhotoEditPage.feature_room)
        return pages.premium.PremiumPage(self.driver)


class EffectsPage(pages.YCP_base.YCPBase):
    def __init__(self) -> None:
        pass


class ToolsPanel(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_tool(self, tool_name: str):
        self.click_element_by_text(tool_name)
        return ToolsCropRotatePage(self.driver)


class ToolsCropRotatePage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_image_roate(self):
        self.click_element(eToolsCropRotatePage.image_roate)
        return self

    def rotate_slidebar_to_45(self):
        self.slidebar_to_right(eToolsCropRotatePage.slide_bar)
        return self

    def click_image_mirror(self):
        self.click_element(eToolsCropRotatePage.image_mirror_button)
        return self

    def click_reset(self):
        self.click_element(eToolsCropRotatePage.reset_button)
        return self

    def click_image_free(self):
        self.click_element(eToolsCropRotatePage.image_free_button)
        return self

    def click_image_1x1(self):
        self.click_element(eToolsCropRotatePage.image_1x1_button)
        return self

    def click_image_1x1(self):
        self.click_element(eToolsCropRotatePage.image_1x1_button)
        return self

    def click_image_2x3(self):
        self.click_element(eToolsCropRotatePage.image_2x3_button)
        return self

    def click_image_3x2(self):
        self.click_element(eToolsCropRotatePage.image_3x2_button)
        return self


class PerspectivePage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_reset(self):
        self.click_element(ePerspectivePage.reset_button)
        return self

    def click_rotate(self):
        self.click_element(ePerspectivePage.rotate_button)
        return self

    def click_horizontal(self):
        self.click_element(ePerspectivePage.horizontal_button)
        return self

    def click_vertical(self):
        self.click_element(ePerspectivePage.vertical_button)
        return self


class HDRPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_edge(self):
        self.click_element(eHDRPage.edge_button)
        return self

    def click_glow(self):
        self.click_element(eHDRPage.glow_button)
        return self


class VignettePage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_feather(self):
        self.click_element(eVignettePage.feather_button)
        return self

    def click_shade(self):
        self.click_element(eVignettePage.shade_button)
        return self

    def set_slider_bar(self, value: int):
        """ set slider bar to value 0 ~ 200
        """
        self.send_keys_to_element(eVignettePage.slide_bar, value)
        return self


class MirrorPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_forbidden(self):
        self.click_element(eMirrorPage.forbidden_button)
        return self

    def select_color_item(self, num: int):
        self.select_element_by_number(eMirrorPage.color_item, num)
        return self

    def select_mirror_item(self, num: int):
        self.select_element_by_number(eMirrorPage.mirror_item, num)
        return self

    def set_offset_slider(self, num: int):
        self.send_keys_to_element(eMirrorPage.slide_bar, num)
        return self


class BlurPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_auto_detect(self):
        self.click_element(eBlurPage.auto_detect_button)
        return self

    def click_eraser(self):
        self.click_element(eBlurPage.eraser_button)
        return self

    def click_paint(self):
        self.click_element(eBlurPage.paint_button)
        return self

    def click_pen(self):
        self.click_element(eBlurPage.pen_button)
        return eBlurPenPanel(self.driver)

    def click_blurtype_star(self):
        self.click_element(eBlurPage.blurtype_star_button)
        return self

    def click_blurtype_love(self):
        self.click_element(eBlurPage.blurtype_love_button)
        return self

    def click_blurtype_light(self):
        self.click_element(eBlurPage.blurtype_light_button)
        return self

    def click_blurtype_circle(self):
        self.click_element(eBlurPage.blurtype_circle_button)
        return self

    def click_blurtype_none(self):
        self.click_element(eBlurPage.blurtype_none_button)
        return self

    def click_rectangle(self):
        self.click_element(eBlurPage.rectangle_button)
        return self

    def click_ellipse(self):
        self.click_element(eBlurPage.ellipse_button)
        return self

    def click_circle(self):
        self.click_element(eBlurPage.circle_button)
        return self

    def click_brush(self):
        self.click_element(eBlurPage.brush_button)
        return self


class BlurPenPanel(pages.YCP_base.YCPBase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_arrow_down(self):
        self.click_element(eBlurPenPanel.arrow_down_button)
        return BlurPage(self.driver)

    def set_pen_opacity(self):
        self.send_keys_to_element(eBlurPenPanel.pen_opacity_bar)
        return self

    def set_pen_size(self):
        self.send_keys_to_element(eBlurPenPanel.pen_size_bar)
        return self

    def set_pen_hardness(self):
        self.send_keys_to_element(eBlurPenPanel.pen_hardness_bar)
        return self


class MosaicPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_invert_mask(self):
        self.click_element(eMosaicPage.invert_mask_button)
        return self

    def click_auto_detect(self):
        self.click_element(eMosaicPage.auto_detect_button)
        return self

    def click_reset(self):
        self.click_element(eMosaicPage.reset_button)
        return self

    def click_undo_buttton(self):
        self.click_element(eMosaicPage.undo_buttton)
        return self

    def click_eraser(self):
        self.click_element(eMosaicPage.eraser_button)
        return self

    def click_paint(self):
        self.click_element(eMosaicPage.paint_button)
        return self

    def select_dot_item(self, num: int):
        self.select_element_by_number(eMosaicPage.dot_item, num)
        return self

    def set_size_slider(self, num: int):
        self.send_keys_to_element(eMosaicPage.slide_bar, num)
        return self


class CutOutPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_auto_detect(self):
        self.click_element(eCutOutPage.auto_detect_button)
        return self

    def click_reverse(self):
        self.click_element(eCutOutPage.reverse_button)
        return self

    def click_reset(self):
        self.click_element(eCutOutPage.reset_button)
        return self

    def click_undo(self):
        self.click_element(eCutOutPage.undo_button)
        return self

    def select_dot_item(self):
        self.select_element_by_number(eCutOutPage.dot_item)
        return

    def click_eraser(self):
        self.click_element(eCutOutPage.eraser_button)
        return self

    def click_paint(self):
        self.click_element(eCutOutPage.paint_button)
        return self

    def click_smart_brush_toggle(self):
        self.click_element(eCutOutPage.smart_brush_toggle)
        return self


class ClonePage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_redo(self):
        self.click_element(eClonePage.redo_button)
        return self

    def click_undo(self):
        self.click_element(eClonePage.undo_button)
        return self

    def select_dot_item(self, num: int):
        self.select_element_by_number(eClonePage.dot_item, num)
        return self

    def click_eraser(self):
        self.click_element(eClonePage.eraser_button)
        return self

    def click_paint(self):
        self.click_element(eClonePage.paint_button)
        return self


class EffectPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_animation_catogory_list(self):
        self.scroll_horizontal(eEffectPage.animation_catogory_list)
        return self

    def scroll_effect_list(self):
        self.scroll_horizontal(eEffectPage.effect_list)
        return self

    def click_capture(self):
        self.click_element(eEffectPage.capture_button)
        return self

    def click_play(self):
        self.click_element(eEffectPage.play_button)
        return self

    def click_pause(self):
        self.click_element(eEffectPage.pause_button)
        return self

    def click_erase(self):
        self.click_element(eEffectPage.erase_button)
        return self

    def click_panel_disable(self):
        self.click_element(eEffectPage.panel_disable_button)
        return self

    def click_forbidden(self):
        self.click_element(eEffectPage.forbidden_button)
        return self

    def click_store(self):
        self.click_element(eEffectPage.store_button)
        return pages.store.StorePage(self.driver)

    def select_filter_item(self, num: int):
        self.select_element_by_number(eEffectPage.effect_panel_item, num)
        return self

    def select_filter(self, feature_name: str):
        for i in range(5):
            try:
                self.click_element_by_text(feature_name)
                break
            except:
                self.scroll_horizontal(eEffectPage.effect_list)
        return self

    def select_animation_category(self, feature_name: str):
        for i in range(5):
            try:
                self.click_element_by_text(feature_name)
                break
            except:
                self.scroll_horizontal(eEffectPage.animation_catogory_list)
        return self

    def select_animation_item(self, num: int):
        self.select_element_by_number(eEffectPage.animation_item, num)
        return self

    def set_intensity_bar(self, num: int):
        self.send_keys_to_element(eEffectPage.effect_intensity_bar, num)
        return self

    def set_speed_bar(self, speed: float):
        self.send_keys_to_element(eEffectPage.effect_intensity_bar, speed)
        return self

    def set_feature_value(self, feature_name: str, value: int):
        self.click_element_by_text(feature_name)
        self.send_keys_to_element(eEffectPage.effect_intensity_bar, value)
        return self

    def click_animation_tab(self):
        self.click_element(eEffectPage.animation_tab)
        return self

    def click_filter_tab(self):
        self.click_element(eEffectPage.filter_tab)
        return self


class AnimationPage(EditFeatureRoom):
    def __init__(self, driver):
        super().__init__(driver)

    def click_wraparounds_tab(self):
        self.click_element(eAnimationPage.wraparounds_tab)
        return self

    def click_stickers_tab(self):
        self.click_element(eAnimationPage.stickers_tab)
        return self

    def click_effects_tab(self):
        self.click_element(eAnimationPage.effects_tab)
        return self


class RemovalPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_remove(self):
        self.click_element(eRemovalPage.remove_button)
        return self

    def click_redo(self):
        self.click_element(eRemovalPage.redo_button)
        return self

    def click_undo(self):
        self.click_element(eRemovalPage.undo_button)
        return self

    def click_eraser(self):
        self.click_element(eRemovalPage.eraser_button)
        return self

    def click_paint(self):
        self.click_element(eRemovalPage.paint_button)
        return self


class AdjustPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def scroll_feature_list(self):
        self.scroll(eAdjustPage.feature_list)
        return self

    def click_undo(self):
        self.click_element(eAdjustPage.undo_button)
        return self

    def select_feature(self, feature_name: str):
        for i in range(5):
            try:
                self.click_element_by_text(feature_name)
                break
            except:
                self.scroll_horizontal(eAdjustPage.feature_list)

    def set_intensity_value(self, num: int):
        self.send_keys_to_element(eAdjustPage.intensity_bar, num)
        return self


class MagicBrushPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_brush_item(self, num: int):
        self.select_element_by_number(eMagicBrushPage.brush_item, num)
        return self

    def click_reset(self):
        self.click_element(eMagicBrushPage.reset_button)
        return self

    def click_undo(self):
        self.click_element(eMagicBrushPage.undo_button)
        return self

    def click_eraser(self):
        self.click_element(eMagicBrushPage.eraser)
        return self


class StickerPage(EditFeatureRoom, ColorPickerPanel):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_store(self):
        self.click_element(eStickerPage.store_button)
        return pages.store.StorePage

    def scroll_sticker_list(self):
        self.scroll_horizontal(eStickerPage.sticker_list)
        return self

    def click_create_my_sticker(self):
        self.click_element(eStickerPage.create_my_sticker)
        return self

    def click_dialog_delete(self):
        self.click_element(eStickerPage.dialog_delete)
        return self

    def click_dialog_cancel(self):
        self.click_element(eStickerPage.dialog_cancel)
        return self

    def click_delete_icon(self):
        self.click_element(eStickerPage.delete_icon)
        return self

    def click_layer_down(self):
        self.click_element(eStickerPage.layer_down_button)
        return self

    def click_layer_up(self):
        self.click_element(eStickerPage.layer_up_button)
        return self

    def select_sticker_panel_item(self, num: int):
        self.select_element_by_number(eStickerPage.sticker_panel_item, num)
        return self


class InstaFitPage(EditFeatureRoom, ColorPickerPanel, RatioPanel, BackgroundPanel):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_tab(self, tab_name: str):
        self.click_element_by_text(tab_name)
        return self

    def click_main_photo(self):
        self.click_element(eInstaFitPage.main_photo)
        return self


class MainPhotoEraserPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_auto_detect(self):
        self.click_element(eMainPhotoEraserPage.auto_detect_button)
        return self

    def click_reset(self):
        self.click_element(eMainPhotoEraserPage.reset_button)
        return self

    def click_undo(self):
        self.click_element(eMainPhotoEraserPage.undo_button)
        return self

    def select_dot_item(self):
        self.select_element_by_number(eMainPhotoEraserPage.dot_item)
        return self

    def click_paint(self):
        self.click_element(eMainPhotoEraserPage.paint_button)
        return self


class FramePage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def scroll_frame_list(self):
        self.scroll_horizontal(eFramePage.frame_list)
        return self

    def click_store(self):
        self.click_element(eFramePage.store_button)
        return pages.store.StorePage(self.driver)

    def select_frame_item(self, frame_name: str):
        self.click_element_in_list(frame_name, eFramePage.frame_list)
        return self


class BackgroundPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_change_background(self):
        self.click_element(eBackgroundPage.change_background_button)
        return ChangeBackgroundPage(self.driver)

    def click_add_background(self):
        self.click_element(eBackgroundPage.add_background_button)
        return AddBackgroundPage(self.driver)

    def click_close(self):
        self.click_element(eBackgroundPage.close_button)
        return PhotoEditPage(self.driver)


class AddBackgroundPage(EditFeatureRoom, RatioPanel, ColorPickerPanel, BackgroundPanel):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def set_blur_slider_bar(self, value: int):
        self.send_keys_to_element(seek_bar, value)
        return self


class TemplatePage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_store(self):
        self.click_element(eTemplatePage.store_button)
        return pages.store.StorePage(self.driver)


class ChangeBackgroundPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)


class AddPhotoPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)


class TextPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_store(self):
        self.click_element(eTextPage.store_button)
        return pages.store.StorePage(self.driver)

    def scroll_bubble_list(self):
        self.scroll_horizontal(eTextPage.bubble_list)
        return self


class BrushPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_reset(self):
        self.click_element(eBrushPage.reset_button)
        return self

    def click_undo(self):
        self.click_element(eBrushPage.undo_button)
        return self

    def click_erase_tab(self):
        self.click_element(eBrushPage.erase_tab)
        return self

    def click_brush_size_item(self):
        self.click_element(eBrushPage.brush_size_item)
        return self

    def click_size_tab(self):
        self.click_element(eBrushPage.size_tab)
        return self

    def select_select_color_item(self, num: int):
        self.select_element_by_number(eBrushPage.select_color_item, num)
        return self

    def click_color_tab(self):
        self.click_element(eBrushPage.color_tab)
        return self

    def select_style_item(self, num: int):
        self.select_element_by_number(eBrushPage.style_item, num)
        return self

    def click_style_tab(self):
        self.click_element(eBrushPage.style_tab)
        return self


class OverlayPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_flip(self):
        self.click_element(eOverlayPage.flip_button)
        return self

    def click_rotate(self):
        self.click_element(eOverlayPage.rotate_button)
        return self

    def click_overlay_list(self):
        self.click_element(eOverlayPage.overlay_list)
        return self


class BeautifyPage(EditFeatureRoom):
    def __init__(self) -> None:
        super().__init__()

    def select_feature_room(self, name: str):
        pass


class BodyTunerPage(EditFeatureRoom):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_ok(self):
        self.click_element(eBodyTunerPage.ok_button)
        return self

    def select_feature_room(self, name: str):
        self.click_element_by_text(name)
        return self
