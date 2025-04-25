Feature: Task Categorization
  As a user
  I want to categorize my tasks
  So that I can organize and find them more easily

  Scenario: Add a category to a task
    Given the task app is running
    And I have a task "Buy groceries"
    When I add the category "Shopping" to the task "Buy groceries"
    Then the task "Buy groceries" should have category "Shopping"

  Scenario: Filter tasks by category
    Given the task app is running
    And I have the following tasks with categories:
      | title           | category    |
      | Buy groceries   | Shopping    |
      | Buy clothes     | Shopping    |
      | Clean apartment | Housework   |
      | Pay rent        | Finance     |
    When I filter tasks by category "Shopping"
    Then I should see 2 tasks in the list
    And the task list should contain "Buy groceries" and "Buy clothes"

  Scenario: Add tags to a task
    Given the task app is running
    And I have a task "Buy groceries"
    When I add the tag "urgent" to the task "Buy groceries"
    And I add the tag "weekly" to the task "Buy groceries"
    Then the task "Buy groceries" should have tags "urgent" and "weekly"