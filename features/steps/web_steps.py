from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize webdriver (you can change this to any browser you are using)
driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')

@given('I am on the product listing page')
def step_impl(context):
    driver.get("http://localhost:5000/products")
    time.sleep(2)  # Allow time for page to load

@when('I click the "Add Product" button')
def step_impl(context):
    add_button = driver.find_element(By.XPATH, '//button[@id="add-product"]')
    add_button.click()
    time.sleep(2)  # Allow time for the page to load

@when('I fill in the product details')
def step_impl(context):
    name_field = driver.find_element(By.NAME, "product_name")
    name_field.send_keys("New Product")

    category_field = driver.find_element(By.NAME, "category")
    category_field.send_keys("Category A")

    price_field = driver.find_element(By.NAME, "price")
    price_field.send_keys("99.99")

    availability_field = driver.find_element(By.NAME, "availability")
    availability_field.send_keys("In Stock")

@when('I click the "Submit" button')
def step_impl(context):
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    time.sleep(2)  # Allow time for the page to load

@then('I should see a new product added to the list')
def step_impl(context):
    product_name = driver.find_element(By.XPATH, '//table/tbody/tr[last()]/td[1]').text
    assert product_name == "New Product", f"Expected 'New Product' but got {product_name}"

@when('I search for a product by name "{name}"')
def step_impl(context, name):
    search_field = driver.find_element(By.NAME, "search_name")
    search_field.send_keys(name)
    search_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow time for search results

@then('I should see the product "{name}" in the list')
def step_impl(context, name):
    product_name = driver.find_element(By.XPATH, f'//table/tbody/tr/td[text()="{name}"]')
    assert product_name.text == name, f"Expected product with name '{name}' but got {product_name.text}"

@when('I search for a product by category "{category}"')
def step_impl(context, category):
    category_field = driver.find_element(By.NAME, "search_category")
    category_field.send_keys(category)
    category_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow time for search results

@then('I should see products from category "{category}"')
def step_impl(context, category):
    category_column = driver.find_elements(By.XPATH, f'//table/tbody/tr/td[text()="{category}"]')
    assert len(category_column) > 0, f"No products found under category '{category}'"

@when('I search for a product by availability "{availability}"')
def step_impl(context, availability):
    availability_field = driver.find_element(By.NAME, "search_availability")
    availability_field.send_keys(availability)
    availability_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow time for search results

@then('I should see products with availability "{availability}"')
def step_impl(context, availability):
    availability_column = driver.find_elements(By.XPATH, f'//table/tbody/tr/td[text()="{availability}"]')
    assert len(availability_column) > 0, f"No products found with availability '{availability}'"

@when('I delete the product "{name}"')
def step_impl(context, name):
    delete_button = driver.find_element(By.XPATH, f'//table/tbody/tr[td[text()="{name}"]]/td/button[@class="delete"]')
    delete_button.click()
    time.sleep(2)  # Allow time for the page to reload

@then('I should not see the product "{name}" in the list')
def step_impl(context, name):
    try:
        product_row = driver.find_element(By.XPATH, f'//table/tbody/tr[td[text()="{name}"]]')
        assert False, f"Product '{name}' was not deleted"
    except:
        pass  # Product is not found, which is expected
