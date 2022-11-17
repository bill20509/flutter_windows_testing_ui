# 各項element ID
from libs.element import Element


class OpeningTutorialPageLocators:
    GetStarted_button = Element(
        "com.cyberlink.youcammakeup:id/getStartBtn", "id", "xxx buton")
    Skip_button = "com.cyberlink.youcammakeup:id/tutorialSkipBtn"
    Skip_confirm_button = "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive"
    Background_id = "com.cyberlink.youcammakeup:id/opening_tutorial_background"


class LauncherLocators:
    Makeup_cam = Element(
        "com.cyberlink.youcammakeup:id/cameraImage", "id", "MakeupCam button")
    Photo_makeup = Element(
        "com.cyberlink.youcammakeup:id/photoMakeupImage", "id", "PhotoMakeup button")
    Store_button = "com.cyberlink.youcammakeup:id/shop_button"
    Aging_tile = Element("com.cyberlink.youcammakeup:id/launcherAgingTile", "id", "Aging tile")
    Skincare_tile = Element("com.cyberlink.youcammakeup:id/launcherSkinCareTile", "id", "Skincare tile")
    YCV_tile = Element("com.cyberlink.youcammakeup:id/launcher_ycvb_tile", "id", "YCV tile")
    YCP_tile = Element("com.cyberlink.youcammakeup:id/launcher_ycp_tile", "id", "YCP tile")
    Crown = Element("com.cyberlink.youcammakeup:id/premium_button", "id", "Crown button")
    AD_banner = Element("com.cyberlink.youcammakeup:id/ad_media_container", "id", "Launcher AD Banner")
    IAP_banner = Element("com.cyberlink.youcammakeup:id/iapFlatBanner", "id", "IAP Banner")
    AD_Close = Element("com.cyberlink.youcammakeup:id/launcher_ad_close_btn", "id", "AD close button")
    Me_button = Element("com.cyberlink.youcammakeup:id/bc_me_icon", "id", "Me Button")
    bc_button = Element("com.cyberlink.youcammakeup:id/bc_discover_icon", "id", "BC button")
    iap = Element("com.cyberlink.youcammakeup:id/dialogExContainer",
                  "id", "Launcher iap")
    AD_hw_back = Element("com.cyberlink.youcammakeup:id/native_ad_media_container", "id", "HW BACK AD")
    Features_card = Element("com.cyberlink.youcammakeup:id/featuredItems", "id", "Features Card")
    Look_card = Element("com.cyberlink.youcammakeup:id/launcherLookItems", "id", "Look Card")
    Howto_card = Element("com.cyberlink.youcammakeup:id/howToItems", "id", "Howto Card")
    Shows_card = Element("com.cyberlink.youcammakeup:id/liveShowItems", "id", "Shows Card")
    Community_trending_card = Element("com.cyberlink.youcammakeup:id/editorChoiceItemsHost", "id", "Trending Card")
    Instant_Makeover_card = Element("com.cyberlink.youcammakeup:id/retouchItems", "id", "Makeover Card")
    Get_Inspired_button = Element("com.cyberlink.youcammakeup:id/launcherInstagramEntry", "id", "GetInspired Button")
    Launcher_view = Element("com.cyberlink.youcammakeup:id/nestedScrollView", "id", "Launcher view")


class PickPhotoLocators:
    album_view = Element(
        "com.cyberlink.youcammakeup:id/AlbumView", "id", "Album view")
    select_folder = Element(
        "com.cyberlink.youcammakeup:id/albumDisplayName", "xpath", "Select folder")
    photo_view = Element(
        "com.cyberlink.youcammakeup:id/PhotoView", "id", "Photo view")
    select_photo = Element(
        "com.cyberlink.youcammakeup:id/photoItemImage", "id", "Select photo")
    Back_to_album = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", "id",
                            "Photo picker back button")
    iap = Element("com.cyberlink.youcammakeup:id/dialogExContainer", "id", "Photo picker iap")
    photo_picker_ad = Element("com.cyberlink.youcammakeup:id/native_ad_media_container", "id", "Photo picker AD")
    delete_button = Element("com.cyberlink.youcammakeup:id/topToolBarDeleteBtn", "id", "Delete button")
    dialog_delete_button = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id",
                                   "Delete button on the dialog")
    system_delete_button = Element("android:id/button1", "id", "Delete button on the system dialog")
    Back_to_launcher = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", "id",
                               "Album page back button")


