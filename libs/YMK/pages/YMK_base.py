from libs.base import BasePage
from libs.YMK.locators import DeepLink
from libs.YMK import pages

from libs.element import Element


class YMKbase(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.send_page = None

    def deeplink_to_launcher(self):
        self.deeplink(DeepLink.Launcher_page)
        return pages.launcher_page.Launcher(self.driver)

    def deeplink_to_photomakeup(self):
        self.deeplink(DeepLink.PhotoMakeup_page)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def deeplink_to_lipstick(self):
        self.deeplink(DeepLink.Mouth.lipstick)
        return pages.photomakeup_page.LipColor(self.driver)

    # TODO: still working on it
    # def deeplink_to_lipstick2(self):
    #     self.deeplink(DeepLink.Mouth.lipstick)
    #     self.send_page = pages.photomakeup_page.LipColor
    #     return pages.photopicker_page.PhotoPicker(self.driver, self.send_page)

    def deeplink_to_lipreshape(self):
        self.deeplink(DeepLink.Mouth.lip_reshape)
        return pages.photomakeup_page.LipReshape(self.driver)

    def deeplink_to_smile(self):
        self.deeplink(DeepLink.Mouth.smile)
        return pages.photomakeup_page.Smile(self.driver)

    def deeplink_to_lipplumper(self):
        self.deeplink(DeepLink.Mouth.lip_plumper)
        return pages.photomakeup_page.LipPlumper(self.driver)

    def deeplink_to_teethwhitener(self):
        self.deeplink(DeepLink.Mouth.whiten_teeth)
        return pages.photomakeup_page.WhitenTeeth(self.driver)

    def deeplink_to_lipart(self):
        self.deeplink(DeepLink.Mouth.lip_art)
        return pages.photomakeup_page.LipArt(self.driver)

    def deeplink_to_skinsmoother(self):
        self.deeplink(DeepLink.Face.skin_smoother)
        return pages.photomakeup_page.Smoother(self.driver)

    def deeplink_to_faceshape(self):
        self.deeplink(DeepLink.Face.face_reshaper)
        return pages.photomakeup_page.FaceShape(self.driver)

    def deeplink_to_noseenhance(self):
        self.deeplink(DeepLink.Face.nose_enhancement)
        return pages.photomakeup_page.NoseEnhance(self.driver)

    def deeplink_to_wrinkle(self):
        self.deeplink(DeepLink.Face.wrinkle)
        return pages.photomakeup_page.Wrinkle(self.driver)

    def deeplink_to_redness(self):
        self.deeplink(DeepLink.Face.redness)
        return pages.photomakeup_page.Redness(self.driver)

    def deeplink_to_unevenskintone(self):
        self.deeplink(DeepLink.Face.uneven_skintone)
        return pages.photomakeup_page.UnevenSkintone(self.driver)

    def deeplink_to_pores(self):
        self.deeplink(DeepLink.Face.pores)
        return pages.photomakeup_page.Pores(self.driver)

    def deeplink_to_foundation(self):
        self.deeplink(DeepLink.Face.foundation)
        return pages.photomakeup_page.Foundation(self.driver)

    def deeplink_to_concealer(self):
        self.deeplink(DeepLink.Face.concealer)
        return pages.photomakeup_page.Concealer(self.driver)

    def deeplink_to_blush(self):
        self.deeplink(DeepLink.Face.blush)
        return pages.photomakeup_page.Blush(self.driver)

    def deeplink_to_contour(self):
        self.deeplink(DeepLink.Face.contour)
        return pages.photomakeup_page.Contour(self.driver)

    def deeplink_to_highlight(self):
        self.deeplink(DeepLink.Face.highlight)
        return pages.photomakeup_page.Highlight(self.driver)

    def deeplink_to_facepaint(self):
        self.deeplink(DeepLink.Face.facepaint)
        return pages.photomakeup_page.FacePaint(self.driver)

    def deeplink_to_blemish(self):
        self.deeplink(DeepLink.Face.blemish)
        return pages.photomakeup_page.Blemish(self.driver)

    def deeplink_to_shineremoval(self):
        self.deeplink(DeepLink.Face.shinremoval)
        return pages.photomakeup_page.ShineRemoval(self.driver)

    def deeplink_to_eyeliner(self):
        self.deeplink(DeepLink.Eye.eyeliner)
        return pages.photomakeup_page.Eyeliner(self.driver)

    def deeplink_to_eyelashes(self):
        self.deeplink(DeepLink.Eye.eyelashes)
        return pages.photomakeup_page.Eyelashes(self.driver)

    def deeplink_to_eyeshadow(self):
        self.deeplink(DeepLink.Eye.eyeshadow)
        return pages.photomakeup_page.EyeShadow(self.driver)

    def deeplink_to_darkcircle(self):
        self.deeplink(DeepLink.Eye.darkcircle)
        return pages.photomakeup_page.DarkCircle(self.driver)

    def deeplink_to_eyetuner(self):
        self.deeplink(DeepLink.Eye.eyetuner)
        return pages.photomakeup_page.EyeTuner(self.driver)

    def deeplink_to_eyebrows(self):
        self.deeplink(DeepLink.Eye.eyebrows)
        return pages.photomakeup_page.Eyebrows(self.driver)

    def deeplink_to_browreshape(self):
        self.deeplink(DeepLink.Eye.eyebrow_reshape)
        return pages.photomakeup_page.BrowReshape(self.driver)

    def deeplink_to_eyecolor(self):
        self.deeplink(DeepLink.Eye.eyecontact)
        return pages.photomakeup_page.EyeColor(self.driver)

    def deeplink_to_eyebag(self):
        self.deeplink(DeepLink.Eye.eyebag)
        return pages.photomakeup_page.EyeBag(self.driver)

    def deeplink_to_brighten(self):
        self.deeplink(DeepLink.Eye.eyebrighten)
        return pages.photomakeup_page.Brighten(self.driver)

    def deeplink_to_doubleeyelid(self):
        self.deeplink(DeepLink.Eye.eyelid)
        return pages.photomakeup_page.DoubleEyelid(self.driver)

    def deeplink_to_redeye(self):
        self.deeplink(DeepLink.Eye.redeye)
        return pages.photomakeup_page.RedEye(self.driver)

    def deeplink_to_hairdye(self):
        self.deeplink(DeepLink.Hair.hairdye)
        return pages.photomakeup_page.HairColor(self.driver)

    def deeplink_to_hairstyle(self):
        self.deeplink(DeepLink.Hair.wig)
        return pages.photomakeup_page.HairStyle(self.driver)

    def deeplink_to_bodytuner(self):
        self.deeplink(DeepLink.body_tuner)
        return pages.bodytuner_page.BodyTuner(self.driver)

    def deeplink_to_removal(self):
        self.deeplink(DeepLink.object_removal)
        return pages.removal_page.Removal(self.driver)

    def deeplink_to_animation(self):
        self.deeplink(DeepLink.animation)
        return pages.animation_page.Animation(self.driver)

    def deeplink_to_effect(self):
        self.deeplink(DeepLink.effect)
        return pages.effects_page.Effects(self.driver)

    def deeplink_to_background(self):
        self.deeplink(DeepLink.background)
        return pages.background_page.Background(self.driver)

    def deeplink_to_eyewear(self):
        self.deeplink(DeepLink.eyewear)
        return pages.accessories_page.Accessories(self.driver)

    def deeplink_to_headband(self):
        self.deeplink(DeepLink.headband)
        return pages.accessories_page.Accessories(self.driver)

    def deeplink_to_necklace(self):
        self.deeplink(DeepLink.necklace)
        return pages.accessories_page.Accessories(self.driver)

    def deeplink_to_earrings(self):
        self.deeplink(DeepLink.earrings)
        return pages.accessories_page.Accessories(self.driver)

    def deeplink_to_hat(self):
        self.deeplink(DeepLink.hat)
        return pages.accessories_page.Accessories(self.driver)

    def deeplink_to_makeupcam(self):
        self.deeplink(DeepLink.MakeupCam_page)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def deeplink_to_aging(self):
        self.deeplink(DeepLink.Aging_page)
        return pages.aging_page.Aging(self.driver)

    def deeplink_to_me(self):
        self.deeplink(DeepLink.me_page)
        return pages.me_page.MePage(self.driver)

    def deeplink_to_makeupcam_eyeshadow(self):
        self.deeplink(DeepLink.MakeupCam.eyeshadow)
        return pages.makeupcam_page.Makeup(self.driver)

    def swipe_element_to_mid(self, element: Element):
        device_size = self.driver.get_window_size()
        device_x_mid = device_size['width']/3
        device_y_mid = device_size['height']/2
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 3)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        self.swipe(m_x, m_y, device_x_mid, device_y_mid, 1000)
        return self

    def deeplink_to_setting(self):
        self.deeplink(DeepLink.setting_page)
        return pages.setting_page.SettingPage(self.driver)