Feature: Example tests on the Sauce Labs Checkout Page

  @browser @medium
  Scenario: Validation for first name shows up
    Given I am on "checkout info"
    When I type "Fake Pass" into the checkout last name field
      And I type "94101" into the checkout zip code field
      And I click the continue button on the checkout info page
    Then the checkout info pages shows one validation error
      And the checkout info pages validation error should include "First Name is required"

  @browser @blocker
  Scenario: Checkout suceeds with a full cart
    Given I am on "inventory"
      And I fill up the cart with all items
      And I am on "checkout overview"
    When I click the finish button
    Then the checkout complete header should appear


