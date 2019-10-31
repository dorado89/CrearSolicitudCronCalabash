Feature: Create a new alarm

  Scenario: As a user I want to be able to create an alarm the first time I open the app
    Given I press "mi_button_skip"
    When I wait for 10 seconds
    And I swipe left
    And I press "Routines"
    And I press "add_button"
    And I enter text "nani" into field with id "routine_edit_name"
    And I press "add_button"
    Then I should see "nani"
