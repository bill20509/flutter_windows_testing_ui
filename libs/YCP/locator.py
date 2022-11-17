
from ast import AsyncFunctionDef
from matplotlib import animation
from matplotlib.style import library
from libs.element import Element
seek_bar = Element('com.cyberlink.youperfect:id/EffectSeekBar', 'id')
loading_panel = Element('com.cyberlink.youperfect:id/loadingPanel', 'id')
progress_bar = Element('android.widget.ProgressBar', 'class name')


class eColorPickerPanel:
    color_list = Element('com.cyberlink.youperfect:id/colorRecyclerView', 'id')
    tool_item = Element('com.cyberlink.youperfect:id/itemImage', 'id')
    color_item = Element('com.cyberlink.youperfect:id/itemColor', 'id')
    add_color = Element(
        'com.cyberlink.youperfect:id/colorPickerAddColor', 'id')
    dripper = Element('com.cyberlink.youperfect:id/colorPickerDropper', 'id')
    color_picker_hide_tab = Element(
        'com.cyberlink.youperfect:id/colorPickerTab', 'id')
    color_picker_show_tab = Element(
        'com.cyberlink.youperfect:id/ArrowUpBtn', 'id')


class eRatioPanel:
    ratio_item = Element('com.cyberlink.youperfect:id/ratio_icon', 'id')
    ratio_list = Element(
        'com.cyberlink.youperfect:id/ratioSelectGridView', 'id')


class eLauncherPage:
    hot_feature_list = Element(
        'com.cyberlink.youperfect:id/featureItemsHost', 'id')
    scroll_view = Element('com.cyberlink.youperfect:id/nestedScrollView', 'id')
    settings_button = Element(
        "com.cyberlink.youperfect:id/settingsButton", "id")
    premium_button = Element("com.cyberlink.youperfect:id/premiumButton", "id")
    app_logo = Element("com.cyberlink.youperfect:id/imageViewLogo", "id")
    camera_button = Element("com.cyberlink.youperfect:id/cameraButton", "id")
    photo_edit_button = Element(
        "com.cyberlink.youperfect:id/editorButton", "id")
    beautify_button = Element(
        "com.cyberlink.youperfect:id/beautIfyButton", "id")
    collage_button = Element("com.cyberlink.youperfect:id/collageButton", "id")

    discovery_button = Element(
        "com.cyberlink.youperfect:id/leftExtraButton", "id")
    store_button = Element(
        "com.cyberlink.youperfect:id/rightExtraButton", "id")

    scroll_down_hint_button = Element(
        "com.cyberlink.youperfect:id/scrollDownHint", "id")
    how_to_see_all = Element(
        "com.cyberlink.youperfect:id/textViewHowToSeeAll", "id")
    trending_see_all = Element(
        "com.cyberlink.youperfect:id/textViewTrendingSeeAll", "id")
    photo_challenge_see_all = Element(
        "com.cyberlink.youperfect:id/textViewPhotoChallengeSeeAll", "id")
    template_see_all = Element(
        'com.cyberlink.youperfect:id/textViewTemplateSeeAll', 'id')


class eEditFeatureRoom:
    apply_button = Element('com.cyberlink.youperfect:id/toolBarApplyBtn', 'id')
    close_button = Element('com.cyberlink.youperfect:id/toolBarCloseBtn', 'id')
    select_photo_button = Element(
        'com.cyberlink.youperfect:id/selectPhotoImage', 'id')
    no_thanks_button = Element(
        'com.cyberlink.youperfect:id/alertDialog_buttonPositive', 'id')
    leave_button = Element(
        'com.cyberlink.youperfect:id/alertDialog_buttonNegative', 'id')


class ePhotoEditTemplate:
    undo_button = Element("com.cyberlink.youperfect:id/EditViewUndoBtn", "id")
    redo_button = Element("com.cyberlink.youperfect:id/EditViewRedoBtn", "id")
    crown_icon_button = Element("com.cyberlink.youperfect:id/btn_hd", "id")
    save_button = Element(
        "com.cyberlink.youperfect:id/topToolBarExportBtn", "id")
    beautify_tab_button = Element(
        "com.cyberlink.youperfect:id/bottomToolBarBeautifyBtn", "id")
    edit_tab_button = Element(
        "com.cyberlink.youperfect:id/bottomToolBarEditBtn", "id")
    compare_button = Element(
        "com.cyberlink.youperfect:id/EditViewCompareBtn", "id")
    photo_view = Element(
        'com.cyberlink.youperfect:id/indicatorsContainer', 'id')


