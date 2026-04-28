Feature: Hybrid Order

  Scenario: API-created order is visible in UI
    Given hybrid order is created through API
    When hybrid user opens the order from order history
    Then hybrid order details should show success message
