Feature: The detaails page works as expected

  @medium @requests
  Scenario: An API Test example, but no good endpoints on site to test
    Given I get "bolt t-shirt details" with requests session
    Then it should have a "200" status code
      And the header "content-type" should contain "charset=utf-8"
      And the response should use https
      And the response url should include "/inventory-item.html?id=1"

