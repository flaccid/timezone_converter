# timezone_converter

Converts an ISO 8601 datetime with the given timezone.

## Usage

### Python

```
>>> import timezone_converter
>>> dts = '2017-01-19T08:45:09.778Z'
>>> tzs = 'America/Los_Angeles'
>>> timezone_converter.convert_time(dts, tzs)
{'date': '2017-01-19', 'locale_time': '00:45:09', 'time': '00:45:09.778000', 'locale_day': 'Thursday', 'datetime': '2017-01-19T00:45:09.778000-08:00'}
```

### Command Line

See `timezone_converter.py --help`

### AWS Lambda

 1. Create the zip file using `make zip`
 2. Upload the code to AWS Lambda using the zip file
 3. Set the configuration to use `timezone_converter.lambda_handler` as the handler of the function.

License and Authors
-------------------
- Author: Chris Fordham (<chris@fordham-nagy.id.au>)

```text
Copyright 2017, Chris Fordham

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
