Feature: The detaails page works as expected

  @requests @medium
  Scenario: An API Test example, but no good endpoints on site to test
    Given I get "bolt t-shirt details" with requests session
    Then it should have a "200" status code
      And the header "content-type" should contain "charset=utf-8"
      And the response should use https
      And the response url should include "/inventory-item.html?id=1"

  @browser @minor
  Scenario: Hovering state on the Add to Cart Buttton works on a Product Details page
    Given I am on "bolt t-shirt details"
    When I hover over the add to cart button
    Then it should have a background-color of "239, 239, 239"