class ePhotoEditPage:
    feature_room = Element(
        "com.cyberlink.youperfect:id/editRecyclerVIew", "id")
    premium_button = Element('Premium', 'text')
    tools_button = Element('Tools', 'text')
    effects_button = Element('Effects', 'text')
    animation_button = Element('Animation', 'text')
    removal_button = Element('Removal', 'text')
    adjust_button = Element('Adjust', 'text')
    magic_brush_button = Element('Magic Brush', 'text')
    sticker_button = Element('Sticker', 'text')
    instafit_button = Element('InstaFit', 'text')
    frame_button = Element('Frame', 'text')
    background_button = Element('Background', 'text')
    add_photo_button = Element('Add Photo', 'text')
    template_button = Element('Template', 'text')
    text_button = Element('Text', 'text')
    brush_button = Element('Brush', 'text')
    overlays_button = Element('Overlays', 'text')


class eToolsCropRotatePage:
    slide_bar = Element('com.cyberlink.youperfect:id/rotate_control_bar', "id")
    image_roate = Element('com.cyberlink.youperfect:id/img_rotate_btn', "id")
    image_mirror_button = Element(
        'com.cyberlink.youperfect:id/img_mirror_btn', "id")
    image_free_button = Element(
        'com.cyberlink.youperfect:id/img_free_btn', "id")
    image_1x1_button = Element('com.cyberlink.youperfect:id/img_1x1_btn', "id")
    image_2x3_button = Element('com.cyberlink.youperfect:id/img_2x3_btn', "id")
    image_3x2_button = Element('com.cyberlink.youperfect:id/img_3x2_btn', "id")
    reset_button = Element('com.cyberlink.youperfect:id/ResetTextBtn', "id")


class ePhotoPickerPage:
    album_item = Element(
        "com.cyberlink.youperfect:id/albumItemImage", "id")
    photo_item = Element(
        "com.cyberlink.youperfect:id/photoItemImage", "id")
    photo_magnifier_icon = Element(
        "com.cyberlink.youperfect:id/photoMagnifierIcon", "id")
    bc_button = Element(
        "com.cyberlink.youperfect:id/library_cloud_album_btn", "id")
    delete_button = Element(
        "com.cyberlink.youperfect:id/library_trash_button", "id")
    delete_photo_button = Element(
        "com.cyberlink.youperfect:id/bottom_delete_btn", "id")
    delete_cancel_button = Element(
        "com.cyberlink.youperfect:id/library_action_text", "id")
    camera_button = Element(
        "com.cyberlink.youperfect:id/library_camera_button", 'id')
    back_button = Element(
        "com.cyberlink.youperfect:id/library_back_btn", 'id')
    v_button = Element(
        'com.cyberlink.youperfect:id/library_action_button', 'id')


class eSinglePhotoPage:
    share_button = Element(
        "com.cyberlink.youperfect:id/bottom_panel_share", "id")
    delete_button = Element(
        "com.cyberlink.youperfect:id/bottom_panel_delete", "id")
    beautify_button = Element(
        "com.cyberlink.youperfect:id/bottom_panel_face_beautify", "id")
    edit_button = Element(
        "com.cyberlink.youperfect:id/bottom_panel_edit", "id")
    dialog_cancel = Element(
        "com.cyberlink.youperfect:id/alertDialog_buttonPositive", "id")
    dialog_delete = Element(
        "com.cyberlink.youperfect:id/alertDialog_buttonNegative", "id")


class eResultPage:
    library_icon = Element("com.cyberlink.youperfect:id/LibraryBtn", "id")
    home_button = Element("com.cyberlink.youperfect:id/HomeBtn", "id")
    continue_editing = Element(
        "com.cyberlink.youperfect:id/continueEditing", "id")
    share_button = Element("com.cyberlink.youperfect:id/shareBtn", "id")
    photo_list_item = Element(
        "com.cyberlink.youperfect:id/display_image", "id")
    bc_button = Element("com.cyberlink.youperfect:id/cloudAlbumBtn", "id")


