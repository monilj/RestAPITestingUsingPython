from behave import *


@given('the Book details which needs to be added to Library')
def step_given(context):
    pass


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute the AddBook PostAPI method')


@then(u'book is successfully added')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then book is successfully added')

