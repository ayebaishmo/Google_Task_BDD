Feature: To-Do List activity

    Scenario: Add a task
        Given the app is running
        When I add the task "listen to podcast"
        Then the task list should contain the task "listen to podcast"

    Scenario: Complete a task
        Given the app is running
        And I add the task like "Read my Bible"
        When I mark the task "Read my Bible" as Complete
        Then the task "Read my Bible" should be marked Complete

    Scenario: Edit a task
        Given the app is running
        And I add a task called "Pray early"
        When I edit the task "Pray early" to "Pray in the morning"

    Scenario: Delete a task
        Given the app is running
        And I add a task called "Go jogging"
        When I delete the task "Go jogging"
        Then the task list should not contain "Go jogging"

        