class ePerspectivePage:
    vertical_button = Element("vertical", "text")
    horizontal_button = Element('horizontal', 'text')
    rotate_button = Element('rotate', 'text')
    reset_button = Element('com.cyberlink.youperfect:id/ResetBtn', 'id')


class eHDRPage:
    glow_button = Element('com.cyberlink.youperfect:id/HdrGlow', 'id')
    edge_button = Element('com.cyberlink.youperfect:id/HdrEdge', 'id')


class eVignettePage:
    shade_button = Element('com.cyberlink.youperfect:id/VGShade', 'id')
    feather_button = Element('com.cyberlink.youperfect:id/VGShade', 'id')
    slide_bar = seek_bar


class eMirrorPage:
    mirror_item = Element(
        'com.cyberlink.youperfect:id/mirror_panel_item_image', "id")
    color_item = Element('com.cyberlink.youperfect:id/colorItemColor', 'id')
    slide_bar = seek_bar
    forbidden_button = Element(
        'com.cyberlink.youperfect:id/frame_panel_empty_item_image', 'id')
    offset_slider_bar = seek_bar


class eBlurPage:
    brush_button = Element('com.cyberlink.youperfect:id/BlurBrush', 'id')
    circle_button = Element('com.cyberlink.youperfect:id/BlurCircle', 'id')
    ellipse_button = Element('com.cyberlink.youperfect:id/BlurEllipse', 'id')
    rectangle_button = Element(
        'com.cyberlink.youperfect:id/BlurRectangle', 'id')
    slide_bar = seek_bar
    blurtype_none_button = Element(
        'com.cyberlink.youperfect:id/blurBokehModeNoneBtn', 'id')
    blurtype_circle_button = Element(
        'com.cyberlink.youperfect:id/blurBokehModeCircleBtn', 'id')
    blurtype_light_button = Element(
        'com.cyberlink.youperfect:id/blurBokehModeCrossBtn', 'id')
    blurtype_love_button = Element(
        'com.cyberlink.youperfect:id/blurBokehModeHeartBtn', 'id')
    blurtype_star_button = Element(
        'com.cyberlink.youperfect:id/blurBokehModeStarBtn', 'id')
    pen_button = Element('com.cyberlink.youperfect:id/BrushAdjustBtn', 'id')
    paint_button = Element('com.cyberlink.youperfect:id/BrushBtn', 'id')
    eraser_panel_button = Element(
        'com.cyberlink.youperfect:id/BottomEraserBtn', 'id')
    auto_detect_button = Element(
        'com.cyberlink.youperfect:id/FaceDetectBtn', 'id')


class eBlurPenPanel:
    pen_size_bar = Element('com.cyberlink.youperfect:id/sizeSeekBar', 'id')
    pen_opacity_bar = Element(
        'com.cyberlink.youperfect:id/opacitySeekBar', 'id')
    pen_hardness_bar = Element(
        'com.cyberlink.youperfect:id/hardnessSeekBar', 'id')
    arrow_down_button = Element(
        'com.cyberlink.youperfect:id/brushAdjustCloseBtn', 'id')


class eMosaicPage:
    dot_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')
    paint_button = Element('com.cyberlink.youperfect:id/MosaicBrushBtn', 'id')
    eraser_button = Element(
        'com.cyberlink.youperfect:id/MosaicEraserBtn', 'id')
    undo_buttton = Element('com.cyberlink.youperfect:id/UndoBtn', 'id')
    reset_button = Element('com.cyberlink.youperfect:id/ClearBtn', 'id')
    auto_detect_button = eBlurPage.auto_detect_button
    invert_mask_button = Element(
        'com.cyberlink.youperfect:id/InvertMaskBtn', 'id')
    slide_bar = seek_bar
    erase_button = Element('com.cyberlink.youperfect:id/EraserBtn', 'id')


