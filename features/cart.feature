Feature: Cart

  Scenario: User adds product to cart
    Given cart user is logged in
    When cart user adds product to the cart
    Then cart should display the selected product
