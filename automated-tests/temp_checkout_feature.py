from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://automationpractice.com/index.php')
product_1 = driver.find_element_by_css_selector('#homefeatured img[title="Faded Short Sleeve T-shirts"]')

webdriver.ActionChains(driver).move_to_element(product_1).perform()
sleep(2)

product_1_add = driver.find_element_by_css_selector('#homefeatured a[href="http://automationpractice.com/index.php'
                                                    '?controller=cart&add=1&id_product=1&token'
                                                    '=e817bb0705dd58da8db074c69f729fd8"]')
product_1_add.click()
driver.find_element_by_css_selector('#layer_cart a[title="Proceed to checkout"]').click()
sleep(2)

driver.find_element_by_css_selector('.cart_navigation a[title="Proceed to checkout"]').click()
sleep(2)

driver.find_element_by_id('email_create').send_keys('varihig924@era7mail.com')
driver.find_element_by_css_selector('#SubmitCreate').click()
sleep(2)

driver.find_element_by_css_selector('#customer_firstname').send_keys('John')
sleep(1)
driver.find_element_by_css_selector('#customer_lastname').send_keys('Kowalski')
sleep(1)
driver.find_element_by_css_selector('#passwd').send_keys('12345')
sleep(1)
driver.find_element_by_css_selector('#address1').send_keys('Kosciuszko Street')
sleep(1)
driver.find_element_by_css_selector('#city').send_keys('Chicago')
sleep(1)
driver.find_element_by_xpath("//select[@name='id_state']/option[text()='Illinois']").click()
sleep(1)
driver.find_element_by_css_selector('#postcode').send_keys('80382')
sleep(1)
driver.find_element_by_css_selector('#phone_mobile').send_keys('123456789')
sleep(1)
driver.find_element_by_css_selector('#submitAccount').click()
sleep(1)
driver.find_element_by_css_selector('button[name="processAddress"]').click()
sleep(1)
driver.find_element_by_css_selector('#cgv').click()
sleep(1)
driver.find_element_by_css_selector('button[name="processCarrier"]').click()
sleep(1)
driver.find_element_by_css_selector('.bankwire').click()
sleep(1)
driver.find_element_by_css_selector('.cart_navigation button[type="submit"]').click()
sleep(1)
order_complete_message = driver.find_element_by_xpath('//*[contains(text(), "Your order on My Store is complete.")]')
print(str(order_complete_message))

driver.quit()
