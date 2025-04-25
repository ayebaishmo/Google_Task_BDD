Feature: Task Creation
  As a user
  I want to add new tasks to my task list
  So that I can keep track of my todos

  Scenario: Create a basic task
    Given the task app is running
    When I create a task with title "Buy groceries"
    Then the task "Buy groceries" should be added to my task list
    And the task status should be "Pending"

  Scenario: Create a task with all details
    Given the task app is running
    When I create a task with the following details:
      | title       | description           | due_date   | priority |
      | Pay bills   | Electricity and water | 2025-05-05 | High     |
    Then the task "Pay bills" should be added to my task list
    And the task should have description "Electricity and water"
    And the task should have due date "2025-05-05"
    And the task should have priority "High"

  Scenario: Cannot create a task without a title
    Given the task app is running
    When I try to create a task without a title
    Then I should see an error message "Task title is required"
    And no new task should be added to my task list