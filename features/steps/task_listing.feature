Feature: Task Listing
  As a user
  I want to view my tasks
  So that I can see what I need to do

  Scenario: List all tasks
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Buy groceries   | Get milk, eggs  | 2025-05-01 | Medium   |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
      | Pay rent        | For May         | 2025-05-05 | High     |
    When I request to see all tasks
    Then I should see 3 tasks in the list
    And the task list should contain "Buy groceries", "Clean apartment", and "Pay rent"

  Scenario: Filter tasks by priority
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Buy groceries   | Get milk, eggs  | 2025-05-01 | Medium   |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
      | Pay rent        | For May         | 2025-05-05 | High     |
    When I filter tasks by priority "High"
    Then I should see 1 task in the list
    And the task list should contain only "Pay rent"

  Scenario: Sort tasks by due date
    Given the task app is running
    And I have the following tasks:
      | title           | description     | due_date   | priority |
      | Pay rent        | For May         | 2025-05-05 | High     |
      | Buy groceries   | Get milk, eggs  | 2025-05-01 | Medium   |
      | Clean apartment | Vacuum, dust    | 2025-05-03 | Low      |
    When I sort tasks by due date
    Then the first task should be "Buy groceries"
    And the last task should be "Pay rent"