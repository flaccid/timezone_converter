#!/usr/bin/env python

import argparse
import os
import pytz
import json
from dateutil import parser
from time import strftime

# example usage:
# timezone_converter.py '2017-01-19T08:45:09.778Z' 'Australia/Sydney'

def convert_time(dts, tzs):
    """Converts an ISO 8601 datetime with the given timezone"""

    tzinfo = pytz.timezone(tzs)
    dt = parser.parse(dts)
    new_dt = dt.replace(tzinfo=pytz.utc).astimezone(tzinfo)
    datetime = new_dt.isoformat()
    date = new_dt.date().isoformat()
    time = new_dt.time().isoformat()
    locale_time = new_dt.strftime("%X")
    locale_day = new_dt.strftime("%A")

    converted = {
        'datetime': datetime,
        'date': date,
        'time': time,
        'locale_time': locale_time,
        'locale_day': locale_day
    }

    return converted

def lambda_handler(event, context):
    """AWS Lambda handler function."""

    params = {}
    keys = ['datetime', 'tz']

    for key in keys:
        if key in os.environ:
            params[key] = os.environ[key]
        elif event:
            if key in event:
                params[key] = event[key]
            elif 'params' in event:
                if 'querystring' in event['params']:
                    params[key] = event['params']['querystring'][key]

    tzs = params['tz']
    dts = params['datetime']

    return convert_time(dts, tzs)

def cli():
    """Entrypoint from CLI."""

    parser = argparse.ArgumentParser(
        description='Converts an ISO 8601 datetime with the given timezone.')
    parser.add_argument('datetime', nargs='+', help='the datetime')
    parser.add_argument('tz', nargs='+', help='the destination timezone')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--json', '-j', action='count',
                        help='output values in json format')
    parser.add_argument('--verbose', '-v', action='count')
    args = parser.parse_args()

    converted = convert_time(args.datetime[0], args.tz[0])

    if args.json:
        print(json.dumps(converted))
    else:
        if args.verbose:
            print("ISO 8601 datetime: {}".format(converted['datetime']))
            print("ISO 8601 date: {}".format(converted['date']))
            print("ISO 8601 time: {}".format(converted['time']))
            print("locale time: {}".format(converted['locale_time']))
            print("locale day: {}".format(converted['locale_day']))
        print(converted['datetime'])

if __name__ == "__main__":
    cli()
