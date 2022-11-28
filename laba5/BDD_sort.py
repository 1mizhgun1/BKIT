from functions.sort import my_sort_with_lambda, my_sort_without_lambda
from pytest_bdd import scenario, given, when, then

@scenario('features\\my_sort_with_lambda.feature','sorting by ABS with lambda')
def testing_my_sort_with_lambda():
    pass

@scenario('features\\my_sort_without_lambda.feature','sorting by ABS without lambda')
def testing_my_sort_without_lambda():
    pass

@given('data', target_fixture='data')
def data():
    return [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

@when('sorting data: my_sort_with_lambda', target_fixture='answer')
def sort_with_lambda(data):
    return my_sort_with_lambda(data)

@when('sorting data: my_sort_without_lambda', target_fixture='answer')
def sort_without_lambda(data):
    return my_sort_without_lambda(data)

@then('data was sorted')
def check_answer(answer):
    assert answer == [0, 1, -1, 4, -4, -30, 30, 100, -100, 123]
