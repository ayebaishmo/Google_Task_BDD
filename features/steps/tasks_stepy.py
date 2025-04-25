from behave import given, when, then
from task_app import TaskManager, Task

@given('the task app is running')
def step_impl(context):
    context.task_manager = TaskManager()
    context.task_manager.tasks = []

@when('I create a task with title "{title}"')
def step_impl(context, title):
    try:
        context.task = context.task_manager.create_task(title)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then('the task "{title}" should be added to my task list')
def step_impl(context, title):
    task = context.task_manager.get_task_by_title(title)
    assert task is not None, f"Task '{title}' was not found in the task list"

@then('the task status should be "{status}"')
def step_impl(context, status):
    assert context.task.status == status, f"Expected status '{status}', got '{context.task.status}'"

@when('I create a task with the following details')
def step_impl(context):
    for row in context.table:
        try:
            context.task = context.task_manager.create_task(
                row['title'], 
                row['description'], 
                row['due_date'], 
                row['priority']
            )
            context.error = None
        except ValueError as e:
            context.error = str(e)

@then('the task should have description "{description}"')
def step_impl(context, description):
    assert context.task.description == description, f"Expected description '{description}', got '{context.task.description}'"

@then('the task should have due date "{due_date}"')
def step_impl(context, due_date):
    assert context.task.due_date == due_date, f"Expected due date '{due_date}', got '{context.task.due_date}'"

@then('the task should have priority "{priority}"')
def step_impl(context, priority):
    assert context.task.priority == priority, f"Expected priority '{priority}', got '{context.task.priority}'"

@when('I try to create a task without a title')
def step_impl(context):
    try:
        context.task = context.task_manager.create_task("")
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then('I should see an error message "{message}"')
def step_impl(context, message):
    assert context.error == message, f"Expected error message '{message}', got '{context.error}'"

@then('no new task should be added to my task list')
def step_impl(context):
    assert len(context.task_manager.tasks) == 0, f"Expected 0 tasks, got {len(context.task_manager.tasks)}"

# Task Listing Steps
@given('I have the following tasks')
def step_impl(context):
    for row in context.table:
        context.task_manager.create_task(
            row['title'], 
            row['description'], 
            row['due_date'], 
            row['priority']
        )

@when('I request to see all tasks')
def step_impl(context):
    context.tasks = context.task_manager.get_all_tasks()

@then('I should see {count:d} tasks in the list')
def step_impl(context, count):
    assert len(context.tasks) == count, f"Expected {count} tasks, got {len(context.tasks)}"

@then('the task list should contain "{title1}", "{title2}", and "{title3}"')
def step_impl(context, title1, title2, title3):
    titles = [task.title for task in context.tasks]
    assert title1 in titles, f"Task '{title1}' not found in task list"
    assert title2 in titles, f"Task '{title2}' not found in task list"
    assert title3 in titles, f"Task '{title3}' not found in task list"

@when('I filter tasks by priority "{priority}"')
def step_impl(context, priority):
    context.tasks = context.task_manager.filter_tasks_by_priority(priority)

@then('the task list should contain only "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.tasks]
    assert title in titles, f"Task '{title}' not found in task list"
    assert len(titles) == 1, f"Expected 1 task, got {len(titles)}"

@when('I sort tasks by due date')
def step_impl(context):
    context.tasks = context.task_manager.sort_tasks_by_due_date()

@then('the first task should be "{title}"')
def step_impl(context, title):
    assert context.tasks[0].title == title, f"Expected first task to be '{title}', got '{context.tasks[0].title}'"

@then('the last task should be "{title}"')
def step_impl(context, title):
    assert context.tasks[-1].title == title, f"Expected last task to be '{title}', got '{context.tasks[-1].title}'"

# Task Updating Steps
@given('I have a task "{title}" with status "{status}"')
def step_impl(context, title, status):
    context.task = context.task_manager.create_task(title, status=status)

@when('I mark the task "{title}" as "{status}"')
def step_impl(context, title, status):
    task = context.task_manager.get_task_by_title(title)
    context.task_manager.update_task(task.id, status=status)

@then('the task "{title}" should have status "{status}"')
def step_impl(context, title, status):
    task = context.task_manager.get_task_by_title(title)
    assert task.status == status, f"Expected status '{status}', got '{task.status}'"

@given('I have a task "{title}" with description "{description}"')
def step_impl(context, title, description):
    context.task = context.task_manager.create_task(title, description=description)

@when('I update the task "{title}" with the following details')
def step_impl(context, title):
    task = context.task_manager.get_task_by_title(title)
    for row in context.table:
        context.task_manager.update_task(
            task.id,
            description=row['description'],
            due_date=row['due_date'],
            priority=row['priority']
        )

@when('I try to update a task "{title}"')
def step_impl(context, title):
    try:
        context.task_manager.update_task_by_title(title, description="New description")
        context.error = None
    except ValueError as e:
        context.error = str(e)

# Task Deletion Steps
@when('I delete the task "{title}"')
def step_impl(context, title):
    task = context.task_manager.get_task_by_title(title)
    context.task_manager.delete_task(task.id)

@then('the task "{title}" should be removed from my task list')
def step_impl(context, title):
    task = context.task_manager.get_task_by_title(title)
    assert task is None, f"Task '{title}' was not removed from the task list"

@when('I try to delete a task "{title}"')
def step_impl(context, title):
    try:
        task = context.task_manager.get_task_by_title(title)
        if task:
            context.task_manager.delete_task(task.id)
            context.error = None
        else:
            raise ValueError("Task not found")
    except ValueError as e:
        context.error = str(e)

@when('I delete all tasks')
def step_impl(context):
    context.task_manager.delete_all_tasks()

@then('my task list should be empty')
def step_impl(context):
    assert len(context.task_manager.get_all_tasks()) == 0, "Task list is not empty"

# Task Categorization Steps
@given('I have a task "{title}"')
def step_impl(context, title):
    context.task = context.task_manager.create_task(title)

@when('I add the category "{category}" to the task "{title}"')
def step_impl(context, category, title):
    task = context.task_manager.get_task_by_title(title)
    context.task_manager.add_category_to_task(task.id, category)

@then('the task "{title}" should have category "{category}"')
def step_impl(context, title, category):
    task = context.task_manager.get_task_by_title(title)
    assert task.category == category, f"Expected category '{category}', got '{task.category}'"

@given('I have the following tasks with categories')
def step_impl(context):
    for row in context.table:
        task = context.task_manager.create_task(row['title'])
        context.task_manager.add_category_to_task(task.id, row['category'])

@when('I filter tasks by category "{category}"')
def step_impl(context, category):
    context.tasks = context.task_manager.filter_tasks_by_category(category)

@then('the task list should contain "{title1}" and "{title2}"')
def step_impl(context, title1, title2):
    titles = [task.title for task in context.tasks]
    assert title1 in titles, f"Task '{title1}' not found in task list"
    assert title2 in titles, f"Task '{title2}' not found in task list"
    assert len(titles) == 2, f"Expected 2 tasks, got {len(titles)}"

@when('I add the tag "{tag}" to the task "{title}"')
def step_impl(context, tag, title):
    task = context.task_manager.get_task_by_title(title)
    context.task_manager.add_tag_to_task(task.id, tag)

@then('the task "{title}" should have tags "{tag1}" and "{tag2}"')
def step_impl(context, title, tag1, tag2):
    task = context.task_manager.get_task_by_title(title)
    assert tag1 in task.tags, f"Tag '{tag1}' not found in task tags"
    assert tag2 in task.tags, f"Tag '{tag2}' not found in task tags"