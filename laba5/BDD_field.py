from functions.field import field
from pytest_bdd import scenario, given, when, then

@scenario('features\\field_1.feature','get goods` fields_1')
def test_1():
    pass

@scenario('features\\field_2.feature','get goods` fields_2')
def test_2():
    pass

@given('goods_1, *args_1', target_fixture='data_1')
def goods():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    args = ['title']
    data_1 = [goods, args]
    return data_1

@given('goods_2, *args_2', target_fixture='data_2')
def goods():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    args = ['title', 'price']
    data_2 = [goods, args]
    return data_2

@when('processing_1', target_fixture='answer_1')
def processing(data_1):
    return field(data_1[0], *data_1[1])

@when('processing_2', target_fixture='answer_2')
def processing(data_2):
    return field(data_2[0], *data_2[1])

@then('answer_1 got')
def check_answer(answer_1):
    assert answer_1 == ['Ковер', 'Диван для отдыха']

@then('answer_2 got')
def check_answer(answer_2):
    assert answer_2 == [
        {'title': 'Ковер', 'price': 2000},
        {'title': 'Диван для отдыха', 'price': 5300}
    ]