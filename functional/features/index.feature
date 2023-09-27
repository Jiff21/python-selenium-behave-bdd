Feature: Tests that should be run on every page

  @browser  @critical
  Scenario: User can login to the site
    Given I am on "index"
    When I click on the Username field
      And I type in "standard_user"
      And I click on the Password field
      And I type in "secret_sauce"
      And I click on the Login Button
      And I wait for the Menu button
    Then the url should contain "/v1/inventory.html"
