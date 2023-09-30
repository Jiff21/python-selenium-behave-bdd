Feature: Example tests on the Sauce Labs Checkout Page

  @browser @blocker
  Scenario: Checkout suceeds with a full cart
    Given I am on "inventory"
      And I fill up the cart with all items
      And I am on "checkout overview"
    When I click the finish button
    Then the checkout complete header should appear