class PhotoMakeupLocators:
    # 介面按鈕
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtn",
                   "id", "Back to photo picker")
    CANCEL = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative",
                     "id", "Back dialog: CANCEL leave edit page")
    LEAVE = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive",
                    "id", "Back dialog: Leave photo edit page")
    Switch_Face = Element(
        "com.cyberlink.youcammakeup:id/TopBarSwitchFaceBtn", "id", "Switch face button")
    Undo = Element("com.cyberlink.youcammakeup:id/EditViewUndoBtn",
                   "id", "Undo edit button")
    Redo = Element("com.cyberlink.youcammakeup:id/EditViewRedoBtn",
                   "id", "Redo edit button")
    Save = Element(
        "com.cyberlink.youcammakeup:id/topToolBarExportBtn", "id", "Save button")
    Manual = Element(
        "com.cyberlink.youcammakeup:id/EditViewManualBtn", "id", "Fine Tune button")
    Detail = Element(
        "com.cyberlink.youcammakeup:id/EditViewDetailBtn", "id", "Detail button")
    Compare = Element(
        "com.cyberlink.youcammakeup:id/EditViewCompareBtn", "id", "Compare button")
    wait_animation = Element(
        "com.cyberlink.youcammakeup:id/lookNameTextView", "id", "Wait animation")
    waiting_cursor = Element(
        "com.cyberlink.youcammakeup:id/busy_indicator_switcher", "id", "waiting cursor")

    # 共享欄位按鈕清單
    brand_menu = Element(
        "com.cyberlink.youcammakeup:id/toolView", "id", "brand menu")
    brand_menu_view = Element(
        "com.cyberlink.youcammakeup:id/skuVendorMenu", "id", "Brand list")
    brand = Element("com.cyberlink.youcammakeup:id/skuItemVendorName",
                    "xpath", "Select brand by name")
    pattern_grid_view = Element(
        "com.cyberlink.youcammakeup:id/patternGridView", "id", "Pattern grid view")
    pattern_recycle_view = Element(
        "com.cyberlink.youcammakeup:id/patternRecyclerView", "id", "pattern_recycle_view")
    sku_series_image = Element(
        "com.cyberlink.youcammakeup:id/sku_series_image", "id", "sku_series_image")
    edit_View_bottom_region = Element(
        "com.cyberlink.youcammakeup:id/editViewBottomBarRegion", "id", "edit_View_bottom_region")
    pattern_list = Element(
        "com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "pattern_list")
    pattern_text = Element(
        "com.cyberlink.youcammakeup:id/camera_lipstick_pattern_text", "xpath", "Select pattern by name")
    tab_recycle_view = Element(
        "com.cyberlink.youcammakeup:id/tabRecyclerView", "id", "Tab view")
    tab_room_pattern = Element(
        "com.cyberlink.youcammakeup:id/room_tab_pattern", "xpath", "Select tab room by name")
    tab_text = Element("com.cyberlink.youcammakeup:id/tabText",
                       "xpath", "Select tab by name")
    color_grid_view = Element(
        "com.cyberlink.youcammakeup:id/colorGridView", "id", "Color grid view")
    color_content = Element(
        "com.cyberlink.youcammakeup:id/item_color_content", "id", "Select content color ball")
    slider_bar = Element(
        "com.cyberlink.youcammakeup:id/unitSeekBar", "id", "Slider bar")
    makeup_menu = Element("com.cyberlink.youcammakeup:id/makeupMenu", "id", "makeup menu")
    category = Element("com.cyberlink.youcammakeup:id/makeup_menu_item_title",
                       "xpath", "Select category by name")
    feature_list = Element(
        "com.cyberlink.youcammakeup:id/makeup_menu_expandable_title", "xpath", "All feature list view")
    reshape_item = Element(
        "com.cyberlink.youcammakeup:id/itemName", "xpath", "Reshape functions list")
    panel_view = Element(
        "com.cyberlink.youcammakeup:id/panel_bottom_area", "id", "panel_view")
    menu_back = Element(
        "com.cyberlink.youcammakeup:id/makeup_menu_expandable_back_btn", "id", "Menu back button")
    yes = Element(
        "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Yes button")
    favorite = Element(
        "com.cyberlink.youcammakeup:id/saveCustomLookButton", "id", "Add to favorite")

    class FineTune:
        Face = Element(
            "com.cyberlink.youcammakeup:id/fineTuneFaceButton", "id", "Face button")
        Left_eye = Element(
            "com.cyberlink.youcammakeup:id/fineTuneLeftEyeButton", "id", "Left_eye button")
        Right_eye = Element(
            "com.cyberlink.youcammakeup:id/fineTuneRightEyeButton", "id", "Right_eye button")
        Lips = Element(
            "com.cyberlink.youcammakeup:id/fineTuneLipsButton", "id", "Lips button")
        Mouth_Open = Element(
            "com.cyberlink.youcammakeup:id/EditViewMouthSwitchBtn", "id", "Mouth Open button")
        Close = Element(
            "com.cyberlink.youcammakeup:id/fineTuneCloseBtn", "id", "Close button")
        Apply = Element(
            "com.cyberlink.youcammakeup:id/fineTuneApplyBtn", "id", "Apply button")

    class SwitchFace:
        Cancel = Element(
            "com.cyberlink.youcammakeup: id/faceSwitcherActionBarCancelButton", "id", "Cancel button")
        Add_Face = Element(
            "com.cyberlink.youcammakeup:id/faceSwitcherActionBarAddFaceButton", "id", "Add face button")
        Apply = Element(
            "com.cyberlink.youcammakeup:id/faceSwitcherActionBarApplyButton", "id", "Apply button")

    class Looks:
        look_item_download_icon = Element(
            "com.cyberlink.youcammakeup:id/lookItemDownloadIcon", "id", "Look item download icon")
        look_item_download_progress = Element(
            "com.cyberlink.youcammakeup:id/lookItemDownloadProgress", "id", "Look item download progress")
        look_item_view = Element("com.cyberlink.youcammakeup:id/makeupLooksGridView", "id", "Look item view")
        look_item_name = Element("com.cyberlink.youcammakeup:id/lookItemName", "xpath", "Select xxx look")
        look_category_view = Element("com.cyberlink.youcammakeup:id/lookCategoryRecyclerView", "id", "")
        look_image = Element("com.cyberlink.youcammakeup:id/lookPhoto", "id", "Click look image")
        CANCEL = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", "id", "Cancel download")
        CONTINUE = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Continue download")
        store = Element("com.cyberlink.youcammakeup:id/lookMoreBtnContainer", "id", "template store button")
        heart = Element("com.cyberlink.youcammakeup:id/favoriteIcon", "id", "Heart favorite icon")
        crown = Element("com.cyberlink.youcammakeup:id/premiumIcon", "id", "Crown premium icon")
        add_favorite = Element("com.cyberlink.youcammakeup:id/circleView", "id", "Add favorite")
        favorite_icon = Element("com.cyberlink.youcammakeup:id/lookFavoriteIcon", "id", "Favorite icon")
        look_info = Element("com.cyberlink.youcammakeup:id/lookInformation", "id", "Look info button")
        share_to_YC = Element("com.cyberlink.youcammakeup:id/shareToYouCam", "id", "share_to_YouCam Community")
        look_view = Element("com.cyberlink.youcammakeup:id/lookPhoto", "id", "look view")

    class Mouth:
        download_store = Element(
            "com.cyberlink.youcammakeup:id/downloadButton", "id", "Mouth download store button")
        mouth_download_progress = Element(
            "com.cyberlink.youcammakeup:id/downloadItemProgress", "id", "Mouth download progress")

    class Face:
        Left = Element("com.cyberlink.youcammakeup:id/leftButton",
                       "id", "Face Reshape left button")
        Overall = Element("com.cyberlink.youcammakeup:id/overallButton",
                          "id", "Face Reshape overall button")
        Right = Element("com.cyberlink.youcammakeup:id/rightButton",
                        "id", "Face Reshape right button")
        process_dialog = Element(
            "com.cyberlink.youcammakeup:id/customToast", "id", "Processing dialog")
        download_store = Element(
            "com.cyberlink.youcammakeup:id/downloadButton", "id", "Hair download store button")
        switch_button = Element(
            "com.cyberlink.youcammakeup:id/switchBtn", "id", "Switch ON and OFF")

    class Eye:
        Left = Element("com.cyberlink.youcammakeup:id/leftButton",
                       "id", "Face Reshape left button")
        Overall = Element("com.cyberlink.youcammakeup:id/overallButton",
                          "id", "Face Reshape overall button")
        Right = Element("com.cyberlink.youcammakeup:id/rightButton",
                        "id", "Face Reshape right button")
        switch_button = Element(
            "com.cyberlink.youcammakeup:id/switchBtn", "id", "Switch ON and OFF")
        tab_pattern = Element(
            "com.cyberlink.youcammakeup:id/room_tab_pattern", "id", "Click pattern tab")
        original_pattern = Element(
            "(//*[@text='Original'])", "xpath", "Click original_pattern")
        tab_color = Element(
            "com.cyberlink.youcammakeup:id/room_tab_color", "id", "Click color tab")
        tab_eyelashes = Element(
            "com.cyberlink.youcammakeup:id/room_tab_eyelashes", "id", "Click eyelashes tab")
        tab_mascara = Element(
            "com.cyberlink.youcammakeup:id/room_tab_mascara", "id", "Click mascara tab")
        eyelid_pattern_list = Element(
            "com.cyberlink.youcammakeup:id/theGridView", "id", "eyelid patterns view")
        eyelid_pattern = Element(
            "com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "Double eyelid patterns")
        eyeshadow_collection = Element(
            "com.cyberlink.youcammakeup:id/sku_series_text", "xpath", "Select Eyeshadow collection")
        eyeshadow_palette = Element(
            "com.cyberlink.youcammakeup:id/colorChooserCover", "id", "Select Eyeshadow palette")
        eyeshadow_palette_box1 = Element(
            "com.cyberlink.youcammakeup:id/colorChooser1", "id", "Select Eyeshadow palette box")
        eyeshadow_palette_Area = Element(
            "com.cyberlink.youcammakeup:id/colorArea", "id", "Eyeshadow palette box")
        delete_palette = Element(
            "com.cyberlink.youcammakeup:id/panel_beautify_template_close_icon", "id", "Select Eyeshadow palette box")
        eyeshadow_extra = Element(
            "com.cyberlink.youcammakeup:id/openPaletteBrowserBtn", "id", "delete Eyeshadow palette")
        eyeshadow_palette_color = Element(
            "com.cyberlink.youcammakeup:id/colorView", "id", "Select Eyeshadow palette color")
        eyeshadow_palette_color_view = Element(
            "com.cyberlink.youcammakeup:id/colorRecyclerView", "id", "Eyeshadow palette color view")
        shimmer_switcher = Element(
            "com.cyberlink.youcammakeup:id/shimmerSwitcher", "id", "Shimmer swithcer icon")
        heart_icon = Element(
            "com.cyberlink.youcammakeup:id/favoriteButton", "id", "Heart icon")
        color_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[1]", "xpath", "Color intensity seekbar")
        size_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "Size intensity seekbar")
        shape_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "Shape intensity seekbar")
        x_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[1]", "xpath", "X intensity seekbar")
        y_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "Y intensity seekbar")
        download_store = Element(
            "com.cyberlink.youcammakeup:id/downloadButton", "id", "download store button")
        smashbox_entry = Element("com.cyberlink.youcammakeup:id/smashBoxAIEntry", "id", "Smashbox AI entry button")

    class Hair:
        color_tab = Element(
            "com.cyberlink.youcammakeup:id/tabText", "xpath", "Hair Style tab menu")
        edit_color = Element(
            "com.cyberlink.youcammakeup:id/editTwoColorView", "id", "2 Colors edit")
        color_palette1 = Element(
            "com.cyberlink.youcammakeup:id/colorChooser1", "id", "2 Colors palette 1")
        color_palette2 = Element(
            "com.cyberlink.youcammakeup:id/colorChooser2", "id", "2 Colors palette 2")
        color_ball_view = Element(
            "com.cyberlink.youcammakeup:id/colorRecyclerView", "id", "2 Colors color ball view")
        color_ball = Element(
            "com.cyberlink.youcammakeup:id/colorItemColorTexture", "id", "2 Colors color ball")
        flip_button = Element(
            "com.cyberlink.youcammakeup:id/colorSwitchButton", "id", "Flip button")
        finetune_button = Element(
            "com.cyberlink.youcammakeup:id/editingManualButton", "id", "Finetune button")
        finetune_close = Element(
            "com.cyberlink.youcammakeup:id/editingActionBarCloseButton", "id", "Finetune close button")
        finetune_apply = Element(
            "com.cyberlink.youcammakeup:id/editingActionBarApplyButton", "id", "Finetune apply button")
        brush_size1 = Element(
            "com.cyberlink.youcammakeup:id/panelHairDyeBrushSizeBtn1", "id", "Finetune brush size 1")
        brush_size2 = Element(
            "com.cyberlink.youcammakeup:id/panelHairDyeBrushSizeBtn2", "id", "Finetune brush size 2")
        brush_size3 = Element(
            "com.cyberlink.youcammakeup:id/panelHairDyeBrushSizeBtn3", "id", "Finetune brush size 3")
        brush_size4 = Element(
            "com.cyberlink.youcammakeup:id/panelHairDyeBrushSizeBtn4", "id", "Finetune brush size 4")
        brush_size5 = Element(
            "com.cyberlink.youcammakeup:id/panelHairDyeBrushSizeBtn5", "id", "Finetune brush size 5")
        category_view = Element(
            "com.cyberlink.youcammakeup:id/categoryLoopView", "id", "Brush and Eraser category view")
        finetune_editroom = Element(
            "com.cyberlink.youcammakeup:id/hairDyeFineTuneView", "id", "Finetune edit room")
        tab_style = Element(
            "com.cyberlink.youcammakeup:id/room_tab_pattern", "id", "Click style tab")
        style_pattern_view = Element(
            "com.cyberlink.youcammakeup:id/patternGridView", "id", "Hair style pattern view")
        style_pattern = Element(
            "com.cyberlink.youcammakeup:id/panel_beautify_template_item_name", "xpath", "Select hair style pattern")
        style_color = Element(
            "com.cyberlink.youcammakeup:id/item_color_content", "id", "Hair style color ball")
        tab_color = Element(
            "com.cyberlink.youcammakeup:id/room_tab_color", "id", "Click color tab")
        download_store = Element(
            "com.cyberlink.youcammakeup:id/downloadButton", "id", "Hair download store button")
        coverage_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[1]", "xpath", "Coverage intensity seekbar")
        blend_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "Blend intensity seekbar")
        shine_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[1]", "xpath", "Shine intensity seekbar")
        color_seekbar = Element(
            "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "Color intensity seekbar")
        x_button_on_patter = Element(
            "com.cyberlink.youcammakeup:id/panel_beautify_template_close_icon", "id", "X button")

    class CrossPromote:
        leave_alert_dialog = Element("com.cyberlink.youcammakeup:id/alertDialog_text", "id", "Leave alert dialog")
        leave_alert_dialog_OK = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id",
                                        "Leave alert dialog OK")


