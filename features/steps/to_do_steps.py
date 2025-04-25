from behave import given, when, then
from app import ToDoApp  # Import the ToDoApp class

# Initialize a global instance of the ToDoApp class
todo_app = ToDoApp()

@given('the app is running')
def step_impl_given_app_is_running(context):
    # Initialize the app before running the test
    global todo_app
    todo_app = ToDoApp()  # Ensure a new instance for each scenario

@when('I add the task "{task_title}"')
def step_impl_add_task(context, task_title):
    try:
        todo_app.add_task(task_title)
    except ValueError as e:
        context.error_message = str(e)

@when('I add a task with an empty name')
def step_impl_add_empty_task(context):
    try:
        todo_app.add_task("")
    except ValueError as e:
        context.error_message = str(e)

@when('I add a task with the name "    "')
def step_impl_add_spaces_only_task(context):
    try:
        todo_app.add_task("    ")
    except ValueError as e:
        context.error_message = str(e)

@then('the task list should contain the task "{task_title}"')
def step_impl_then_task_is_added(context, task_title):
    tasks = [task["title"] for task in todo_app.list_tasks()]
    assert task_title in tasks, f"Expected task '{task_title}' to be in the task list, but it was not found."

@then('I should get an error "{expected_error_message}"')
def step_impl_then_error_message(context, expected_error_message):
    assert hasattr(context, 'error_message'), "Expected an error, but none was raised."
    assert context.error_message == expected_error_message, f"Expected error message '{expected_error_message}', but got '{context.error_message}'"
