Feature: Tests that should be run on every page

  @browser  @chrome-only @critical
  Scenario: There should be no severe console log errors on index page
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors

  @requests @minor
  Scenario: SEO Best practices insist you should have Facebook open graph data
    Given I get "index" with requests session
    Then it should have an og:title
      And the content attribute should not be empty
      And it should have an og:description
      And the content attribute should not be empty
      And it should have an og:image
      And the content attribute should not be empty
      And it should have an og:url
      And the content attribute should not be empty

  @requests @minor
  Scenario: SEO Best practices insist you should have Twitter Card data
    Given I get "index" with requests session
    Then it should have a twitter:card meta tag
      And the content attribute should not be empty
      And it should have a twitter:site meta tag
      And the content attribute should not be empty
      And it should have a twitter:image meta tag
      And the content attribute should not be empty
      And it should have a twitter:title meta tag
      And the content attribute should not be empty
      And it should have a twitter:description meta tag
      And the content attribute should not be empty