class BodyTunerLocators:
    tutorial_dialog = Element(
        "com.cyberlink.youcammakeup:id/title", "id", "Tutorial dialog")
    tutorial_OK = Element(
        "com.cyberlink.youcammakeup:id/button", "id", "Tutorial OK button")
    toolbar_view = Element(
        "com.cyberlink.youcammakeup:id/toolBar", "id", "Toolbar view")
    toolbar = Element("com.cyberlink.youcammakeup:id/textView",
                      "xpath", "Select body tuner items")
    effect_seekbar = Element(
        "com.cyberlink.youcammakeup:id/EffectSeekBar", "id", "Effect seek bar")
    X_button = Element(
        "com.cyberlink.youcammakeup:id/toolBarCloseBtn", "id", "X button")
    V_button = Element(
        "com.cyberlink.youcammakeup:id/toolBarApplyBtn", "id", "V button")
    undo = Element("com.cyberlink.youcammakeup:id/UndoBtn",
                   "id", "Undo button")
    redo = Element("com.cyberlink.youcammakeup:id/RedoBtn",
                   "id", "Redo button")
    clear = Element("com.cyberlink.youcammakeup:id/ClearBtn",
                    "id", "Clear button")
    smart_brush = Element(
        "com.cyberlink.youcammakeup:id/smartBrushSwitchBtn", "id", "Smart brush button")
    brush = Element("com.cyberlink.youcammakeup:id/brushBtn",
                    "id", "Brush button")
    eraser = Element("com.cyberlink.youcammakeup:id/eraserBtn",
                     "id", "Eraser button")
    detect = Element("com.cyberlink.youcammakeup:id/detectBtn",
                     "id", "Detect button")
    waiting_cursor = Element(
        "com.cyberlink.youcammakeup:id/busy_indicator_switcher", "id", "waiting cursor")


class RemovalLocators:
    quality_alert_dialog = Element('com.cyberlink.youcammakeup:id/pf_dialog_body', 'id', "Quality Alert Dialog")
    quality_alert_ok = Element('com.cyberlink.youcammakeup:id/alertDialog_buttonNegative', 'id', "Quality Alert OK btn")
    brush_button = Element('com.cyberlink.youcammakeup:id/removalPanelBrushBtn', 'id', "Removal Brush btn")
    eraser_button = Element('com.cyberlink.youcammakeup:id/removalPanelEraseBtn', 'id', "Removal Eraser btn")
    apply_button = Element('com.cyberlink.youcammakeup:id/removeBtn', 'id', "Removal Apply btn")
    x_button = Element('com.cyberlink.youcammakeup:id/toolBarCloseBtn', 'id', "Removal X btn")
    v_button = Element('com.cyberlink.youcammakeup:id/toolBarApplyBtn', 'id', "Removal V btn")
    undo_redo_panel = Element('com.cyberlink.youcammakeup:id/UndoRedoPanel', 'id', "Undo/Redo panel")
    undo_button = Element('com.cyberlink.youcammakeup:id/EditViewUndoBtn', 'id', "Undo btn")
    redo_button = Element('com.cyberlink.youcammakeup:id/EditViewRedoBtn', 'id', "Redo btn")
    removal_canvas = Element('com.cyberlink.youcammakeup:id/makeupResultImageView', 'id', "Removal Canvas")
    addface_button = Element('com.cyberlink.youcammakeup:id/alertDialog_buttonPositive', 'id', "ADD FACE btn")
    addface_v_button = Element('com.cyberlink.youcammakeup:id/faceSwitcherActionBarApplyButton', 'id', "ADD FACE V btn")
    save_button = Element('com.cyberlink.youcammakeup:id/topToolBarExportBtn', 'id', "PhotoMakeup Save btn")


