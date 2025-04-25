# Feature: View Tasks
#   As a user
#   I want to see all tasks
#   So that I can review what I need to do

#   Scenario: View all tasks in the list
#     Given the app is running
#     And I add the task "Do homework"
#     And I add the task "Water plants"
#     When I list all tasks
#     Then the task list should contain the task "Do homework"
#     And the task list should contain the task "Water plants"

#   Scenario: View an empty task list
#     Given the app is running
#     When I list all tasks
#     Then the task list should be empty

#   Scenario: View tasks after completing one
#     Given the app is running
#     And I add the task "Go to the gym"
#     And I mark the task "Go to the gym" as complete
#     When I list all tasks
#     Then the task list should contain the task "Go to the gym"
#     And the task "Go to the gym" should be marked as complete
