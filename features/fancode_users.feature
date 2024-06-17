Feature: Verify FanCode users' todos completion rate

  Scenario: All FanCode users should have more than half of their todos completed
    Given the list of users and their todos
    When filtering users from the city "FanCode"
    Then each FanCode user should have more than 50% of their todos completed
