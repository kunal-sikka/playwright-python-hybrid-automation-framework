Feature: Order History

  Scenario: User sees API-created order in order history
    Given order history has an order created by API
    When order history user opens order history page
    Then order history should display the created order
