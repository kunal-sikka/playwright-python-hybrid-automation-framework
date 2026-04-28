Feature: API Order

  Scenario: Create order using API
    Given api order user is authenticated
    When api order user creates an order
    Then api order response should contain order id
