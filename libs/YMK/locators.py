# 各項element ID
from libs.element import Element


class OpeningTutorialPageLocators:
    GetStarted_button = Element("com.cyberlink.youcammakeup:id/getStartBtn", "id", "xxx buton")
    Skip_button = "com.cyberlink.youcammakeup:id/tutorialSkipBtn"
    Skip_confirm_button = "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive"
    Background_id = "com.cyberlink.youcammakeup:id/opening_tutorial_background"


class LauncherLocators:
    Makeup_cam = Element("com.cyberlink.youcammakeup:id/cameraImage", "id", "MakeupCam button")
    Photo_makeup = Element("com.cyberlink.youcammakeup:id/photoMakeupImage", "id", "PhotoMakeup button")
    Store_button = "com.cyberlink.youcammakeup:id/shop_button"
    Aging_tile = "com.cyberlink.youcammakeup:id/launcherAgingTile"
    Skincare_tile = "com.cyberlink.youcammakeup:id/launcherSkinCareTile"
    YCV_tile = "com.cyberlink.youcammakeup:id/launcherPromoteTile1"
    YCP_tile = "com.cyberlink.youcammakeup:id/launcher_ycp_tile"
    Crown_LayoutA = "com.cyberlink.youcammakeup:id/launcherSubscriptionEntryButton"
    Crown_LayoutB = "com.cyberlink.youcammakeup:id/premium_button"
    AD_banner_LayoutB = "com.cyberlink.youcammakeup:id/CenterAdContainer"
    Me_button = "com.cyberlink.youcammakeup:id/bc_me_icon"


class PickPhotoLocators:
    album_view = Element("com.cyberlink.youcammakeup:id/AlbumView", "id", "Album view")
    select_folder = Element("com.cyberlink.youcammakeup:id/albumDisplayName", "xpath", "Select folder")
    photo_view = Element("com.cyberlink.youcammakeup:id/PhotoView", "id", "Photo view")
    select_photo = Element("com.cyberlink.youcammakeup:id/photoItemImage", "id", "Select photo")
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", "id", "Photo picker back button")


