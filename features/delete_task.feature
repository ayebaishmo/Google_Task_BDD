# Feature: Delete Task
#   As a user
#   I want to remove tasks I no longer need
#   So that my list stays clean

#   Scenario: Delete a task successfully
#     Given the app is running
#     And I add a task called "Go jogging"
#     When I delete the task "Go jogging"
#     Then the task list should not contain the task "Go jogging"

#   Scenario: Delete a task that does not exist
#     Given the app is running
#     When I delete the task "Watch movie"
#     Then I should get an error "Task not found"

#   Scenario: Delete all tasks from the list
#     Given the app is running
#     And I add the task "Wash dishes"
#     And I add the task "Clean room"
#     When I delete the task "Wash dishes"
#     And I delete the task "Clean room"
#     Then the task list should be empty
