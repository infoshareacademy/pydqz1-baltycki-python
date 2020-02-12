class CartPageSignIn:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.create_account_email_text_box = '#email_create'
        self.create_account_button = 'button[name="SubmitCreate"]'
        self.registered_user_email_text_box = '#email'
        self.registered_user_password_text_box = '#passwd'
        self.registered_user_signin_button = '#SubmitLogin'

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.registered_user_email_text_box).send_keys\
            ('varihig919@era7mail.com')
        self.driver.find_element_by_css_selector(self.registered_user_password_text_box).send_keys('12345')
        self.driver.find_element_by_css_selector(self.registered_user_signin_button).click()
