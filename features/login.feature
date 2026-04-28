Feature: Login

  Scenario: User logs in with valid credentials
    Given login user is on the login page
    When login user logs in with valid credentials
    Then login user should see the products page
