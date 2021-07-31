import requests
from behave import *
from API_Automation_Using_Python.PayLoad import *
from util.configurations import *
from util.resources import *


@given('the Book details which needs to be added to Library')
def step_given(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad("manfdfppt", "433")


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then(u'book is successfully added')
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad(isbn, aisle);


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('rahulshettyacademy', 'password')


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
