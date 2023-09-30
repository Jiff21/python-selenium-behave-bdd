Feature: Example tests on the Sauce Labs Inventory Page

  @browser @medium
  Scenario: Add to cart button works
    Given I am on "inventory"
    When I Click the Bike Light Add to Cart Button
    Then the button should contain the Text "REMOVE"
      And the cart badge displays "1"

  @browser @medium
  Scenario: In page Remove from cart button works
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
  Scenario: The High to Low Selector orders the highest priced item first
    Given I am on "inventory"
    When I select "Price (high to low)" from the sort selector
    Then item "1" shold be "Sauce Labs Fleece Jacket"

  @browser @minor
    Scenario: The Low to High Selector orders the Lowest priced item first
      Given I am on "inventory"
      When I select "Price (low to high)" from the sort selector
      Then item "1" shold be "Sauce Labs Onesie"

  @browser @minor
    Scenario: The Name A to Z Selector orders correctly
      Given I am on "inventory"
        And I select "Price (low to high)" from the sort selector
      When I select "Name (A to Z)" from the sort selector
      Then item "1" shold be "Sauce Labs Backpack"

  @browser @minor
    Scenario: The Name Z to A Selector orders correctly
      Given I am on "inventory"
      When I select "Name (Z to A)" from the sort selector
      Then item "1" shold be "Test.allTheThings() T-Shirt (Red)"

  @browser @medium
  Scenario: Adding item from inventory transfers to cart
    Given I am on "inventory"
    When I Click the Bike Light Add to Cart Button
      And I Click the Test all the things T-Shirt Add to Cart Button
      And I click on the cart icon
      And I wait for at least one cart item to load
    Then the price for item "1" should be "9.99"
      And the price for item "2" should be "15.99"
      And I click the checkout button
      And I fill out the contact information with "Guy" "Incognito" from the "94112"
      And I hit the Return/Enter Key
      And I wait for the checkout summary to load
      And the subtotal should be "$25.98"
      And the tax should be "$2.08"
      And the total should be "$28.06"
      And I click the finish button
      And the checkout complete header should appear
      