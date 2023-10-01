''' Step definition for check_once.feature'''
# pylint: disable=consider-using-f-string
import re
import json
from behave import step, then
from settings import API_URL, log


json_headers = {
    'Accept-Charset': 'UTF-8',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36, QA Tests'
}


@step('I "{method}" "{uri}" with requests')
def get(context, method, uri):
    context.current_url = API_URL + uri
    if method == "GET":
        log.debug('Getting this url with requests %s', context.current_url)
        context.response = context.session.get(
            context.current_url,
            headers=json_headers
        )


@step('I "{method}" "{uri}" with the parameters "{parameters}"')
def get(context, method, uri, parameters):
    context.current_url = API_URL + uri + parameters
    if method == "GET":
        log.debug('Getting this url with requests %s', context.current_url)
        context.response = context.session.get(
            context.current_url,
            headers=json_headers
        )


@then('the json response should be a list of least "{int:d}" items')
def get(context, int):
    data = context.response.json()
    assert len(data) >= int, 'List was {result} items, expected greater than {expected}'.format(
        result=len(data),
        expected=int
    )


@then('the json response should contain a dog named "{name}"')
def get(context, name):
    data = context.response.json()
    import pdb; pdb.set_trace
    assert any(dog['name'] == name for dog in data), 'Did not find a dog named {}'.format(name)


@then('the json response should not contain a dog named "{name}"')
def get(context, name):
    data = context.response.json()
    for dog in data:
        try:
            assert not dog['name'] == name, 'Unexpectedly found a dog named {}'.format(name)
        except KeyError:
            continue


@then('all dogs should have a name')
def get(context):
    data = context.response.json()
    assert all('name' in dog for dog in data), 'A dog was missing the name key'


@then('all dogs should have an ID')
def get(context):
    data = context.response.json()
    assert all('id' in dog for dog in data), 'A dog was missing ID data'


@then('all dogs should have a status')
def get(context):
    data = context.response.json()
    assert all('status' in dog for dog in data), 'A dog was missing status data'


@then('should not reveal dog pii')
def get(context):
    data = context.response.json()
    assert not any('dob' in dog for dog in data), 'Data should not include a dogs Personal Identifiable Information'