'''
Test cases for stix2patterns/validator.py.
'''
import os

import pytest

from stix2patterns.validator import validate

TEST_CASE_FILE = os.path.join(os.path.dirname(__file__), 'spec_examples.txt')
with open(TEST_CASE_FILE) as f:
    SPEC_CASES = [x.strip() for x in f.readlines()]


@pytest.mark.parametrize("test_input", SPEC_CASES)
def test_spec_patterns(test_input):
    '''
    Validate patterns from STIX 2.0 Patterning spec.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is True


FAIL_CASES = [
    "file:size = 1280",  # Does not use square brackets
    "[file:hashes.MD5 = cead3f77f6cda6ec00f57d76c9a6879f]"  # No quotes around string
    "[file.size = 1280]",  # Use period instead of colon
    "[file:name MATCHES /.*\\.dll/]",  # Quotes around regular expression
    # TODO: add more failing test cases.
]


@pytest.mark.parametrize("test_input", FAIL_CASES)
def test_fail_patterns(test_input):
    '''
    Validate that patterns fail as expected.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is False


PASS_CASES = [
    "[file:size = 1280]",
    "[file:size != 1280]",
    "[file:size < 1024]",
    "[file:size <= 1024]",
    "[file:size > 1024]",
    "[file:size >= 1024]",
    "[file:file_name = 'my_file_name']",
    "[file:extended_properties.ntfs-ext.sid = '234']",
    "[emailaddr:value MATCHES '.+\@ibm\.com$' OR file:name MATCHES '^Final Report.+\.exe$']",
    "[ipv4addr:value ISSUBSET '192.168.0.1/24']",
    "[ipv4addr:value NOT ISSUBSET '192.168.0.1/24']",
    "[user-account:value = 'Peter'] AND [user-account:value != 'Paul'] AND [user-account:value = 'Mary'] WITHIN 5 MINUTES",
    "[file:file_system_properties.file_name LIKE 'name%']",
    "[file:file_name IN ('test.txt', 'test2.exe', 'README')]",
    "[file:size IN (1024, 2048, 4096)]",
    "[network-connection:extended_properties[0].source_payload MATCHES 'dGVzdHRlc3R0ZXN0']",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 MILLISECONDS",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 SECONDS",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 HOURS",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 DAYS",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 MONTHS",
    "[win-registry-key:key = 'hkey_local_machine\\foo\\bar'] WITHIN 5 YEARS"
]


@pytest.mark.parametrize("test_input", PASS_CASES)
def test_pass_patterns(test_input):
    '''
    Validate that patterns pass as expected.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is True
