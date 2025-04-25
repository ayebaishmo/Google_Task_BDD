Feature: Edit Task
  As a user
  I want to update task names
  So that they remain relevant

  Scenario: Edit an existing task
    Given the app is running
    And I add a task called "Pray early"
    When I edit the task "Pray early" to "Pray in the morning"
    Then the task list should contain the task "Pray in the morning"

  Scenario: Edit a task that does not exist
    Given the app is running
    When I try to edit the task "Read book" to "Read more books"
    Then I should get an error "Task not found"

  Scenario: Edit a task with an empty name
    Given the app is running
    And I add a task called "Exercise"
    When I edit the task "Exercise" to ""
    Then I should get an error "Task name cannot be empty"