class AnimationLocators:
    Animation_button = Element(
        "00000000-0000-0e93-ffff-ffff000005ad", "id", "Animation button")
    EFFECTS = Element("com.cyberlink.youcammakeup:id/animationEffectTab",
                      "id", " Animation EFFECTS button")
    STICKERS = Element("com.cyberlink.youcammakeup:id/animationStickerTab",
                       "id", "Animation STICKERS button")
    X_button = Element(
        "com.cyberlink.youcammakeup:id/toolBarCloseBtn", "id", "Animation X button")
    V_button = Element(
        "com.cyberlink.youcammakeup:id/toolBarApplyBtn", "id", "Animation V button")
    take_photo = Element(
        "com.cyberlink.youcammakeup:id/animationTakePhotoView", "id", "Take photo button")
    null_button = Element(
        "com.cyberlink.youcammakeup:id/no_effect_btn", "id", "Effect category null button")
    effect_view = Element(
        "com.cyberlink.youcammakeup:id/effectSelectRecycleView", "id", "Effect category view")
    effect_icon = Element(
        "com.cyberlink.youcammakeup:id/effect_icon", "id", "Effect category items")
    sticker_view = Element(
        "com.cyberlink.youcammakeup:id/stickerSelectRecycleView", "id", "Sticker category view")
    sticker_icon = Element(
        "com.cyberlink.youcammakeup:id/sticker_icon", "id", "Sticker category items")
    category_text_view = Element(
        "com.cyberlink.youcammakeup:id/effectCategoryRecycleView", "id", "Category text view")
    category_text = Element(
        "com.cyberlink.youcammakeup:id/txtCategory", "xpath", "Category text")
    seekbar = Element(
        "com.cyberlink.youcammakeup:id/EffectSeekBar", "id", "Effect seekbar")
    play_cursor = Element(
        "com.cyberlink.youcammakeup:id/playCursor", "id", "Pause / Resume button")
    eraser_extend_button = Element(
        "com.cyberlink.youcammakeup:id/BottomEraserBtn", "id", "Animation Eraser button")
    detect_button = Element(
        "com.cyberlink.youcammakeup:id/FaceDetectBtn", "id", "Detect button")
    draw_button = Element(
        "com.cyberlink.youcammakeup:id/BrushBtn", "id", "Draw button")
    erase_button = Element(
        "com.cyberlink.youcammakeup:id/EraserBtn", "id", "Erase button")
    brush_view = Element(
        "com.cyberlink.youcammakeup:id/BrushStyleGridView", "id", "Stroke size")
    undo_button = Element(
        "com.cyberlink.youcammakeup:id/UndoBtn", "id", "Eraser Undo button")
    reset_button = Element(
        "com.cyberlink.youcammakeup:id/ClearBtn", "id", "Eraser Reset button")

    class Export:
        back_button = Element(
            "com.cyberlink.youcammakeup:id/topToolBarBackBtn", "id", "Back button")
        video_button = Element(
            "com.cyberlink.youcammakeup:id/videoTypeBtn", "id", "Video button")
        GIF_button = Element(
            "com.cyberlink.youcammakeup:id/gifTypeBtn", "id", "GIF button")
        Instagram_button = Element(
            "com.cyberlink.youcammakeup:id/instagramTypeBtn", "id", "Instagram button")
        Facebook_button = Element(
            "com.cyberlink.youcammakeup:id/facebookTypeBtn", "id", "Facebook button")
        ratio_view = Element(
            "com.cyberlink.youcammakeup:id/cropTypeCollection", "id", "Video ratio view")
        crop_original = Element(
            "com.cyberlink.youcammakeup:id/cropOriginal", "id", "Crop original")
        crop_16to9 = Element(
            "com.cyberlink.youcammakeup:id/crop16to9", "id", "Crop 16 to 9")
        crop_1to1 = Element(
            "com.cyberlink.youcammakeup:id/crop1to1", "id", "Crop 1 to 1")
        crop_3to4 = Element(
            "com.cyberlink.youcammakeup:id/crop3to4", "id", "Crop 3 to 4")
        crop_9to16 = Element(
            "com.cyberlink.youcammakeup:id/crop9to16", "id", "Crop 9 to 16")
        crop_4to3 = Element(
            "com.cyberlink.youcammakeup:id/crop4to3", "id", "Crop 4 to 3")
        crop_feed = Element(
            "com.cyberlink.youcammakeup:id/cropFeed", "id", "Crop feed")
        crop_story = Element(
            "com.cyberlink.youcammakeup:id/cropStory", "id", "Crop story")
        crop_4to5 = Element(
            "com.cyberlink.youcammakeup:id/crop4to5", "id", "Crop 4 to 5")
        crop_cover = Element(
            "com.cyberlink.youcammakeup:id/cropCover", "id", "Crop cover")
        crop_profile = Element(
            "com.cyberlink.youcammakeup:id/cropProfile", "id", "crop profile")
        duration_seekbar = Element(
            "com.cyberlink.youcammakeup:id/durationSeekBar", "id", "Duration seekbar")
        quality_720p = Element(
            "com.cyberlink.youcammakeup:id/quality720pBtn", "id", "Quality 720p button")
        quality_1080p = Element(
            "com.cyberlink.youcammakeup:id/quality1080pBtn", "id", "Quality 1080p button")
        quality_4k = Element(
            "com.cyberlink.youcammakeup:id/quality4KBtn", "id", "Quality 4k button")
        Export_button = Element(
            "com.cyberlink.youcammakeup:id/exportButton", "id", "Export button")
        alert_dialog = Element(
            "com.cyberlink.youcammakeup:id/alertDialog_buttonsContainer", "id", "alert_dialog")

    class Result:
        back_up_now_button = Element(
            "com.cyberlink.youcammakeup:id/enableBackupBtn", "id", "Back up now button")


class EffectsLocators:
    store_button = Element(
        "com.cyberlink.youcammakeup:id/downloadButton", "id", "Store button")
    collection = Element(
        "com.cyberlink.youcammakeup:id/smallEffectImage", "id", "Collection button")
    collection_back = Element(
        "com.cyberlink.youcammakeup:id/backCollection", "id", "Collection back button")
    effect_view = Element(
        "com.cyberlink.youcammakeup:id/effectRecyclerView", "id", "Effect view")
    effect_item = Element(
        "com.cyberlink.youcammakeup:id/effectItem", "id", "Effect item")
    intensity_seekbar = Element(
        "com.cyberlink.youcammakeup:id/unitSeekBar", "id", "Intensity seekbar")
    effect_download = Element(
        "com.cyberlink.youcammakeup:id/effectDownloadIcon", "id", "Effect download button")
    crown_effect_pack = Element(
        "com.cyberlink.youcammakeup:id/lookHotSaleIcon", "id", "crown button")
    pack_download_progress = Element(
        "com.cyberlink.youcammakeup:id/lookItemDownloadProgress", "id", "Pack download progress")
    effect_name = Element(
        "com.cyberlink.youcammakeup:id/effectThumbName", "id", "Effect Thumb Name")


class BackgroundLocators:
    background_item = Element(
        "com.cyberlink.youcammakeup:id/backgroundItem", "id", "Background item")
    background_view = Element(
        "com.cyberlink.youcammakeup:id/backgroundRecyclerView", "id", "Background view")
    background_reset = Element(
        "com.cyberlink.youcammakeup:id/backgroundReset", "id", "Background reset")
    background_brush = Element(
        "com.cyberlink.youcammakeup:id/backgroundBrush", "id", "Background brush")
    background_eraser = Element(
        "com.cyberlink.youcammakeup:id/backgroundEraser", "id", "Background eraser")
    draw_size1 = Element(
        "com.cyberlink.youcammakeup:id/drawSize1", "id", "Draw size 1")
    draw_size2 = Element(
        "com.cyberlink.youcammakeup:id/drawSize2", "id", "Draw size 2")
    draw_size3 = Element(
        "com.cyberlink.youcammakeup:id/drawSize3", "id", "Draw size 3")
    draw_size4 = Element(
        "com.cyberlink.youcammakeup:id/drawSize4", "id", "Draw size 4")
    draw_size5 = Element(
        "com.cyberlink.youcammakeup:id/drawSize5", "id", "Draw size 5")
    background_central = Element(
        "com.cyberlink.youcammakeup:id/compareLineView", "id", "")
    premium_icon = Element(
        "com.cyberlink.youcammakeup:id/premiumIcon", "id", "Premium Icon")
    photo_pick_icon = Element(
        "com.cyberlink.youcammakeup:id/photoPickIcon", "id", "Photo Pick Icon")
    no_thanks_button = Element(
        "com.cyberlink.youcammakeup:id/no_thanks_button", "id", "no thanks button")
    download_store = Element(
        "com.cyberlink.youcammakeup:id/downloadButton", "id", "background download store button")


