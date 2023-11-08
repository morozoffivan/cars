import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


"""Создаем переменные для ввода данных о пользователе"""
last_name_var = 'Morozov'
first_name_var = 'Ivan'
middle_name_var = 'Vladimirovich'
age_var = '26'
phone_number_var = '89992332323'
full_name = f'{last_name_var} {first_name_var} {middle_name_var}'
model_car = 'S500 Cabriolet AMG'


"""Открываем страницу"""
driver = webdriver.Chrome()
driver.get('https://testdrive.andersenlab.com/')


"""Первый этап -> выбор авто"""
btn_continue_step_1 = driver.find_element(By.XPATH, '//*[@id="go_to_step_2"]')
btn_continue_step_2 = driver.find_element(By.XPATH, '//*[@id="go_to_step_3"]')
btn_continue_step_1.click()


# """Получение название выбранного авто"""
# chosen_auto = driver.find_element(By.XPATH, '//*[@id="title"]')
# print(chosen_auto.text)


"""Второй этап -> выбор типа двигателя и коробки передачи"""
engine = driver.find_element(By.XPATH, '//*[@id="engine"]')
engine.click()
engine.send_keys(Keys.RETURN)
engine_optional_1 = driver.find_element(By.XPATH, '//*[@id="engine"]/option[1]').text
engine_optional_2 = driver.find_element(By.XPATH, '//*[@id="engine"]/option[2]').text
# engine.send_keys(Keys.ARROW_DOWN)


transmission = driver.find_element(By.XPATH, '//*[@id="transmission"]')
transmission_optional_1 = driver.find_element(By.XPATH, '//*[@id="transmission"]/option').text
transmission.click()
# transmission.send_keys(Keys.ARROW_DOWN)
# transmission.send_keys(Keys.RETURN)


btn_continue_step_2.click()


"""Ввод данных пользователя"""
last_name = driver.find_element(By.XPATH, '//*[@id="form_last_name"]')
last_name.send_keys(last_name_var)
first_name = driver.find_element(By.XPATH, '//*[@id="form_first_name"]')
first_name.send_keys(first_name_var)
middle_name = driver.find_element(By.XPATH, '//*[@id="form_middle_name"]')
middle_name.send_keys(middle_name_var)
age = driver.find_element(By.XPATH, '//*[@id="form_age"]')
age.send_keys(age_var)
phone_number = driver.find_element(By.XPATH, '//*[@id="form_phone"]')
phone_number.send_keys()
phone_number.send_keys(phone_number_var)
btn_continue_step_3 = driver.find_element(By.XPATH, '//*[@id="go_to_step_4"]')
"""Скриншот формы ввода + дата"""
time.sleep(2)
now_date = datetime.datetime.utcnow().strftime('%d.%m.%Y_%H.%M')
driver.save_screenshot(f'screenshot_form_date {now_date}.png')


btn_continue_step_3.click()


"""Проверка правильности отображения имени пользователя"""
check_name = driver.find_element(By.XPATH, '//*[@id="step_4_name"]')
assert check_name.text == full_name
print('Name matched')


"""Проверка правильности отображения номера пользователя"""
check_phone_number = driver.find_element(By.XPATH, '//*[@id="step_4_phone"]')
assert check_phone_number.text == phone_number_var
print('Phone matched')


"""Проверка правильности отображения выбранного авто"""
get_name_auto = driver.find_element(By.XPATH, '//*[@id="step_4_car"]')
assert model_car == get_name_auto.text
print('Brand of auto matched')


"""Проверка правильности отображения выбранного вида двигателя и коробки передачи"""
get_engine_and_transmission = driver.find_element(By.XPATH, '//*[@id="step_4_equipment"]')
assert get_engine_and_transmission.text == f'{engine_optional_1} engine , {transmission_optional_1} transmission'
print('Transmission matched')


"""Проверка правильности отображения введенного возраста пользователя"""
get_age = driver.find_element(By.XPATH, '//*[@id="step_4_age"]')
assert get_age.text == age_var
print('Age matched')


time.sleep(2)
driver.save_screenshot(f'screenshot_booking {now_date}.png')




book = driver.find_element(By.XPATH, '//*[@id="finish"]')
ok = driver.find_element(By.XPATH, '//*[@id="title"]')


book.click()
assert ok.text == 'Thank you for booking the test drive!'
print('Test passed')