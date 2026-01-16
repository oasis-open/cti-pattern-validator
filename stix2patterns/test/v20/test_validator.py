"""
Test cases for stix2patterns/validator.py.
"""
import os

import pytest

from stix2patterns.validator import validate

TEST_CASE_FILE = os.path.join(os.path.dirname(__file__), 'spec_examples.txt')
with open(TEST_CASE_FILE) as f:
    SPEC_CASES = [x.strip() for x in f.readlines()]


@pytest.mark.parametrize("test_input", SPEC_CASES)
def test_spec_patterns(test_input):
    """
    Validate patterns from STIX 2.0 Patterning spec.
    """
    pass_test = validate(test_input, stix_version='2.0', print_errs=True)
    assert pass_test is True


FAIL_CASES = [
    ("file:size = 1280",  # Does not use square brackets
        "FAIL: Error found at line 1:0. input is missing square brackets"),
    ("[file:size = ]",  # Missing value
        "FAIL: Error found at line 1:13. mismatched input ']'"),
    ("[file:hashes.MD5 = cead3f77f6cda6ec00f57d76c9a6879f]",  # No quotes around string
        "FAIL: Error found at line 1:19. mismatched input 'cead3f77f6cda6ec00f57d76c9a6879f'"),
    ("[file.size = 1280]",  # Use period instead of colon
        "FAIL: Error found at line 1:5. no viable alternative at input 'file.'"),
    ("[file:name MATCHES /.*\\.dll/]",  # Quotes around regular expression
        "FAIL: Error found at line 1:19. mismatched input '/' expecting StringLiteral"),
    ("[win-registry-key:key = 'hkey_local_machine\\\\foo\\\\bar'] WITHIN ]",  # Missing Qualifier value
        "FAIL: Error found at line 1:63. mismatched input ']' expecting {IntPosLiteral, FloatPosLiteral}"),
    ("[win-registry-key:key = 'hkey_local_machine\\\\foo\\\\bar'] WITHIN 5 HOURS]",  # SECONDS is the only valid time unit
        "FAIL: Error found at line 1:65. mismatched input 'HOURS' expecting 'SECONDS'"),
    ("[win-registry-key:key = 'hkey_local_machine\\\\foo\\\\bar'] WITHIN -5 SECONDS]",  # Negative integer is invalid
        "FAIL: Error found at line 1:63. mismatched input '-5' expecting {IntPosLiteral, FloatPosLiteral}"),
    ("[network-traffic:dst_ref.value ISSUBSET ]",  # Missing second Comparison operand
        "FAIL: Error found at line 1:40. missing StringLiteral at ']'"),
    ("[file:hashes.MD5 =? 'cead3f77f6cda6ec00f57d76c9a6879f']",  # '=?' isn't a valid operator
        "FAIL: Error found at line 1:18. extraneous input '?'"),
    ("[x_whatever:detected == t'2457-73-22T32:81:84.1Z']",  # Not a valid date
        "FAIL: Error found at line 1:24. extraneous input 't'"),
    ("[artifact:payload_bin = b'====']",  # Not valid Base64
        "FAIL: Error found at line 1:24. extraneous input 'b'"),
    ("[foo:bar=1] within 2 seconds",  # keywords must be uppercase
        "FAIL: Error found at line 1:12. mismatched input 'within' expecting <EOF>"),
    ("[file:hashes.'SHA-256' = 'f00']",  # Malformed hash value
        "FAIL: 'f00' is not a valid SHA-256 hash"),
    # TODO: add more failing test cases.
]


@pytest.mark.parametrize("test_input,test_output", FAIL_CASES)
def test_fail_patterns(test_input, test_output):
    """
    Validate that patterns fail as expected.
    """
    pass_test, errors = validate(test_input, stix_version='2.0', ret_errs=True, print_errs=True)
    assert errors[0].startswith(test_output)
    assert pass_test is False


TIMESTAMP_PASS_CASES = [
    # Basic valid timestamps
    "[x:created = t'2024-01-15T12:30:45Z']",
    "[x:created = t'2024-12-31T23:59:59Z']",
    "[x:created = t'2024-01-01T00:00:00Z']",
    # Millisecond precision
    "[x:created = t'2024-01-15T12:30:45.123Z']",
    "[x:created = t'2024-01-15T12:30:45.123456Z']",
    # Leap year Feb 29
    "[x:created = t'2024-02-29T12:00:00Z']",  # 2024 is a leap year
    "[x:created = t'2000-02-29T12:00:00Z']",  # 2000 is a leap year (divisible by 400)
    # START/STOP qualifiers with timestamps
    "[file:name = 'test'] START t'2024-01-01T00:00:00Z' STOP t'2024-12-31T23:59:59Z'",
    # Note: The grammar validates timestamp SYNTAX but not SEMANTIC correctness.
    # These are syntactically valid (day 01-31, month 01-12) but semantically invalid dates.
    # Calendar validation (e.g., Feb has 28/29 days) is not performed by the parser.
    "[x:created = t'2024-02-30T12:00:00Z']",  # Feb 30 - syntactically valid
    "[x:created = t'2024-04-31T12:00:00Z']",  # Apr 31 - syntactically valid
    "[x:created = t'2023-02-29T12:00:00Z']",  # Non-leap year Feb 29 - syntactically valid
]