class AccessoriesLocators:
    accessories_menu = Element(
        "com.cyberlink.youcammakeup:id/makeup_menu_item_title", "xpath", "Accessories menu")
    store_button = Element(
        "com.cyberlink.youcammakeup:id/downloadButton", "id", "Store button")
    pattern_view = Element(
        "com.cyberlink.youcammakeup:id/patternRecyclerView", "id", "Pattern view")
    pattern_item = Element(
        "com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "Pattern item")
    editroom_view = Element(
        "com.cyberlink.youcammakeup:id/compareLineView", "id", "Editroom view")


class DialogLocators:
    BIPA_Agree = Element(
        "com.cyberlink.youcammakeup:id/agree_btn", "id", "BIPA agree button")
    BIPA_Cancel = Element(
        "com.cyberlink.youcammakeup:id/cancel_btn", "id", "BIPA cancel button")
    AD_dialog = Element(
        "com.cyberlink.youcammakeup:id/dialog", "id", "AD notice dialog")
    AD_close = Element("com.cyberlink.youcammakeup:id/close",
                       "id", "AD close button")
    AD_tryit = Element("com.cyberlink.youcammakeup:id/tryIt",
                       "id", "AD try it button")
    Back = Element("com.cyberlink.youcammakeup:id/cameraBackIcon",
                   "id", "Back to Launcher page")
    promote = Element(
        "com.cyberlink.youcammakeup:id/promote_close_btn", "id", "Promote close button")

class SkincareLocators:
    Back = Element("com.cyberlink.youcammakeup: id / cameraBackButton", "id", "Back to Launcher page")
    Daily = Element(
        "com.cyberlink.youcammakeup:id/cameraDailyButton", "id", "Daily button")
    Facing_button = Element(
        "com.cyberlink.youcammakeup: id / cameraFacingButton", "id", "Facing button")
    Skin_diary_button = Element("com.cyberlink.youcammakeup:id/skinDiaryBtn", "id", "Skin Diary Button")
    Avatar = Element("com.cyberlink.youcammakeup:id/post_avatar", "id", "Avatar")
    Delete_button = Element("com.cyberlink.youcammakeup:id/skinCareDetailDeleteButton", "id", "Delete Button")
    Dialog_delete = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Dialog Delete Button")


class AgingLocators:
    Try_it = Element(
        "com.cyberlink.youcammakeup:id/tryItButton", "id", "Try it button")
    Choose_photo = Element(
        "com.cyberlink.youcammakeup:id/photoEntryButtonText", "id", "Choose photo")
    Take_photo = Element("com.cyberlink.youcammakeup:id/cameraEntryButtonText", "id", "Take photo")
    Live_camera = Element("com.cyberlink.youcammakeup:id/cameraEntryButtonText", "id", "Live Camera")
    Photo = Element("com.cyberlink.youcammakeup:id/modeImage1", "id", "Photo view button")
    Before_After = Element("com.cyberlink.youcammakeup:id/modeImage2", "id", "Before After view button")
    Grid = Element("com.cyberlink.youcammakeup:id/modeImage3", "id", "Grid view button")
    Video = Element("com.cyberlink.youcammakeup:id/modeImage4", "id", "Video view button")
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtn", "id", "Back button")
    Home = Element("com.cyberlink.youcammakeup:id/homeButton", "id", "Home button")
    Save = Element("com.cyberlink.youcammakeup:id/topToolBarDoneBtn", "id", "Save button")
    Start = Element("com.cyberlink.youcammakeup:id/photoEntryButtonBackground", "id", "Start button")
    Agree = Element("com.cyberlink.youcammakeup:id/agree_btn", "id", "Agree button")
    OK = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "OK button")
    Allow = Element("com.android.permissioncontroller:id/permission_allow_button", "id", "Allow button")
    waiting_cursor = Element(
        "com.cyberlink.youcammakeup:id/busy_indicator_switcher", "id", "waiting cursor")
    Time_Machine_Animation = Element("com.cyberlink.youcammakeup:id/backgroundVideo", "id", "Time Machine animation")
    Network_Error = Element("com.cyberlink.youcammakeup:id/alertDialog_text", "id", "No Network")
    Aging_Slider_Bar = Element("com.cyberlink.youcammakeup:id/agingSeekBar", "id", "Slider bar")
    AD_result_page = Element("com.cyberlink.youcammakeup:id/ad_media_container", "id", "result page AD")
    AD_save_page = Element("com.cyberlink.youcammakeup:id/previewAdContainer", "id", "save page AD")
    Result_image = Element("com.cyberlink.youcammakeup:id/resultImage", "id", "result image")
    Network_error_dialog = Element("com.cyberlink.youcammakeup:id/alertDialog_text", "id", "Network error dialog")
    Network_RETRY = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", "id", "RETRY button")
    Network_OK = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Network OK button")
    share_post = Element("com.cyberlink.youcammakeup:id/bc_dialog_share_post", "id", "Share post")
    post_button = Element("com.cyberlink.youcammakeup:id/top_bar_right_text_btn", "id", "Post button")
    Aging_saved_page = Element("com.cyberlink.youcammakeup:id/agingImageView", "id", "Aging saved page")


class ResultLocators:
    result_page_view = Element(
        "com.cyberlink.youcammakeup:id/sharePageScrollView", "id", "Result page view")
    Back = Element("com.cyberlink.youcammakeup:id/continueEditing", "id", "Result page back to editing page button")
    Album = Element("com.cyberlink.youcammakeup:id/sharePageLibraryBtn", "id", "Result page album list button")
    Home = Element("com.cyberlink.youcammakeup:id/homeButton", "id", "Result page home button")
    rating_page = Element("com.cyberlink.youcammakeup:id/starDisplayPanel", "id", "Rating page stars")
    Share_item = Element("com.cyberlink.youcammakeup:id/shareItemName", "id", "share item")
    Share_look = Element( "com.cyberlink.youcammakeup:id/sharePageCardBC", "id", "Share to YouCam Community")
    result_page_ad_banner = Element("com.cyberlink.youcammakeup:id/native_ad_media_container", "id",
                                    "result page AD banner")
    ycp_card_padding = Element("com.cyberlink.youcammakeup:id/sharePageYCPBottomPadding", "id", "YCP card padding")
    ycn_card_padding = Element("com.cyberlink.youcammakeup:id/sharePageYCNBottomPadding", "id", "YCN card padding")
    ycp_card_icon = Element("com.cyberlink.youcammakeup:id/sharePageYCPIcon", "id", "YCP card icon")
    ycn_card_icon = Element("com.cyberlink.youcammakeup:id/sharePageYCNIcon", "id", "YCN card icon")
    create_with_ycp = Element("com.cyberlink.youcammakeup:id/sharePageYCPEditBtn", "id", "YCP CREATE btn")
    create_with_ycn = Element("com.cyberlink.youcammakeup:id/sharePageYCNEditBtn", "id", "YCN CREATE btn")
    create_collage_btn = Element("com.cyberlink.youcammakeup:id/sharePageBeforeAfterBtn", "id", "Collage btn")
    ycp_permission_ok = Element("com.android.packageinstaller:id/permission_allow_button", "id", "YCP permission OK")
    ycp_bipa_agree = Element("com.cyberlink.youperfect:id/agree_btn", "id", "YCP BIPA agree")
    get_free_ycp = Element("com.cyberlink.youcammakeup:id/sharePageYCPFreeBtnText", "id", "YCP GetFree btn")
    open_with_panel = Element("android:id/resolver_list", "id", "Open_with_app panel")
    open_with_app = Element("android:id/text1", "xpath", "Select open_with by name")
    collage_save_btn = Element("com.cyberlink.youcammakeup:id/collageDoneBtn", "id", "Collage SAVE btn")
    collage_share_btn = Element("com.cyberlink.youcammakeup:id/collageRightButtonText", "id", "Collage SHARE btn")


class ShareLookLocators:
    share = Element("com.cyberlink.youcammakeup:id/descriptionText", "id", "SHARE button")
    share_dialog = Element("com.cyberlink.youcammakeup:id/bc_upload_dialog_message", "id", "Share dialog")
    share_look_to = Element("com.cyberlink.youcammakeup:id/shareItemRecyclerView", "id", "Also share look to")
    post_title = Element("com.cyberlink.youcammakeup:id/about", "id", "post title")
    share_item_icon = Element("com.cyberlink.youcammakeup:id/shareItemIcon", "id", "share app icon")


