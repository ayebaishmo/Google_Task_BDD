  # Feature: Complete Task
  #   As a user
  #   I want to mark tasks as complete
  #   So that I can track my progress

  #   Scenario: Complete a task successfully
  #     Given the app is running
  #     And I add the task "Read my Bible"
  #     When I mark the task "Read my Bible" as complete
  #     Then the task "Read my Bible" should be marked as complete

  #   Scenario: Mark a task as complete when already completed
  #     Given the app is running
  #     And I add the task "Exercise"
  #     And I mark the task "Exercise" as complete
  #     When I mark the task "Exercise" as complete again
  #     Then the task "Exercise" should still be marked as complete

  #   Scenario: Try to complete a non-existing task
  #     Given the app is running
  #     When I mark the task "Go shopping" as complete
  #     Then I should get an error "Task not found"
