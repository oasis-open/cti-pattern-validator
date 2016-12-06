'''
Test cases for stix2patterns/validator.py.
'''

import pytest

from stix2patterns.validator import validate

###############################################################################
# EXAMPLES FROM PATTERNING SPEC
###############################################################################

SPEC_CASES = [
    "[file:hashes.SHA-256 = 'aec070645fe53ee3b3763059376134f058cc337247c978add178b6ccdfb0019f']",
    "[ipv4-addr:value = '192.168.0.1/24']",
    "[email-message:from_ref.value MATCHES /.+\@ibm\.com$/ AND email-message:body_multipart[*].body_raw_ref.file_name MATCHES /^Final Report.+\.exe$/]",
    "[file:hashes.SHA-256 = 'aec070645fe53ee3b3763059376134f058cc337247c978add178b6ccdfb0019f' AND file:mime_type = 'application/x-pdf']",
    ("[file:hashes.SHA-256 = 'bf07a7fbb825fc0aae7bf4a1177b2b31fcf8a3feeaf7092761e18c859ee52a9c' OR "
        "file:hashes.MD5 = 'cead3f77f6cda6ec00f57d76c9a6879f'] ALONGWITH "
        "[file:hashes.SHA-256 = 'aec070645fe53ee3b3763059376134f058cc337247c978add178b6ccdfb0019f']"),
    "[file:hashes.MD5 = '79054025255fb1a26e4bc422aef54eb4'] FOLLOWEDBY [win-registry-key:key = 'HKEY_LOCAL_MACHINE\\foo\\bar'] WITHIN 300 SECONDS",
    ("[user-account:account_type = 'unix' AND user-account:user_id = '1007' AND user-account:account_login = 'Peter'] ALONGWITH "
        "[user-account:account_type = 'unix' AND user-account:user_id = '1008' AND user-account:user_id = 'Paul'] ALONGWITH "
        "[user-account:account_type = 'unix' AND user-account:user_id = '1009' AND user-account:user_id = 'Mary']"),
    "[artifact:mime_type = 'application/vnd.tcpdump.pcap' AND artifact:payload_bin MATCHES /d4c3b2a102000400/]",
    "[network-traffic:src_payload_ref.payload_bin MATCHES /0026160000d200/]",
    "[file:file_name = 'foo.dll' AND file:parent_directory_ref.path = 'C:\Windows\System32']",
    "[file:extended_properties.windows-pebinary-ext.sections[*].entropy > 7.0]",
    "[file:mime_type = 'image/bmp' AND file:magic_number_hex = 'ffd8']",
    "[network-traffic:dst_ref.type = 'ipv4-addr' AND network-traffic:dst_ref.value = '192.168.1.1']",
    "[network-traffic:dst_ref.type = 'domain-name' AND network-traffic:dst_ref.value = 'foo.com'] REPEATED 5 TIMES WITHIN 30 MINUTES",
    "[domain-name:value = 'www.5z8.info' OR domain-name:resolves_to_refs[*].value = '184.22.62.34']",
    "[url:value = 'beg.rocklandgrad.com/forum/wm/keys/WFolw' OR url:value = 'beg.rocklandgrad.com/forum/wm/keys/7T8INre2']",
    "[x509-certificate:issuer = 'CN=WEBMAIL' AND x509-certificate:serial_number = '4c:0b:1d:19:74:86:a7:66:b4:1a:bf:40:27:21:76:28']",
    ("[windows-registry-key:key = 'HKEY_CURRENT_USER\Software\CryptoLocker\Files' OR "
        "windows-registry-key:key = 'HKEY_CURRENT_USER\Software\Microsoft\CurrentVersion\Run\CryptoLocker_0388']"),
    "[(file:file_name = 'pdf.exe' OR file:size = '371712') AND file:created = '2014-01-13T07:03:17Z']",
    "[email-message:sender_ref.value = 'invite@aeroconf2014.org' AND email-message:subject = 'IEEE Aerospace Conference 2014']",
    "[x-usb-device:usbdrive.serial_number = '575833314133343231313937']",
    ("[process:arguments = '>-add GlobalSign.cer -c -s -r localMachine Root'] FOLLOWEDBY "
        "[process:arguments = '>-add GlobalSign.cer -c -s -r localMachineTrustedPublisher'] WITHIN 5 MINUTES"),
    "[x-interface:network CONTAINS '192.168.5.10']",
]


@pytest.mark.parametrize("test_input", SPEC_CASES)
def test_spec_patterns(test_input):
    '''
    Validate patterns from STIX 2.0 Patterning spec.
    '''
    pass_test = validate(test_input, print_errs=True)
    assert pass_test is True


###############################################################################
# TEST CASES EXPECTED TO FAIL
###############################################################################
FAIL_CASES = [
    "file:size = 1280",  # Does not use square brackets
    "[file:hashes.MD5 = cead3f77f6cda6ec00f57d76c9a6879f]"  # No quotes around string
    "[file.size = 1280]",  # Use period instead of colon
    "[file:name MATCHES '/.*\\.dll/'",  # Quotes around regular expression
    # TODO: add more failing test cases.
]


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
PASS_CASES = [
    "[file:size = 1280]",
    "[file:size != 1280]",
    "[file:size < 1024]",
    "[file:size <= 1024]",
    "[file:size > 1024]",
    "[file:size >= 1024]",
    "[file:file_name = 'my_file_name']",
    "[file:extended_properties.ntfs-ext.sid = '234']",
    "[emailaddr:value MATCHES /.+\@ibm\.com$/ OR file:name MATCHES /^Final Report.+\.exe$/]",
    "[ipv4addr:value INSUBNET '192.168.0.1/24']",
    "[ipv4addr:value NOT INSUBNET '192.168.0.1/24']",
    "[user-account:value = 'Peter'] ALONGWITH [user-account:value != 'Paul'] ALONGWITH [user-account:value = 'Mary'] WITHIN 5 MINUTES",
    "[file:file_system_properties.file_name LIKE 'name%']",
    "[file:file_name IN ('test.txt', 'test2.exe', 'README')]",
    "[file:size IN (1024, 2048, 4096)]",
    "[network-connection:extended_properties[0].source_payload MATCHES /dGVzdHRlc3R0ZXN0/]",
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
