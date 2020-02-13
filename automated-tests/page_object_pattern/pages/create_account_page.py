class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_text_box = '#customer_firstname'
        self.last_name_text_box = '#customer_lastname'
        self.user_password_text_box = '#passwd'
        self.address_text_box = '#address1'
        self.city_text_box = '#city'
        self.state_dropbox = 'id_state'
        self.zip_text_box = '#postcode'
        self.mobile_phone_text_box = '#phone_mobile'
        self.register_button = '#submitAccount'

    def enter_user_data(self):
        self.driver.find_element_by_css_selector(self.first_name_text_box).send_keys('John')
        self.driver.find_element_by_css_selector(self.last_name_text_box).send_keys('Testowy')
        self.driver.find_element_by_css_selector(self.user_password_text_box).send_keys('12345')
        self.driver.find_element_by_css_selector(self.address_text_box).send_keys('Testing Avenue 565')
        self.driver.find_element_by_css_selector(self.city_text_box).send_keys('Chicago')
        self.driver.find_element_by_xpath('//select[@name="' + self.state_dropbox + \
                                          '"]/option[text()=\'Illinois\']').click()
        self.driver.find_element_by_css_selector(self.zip_text_box).send_keys('85356')
        self.driver.find_element_by_css_selector(self.mobile_phone_text_box).send_keys('1234554322')

    def click_register_button(self):
        self.driver.find_element_by_css_selector(self.register_button).click()
