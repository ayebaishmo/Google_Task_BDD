Feature: Task Deletion
  As a user
  I want to delete tasks from my task list
  So that I can remove completed or unnecessary tasks

  Scenario: Delete a task
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Buy groceries   | Get milk, eggs  | 2025-05-01 | Medium   |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
    When I delete the task "Buy groceries"
    Then the task "Buy groceries" should be removed from my task list
    And I should see 1 task in the list

  Scenario: Cannot delete a non-existent task
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
    When I try to delete a task "Buy groceries"
    Then I should see an error message "Task not found"
    And I should see 1 task in the list

  Scenario: Delete all tasks
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Buy groceries   | Get milk, eggs  | 2025-05-01 | Medium   |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
      | Pay rent        | For May         | 2025-05-05 | High     |
    When I delete all tasks
    Then my task list should be empty