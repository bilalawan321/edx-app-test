# coding=utf-8
"""
    Course Discovery Page Module
"""

from tests.common import strings
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage
from tests.ios.pages.ios_new_landing import IosNewLanding
from tests.ios.pages.ios_whats_new import IosWhatsNew
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time


class IosCourseDiscovery(IosBasePage):
    """
    Course Discovery
    """

    def get_discovery_tab(self):
        """
        Get Discovery Tab

        Returns:
            webdriver elements List: Discovery tab
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.fifth_existence]

    def get_profile_icon(self):
        """
        Get Profile Icon

        Returns:
            webdriver elements List: Profile icon
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.main_dashboard_profile_icon
        )

    def get_search_icon(self):
        """
        Get search icon

        Returns:
            webdriver element: search icon Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.search_icon
        )
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.search_icon
        )

    def get_browse_by_subject_icon(self):
        """
        Get browse by subject icon

        Returns:
            webdriver element: browse by subject icon Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.browse_by_subject_icon
        )
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.browse_by_subject_icon
        )

    def get_filter_courses_view(self, driver):
        """
        Get filter courses icon

        Returns:
            webdriver element: filter courses search field Element
        """
        time.sleep(20)
        contexts = self.driver.contexts
        for x in contexts:
            if x:
                webview = x
        self.driver.switch_to.context(webview)

        # do some webby stuff
        # first_element = self.driver.find_elements_by_class_name("js-result-msg")
        # first_element = self.driver.find_elements_by_class_name("js-facet-toggle")
        # first_element = self.driver.find_element_by_class_name("img-wrapper")
        # first_element = driver.find_element(By.CLASS_NAME, "js-facet-toggle facet-toggel show-phone")
        first_element = driver.find_element(MobileBy.CLASS_NAME, "js-facet-toggle")

        # switch back to native view
        # driver.switch_to.context(driver.contexts.first)

        # for x in first_element:
        #     print('text', x.text)
        first_element.click()
        time.sleep(10)
        print('first_element::  ', first_element)
        print('first_element-text::  ', first_element.text)
        print('label::  ', first_element.get_attribute('label'))
        print('name::  ', first_element.get_attribute('name'))
        print('type::  ', first_element.get_attribute('type'))
        print('value::', first_element.get_attribute('value'))

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.browse_by_subject_icon
        )
    # def on_screen(self):
    #     """
    #     Load Login screen

    #     Returns:
    #         str: Login screen Title Name
    #     """

    #     return self.get_sign_in_button()

    # def get_close_button(self):
    #     """
    #     Get Close Button

    #     Returns:
    #          webdriver element: Close Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_close_button
    #     )

    # def get_title_textview(self):
    #     """
    #     Get Screen Title

    #     Returns:
    #         webdriver element: Screen Title Element
    #     """

    #     return self.driver.find_element_by_id(ios_elements.login_title_textview)

    # def get_logo(self):
    #     """
    #     Get edX logo

    #     Returns:
    #          webdriver element: Logo Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_edx_logo
    #     )

    # def get_username_editfield(self):
    #     """
    #     Get Username

    #     Returns:
    #          webdriver element: Username Element
    #     """
    #     user_name = self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_user_name_editfield
    #     )
    #     user_name.clear()
    #     self.get_logo().click()
    #     return user_name

    # def get_password_editfield(self):
    #     """
    #     Get Password

    #     Returns:
    #          webdriver element: Password Element
    #     """
    #     self.get_logo().click()
    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_password_editfield
    #     )

    # def get_forgot_password_textview(self):
    #     """
    #     Get Forgot Password

    #     Returns:
    #          webdriver element: Forgot Password Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_forgot_password_textview
    #     )

    # def get_sign_in_button(self):
    #     """
    #     Get Sing In

    #     Returns:
    #          webdriver element: Sing In Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_signin_button
    #     )

    # def get_login_with_email_divider_textview(self):
    #     """
    #     Get Login with Email Divider

    #     Returns:
    #          webdriver element: Login with Email Divider Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_signin_divider_textview
    #     )

    # def get_facebook_textview(self):
    #     """
    #     Get Facebook

    #     Returns:
    #          webdriver element: Facebook Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_facebook_textview
    #     )

    # def get_google_textview(self):
    #     """
    #     Get Google

    #     Returns:
    #          webdriver element: Google Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_google_textview
    #     )

    # def get_agreement_textview(self):
    #     """
    #     Get Agreement

    #     Returns:
    #          webdriver element: Agreement Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_agreement_textview
    #     )

    # def get_eula_textview(self):
    #     """
    #     Get EULA

    #     Returns:
    #          webdriver element: EULA Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_eula_textview
    #     )

    # def get_terms_textview(self):
    #     """
    #     Get Terms

    #     Returns:
    #          webdriver element: Terms Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_terms_textview
    #     )

    # def get_privacy_textview(self):
    #     """
    #     Get Privacy

    #     Returns:
    #          webdriver element: Privacy Element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_privacy_textview
    #     )

    # def get_agreement_close_button(self):
    #     """
    #     Get Close

    #     Returns:
    #          webdriver element: Close Element
    #     """

    #     return self.global_contents.get_all_views_on_ios_screen(
    #         self.driver,
    #         ios_elements.all_buttons
    #     )[self.global_contents.first_existence]

    # def load_eula_screen(self):
    #     """
    #     Load EULA screen and then close it

    #     Returns:
    #          webdriver element: Login Button Element
    #     """

    #     self.get_eula_textview().click()
    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         self.get_agreement_close_button()
    #     )
    #     self.get_agreement_close_button().click()

    #     return self.get_sign_in_button()

    # def load_terms_screen(self):
    #     """
    #     Load Terms screen and then close it

    #     Returns:
    #          webdriver element: Login Button Element
    #     """

    #     self.get_terms_textview().click()
    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         self.get_agreement_close_button()
    #     )
    #     self.get_agreement_close_button().click()

    #     return self.get_sign_in_button()

    # def load_privacy_screen(self):
    #     """
    #     Load Privacy screen and then close it

    #     Returns:
    #          webdriver element: Login Button Element
    #     """

    #     self.get_privacy_textview().click()
    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         self.get_agreement_close_button()
    #     )
    #     self.get_agreement_close_button().click()

    #     return self.get_sign_in_button()

    # def login(self, user_name, password, is_first_time=True):
    #     """
    #     Login

    #     Arguments:
    #         user_name (str): username
    #         password (str): password
    #         is_first_time (bool): True or False

    #     Returns:
    #         str: Whats New screen Title
    #     """
    #     self.get_username_editfield().click()
    #     self.get_username_editfield().clear()
    #     self.get_username_editfield().send_keys(user_name)

    #     self.get_password_editfield().click()
    #     self.get_password_editfield().send_keys(password)
    #     self.get_logo().click()
    #     self.get_sign_in_button().click()

    #     output = self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         ios_elements.login_wrong_credential_alert_title
    #     )

    #     if output:
    #         self.global_contents.wait_and_get_element(
    #             self.driver,
    #             ios_elements.login_wrong_credential_alert_title
    #         )
    #         self.global_contents.wait_and_get_element(
    #             self.driver,
    #             ios_elements.login_wrong_credential_alert_msg
    #         )
    #         wrong_credentials_alert_ok = self.global_contents.wait_and_get_element(
    #             self.driver,
    #             ios_elements.login_reset_password_alert_ok_button
    #         )
    #         wrong_credentials_alert_ok.click()

    #         return False

    #     else:
    #         if is_first_time is True:
    #             textview_screen_title = IosWhatsNew(self.driver, self.log).get_title_textview()
    #             self.global_contents.is_first_time = False
    #         else:
    #             # textview_screen_title = IosWhatsNew(self.driver, self.log).get_close_button()
    #             # textview_screen_title.click()

    #             textview_screen_title = self.global_contents.wait_and_get_element(
    #                 self.driver,
    #                 ios_elements.main_dashboard_navigation_icon
    #             )
    #     return textview_screen_title

    # def back_and_forth_new_landing(self):
    #     """
    #     From Login screen tapping back will load New Landing screen and tapping Login will
    #         load Login screen

    #     Returns:
    #          bool: Returns True if app is back on Login screen from New Landing screen
    #     """

    #     ios_new_landing = IosNewLanding(self.driver, self.log)

    #     if self.on_screen().text == strings.LOGIN:
    #         self.driver.back()
    #         if ios_new_landing.load_login_screen().text != strings.LOGIN:
    #             self.log.error('Problem - New Landing screen is not loaded')
    #             self.global_contents.flag = False
    #     else:
    #         self.log.info('Problem - Login screen is not loaded')
    #         self.global_contents.flag = False

    #     return self.global_contents.flag

    # def back_and_forth_terms(self):
    #     """
    #     From Login screen tapping 'edX Terms of Service...' will load Terms & Conditions screen
    #         and tapping back will load Login screen

    #     Returns:
    #          bool: Returns True if app is back on Login screen from edX Terms of Service
    #     """

    #     if self.on_screen().text == strings.LOGIN:
    #         self.global_contents.flag = True
    #         self.get_terms_textview().click()

    #         self.global_contents.wait_and_get_element(
    #             self.driver,
    #             ios_elements.login_agreement_close).click()
    #         if self.on_screen().text == strings.LOGIN:
    #             self.global_contents.flag = True
    #         else:
    #             self.log.error('Problem - Terms screen is not loaded')
    #             self.global_contents.flag = False
    #     else:
    #         self.log.info('Problem - Login screen is not loaded')
    #         self.global_contents.flag = False

    #     return self.global_contents.flag

    # def get_forgot_password_alert(self):
    #     """
    #     Load forgot Password alert

    #     Returns:
    #          webdriver element: alert element
    #     """

    #     self.get_forgot_password_textview().click()
    #     return self.driver.find_element_by_id(ios_elements.login_reset_password_alert_title)

    # def get_forgot_password_alert_title(self):
    #     """
    #     Get alert's title element on Forgot Password Alert

    #     Returns:
    #          webdriver element: alert title element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_reset_password_alert_title
    #     )

    # def get_forgot_password_alert_msg(self):
    #     """
    #     Get alert message element on Forgot Password Alert

    #     Returns:
    #          webdriver element: message element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_reset_password_alert_msg
    #     )

    # def get_forgot_password_alert_ok_button(self):
    #     """
    #     Get OK button element on Forgot Password Alert

    #     Returns:
    #          webdriver element: OK element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_reset_password_alert_ok_button
    #     )

    # def get_forgot_password_alert_cancel_button(self):
    #     """
    #     Get Cancel button element on Forgot Password Alert

    #     Returns:
    #          webdriver element: CANCEL element
    #     """

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         ios_elements.login_reset_password_alert_cancel_button
    #     )

    # def close_forgot_password_alert(self):
    #     """
    #     Close forgot password alert

    #     Returns:
    #          bool: True if alert is closed, False if alert is not closed
    #     """

    #     self.get_forgot_password_alert_cancel_button().click()
    #     return self.global_contents.wait_for_element_invisibility(
    #         self.driver,
    #         ios_elements.login_reset_password_alert_cancel_button
    #     )
