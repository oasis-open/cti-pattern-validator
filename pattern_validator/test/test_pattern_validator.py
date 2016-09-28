# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms

'''
Test cases for pattern_validator.py.
'''

import pytest
from pattern_validator.pattern_validator import validate

###############################################################################
# TEST CASES FROM CYBOX 3.0 SPEC
###############################################################################

# NOTE: Added quotes around reg expressions - different from spec. Also changed
# all single quotes to fit correct UNICODE character (U+0027).
SPEC_CASES = ["file-object:hashes.sha-256 = "
              "'aec070645fe53ee3b3763059376134f0"
              "58cc337247c978add178b6ccdfb0019f'",
              "'192.168.0.1/24' CONTAINS ipv4addr-object:value",
              "emailaddr-object:value MATCHES /.+\@ibm\.com$/ AND "
              "file-object:name MATCHES /^Final Report.+\.exe$/",
              "file-object:hashes.sha256 = "
              "'aec070645fe53ee3b3763059376134f"
              "058cc337247c978add178b6ccdfb0019f'"
              "AND file-object:mime_type = 'application/x-pdf'",
              "file-object:hashes.sha-256 = "
              "'bf07a7fbb825fc0aae7bf4a1177b2b3"
              "1fcf8a3feeaf7092761e18c859ee52a9c' "
              "ALONGWITH file-object:hashes.sha-256 = "
              "'aec070645fe53ee3b3763059376134f0"
              "58cc337247c978add178b6ccdfb0019f'",
              "file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4' "
              "FOLLOWEDBY win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 MINUTES",
              "Artifact:log = 'Login failed.' REPEATED 5 TIMES START "
              "'2016-01-20T12:31:12.12345Z' STOP '2016-01-20T12:31:12.12345Z'",
              "( user-account-object:value = 'Peter' ALONGWITH "
              "user-account-object:value = 'Paul' ALONGWITH "
              "user-account-object:value = 'Mary' ) WITHIN 5 MINUTES",
              "artifact-object:mime-type = 'application/vnd.tcpdump.pcap' "
              "AND artifact-object:payload MATCHES /Zm9vYmFy/",
              "network-connection-object:extended_properties"
              "['flow-extension'].source_payload MATCHES /dGVzdHRlc3R0ZXN0/",
              # The original in the spec is missing the first AND
              "file-object:file_system_properties.file_path.delimiter = '\\' "
              "AND file-object:file_system_properties.file_path.components[0] "
              "= 'C:' AND file-object:file_system_properties.file_path."
              "components[1] = 'Windows' AND file-object:"
              "file_system_properties.file_path.components[2] = 'System32' "
              "AND file-object:file_system_properties.file_name = 'foo.dll'"]


@pytest.mark.parametrize("test_input", SPEC_CASES)
def test_spec_patterns(test_input):
    '''
    Validate patterns from CybOX 3.0 spec.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is True


###############################################################################
# TEST CASES EXPECTED TO FAIL
###############################################################################
FAIL_CASES = ["file-object:hashes.sha-256 = "
              "aec070645fe53ee3b3763059376134f0"
              "58cc337247c978add178b6ccdfb0019f",
              "file-object.size = 1280",
              "network-connection-object:extended_properties"
              "['flow-extension']:source_payload MATCHES '['",
              "file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4' "
              "FOLLOWED BY win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar'",
              "( user-account-object:value = 'Peter' ALONGWITH "
              "(user-account-object:value = 'Paul') NOT ALONGWITH "
              "user-account-object:value = 'Mary' ) WITHIN 5 MINUTES",
              "file-object:name MATCHES /href=\'(.*)\'",
              "network-connection-object:extended_properties[-1]"
              ".source_payload MATCHES /dGVzdHRlc3R0ZXN0/"]


@pytest.mark.parametrize("test_input", FAIL_CASES)
def test_fail_patterns(test_input):
    '''
    Validate that patterns fail as expected.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is False


###############################################################################
# TEST CASES EXPECTED TO PASS
###############################################################################
PASS_CASES = ["file-object:size = 1280",
              "file-object:size != 1280",
              "file-object:file_system_properties.file_name = 'my_file_name'",
              "file-object:extended_properties['metadata'].magic_number = 234",
              "emailaddr-object:value MATCHES /.+\@ibm\.com$/ OR "
              "file-object:name MATCHES /^Final Report.+\.exe$/",
              "NOT '192.168.0.1/24' CONTAINS ipv4addr-object:value",
              "ipv4addr-object:value CONTAINS '192.168.0.1/24'",
              "( user-account-object:value = 'Peter' ALONGWITH "
              "NOT (user-account-object:value = 'Paul') ALONGWITH "
              "user-account-object:value = 'Mary' ) WITHIN 5 MINUTES",
              "file-object:size < file-object:size1",
              "file-object:size <= file-object:size1",
              "file-object:size > file-object:size1",
              "file-object:size >= file-object:size1",
              "NOT file-object:size >= file-object:size1",
              "file-object:file_system_properties.file_name LIKE 'name%'",
              "'stringvalue' IN ('str1', file-object:size, 'str3')",
              "file-object:size IN ('str1', file-object2:size, 'str3')",
              "network-connection-object:extended_properties[0]"
              ".source_payload MATCHES /dGVzdHRlc3R0ZXN0/",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 MILLISECONDS",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 SECONDS",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 HOURS",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 DAYS",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 MONTHS",
              "win-registry-key-object:key = "
              "'hkey_local_machine\\foo\\bar' WITHIN 5 YEARS"]


@pytest.mark.parametrize("test_input", PASS_CASES)
def test_pass_patterns(test_input):
    '''
    Validate that patterns pass as expected.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is True