class ChurnUserRecoveryLocators:
    Close_button = Element(
        "com.cyberlink.youcammakeup:id/churn_recovery_dialog_cancel_button", "id", "close button")
    Continue_button = Element(
        "com.cyberlink.youcammakeup:id/churn_recovery_dialog_continue_button", "id", "continue button")


class TemplateStoreLocator:
    class Hair:
        female_new_download_wig = Element("//div[@class='ymk_ts-common-item-template__image']", "xpath", "")
        female_new_list = Element("//div[@class='ymk_ts-common-main-template-page-item-list__items']", "xpath", "")

    class Look:
        all = Element("(//android.view.View[@content-desc=\"All >\"])[2]/android.widget.TextView", "xpath", "all")

    class Effect:
        content_view = Element("android:id/content", "id", "effect content view")


class DeepLink:
    MakeupCam_page = "ymk://action_makeupcam"
    PhotoMakeup_page = "ymk://action/pickphoto/"

    class MakeupCam:
        eyeshadow = "ymk://action_makeupcam/eye_shadow"

    class Mouth:
        lipstick = "ymk://action/pickphoto/lipstick"
        lip_reshape = "ymk://action/pickphoto/lip_reshape"
        smile = "ymk://action/pickphoto/smile"
        lip_plumper = "ymk://action/pickphoto/lip_plumper"
        whiten_teeth = "ymk://action/pickphoto/whiten_teeth"
        lip_art = "ymk://action/pickphoto/lip_art"

    class Face:
        skin_smoother = "ymk://action/pickphoto/skin_smooth"
        face_reshaper = "ymk://action/pickphoto/face_reshaper"
        nose_enhancement = "ymk://action/pickphoto/nose_enhancement"
        wrinkle = "ymk://action/pickphoto/face_wrinkle"
        redness = "ymk://action/pickphoto/redness"
        uneven_skintone = "ymk://action/pickphoto/uneven_skintone"
        pores = "ymk://action/pickphoto/pores"
        foundation = "ymk://action_pickphoto/skin_toner"
        concealer = "ymk://action/pickphoto/concealer"
        blush = "ymk://action_pickphoto/blush"
        contour = "ymk://action_pickphoto/face_contour_pattern"
        highlight = "ymk://action_pickphoto/face_contour_pattern?subType=highlight"
        facepaint = "ymk://action_pickphoto/face_art"
        blemish = "ymk://action_pickphoto/blemish_removal"
        shinremoval = "ymk://action/pickphoto/anti_shine"

    class Eye:
        eyeliner = "ymk://action/pickphoto/eye_line"
        eyelashes = "ymk://action/pickphoto/eye_lash"
        eyeshadow = "ymk://action/pickphoto/eye_shadow"
        darkcircle = "ymk://action/pickphoto/dark_circle"
        eyecontact = "ymk://action/pickphoto/eye_contact"
        eyebag = "ymk://action/pickphoto/eye_bag"
        eyebrighten = "ymk://action/pickphoto/eye_sparkle"
        eyelid = "ymk://action/pickphoto/eye_lid"
        redeye = "ymk://action/pickphoto/red_eye"
        eyebrow_reshape = "ymk://action/pickphoto/eyebrow_reshape"
        eyetuner = "ymk://action/pickphoto/eye_enlarge"
        eyebrows = "ymk://action/pickphoto/eye_brow"

    class Hair:
        hairdye = "ymk://action/pickphoto/hair_dye"
        wig = "ymk://action/pickphoto/wig"

    body_tuner = "ymk://action_pickphoto/body_tuner"
    object_removal = "ymk://action_pickphoto/object_removal"
    animation = "ymk://action_pickphoto/animation"
    effect = "ymk://action/tryEffect?editMode=Edit"
    background = "ymk://action/tryBackground?editMode=Edit"
    eyewear = "ymk://action/pickphoto/eye_wear"
    headband = "ymk://action/pickphoto/hair_band"
    necklace = "ymk://action/pickphoto/necklace"
    earrings = "ymk://action/pickphoto/earrings"
    hat = "ymk://action/pickphoto/hat"
    Launcher_page = "ymk://launcher"
    Aging_page = "ymk://action/ai_aging"
    me_page = "ymkbc://profile"
    setting_page = "ymk://action/about"


class SettingLocators:
    back_button = Element("com.cyberlink.youcammakeup:id/btn_setting_back", "id", "back button")
    user_id = Element("com.cyberlink.youcammakeup:id/userId", "id", "User ID")
    about_me = Element("com.cyberlink.youcammakeup:id/aboutMe", "id", "About Me")
    beauty_profile = Element("com.cyberlink.youcammakeup:id/beautyProfile", "id", "Beauty Profile")
    email_subscription = Element("com.cyberlink.youcammakeup:id/emailSubscriptions", "id", "Email Subscriptions")
    change_password = Element("com.cyberlink.youcammakeup:id/changePassword", "id", "Change Password")
    delete_account = Element("com.cyberlink.youcammakeup:id/deleteAccount", "id", "Delete Account")
    auto_save = "com.cyberlink.youcammakeup:id/autoSaveBtn"
    front_camera_mirror = "com.cyberlink.youcammakeup:id/autoFlipPhotoBtn"
    skin_beautifier = "com.cyberlink.youcammakeup:id/skinBeautyBtn"
    countdown_sound = "com.cyberlink.youcammakeup:id/countdownSoundBtn"
    face_metering = "com.cyberlink.youcammakeup:id/faceMeteringBtn"
    gps = "com.cyberlink.youcammakeup:id/accessGpsBtn"
    gps_item = Element("com.cyberlink.youcammakeup:id/accessGpsBtn", "id", "GPS item")
    photo_watermark = Element("com.cyberlink.youcammakeup:id/watermarkBtn", "id", "photo watermark")
    video_watermark = Element("com.cyberlink.youcammakeup:id/videoWatermarkBtn", "id", "video watermark")
    view = Element("android:id/content", "id", "setting view")
    switcher_item = "com.cyberlink.youcammakeup:id/item_switch"
    item = Element("com.cyberlink.youcammakeup:id/bc_goto_left_text", "xpath", "Select item")
    apply = Element("com.cyberlink.youcammakeup:id/top_bar_right_icon", "id", "apply button")
    about_me_text = Element("com.cyberlink.youcammakeup:id/edit_about_text", "id", "about me field")
    about_me_website = Element("com.cyberlink.youcammakeup:id/edit_website_text", "id", "website field")
    quality = Element("com.cyberlink.youcammakeup:id/photoQualityRowBtn", "id", "Quality")
    back_quality = Element("com.cyberlink.youcammakeup:id/aboutBackBtn", "id", "back button")
    faq = Element("com.cyberlink.youcammakeup:id/sendFeedbackBtn", "id", "FAQ")
    feedback_text = Element("com.cyberlink.youcammakeup:id/edit_feedback_text", "id", "Feedback field")
    submit = Element("com.cyberlink.youcammakeup:id/btn_agree_continue", "id", "Agree and Submit")
    feedback_dialog = Element("com.cyberlink.youcammakeup:id/alertDialog_title", "id",
                              "Thank you for the feedback dialog")
    about = Element("com.cyberlink.youcammakeup:id/aboutBtn", "id", "About")
    events = Element("com.cyberlink.youcammakeup:id/eventsAndVersionBtn", "id", "Events & Version Updates")
    country = Element("com.cyberlink.youcammakeup:id/countryBtn", "id", "Country")
    tutorial = Element("com.cyberlink.youcammakeup:id/tutorialBtn", "id", "Tutorials")
    search_bar = Element("com.cyberlink.youcammakeup:id/country_picker_search_bar", "id", "search bar")
    country_name = Element("com.cyberlink.youcammakeup:id/country_name", "id", "country name")
    dialog_ok = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "OK")
    rate_us = Element("com.cyberlink.youcammakeup:id/rateUsBtn", "id", "Rate us")
    follow_us = Element("com.cyberlink.youcammakeup:id/followUsBtn", "id", "Follow Us")
    current_country_name = Element("com.cyberlink.youcammakeup:id/current_country_name", "id", "Current country name")
    premium_banner = Element("com.cyberlink.youcammakeup:id/bannerArea", "id", "Premium banner")
    save_path = Element("com.cyberlink.youcammakeup:id/photoSavePathBtn", "id", "Save Path")
    Account_login = Element("com.cyberlink.youcammakeup:id/accountLoginBtn", "id", "Account login")
    Logout_button = Element("com.cyberlink.youcammakeup:id/bc_log_out_btn", "id", "Log out")
    Dialog_logout_button = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", "id",
                                   "Select dialog Log out button")
    Backup_to_cloud = Element("com.cyberlink.youcammakeup:id/CloudAlbumBtn", "id", "Backup status")
    Log_in_here = Element("com.cyberlink.youcammakeup:id/bc_have_an_account", "id", "Login BC account entry")
    Login_view = Element("com.cyberlink.youcammakeup:id/register_info_panel", "id", "Login Panel")
    account = Element("com.cyberlink.youcammakeup:id/register_id", "id", "Account")
    password = Element("com.cyberlink.youcammakeup:id/register_password", "id", "Password")
    Login_button = Element("com.cyberlink.youcammakeup:id/register_accept_btn", "id", "Password")
    email = Element("com.cyberlink.youcammakeup:id/email_text", "id", "email text")

