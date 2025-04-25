Feature: Add Task
  As a user
  I want to add tasks to my to-do list
  So that I can track things I need to do

  Scenario: Add a task successfully
    Given the app is running
    When I add the task "listen to podcast"
    Then the task list should contain the task "listen to podcast"

  Scenario: Add a task with an empty name
    Given the app is running
    When I add a task with an empty name
    Then I should get an error "Task name cannot be empty"

  Scenario: Add a task with spaces only
    Given the app is running
    When I add a task with the name "    "
    Then I should get an error "Task name cannot be only spaces"
