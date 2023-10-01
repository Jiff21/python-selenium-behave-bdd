Feature: An example of API Tests on the Swagger Pet Store API

  @requests @medium
  Scenario Outline: <method> <uri><parameters> returns expected pet
    Given I "<method>" "<uri>" with the parameters "<parameters>"
    Then it should have a "200" status code
      And the json response should be a list of least "1" items
      And the json response should contain a dog named "<pet_name>"
      And the json response should not contain a dog named "<not_pet>"

    Examples: Filtering by parameters works
    | method  | uri                | parameters         | pet_name    | not_pet    |
    | GET     | /pet/findByStatus  | ?status=available  | fish        | hello kity |
    | GET     | /pet/findByStatus  | ?status=pending    | doggie      | fish       |
    | GET     | /pet/findByStatus  | ?status=sold       | hello kity  | fish       |


  @requests @medium
  Scenario: All dogs should have a name, status & ID
    Given I "GET" "/pet/findByStatus" with requests
    Then it should have a "200" status code
      And all dogs should have a name
      And all dogs should have an ID
      And all dogs should have a status
      And the response should use https
      And should not reveal dog pii
