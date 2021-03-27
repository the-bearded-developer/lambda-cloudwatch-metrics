import json
import logging
from datetime import datetime
import random

import boto3


def lambda_handler(event, context):
    logging.info(f'Event received {event}')

    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_data(
        Namespace='MyAwesomeProduct',
        MetricData=[{
            'MetricName': 'SomeMetricImInterestedIn',
            'Timestamp': datetime.now(),
            'Value': 1,
            'Unit': 'Count',
            'Dimensions': [{
                'Name': 'Action',
                'Value': 'SomethingHappened'
            }]
        }]
    )

    cloudwatch.put_metric_data(
        Namespace='MyAwesomeProduct',
        MetricData=[{
            'MetricName': 'SomeMetricImInterestedIn',
            'Timestamp': datetime.now(),
            'Value': random.randint(1, 100),
            'Unit': 'Seconds',
            'Dimensions': [{
                'Name': 'Domain',
                'Value': 'Client'
            }, {
                'Name': 'Type',
                'Value': 'Basic'
            }, {
                'Name': 'Foo',
                'Value': 'Bar'
            }]
        }]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Metrics sent successfully!')
    }
