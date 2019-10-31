Feature: Create a new user

  Scenario: As a user I want to be able to create a user the first time I open the app
    Given I press "mi_button_skip"
    When I wait for 10 seconds
    And I swipe left
    And I press "Patients"
    And I press "add_button"
    And I enter text "nani" into field with id "patient_name"
    And I press "action_done"
    Then I should see "nani"