TIMESTAMP_FAIL_CASES = [
    # Invalid month (must be 01-12)
    ("[x:created = t'2024-13-01T12:00:00Z']",
        "FAIL: Error found at line 1:"),
    ("[x:created = t'2024-00-01T12:00:00Z']",
        "FAIL: Error found at line 1:"),
    # Invalid day (must be 01-31)
    ("[x:created = t'2024-01-32T12:00:00Z']",
        "FAIL: Error found at line 1:"),
    ("[x:created = t'2024-01-00T12:00:00Z']",
        "FAIL: Error found at line 1:"),
    # Invalid hour (must be 00-23)
    ("[x:created = t'2024-01-15T25:00:00Z']",
        "FAIL: Error found at line 1:"),
    # Invalid minute (must be 00-59)
    ("[x:created = t'2024-01-15T12:60:00Z']",
        "FAIL: Error found at line 1:"),
    # Invalid second (must be 00-59)
    ("[x:created = t'2024-01-15T12:30:61Z']",
        "FAIL: Error found at line 1:"),
    # Missing timezone designator
    ("[x:created = t'2024-01-15T12:30:45']",
        "FAIL: Error found at line 1:"),
    # Malformed timestamp format
    ("[x:created = t'not-a-timestamp']",
        "FAIL: Error found at line 1:"),
    ("[x:created = t'2024/01/15T12:30:45Z']",
        "FAIL: Error found at line 1:"),
]

PASS_CASES = [
    "[file:size = 1280]",
    "[file:size != 1280]",
    "[file:size < 1024]",
    "[file:size <= 1024]",
    "[file:size > 1024]",
    "[file:size >= 1024]",
    "[file:file_name = 'my_file_name']",
    "[file:extended_properties.'ntfs-ext'.sid = '234']",
    r"[emailaddr:value MATCHES '.+\\@ibm\\.com$' OR file:name MATCHES '^Final Report.+\\.exe$']",
    "[ipv4addr:value ISSUBSET '192.168.0.1/24']",
    "[ipv4addr:value NOT ISSUBSET '192.168.0.1/24']",
    "[user-account:value = 'Peter'] AND [user-account:value != 'Paul'] AND [user-account:value = 'Mary'] WITHIN 5 SECONDS",
    "[file:file_system_properties.file_name LIKE 'name%']",
    "[file:file_name IN ('test.txt', 'test2.exe', 'README')]",
    "[file:size IN (1024, 2048, 4096)]",
    "[network-connection:extended_properties[0].source_payload MATCHES 'dGVzdHRlc3R0ZXN0']",
    "[win-registry-key:key = 'hkey_local_machine\\\\foo\\\\bar'] WITHIN 5 SECONDS",
    "[x_whatever:detected == t'2018-03-22T12:11:14.1Z']",
    "[artifact:payload_bin = b'dGhpcyBpcyBhIHRlc3Q=']",
    "[foo:bar=1] REPEATS 9 TIMES",
    "[network-traffic:start = '2018-04-20T12:36:24.558Z']",
    "( [(network-traffic:dst_port IN(443,6443,8443) AND network-traffic:src_packets != 0) ])",  # Misplaced whitespace
    "[file:hashes[*] = '8665c8d477534008b3058b72e2dae8ae']",
]


@pytest.mark.parametrize("test_input", PASS_CASES)
def test_pass_patterns(test_input):
    """
    Validate that patterns pass as expected.
    """
    pass_test = validate(test_input, stix_version='2.0', print_errs=True)
    assert pass_test is True


@pytest.mark.parametrize("test_input", TIMESTAMP_PASS_CASES)
def test_timestamp_pass_patterns(test_input):
    """
    Validate that valid timestamp patterns pass.
    """
    pass_test = validate(test_input, stix_version='2.0', print_errs=True)
    assert pass_test is True


@pytest.mark.parametrize("test_input,test_output", TIMESTAMP_FAIL_CASES)
def test_timestamp_fail_patterns(test_input, test_output):
    """
    Validate that invalid timestamp patterns fail.
    """
    pass_test, errors = validate(test_input, stix_version='2.0', ret_errs=True, print_errs=True)
    assert errors[0].startswith(test_output)
    assert pass_test is False
