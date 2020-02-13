class CartPageSignIn:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.create_account_email_text_box = '#email_create'
        self.create_account_button = 'button[name="SubmitCreate"]'
        self.registered_user_email_text_box = '#email'
        self.registered_user_password_text_box = '#passwd'
        self.registered_user_signin_button = '#SubmitLogin'

    def login_as_registered_user(self):
        self.driver.find_element_by_css_selector(self.registered_user_email_text_box).send_keys\
            ('varihig919@era7mail.com')
        self.driver.find_element_by_css_selector(self.registered_user_password_text_box).send_keys('12345')
        self.driver.find_element_by_css_selector(self.registered_user_signin_button).click()

    def create_new_account(self):
        self.driver.find_element_by_css_selector(self.create_account_email_text_box).send_keys\
            ('2pantestowy@era7mail.com')
        self.driver.find_element_by_css_selector(self.create_account_button).click()
