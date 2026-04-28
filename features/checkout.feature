Feature: Checkout

  Scenario: User places an order from checkout
    Given checkout user is logged in
    And checkout user has product in cart
    When checkout user places the order
    Then checkout user should see order confirmation
