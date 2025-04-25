from behave import given, when, then
from app import ToDoApp

# App is running Step 
@given("the app is running")
def step_start_app(context):
    context.app = ToDoApp()

# Add Task
@when('I add the task "{title}"')
def step_add_task(context, title):
    context.error_message = None
    try:
        context.app.add_task(title)
    except ValueError as e:
        context.error_message = str(e)

@when('I add a task with an empty name')
def step_add_empty_task(context):
    context.error_message = None
    try:
        context.app.add_task("")
    except ValueError as e:
        context.error_message = str(e)

@when('I add a task with the name "    "')
def step_add_task_with_spaces_only(context):
    context.error_message = None
    try:
        context.app.add_task("    ")
    except ValueError as e:
        context.error_message = str(e)

@then('the task list should contain the task "{title}"')
def step_task_should_exist(context, title):
    tasks = [task["title"] for task in context.app.list_tasks()]
    assert title in tasks, f'"{title}" not found in task list'

@then('I should get an error "{message}"')
def step_check_error_message(context, message):
    assert context.error_message == message, f"Expected error message '{message}', but got '{context.error_message}'"

# Complete Task
@given('I add the task "{title}"')
def step_add_task_given(context, title):
    context.app.add_task(title)

@when('I mark the task "{title}" as complete')
def step_mark_complete(context, title):
    try:
        context.app.complete_task(title)
    except ValueError as e:
        context.error_message = str(e)

@when('I mark the task "{title}" as complete again')
def step_mark_complete_again(context, title):
    try:
        context.app.complete_task(title)
    except ValueError as e:
        context.error_message = str(e)

@then('the task "{title}" should be marked as complete')
def step_check_task_done(context, title):
    for task in context.app.list_tasks():
        if task["title"] == title:
            assert task["done"] is True
            return
    assert False, f'Task "{title}" not found in list'

# Delete Task
@given('I add a task called "{title}"')
def step_add_named_task(context, title):
    context.app.add_task(title)

@when('I delete the task "{title}"')
def step_delete_task(context, title):
    try:
        context.app.delete_task(title)
    except ValueError as e:
        context.error_message = str(e)

@then('the task list should not contain the task "{title}"')
def step_check_task_not_exist(context, title):
    tasks = [task["title"] for task in context.app.list_tasks()]
    assert title not in tasks, f'Task "{title}" was not deleted'

@then("the task list should be empty")
def step_list_should_be_empty(context):
    assert len(context.app.list_tasks()) == 0

# Edit Task
@when('I edit the task "{old}" to "{new}"')
def step_edit_task(context, old, new):
    context.error_message = None
    try:
        context.app.edit_task(old, new)
    except ValueError as e:
        context.error_message = str(e)

@when('I try to edit the task "{old}" to "{new}"')
def step_try_edit_task(context, old, new):
    context.error_message = None
    try:
        context.app.edit_task(old, new)
    except ValueError as e:
        context.error_message = str(e)

# View Tasks
@when("I list all tasks")
def step_list_tasks(context):
    context.task_list = context.app.list_tasks()

@then('the task list should contain the task "{title}"')
def step_task_in_list(context, title):
    titles = [task["title"] for task in context.task_list]
    assert title in titles, f'Task "{title}" not found'

@then('the task "{title}" should be marked as complete')
def step_task_marked_complete(context, title):
    for task in context.task_list:
        if task["title"] == title:
            assert task["done"] is True, f'Task "{title}" is not marked complete'
            return
    assert False, f'Task "{title}" not found in task list'
