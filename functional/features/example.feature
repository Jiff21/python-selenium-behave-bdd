Feature: Example tests on the Sauce Labs Inventory Page

  @browser @medium
  Scenario: Add to cart button works
    Given I am on "inventory"
    When I Click the Bike Light Add to Cart Button
    Then the button should contain the Text "REMOVE"
      And the cart badge displays "1"

  @browser @medium
  Scenario: Remove from cart button works
    Given I am on "inventory"
      And I Click the Bike Light Add to Cart Button
      And the cart badge displays "1"
    When I Click the Bike Light Add to Cart Button
    Then the button should contain the Text "ADD TO CART"
      And the cart badge should not be present

  @browser @chrome-only @normal @local-only
  Scenario: Inventory Page should have no console errors if user has slow internet
    Given I am on "index"
    When I throttle network speed to "10.0" MB/s down, "10.0" MB/s up, with "0.0" ms latency
      And I am on "inventory"
      And I check the console logs
    Then there should be no severe console log errors

  @browser @minor
  Scenario: The first result for Python behave should contain expected title
    Given I am on "index"
    When I type in "Behave Python"
    Then the results should contain "Welcome to behave!"
