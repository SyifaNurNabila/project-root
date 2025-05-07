Feature: Product Management
  As a user, I want to manage products so that I can read, update, delete, list, and search for products based on various criteria.

  # Scenario for READING a Product
  Scenario: Reading a product
    Given a product with name "Laptop" exists
    When I view the product details
    Then I should see the details of the product "Laptop"

  # Scenario for UPDATING a Product
  Scenario: Updating a product
    Given a product with name "Laptop" exists
    When I update the product's name to "Gaming Laptop"
    Then I should see the updated product with name "Gaming Laptop"

  # Scenario for DELETING a Product
  Scenario: Deleting a product
    Given a product with name "Laptop" exists
    When I delete the product
    Then the product "Laptop" should no longer exist

  # Scenario for LISTING ALL PRODUCTS
  Scenario: Listing all products
    Given multiple products exist in the system
    When I view the list of all products
    Then I should see a list of all products

  # Scenario for Searching a Product based on Category
  Scenario: Searching a product by category
    Given there are products in the system with categories
    When I search for products in the "Electronics" category
    Then I should see a list of products in the "Electronics" category

  # Scenario for Searching a Product based on Availability
  Scenario: Searching a product by availability
    Given there are products with varying availability
    When I search for products that are "available"
    Then I should see a list of products that are available

  # Scenario for Searching a Product based on Name
  Scenario: Searching a product by name
    Given a product with name "Laptop" exists
    When I search for the product by name "Laptop"
    Then I should see the product "Laptop"

  # Scenario for Searching a Product based on Category and Availability
  Scenario: Searching a product by category and availability
    Given there are products in the "Electronics" category and their availability status
    When I search for available products in the "Electronics" category
    Then I should see a list of available products in the "Electronics" category
