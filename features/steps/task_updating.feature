Feature: Task Updating
  As a user
  I want to update my tasks
  So that I can keep track of changes and progress

  Scenario: Mark a task as completed
    Given the task app is running
    And I have a task "Buy groceries" with status "Pending"
    When I mark the task "Buy groceries" as "Completed"
    Then the task "Buy groceries" should have status "Completed"

  Scenario: Update task details
    Given the task app is running
    And I have a task "Clean apartment" with description "Vacuum"
    When I update the task "Clean apartment" with the following details:
      | description        | due_date   | priority |
      | Vacuum and dust    | 2025-05-10 | High     |
    Then the task "Clean apartment" should have description "Vacuum and dust"
    And the task should have due date "2025-05-10"
    And the task should have priority "High"

  Scenario: Cannot update a non-existent task
    Given the task app is running
    When I try to update a task "Non-existent task"
    Then I should see an error message "Task not found"