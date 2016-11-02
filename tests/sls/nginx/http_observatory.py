"""
test the http observatory headers
"""
import urllib.request

from httpobs.scanner.local import scan

from tests.util import Failure, Success


def run():
    scan_result = scan('localhost')
    if scan_result['scan']['score'] <= 65:
        return Failure('The http observatory score is less than 65',
                "Score: {0[score]}, "
                "Grade: {0[grade]}".format(scan_result['scan']))
    else:
        return Success('The http observatory score is not less than 65')
