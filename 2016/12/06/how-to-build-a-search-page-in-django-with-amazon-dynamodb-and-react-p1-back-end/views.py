from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

# dynamodb configuration
dynamodb = boto3.resource(
  'dynamodb',
  aws_access_key_id='put_your_aws_access_key_here',
  aws_secret_access_key='put_your_aws_secret_access_key_here',
  region_name='puy_your_amazon_dynamodb_region_here')

# http://127.0.0.1:8000/search
# http://127.0.0.1:8000/search/
def search(request):
  template = loader.get_template('search.html')
  params = retrieve_all_get_parameters(request)
  billionaires = get_list_of_billionaires(params)
  context = {
    'billionaires' : billionaires
  }

  return HttpResponse(template.render(context, request))

def get_list_of_billionaires(param):
  filter_expression = []
  expression_attribute_names = {}
  expression_attribute_values = {}

  try:
    net_worth_under = param['net_worth_under']
    filter_expression.append('(#net_worth <= :net_worth_under)')
    expression_attribute_names['#net_worth'] = 'net_worth'
    expression_attribute_values[':net_worth_under'] = net_worth_under
  except KeyError:
    pass
  try:
    current_residence = param['current_residence']
    filter_expression.append('(#l = :current_residence)')
    expression_attribute_names['#l'] = 'current_location'
    expression_attribute_values[':current_residence'] = current_residence
  except KeyError:
    pass
  try:
    table = dynamodb.Table('put_your_amazon_dynamodb_table_name_here')
  except botocore.exceptions.ClientError as e:
    # http://stackoverflow.com/questions/33068055/boto3-python-and-how-to-handle-errors
    return 'failed'
  else:
    filtered_string = filter_expression_to_string(filter_expression)
    if filtered_string != '' and expression_attribute_names and expression_attribute_values:
      response = table.scan(
        FilterExpression = filtered_string,
        ExpressionAttributeNames = expression_attribute_names,
        ExpressionAttributeValues = expression_attribute_values,
      )
    else:
      response = table.scan(
        ReturnConsumedCapacity = 'TOTAL',
      )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      try:
        item = response['Item']
      except KeyError:
        return None
      return item

def retrieve_all_get_parameters(request):
  param = {}
  net_worth_under = request.GET.get('net_worth_under')
  current_residence = request.GET.get('current_residence')

  if net_worth_under != None and net_worth_under != '':
    param['net_worth_under'] = net_worth_under
  if current_residence != None and current_residence != '':
    param['current_residence'] = current_residence

  return param

def filter_expression_to_string(filter_expression):
  if not filter_expression:
    return ''
  length_of_filter_expression = len(filter_expression)
  filter_expression_to_string = ''
  for x in range(length_of_filter_expression):
    filter_expression_to_string += filter_expression[x]
    if x + 1 != length_of_filter_expression:
      filter_expression_to_string += ' and '
  return filter_expression_to_string