class MeLocators:
    setting_button = Element("com.cyberlink.youcammakeup:id/bc_top_bar_left_btn", "id", "setting button")
    Home_button = Element("com.cyberlink.youcammakeup:id/bottom_bar_tab_add", "id", "Home button")
    Enable_backup_button = Element("com.cyberlink.youcammakeup:id/enableBackupBtn", "id", "Enable backup button")
    Backup_view = Element("com.cyberlink.youcammakeup:id/imageViewPhoto", "id", "Cloud Album view")
    Video_play_icon = Element("com.cyberlink.youcammakeup:id/video_play_icon", "id", "Backup video file")
    View = Element("com.cyberlink.youcammakeup:id/mePageContainer", "id", "Me page view")
    Register_Now_button = Element("com.cyberlink.youcammakeup:id/register_now_btn", "id", "Register Now Button")
    Post_view = Element("com.cyberlink.youcammakeup:id/post_cover", "id", "Post View")


class MakeupCamLocators:
    # 介面按鈕
    Back = Element(
        "com.cyberlink.youcammakeup:id/cameraBackIcon", "id", "Back Button")
    Detail = Element(
        "com.cyberlink.youcammakeup:id/camera_detail_button", "id", "Detail Button")
    Compare = Element(
        "com.cyberlink.youcammakeup:id/compareButton", "id", "Compare Button")
    Reset = Element(
        "com.cyberlink.youcammakeup:id/cameraResetEffectIcon", "id", "Reset Button")
    Remove = Element(
        "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Remove Button")
    Switch_Camera = Element(
        "com.cyberlink.youcammakeup:id/cameraFacingButton", "id", "Switch Camera Button")
    Timer_Mode = Element(
        "com.cyberlink.youcammakeup:id/cameraTimerModeButton", "id", "Timer Mode Button")
    Photo_Mode = Element(
        "com.cyberlink.youcammakeup:id/cameraShotButton", "id", "Photo Mode Button")
    Video_Mode = Element(
        "com.cyberlink.youcammakeup:id/videoRecBtn", "id", "Video Mode Button")
    Camera_Shot = Element(
        "com.cyberlink.youcammakeup:id/cameraShotButton", "id", "Camera Shot button")
    Video_Rec = Element(
        "com.cyberlink.youcammakeup:id/videoRecBtn", "id", "Video Rec button")
    Switch_Mode = Element(
        "com.cyberlink.youcammakeup:id/videoRecModeBtn", "id", "Switch Video/Photo Mode")
    Stop_Record = Element(
        "com.cyberlink.youcammakeup:id/videoPauseCircle", "id", "Stop Record Button")
    SeekBar_V = Element(
        "com.cyberlink.youcammakeup:id/unitSeekBar", "id", "SeekBar")
    SeekBar_V_1 = Element(
        "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[1]", "xpath", "seekbar(1)")
    SeekBar_V_2 = Element(
        "(//*[@resource-id='com.cyberlink.youcammakeup:id/unitSeekBar'])[2]", "xpath", "seekbar(2)")
    SeekBar_H = Element(
        "com.cyberlink.youcammakeup:id/seekBarContainer", "id", "SeekBar")
    Compare_Line = Element(
        "com.cyberlink.youcammakeup:id/compareView", "id", "Compare_Line")
    Photo_Picker = Element(
        "com.cyberlink.youcammakeup:id/cameraPhotoPickerButton", "id", "Photo Picker")
    Makeup_Menu_id = Element(
        "com.cyberlink.youcammakeup:id/category", "id", "Makeup Menu")
    Makeup_Menu_xpath = Element(
        "com.cyberlink.youcammakeup:id/category", "xpath", "Makeup Menu")
    brand_menu = Element(
        "com.cyberlink.youcammakeup:id/toolViewImage", "id", "Open brand menu")
    brand_menu_view = Element(
        "com.cyberlink.youcammakeup:id/skuVendorMenu", "id", "Brand list")
    brand = Element(
        "com.cyberlink.youcammakeup:id/skuItemVendorName", "xpath", "Select brand by name")
    color_grid_view = Element(
        "com.cyberlink.youcammakeup:id/liveColorGridView", "id", "Color grid view")
    color_content = Element(
        "com.cyberlink.youcammakeup:id/item_color_content", "id", "Select content color ball")
    palette = Element(
        "com.cyberlink.youcammakeup:id/colorChooser1", "id", "")
    Rating_Page = Element(
        "com.cyberlink.youcammakeup:id/starDisplayPanel", "id", "Rating page stars")
    premium_categorya = Element(
        "com.cyberlink.youcammakeup:id/premiumIcon", "id", "premium_categorya")

    class PhotoPreview:
        Photo_Retake = Element(
            "com.cyberlink.youcammakeup:id/videoRetakeButton", "id", "Photo Retake Button")
        Photo_Frame = Element(
            "com.cyberlink.youcammakeup:id/frameButton", "id", "Photo Frame Button")
        Photo_Edit = Element(
            "com.cyberlink.youcammakeup:id/makeupButton", "id", "Photo Edit Button")
        Photo_Save = Element(
            "com.cyberlink.youcammakeup:id/saveButton", "id", "Photo Save Button")
        Photo_Share = Element(
            "com.cyberlink.youcammakeup:id/shareButton", "id", "Photo Share Button")
        Rating_Page = Element(
            "com.cyberlink.youcammakeup:id/starDisplayPanel", "id", "Rating page stars")

    class VideoPreview:
        Video_Play = Element(
            "com.cyberlink.youcammakeup:id/videoPlayButton", "id", "Video Play Button")
        Video_Retake = Element(
            "com.cyberlink.youcammakeup:id/videoRetakeButton", "id", "Video Retake Button")
        Video_Edit = Element(
            "com.cyberlink.youcammakeup:id/videoEditButton", "id", "Video Edit Button")
        Video_Save = Element(
            "com.cyberlink.youcammakeup:id/videoSaveButton", "id", "Video Save Button")
        Volume_Switcher = Element(
            "com.cyberlink.youcammakeup:id/volumeSwitcher", "id", "Volume Switcher Button")
        Remove_Watermark = Element(
            "com.cyberlink.youcammakeup:id/removeWatermarkBtn", "id", "Remove Watermark")
        IAP = Element(
            "com.cyberlink.youcammakeup:id/dialogExContainer", "id", "Video IAP")

    class Looks:
        tab_text = Element(
            "com.cyberlink.youcammakeup:id/tabText", "xpath", "Select tab by name")
        look_category_view = Element(
            "com.cyberlink.youcammakeup:id/lookCategoryRecyclerView", "id", "look_category_view")
        look_item_name = Element(
            "com.cyberlink.youcammakeup:id/effectThumbName", "xpath", "Select xxx look")
        look_item_view = Element(
            "com.cyberlink.youcammakeup:id/cameraLookGridArea", "id", "Look item view")
        look_item = Element(
            "com.cyberlink.youcammakeup:id/effectItem", "id", "look_item")
        premium_category = Element(
            "com.cyberlink.youcammakeup:id/premiumIcon", "id", "premium_category")
        premium_pack = Element(
            "com.cyberlink.youcammakeup:id/effectGridPhoto", "id", "premium_pack")
        premium_look = Element(
            "com.cyberlink.youcammakeup:id/shopButton", "id", "premium_look")
        switch_button = Element(
            "com.cyberlink.youcammakeup:id/switchBtn", "id", "switch_button")
        download_icon = Element(
            "com.cyberlink.youcammakeup:id/effectDownloadIcon", "id", "download_icon")
        info_button = Element(
            "com.cyberlink.youcammakeup:id/infoButton", "id", "info_button")
        look_details = Element(
            "com.cyberlink.youcammakeup:id/look_details", "id", "look_details")
        favorite_category = Element(
            "com.cyberlink.youcammakeup:id/favoriteCategory", "id", "favorite_category")
        favorite_icon = Element(
            "com.cyberlink.youcammakeup:id/favoriteIcon", "id", "favorite_icon")
        add_favorite = Element(
            "com.cyberlink.youcammakeup:id/circleView", "id", "Add favorite")

    class Hair:
        color_tab = Element(
            "com.cyberlink.youcammakeup:id/tabText", "xpath", "Hair Style tab menu")
        color_ball = Element(
            "com.cyberlink.youcammakeup:id/colorItemColorTexture", "id", "2 Colors color ball")
        color_ball_view = Element(
            "com.cyberlink.youcammakeup:id/colorRecyclerView", "id", "2 Colors color ball view")
        brand_menu = Element(
            "com.cyberlink.youcammakeup:id/toolView", "id", "Open brand menu")

    class Makeup:
        feature_list = Element(
            "com.cyberlink.youcammakeup:id/liveMakeupName", "xpath", "feature_list")
        color_content = Element(
            "com.cyberlink.youcammakeup:id/item_color_content", "id", "Select content color ball")
        color_grid_view = Element(
            "com.cyberlink.youcammakeup:id/colorGridView", "id", "Color grid view")
        makeup_menu = Element(
            "com.cyberlink.youcammakeup:id/live_makeup_menu_recycler_view", "id", "makeup menu")
        color_tab = Element(
            "com.cyberlink.youcammakeup:id/tabText", "xpath", "tab menu")
        crown_icon = Element(
            "com.cyberlink.youcammakeup:id/hotIcon", "id", "crown_icon")
        premium_lip = Element(
            "com.cyberlink.youcammakeup:id/shopView", "id", "premium_lip")
        close_button = Element(
            "com.cyberlink.youcammakeup:id/live_cam_close_button_icon_image", "id", "close_button")
        smashbox_entry = Element(
            "com.cyberlink.youcammakeup:id/smashBoxAIEntry", "id", "Smashbox AI entry button")
        template_button = Element(
            "com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "template_button")
        none_button = Element(
            "com.cyberlink.youcammakeup:id/btn_livecam_none", "id", "none_button")
        shimmer_switcher = Element(
            "com.cyberlink.youcammakeup:id/eyeShadowShimmerSwitcherBtn", "id", "shimmer_switcher")
        lip_art_pattern = Element(
            "com.cyberlink.youcammakeup:id/paletteImage", "id", "lip_art_pattern")
        pattern_text = Element(
            "com.cyberlink.youcammakeup:id/camera_lipstick_pattern_text", "xpath", "Select pattern by name")
        pattern_grid_view = Element(
            "com.cyberlink.youcammakeup:id/patternGridView", "id", "Pattern grid view")


    class Effects:
        premium_pack = Element(
            "com.cyberlink.youcammakeup:id/lookHotSaleIcon", "id", "premium_pack")
        effect_grid_area = Element(
            "com.cyberlink.youcammakeup:id/cameraLookGridArea", "id", "effect_grid_area")
        effect = Element(
            "com.cyberlink.youcammakeup:id/smallEffectImage", "id", "effect")
        premium_effect = Element(
            "com.cyberlink.youcammakeup:id/shopButton", "id", "premium_effect")

    class Reshape:
        feature_list = Element(
            "com.cyberlink.youcammakeup:id/retouchName", "xpath", "feature_list")
        retouch_menu = Element(
            "com.cyberlink.youcammakeup:id/retouchMenu", "id", "retouch menu")


class SmashboxLocators:
    Back = Element("com.cyberlink.youcammakeup:id/cameraBackButton", "id", "Back to Launcher page")
    switch_to_rear_cam = Element("com.cyberlink.youcammakeup:id/cameraFacingButton", "id", "Back to Launcher page")
    result_page = Element("com.cyberlink.youcammakeup:id/bc_pull_to_refresh_layout", "id", "Analysis Report page")
    capture_button = Element("com.cyberlink.youcammakeup:id/cameraShotButton", "id", "capture button")
    save_photo_button = Element("com.cyberlink.youcammakeup:id/savePhotoButton", "id", "Save Photo")
    preview_image = Element("com.cyberlink.youcammakeup:id/previewImage", "id", "Preview image")
    share_post = Element("com.cyberlink.youcammakeup:id/bc_dialog_share_post", "id", "Share post")
    post_button = Element("com.cyberlink.youcammakeup:id/top_bar_right_text_btn", "id", "Post button")


class BCLocators:
    bc_ad = Element("com.cyberlink.youcammakeup:id/google_ad_cover_image", "id", "setting button")
    bc_ad_panel = Element("com.cyberlink.youcammakeup:id/ad_info_panel", "id", "ad panel")
    navigator_bar = Element("com.cyberlink.youcammakeup:id/fragment_bottombar_panel", "id", "navigator bar")
    post_button = Element("com.cyberlink.youcammakeup:id/top_bar_right_panel", "id", "Post button")
    post_title = Element("com.cyberlink.youcammakeup:id/write_post_title", "id", "Post title textbox")
    Log_in_here = Element("com.cyberlink.youcammakeup:id/bc_have_an_account", "id", "Login BC account entry")
    Login_view = Element("com.cyberlink.youcammakeup:id/register_info_panel", "id", "Login Panel")
    account = Element("com.cyberlink.youcammakeup:id/register_id", "id", "Account")
    password = Element("com.cyberlink.youcammakeup:id/register_password", "id", "Password")
    Login_button = Element("com.cyberlink.youcammakeup:id/register_accept_btn", "id", "Password")
    rating_dialog = Element("com.cyberlink.youcammakeup:id/starDisplayPanel", "id", "Rating dialog")


class CloudAlbumViewLocators:
    Back_button = Element("com.cyberlink.youcammakeup:id/top_bar_btn_back", "id", "Back to me page")
    Edit_button = Element("com.cyberlink.youcammakeup:id/cloud_album_detail_edit", "id", "Edit button")
    Delete_button = Element("com.cyberlink.youcammakeup:id/cloud_album_detail_delete", "id", "Delete button")
    Download_button = Element("com.cyberlink.youcammakeup:id/cloud_album_detail_save", "id", "Download button")
    Try_it_button = Element("com.cyberlink.youcammakeup:id/cloud_album_try_it_button", "id", "Try it button")
    Live_makeup_button = Element("com.cyberlink.youcammakeup:id/itemTakePhoto", "id", "Try look on live Makeup")
    Photo_makeup_button = Element("com.cyberlink.youcammakeup:id/itemPhotoLibrary", "id", "Try look on Photo Makeup")
    Download_completed = Element("com.cyberlink.youcammakeup:id/download_icon_img", "id", "Download completed")
    Download_status = Element("com.cyberlink.youcammakeup:id/state_text", "id", "Download status")
    Dialog_delete_button = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id",
                                   "Select delete button on dialog")
    Download_video_icon = Element("com.cyberlink.youcammakeup:id/video_download_icon", "id", "Download video icon")