class PhotoMakeupLocators:
    # 介面按鈕
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", "id", "Back to photo picker")
    CANCEL = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", "id", "Back dialog: CANCEL leave edit page")
    LEAVE = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Back dialog: Leave photo edit page")
    Switch_Face = Element("com.cyberlink.youcammakeup:id/TopBarSwitchFaceBtn", "id", "Switch face button")
    Undo = Element("com.cyberlink.youcammakeup:id/EditViewUndoBtn", "id", "Undo edit button")
    Redo = Element("com.cyberlink.youcammakeup:id/EditViewRedoBtn", "id", "Redo edit button")
    Save = Element("com.cyberlink.youcammakeup:id/topToolBarExportBtn", "id", "Save Photo")
    Manual = Element("com.cyberlink.youcammakeup:id/EditViewManualBtn", "id", "Fine Tune button")
    Detail = Element("com.cyberlink.youcammakeup:id/EditViewDetailBtn", "id", "Detail button")
    Compare = Element("com.cyberlink.youcammakeup:id/EditViewCompareBtn", "id", "Compare button")
    wait_animation = Element("com.cyberlink.youcammakeup:id/lookNameTextView", "id", "Wait animation")
    waiting_cursor = Element("com.cyberlink.youcammakeup:id/busy_indicator_switcher", "id", "waiting cursor")
    # 共享欄位按鈕清單
    brand_menu = Element("//*[@resource-id='com.cyberlink.youcammakeup:id/toolView']", "xpath", "Open brand menu")
    brand = Element("com.cyberlink.youcammakeup:id/skuItemVendorName", "xpath", "Select brand by name")
    pattern_grid_view = Element("com.cyberlink.youcammakeup:id/patternGridView", "id", "Pattern view")
    pattern_recycle_view = Element("com.cyberlink.youcammakeup:id/patternRecyclerView", "id", "")
    pattern_list = Element("com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "")
    pattern_text = Element("com.cyberlink.youcammakeup:id/camera_lipstick_pattern_text", "xpath", "Select pattern by name")
    tab_recycle_view = Element("com.cyberlink.youcammakeup:id/tabRecyclerView", "id", "Tab view")
    tab_room_pattern = Element("com.cyberlink.youcammakeup:id/room_tab_pattern", "xpath", "Select tab room by name")
    tab_text = Element("com.cyberlink.youcammakeup:id/tabText", "xpath", "Select tab by name")
    color_grid_view = Element("com.cyberlink.youcammakeup:id/colorGridView", "id", "Color grid view")
    color_content = Element("com.cyberlink.youcammakeup:id/item_color_content", "id", "Select content color ball")
    slider_bar = Element("com.cyberlink.youcammakeup:id/unitSeekBar", "id", "Slider bar")
    makeup_menu = Element("com.cyberlink.youcammakeup:id/makeupMenu", "id", "")
    category = Element("com.cyberlink.youcammakeup:id/makeup_menu_item_title", "id", "Select category by name")
    feature_list = Element("com.cyberlink.youcammakeup:id/makeup_menu_expandable_title", "xpath", "All feature list view")
    reshape_item = Element("com.cyberlink.youcammakeup:id/itemName", "xpath", "Reshape functions list")
    panel_view = Element("com.cyberlink.youcammakeup:id/panel_bottom_area", "id", "")
    menu_back = Element("com.cyberlink.youcammakeup:id/makeup_menu_expandable_back_btn", "id", "Menu back button")

    class FineTune:
        Face = Element("com.cyberlink.youcammakeup:id/fineTuneFaceButton", "id", "Face button")
        Left_eye = Element("com.cyberlink.youcammakeup:id/fineTuneLeftEyeButton", "id", "Left_eye button")
        Right_eye = Element("com.cyberlink.youcammakeup:id/fineTuneRightEyeButton", "id", "Right_eye button")
        Lips = Element("com.cyberlink.youcammakeup:id/fineTuneLipsButton", "id", "Lips button")
        Mouth_Open = Element("com.cyberlink.youcammakeup:id/EditViewMouthSwitchBtn", "id", "Mouth Open button")
        Close = Element("com.cyberlink.youcammakeup:id/fineTuneCloseBtn", "id", "Close button")
        Apply = Element("com.cyberlink.youcammakeup:id/fineTuneApplyBtn", "id", "Apply button")

    class SwitchFace:
        Cancel = ("com.cyberlink.youcammakeup: id / faceSwitcherActionBarCancelButton", "id", "Cancel button")
        Add_Face = ("com.cyberlink.youcammakeup:id/faceSwitcherActionBarAddFaceButton", "id", "Add face button")
        Apply = Element("com.cyberlink.youcammakeup:id/faceSwitcherActionBarApplyButton", "id", "Apply button")

    class Looks:
        look_item_download_icon = Element("com.cyberlink.youcammakeup:id/lookItemDownloadIcon", "id", "Look item download icon")
        look_item_download_progress = Element("com.cyberlink.youcammakeup:id/lookItemDownloadProgress", "id", "Look item download progress")
        look_item_name = Element("com.cyberlink.youcammakeup:id/lookItemName", "xpath", "Select xxx look")
        CANCEL = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", "id", "Cancel download")
        CONTINUE = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", "id", "Continue download")
        store = Element("com.cyberlink.youcammakeup:id/lookMoreBtnContainer", "id", "template store button")
        heart = Element("com.cyberlink.youcammakeup:id/favoriteIcon", "id", "Heart favorite icon")
        crown = Element("com.cyberlink.youcammakeup:id/premiumIcon", "id", "Crown premium icon")
        add_favorite = Element("com.cyberlink.youcammakeup:id/circleView", "id", "")
        favorite_icon = Element("com.cyberlink.youcammakeup:id/lookFavoriteIcon", "id", "")

    class Mouth:
        download_store = Element("com.cyberlink.youcammakeup:id/downloadButton", "id", "Mouth download store button")

    class Face:
        Left = Element("com.cyberlink.youcammakeup:id/leftButton", "id", "Face Reshape left button")
        Overall = Element("com.cyberlink.youcammakeup:id/overallButton", "id", "Face Reshape overall button")
        Right = Element("com.cyberlink.youcammakeup:id/rightButton", "id", "Face Reshape right button")
        process_dialog = Element("com.cyberlink.youcammakeup:id/customToast", "id", "Processing dialog")
        download_store = Element("com.cyberlink.youcammakeup:id/downloadButton", "id", "Hair download store button")
        switch_button = Element("com.cyberlink.youcammakeup:id/switchBtn", "id", "Switch ON and OFF")

    class Eye:
        Left = Element("com.cyberlink.youcammakeup:id/leftButton", "id", "Face Reshape left button")
        Overall = Element("com.cyberlink.youcammakeup:id/overallButton", "id", "Face Reshape overall button")
        Right = Element("com.cyberlink.youcammakeup:id/rightButton", "id", "Face Reshape right button")
        switch_button = Element("com.cyberlink.youcammakeup:id/switchBtn", "id", "Switch ON and OFF")
        tab_pattern = Element("com.cyberlink.youcammakeup:id/room_tab_pattern", "id", "Click pattern tab")
        tab_color = Element("com.cyberlink.youcammakeup:id/room_tab_color", "id", "Click color tab")
        tab_eyelashes = Element("com.cyberlink.youcammakeup:id/room_tab_eyelashes", "id", "Click eyelashes tab")
        tab_mascara = Element("com.cyberlink.youcammakeup:id/room_tab_mascara", "id", "Click mascara tab")
        eyelid_pattern = Element("com.cyberlink.youcammakeup:id/theGridView", "xpath", "Select eyelid patterns")

    class Hair:
        tab_style = Element("com.cyberlink.youcammakeup:id/room_tab_pattern", "id", "Click style tab")
        tab_color = Element("com.cyberlink.youcammakeup:id/room_tab_color", "id", "Click color tab")
        download_store = Element("com.cyberlink.youcammakeup:id/downloadButton", "id", "Hair download store button")


class BodyTunerLocators:
    enhancer_slim_ok = Element("com.cyberlink.youcammakeup:id/button", "id", "Enhancer OK button")
    toolbar_view = Element("com.cyberlink.youcammakeup:id/toolBar", "id", "")
    toolbar = Element("com.cyberlink.youcammakeup:id/textView", "xpath", "Select body tuner items")
    effect_seekbar = Element("com.cyberlink.youcammakeup:id/EffectSeekBar", "id", "Effect seek bar")
    X_button = Element("com.cyberlink.youcammakeup:id/toolBarCloseBtn", "id", "X button")
    V_button = Element("com.cyberlink.youcammakeup:id/toolBarApplyBtn", "id", "V button")
    undo = Element("com.cyberlink.youcammakeup:id/UndoBtn", "id", "Undo button")
    redo = Element("com.cyberlink.youcammakeup:id/RedoBtn", "id", "Redo button")
    clear = Element("com.cyberlink.youcammakeup:id/ClearBtn", "id", "")
    smart_brush = Element("com.cyberlink.youcammakeup:id/smartBrushSwitchBtn", "id", "")
    brush = Element("com.cyberlink.youcammakeup:id/brushBtn", "id", "")
    eraser = Element("com.cyberlink.youcammakeup:id/eraserBtn", "id", "")
    detect = Element("com.cyberlink.youcammakeup:id/detectBtn", "id", "")
    waiting_cursor = Element("com.cyberlink.youcammakeup:id/busy_indicator_switcher", "id", "waiting cursor")


class AnimationLocators:
    Animation_button = Element("00000000-0000-0e93-ffff-ffff000005ad", "id", "Animation button")
    EFFECTS = Element("com.cyberlink.youcammakeup:id/animationEffectTab", "id", " Animation EFFECTS button")
    STICKERS = Element("com.cyberlink.youcammakeup:id/animationEffectTabUnderline", "id", "Animation STICKERS button")
    X_button = Element("com.cyberlink.youcammakeup:id/toolBarCloseBtn", "id", "Animation X button")
    V_button = Element("com.cyberlink.youcammakeup:id/toolBarApplyBtn", "id", "Animation V button")
    take_photo = Element("com.cyberlink.youcammakeup:id/animationTakePhotoView", "id", "Take photo button")
    null_button = Element("com.cyberlink.youcammakeup:id/no_effect_btn","id", "Effect category null button")
    effect_view = Element("com.cyberlink.youcammakeup:id/effectSelectRecycleView", "id", "Effect category view")
    sticker_view = Element("com.cyberlink.youcammakeup:id/stickerSelectRecycleView", "id", "Sticker category view")
    stickers = Element("com.cyberlink.youcammakeup:id/sticker_icon", "id", "")
    category_text_view = Element("com.cyberlink.youcammakeup:id/effectCategoryRecycleView", "id", "Category text view")
    category_text = Element("com.cyberlink.youcammakeup:id/txtCategory", "xpath", "Category text")
    seekbar = Element("com.cyberlink.youcammakeup:id/EffectSeekBar", "id", "Effect seekbar")
    play_cursor = Element("com.cyberlink.youcammakeup:id/playCursor", "id", "Pause / Resume button")
    eraser_extend_button = Element("com.cyberlink.youcammakeup:id/BottomEraserBtn", "id", "Animation Eraser button")
    detect_button = Element("com.cyberlink.youcammakeup:id/FaceDetectBtn", "id", "Detect button")
    draw_button = Element("com.cyberlink.youcammakeup:id/BrushBtn", "id", "Draw button")
    erase_button = Element("com.cyberlink.youcammakeup:id/EraserBtn", "id", "Erase button")
    brush_view = Element("com.cyberlink.youcammakeup:id/BrushStyleGridView", "id", "Stroke size")
    undo_button = Element("com.cyberlink.youcammakeup:id/UndoBtn", "id", "Eraser Undo button")
    reset_button = Element("com.cyberlink.youcammakeup:id/ClearBtn", "id", "Eraser Reset button")

    class Export:
        back_button = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtn", "id", "Back button")
        video_button = Element("com.cyberlink.youcammakeup:id/videoTypeBtn", "id", "Video button")
        GIF_button = Element("com.cyberlink.youcammakeup:id/gifTypeBtn", "id", "GIF button")
        Instagram_button = Element("com.cyberlink.youcammakeup:id/instagramTypeBtn", "id", "Instagram button")
        Facebook_button = Element("com.cyberlink.youcammakeup:id/facebookTypeBtn", "id", "Facebook button")
        crop_original = Element("com.cyberlink.youcammakeup:id/cropOriginal", "id", "Crop original")
        crop_16to9 = Element("com.cyberlink.youcammakeup:id/crop16to9", "id", "Crop 16 to 9")
        crop_1to1 = Element("com.cyberlink.youcammakeup:id/crop1to1", "id", "Crop 1 to 1")
        crop_3to4 = Element("com.cyberlink.youcammakeup:id/crop3to4", "id", "Crop 3 to 4")
        crop_9to16 = Element("com.cyberlink.youcammakeup:id/crop9to16", "id", "Crop 9 to 16")
        crop_4to3 = Element("com.cyberlink.youcammakeup:id/crop4to3", "id", "Crop 4 to 3")
        crop_feed = Element("com.cyberlink.youcammakeup:id/cropCover", "id", "Crop feed")
        crop_story = Element("com.cyberlink.youcammakeup:id/cropStory", "id", "Crop story")
        crop_4to5 = Element("com.cyberlink.youcammakeup:id//crop4to5", "id", "Crop 4 to 5")
        crop_cover = Element("com.cyberlink.youcammakeup:id/cropCover", "id", "Crop cover")
        crop_profile = Element("com.cyberlink.youcammakeup:id/cropProfile", "id", "crop profile")
        duration_seekbar = Element("com.cyberlink.youcammakeup:id/durationSeekBar", "id", "Duration seekbar")
        quality_720p = Element("com.cyberlink.youcammakeup:id/quality720pBtn", "id", "Quality 720p button")
        quality_1080p = Element("com.cyberlink.youcammakeup:id/quality1080pBtn", "id", "Quality 1080p button")
        quality_4k = Element("com.cyberlink.youcammakeup:id/quality4KBtn", "id", "Quality 4k button")
        Export_button = Element("com.cyberlink.youcammakeup:id/exportButton", "id", "Export button")


class EffectsLocators:
    store_button = Element("com.cyberlink.youcammakeup:id/downloadButton", "id", "Store button")
    collection = Element("com.cyberlink.youcammakeup:id/smallEffectImage", "id", "Collection button")
    collection_back = Element("com.cyberlink.youcammakeup:id/backCollection", "id", "Collection back button")
    effect_view = Element("com.cyberlink.youcammakeup:id/effectRecyclerView", "id", "Effect view")
    effect_item = Element("com.cyberlink.youcammakeup:id/effectItem", "id", "Effect item")
    intensity_seekbar = Element("com.cyberlink.youcammakeup:id/unitSeekBar", "id", "Intensity seekbar")
    effect_download = Element("com.cyberlink.youcammakeup:id/effectDownloadIcon", "id", "Effect download button")


class BackgroundLocators:
    background_item = Element("com.cyberlink.youcammakeup:id/backgroundItem", "id", "Background item")
    background_view = ("com.cyberlink.youcammakeup:id/backgroundRecyclerView", "id", "Background view")
    background_reset = Element("com.cyberlink.youcammakeup:id/backgroundReset", "id", "")
    background_brush = Element("com.cyberlink.youcammakeup:id/backgroundBrush", "id", "")
    background_eraser = Element("com.cyberlink.youcammakeup:id/backgroundEraser", "id", "")
    draw_size1 = Element("com.cyberlink.youcammakeup:id/drawSize1", "id", "Draw size 1")
    draw_size2 = Element("com.cyberlink.youcammakeup:id/drawSize2", "id", "Draw size 2")
    draw_size3 = Element("com.cyberlink.youcammakeup:id/drawSize3", "id", "Draw size 3")
    draw_size4 = Element("com.cyberlink.youcammakeup:id/drawSize4", "id", "Draw size 4")
    draw_size5 = Element("com.cyberlink.youcammakeup:id/drawSize5", "id", "Draw size 5")


class AccessoriesLocators:
    accessories_menu = Element("com.cyberlink.youcammakeup:id/makeup_menu_item_title", "xpath", "")
    store_button = Element("com.cyberlink.youcammakeup:id/downloadButton", "id", "Store button")
    pattern_view = Element("com.cyberlink.youcammakeup:id/patternRecyclerView", "id")
    pattern_item = Element("com.cyberlink.youcammakeup:id/panel_beautify_template_button_image", "id", "")
    editroom_view = Element("com.cyberlink.youcammakeup:id/compareLineView", "id", "")


class MakeupCamLocators:
    BIPA_Agree = Element("com.cyberlink.youcammakeup:id/agree_btn", "id", "BIPA agree button")
    BIPA_Cancel = Element("com.cyberlink.youcammakeup:id/cancel_btn", "id", "BIPA cancel button")
    Feature_Notice_Close = Element("com.cyberlink.youcammakeup:id/close", "id", "Feature notice close button")
    Back = Element("com.cyberlink.youcammakeup:id/cameraBackIcon", "id", "Back to Launcher page")
    promote = Element("com.cyberlink.youcammakeup:id/promote_close_btn", "id", "Promote close button")
    AD_close = Element("com.cyberlink.youcammakeup:id/close", "id", "AD close button")
    AD_tryit = Element("com.cyberlink.youcammakeup:id/tryIt", "id", "AD try it button")


class AgingLocators:
    Try_it = Element("com.cyberlink.youcammakeup:id/tryItButton", "id", "Try it button")
    Choose_photo = Element("com.cyberlink.youcammakeup:id/photoEntryButtonText", "id", "Choose photo")
    Take_photo = "com.cyberlink.youcammakeup:id/cameraEntryButtonText"
    Live_camera = "com.cyberlink.youcammakeup:id/cameraEntryButtonText"
    Photo = "com.cyberlink.youcammakeup:id/modeImage1"
    Before_After = "com.cyberlink.youcammakeup:id/modeImage2"
    Grid = "com.cyberlink.youcammakeup:id/modeImage3"
    Video = "com.cyberlink.youcammakeup:id/modeImage4"
    Back = "com.cyberlink.youcammakeup:id/topToolBarBackBtn"
    Home = "com.cyberlink.youcammakeup:id/homeButton"
    Save = "com.cyberlink.youcammakeup:id/topToolBarDoneBtn"
    Start = "com.cyberlink.youcammakeup:id/photoEntryButtonBackground"
    Agree = "com.cyberlink.youcammakeup:id/agree_btn"
    OK = "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive"
    Allow = "com.android.permissioncontroller:id/permission_allow_button"


class ResultLocators:
    share_page_view = Element("com.cyberlink.youcammakeup:id/sharePageScrollView", "id", "Share page view")
    Back = Element("com.cyberlink.youcammakeup:id/continueEditing", "id", "Share page back to editing page button")
    Album = Element("com.cyberlink.youcammakeup:id/sharePageLibraryBtn", "id", "Share page album list button")
    Home = Element("com.cyberlink.youcammakeup:id/sharePageHomeButton", "id", "Share page home button")


class ChurnUserRecoveryLocators:
    Close_button = Element("com.cyberlink.youcammakeup:id/churn_recovery_dialog_cancel_button", "id", "")
    Continue_button = Element("com.cyberlink.youcammakeup:id/churn_recovery_dialog_continue_button", "id", "")


class MeLocators:
    Settings_button = "com.cyberlink.youcammakeup:id/bc_top_bar_left_btn"


class DeepLink:
    MakeupCam_page = "ymk://action_makeupcam"
    PhotoMakeup_page = "ymk://action/pickphoto/"

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
        darkcircle = "ymk://action/pickphoto/darkcircle"
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