class eClonePage:
    paint_button = Element(
        'com.cyberlink.youperfect:id/clonePanelBrushBtn', 'id')
    eraser_button = Element(
        'com.cyberlink.youperfect:id/clonePanelEraseBtn', 'id')
    dot_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/EditViewUndoBtn', 'id')
    redo_button = Element('com.cyberlink.youperfect:id/EditViewRedoBtn', 'id')


class eEffectPage:
    filter_tab = Element('com.cyberlink.youperfect:id/filterTextView', 'id')
    animation_tab = Element(
        'com.cyberlink.youperfect:id/animationTextView', 'id')
    effect_list = Element(
        'com.cyberlink.youperfect:id/EffectRecyclerArea', 'id')
    animation_catogory_list = Element(
        'com.cyberlink.youperfect:id/effectCategoryRecycleView', 'id')
    filter_item = Element(
        'com.cyberlink.youperfect:id/effect_panel_item_image', 'id')
    store_button = Element(
        'com.cyberlink.youperfect:id/effect_store_btn', 'id')
    effect_intensity_bar = seek_bar
    forbidden_button = Element(
        'com.cyberlink.youperfect:id/no_effect_btn', 'id')
    panel_disable_button = Element(
        'com.cyberlink.youperfect:id/ExtendFunctionPanel', 'id')
    erase_button = Element('com.cyberlink.youperfect:id/BottomEraserBtn', 'id')
    pause_button = Element('com.cyberlink.youperfect:id/pauseButton', 'id')
    play_button = Element('com.cyberlink.youperfect:id/playButton', 'id')
    capture_button = Element(
        'com.cyberlink.youperfect:id/animationTakePhotoView', 'id')
    animation_item = Element('com.cyberlink.youperfect:id/effect_icon', 'id')

    fold_button = Element(
        'com.cyberlink.youperfect:id/try_it_image_view_background', 'id')
    adjust_panel_button = Element(
        'com.cyberlink.youperfect:id/grid_adjust', 'id')


class eAnimationPage:
    effects_tab = Element('EFFECTS', 'text')
    stickers_tab = Element('STICKERS', 'text')
    wraparounds_tab = Element('WRAPAROUNDS', 'text')
    animation_item = Element('com.cyberlink.youperfect:id/effect_icon', 'id')
    forbidden_button = Element(
        'com.cyberlink.youperfect:id/no_effect_btn', 'id')
    speed_bar = seek_bar
    capture_button = Element(
        "com.cyberlink.youperfect:id/animationTakePhotoView", 'id')


class eRemovalPage:
    paint_button = Element(
        'com.cyberlink.youperfect:id/removalPanelBrushBtn', 'id')
    eraser_button = Element(
        'com.cyberlink.youperfect:id/removalPanelEraseBtn', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/EditViewUndoBtn', 'id')
    redo_button = Element('com.cyberlink.youperfect:id/EditViewRedoBtn', 'id')
    i_button = Element('com.cyberlink.youperfect:id/moduleTitleIcon', 'id')
    remove_button = Element('com.cyberlink.youperfect:id/removeBtn', 'id')


class eAdjustPage:
    feature_list = Element('com.cyberlink.youperfect:id/scrollView', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/UndoBtn', 'id')
    intensity_bar = seek_bar
    hue_bar = Element('com.cyberlink.youperfect:id/hueSeekBar', 'id')
    saturation_bar = Element(
        'com.cyberlink.youperfect:id/saturationSeekBar', 'id')
    lightness_bar = Element(
        'com.cyberlink.youperfect:id/lightnessSeekBar', 'id')


class eMagicBrushPage:
    eraser = Element('com.cyberlink.youperfect:id/BottomEraserBtn', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/UndoBtn', 'id')
    reset_button = Element('com.cyberlink.youperfect:id/ClearBtn', 'id')
    brush_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')


class eCutOutPage:
    smart_brush_toggle = Element(
        'com.cyberlink.youperfect:id/smartBrushSwitch', 'id')
    paint_button = Element('com.cyberlink.youperfect:id/toolBarBrushBtn', 'id')
    eraser_button = Element(
        'com.cyberlink.youperfect:id/toolBarEraseBtn', 'id')
    dot_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')
    undo_button = Element(
        'com.cyberlink.youperfect:id/cutoutMaskUndoBtn', 'id')
    reset_button = Element(
        'com.cyberlink.youperfect:id/cutoutMaskClearBtn', 'id')
    reverse_button = Element(
        'com.cyberlink.youperfect:id/cutoutMaskInvertBtn', 'id')
    auto_detect_button = Element(
        'com.cyberlink.youperfect:id/cutoutAutoMaskBtn', 'id')


class eStickerPage:
    sticker_list = Element(
        'com.cyberlink.youperfect:id/EffectRecyclerArea', 'id')
    sticker_panel_item = Element(
        'com.cyberlink.youperfect:id/sticker_panel_item_image', 'id')
    layer_up_button = Element('com.cyberlink.youperfect:id/layerUpBtn', 'id')
    layer_down_button = Element(
        'com.cyberlink.youperfect:id/layerDownBtn', 'id')
    delete_icon = Element('com.cyberlink.youperfect:id/delete_ico', 'id')
    dialog_cancel = Element(
        "com.cyberlink.youperfect:id/alertDialog_buttonPositive", "id")
    dialog_delete = Element(
        "com.cyberlink.youperfect:id/alertDialog_buttonNegative", "id")
    create_my_sticker = Element(
        'com.cyberlink.youperfect:id/myStickerActionTxt', 'id')
    store_button = Element(
        'com.cyberlink.youperfect:id/effect_store_btn', 'id')
    auto_cut_button = Element(
        'com.cyberlink.youperfect:id/cutoutAutoMaskBtn', 'id')


class eBackgroundPanel:
    background_item = Element(
        'com.cyberlink.youperfect:id/background_icon', 'id')
    library_icon = Element(
        'com.cyberlink.youperfect:id/background_album', 'id')
    store_button = Element(
        'com.cyberlink.youperfect:id/background_store_btn', 'id')
    background_list = Element(
        'com.cyberlink.youperfect:id/backgroundSelectGridView', 'id')

    forbidden_button = Element(
        'com.cyberlink.youperfect:id/frame_panel_empty_item_image', 'id')
    unpanel_button = Element(
        'com.cyberlink.youperfect:id/BottomEraserBtn', 'id')

    config_icon = Element('com.cyberlink.youperfect:id/advancedAdjust', 'id')
    feather_button = Element('Feather', 'text')
    blur_button = Element('Blur', 'text')
    apply_button = Element('com.cyberlink.youperfect:id/toolBarApplyBtn', 'id')
    save_button = Element(
        'com.cyberlink.youperfect:id/topToolBarExportBtn', 'id')


class eMainPhotoPage:

    tools_list = Element('com.cyberlink.youperfect:id/editBottomToolBar', 'id')
    effect_bar = seek_bar
    blender_list = Element(
        'com.cyberlink.youperfect:id/blenderSwipeTabBar', 'id')
    opacity_button = Element('Opacity', 'text')
    border_button = Element('Border', 'text')
    blender_button = Element('Blender', 'text')
    eraser_button = Element('Eraser', 'text')
    effects_button = Element('Effects', 'text')
    crop_and_rotate = Element('Crop & Rotate', 'text')
    cutout_button = Element('Cutout', 'text')
    adjust_button = Element('Adjust', 'text')


class eInstaFitPage:
    main_photo = Element('com.cyberlink.youperfect:id/photoEditView', 'id')


class eMainPhotoEraserPage:
    paint_button = Element('com.cyberlink.youperfect:id/BrushBtn', 'id')
    dot_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/UndoBtn', 'id')
    reset_button = Element('com.cyberlink.youperfect:id/ClearBtn', 'id')
    auto_detect_button = Element(
        'com.cyberlink.youperfect:id/FaceDetectBtn', 'id')


class eFramePage:
    store_button = Element('com.cyberlink.youperfect: id/store_btn', 'id')
    frame_list = Element(
        'com.cyberlink.youperfect:id/frame_recycler_view', 'id')


class eBackgroundPage:
    close_button = Element(
        'com.cyberlink.youperfect:id/bottomToolBarBackgroundCloseBtn', 'id')
    add_background_button = Element(
        'com.cyberlink.youperfect:id/bottomToolBarAddBackgroundBtn', 'id')
    change_background_button = Element(
        'com.cyberlink.youperfect:id/bottomToolBarChangeBackgroundBtn', 'id')


class eAddBackgroundPage:
    blur_slider_bar = seek_bar


class eChangeBackgroundPage:
    pass


class eAddPhotoPage:
    # Josh
    add_more_button = Element('com.cyberlink.youperfect:id/layerPlusBtn', 'id')
    add_photo_button = Element('com.cyberlink.youperfect:id/AddPhotoBtn', 'id')
    add_text_button = Element('com.cyberlink.youperfect:id/AddTextBtn', 'id')
    add_stickers_button = Element(
        'com.cyberlink.youperfect:id/AddStickerBtn', 'id')
    crop_reset_button = Element('com.cyberlink.youperfect:id/resetBtn', 'id')
    duplicate_button = Element(
        'com.cyberlink.youperfect:id/layerDuplicateBtn', 'id')
    undo_button = Element('com.cyberlink.youperfect:id/EditViewUndoBtn', 'id')
    redo_button = Element('com.cyberlink.youperfect:id/EditViewRedoBtn', 'id')
    yes_button = Element(
        'com.cyberlink.youperfect:id/alertDialog_buttonPositive', 'id')
    no_button = Element(
        'com.cyberlink.youperfect:id/alertDialog_buttonNegative', 'id')


class eTemplatePage:
    store_button = Element(
        'com.cyberlink.youperfect:id/templateStoreBtn', 'id')


class eTextPage:
    bubble_list = Element(
        'com.cyberlink.youperfect:id/tbBubbleTemplateGridView', 'id')
    effect_intensity_bar = seek_bar
    store_button = Element(
        'com.cyberlink.youperfect:id/frameItemMoreImage', 'id')


class eBrushPage:
    style_tab = Element('STYLE', 'text')
    style_item = Element('com.cyberlink.youperfect:id/brush_style_icon', 'id')
    color_tab = Element('COLOR', 'text')
    select_color_item = Element(
        'com.cyberlink.youperfect:id/brush_style_icon', 'id')
    size_tab = Element('SIZE', 'text')
    brush_size_item = Element(
        'com.cyberlink.youperfect:id/brush_style_icon', 'id')
    erase_tab = Element('ERASE', 'text')
    undo_button = Element('com.cyberlink.youperfect:id/UndoBtn', 'id')
    reset_button = Element('com.cyberlink.youperfect:id/ClearBtn', 'id')


class eOverlayPage:
    overlay_list = Element(
        'com.cyberlink.youperfect:id/overlaysGridArea', 'id')
    rotate_button = Element('com.cyberlink.youperfect:id/RotateBtn', 'id')
    flip_button = Element('com.cyberlink.youperfect:id/FlipBtn', 'id')


class eCameraPage:
    mode_button = Element(
        'com.cyberlink.youperfect:id/cameraSettingButton', 'id')
    mode_general = Element(
        'com.cyberlink.youperfect:id/captureGeneralButton', 'id')
    mode_touch = Element(
        'com.cyberlink.youperfect:id/captureTouchButton', 'id')
    mode_detect = Element(
        'com.cyberlink.youperfect:id/captureDetectButton', 'id')
    mode_wave_detect = Element(
        'com.cyberlink.youperfect:id/captureWaveDetectButton', 'id')
    more_button = Element(
        'com.cyberlink.youperfect:id/camera_menu_btn', 'id')
    more_blur_button = Element(
        'com.cyberlink.youperfect:id/liveBlurButton', 'id')
    more_grid_button = Element(
        'com.cyberlink.youperfect:id/liveLineButton', 'id')
    more_timestamp_button = Element(
        'com.cyberlink.youperfect:id/cameraTimeStamp', 'id')
    more_autosave_button = Element(
        'com.cyberlink.youperfect:id/cameraAutoSave', 'id')
    more_settings_button = Element(
        'com.cyberlink.youperfect:id/cameraSettings', 'id')
    timer_button = Element(
        'com.cyberlink.youperfect:id/cameraTimerButton', 'id')
    switch_camera_button = Element(
        'com.cyberlink.youperfect:id/cameraFacingButton', 'id')


class eBodyTunerPage:
    ok_button = Element('com.cyberlink.youperfect:id/button', 'id')
