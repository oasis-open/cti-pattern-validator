import re

HASHES_REGEX = {
    "MD5": (r"^[a-fA-F0-9]{32}$", "MD5"),
    "MD6": (r"^[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{56}|\
    [a-fA-F0-9]{64}|[a-fA-F0-9]{96}|[a-fA-F0-9]{128}$", "MD6"),
    "RIPEMD160": (r"^[a-fA-F0-9]{40}$", "RIPEMD-160"),
    "SHA1": (r"^[a-fA-F0-9]{40}$", "SHA-1"),
    "SHA224": (r"^[a-fA-F0-9]{56}$", "SHA-224"),
    "SHA256": (r"^[a-fA-F0-9]{64}$", "SHA-256"),
    "SHA384": (r"^[a-fA-F0-9]{96}$", "SHA-384"),
    "SHA512": (r"^[a-fA-F0-9]{128}$", "SHA-512"),
    "SHA3224": (r"^[a-fA-F0-9]{56}$", "SHA3-224"),
    "SHA3256": (r"^[a-fA-F0-9]{64}$", "SHA3-256"),
    "SHA3384": (r"^[a-fA-F0-9]{96}$", "SHA3-384"),
    "SHA3512": (r"^[a-fA-F0-9]{128}$", "SHA3-512"),
    "SSDEEP": (r"^[a-zA-Z0-9/+:.]{1,128}$", "ssdeep"),
    "WHIRLPOOL": (r"^[a-fA-F0-9]{128}$", "WHIRLPOOL"),
}


def verify_object(pattern):
    """ Verifies obervation expression against regex for correct syntax """

    pattern = str(pattern).replace(']', '').replace('[', '')

    # Split list by possible Obervation Operators
    pattern_list = re.split(" AND | FOLLOWEDBY | OR ", pattern)
    error_list = []
    for observation in pattern_list:
        try:
            hash_search = re.findall(r':(.*?)\.', observation)[0]
        except Exception:
            hash_search = None
        if hash_search == 'hashes':
            try:
                hash_type = re.findall(r'\.(.+?)\s', observation)[0].\
                    replace("\'", "").replace("\'", "")
            except Exception:
                return
            hash_type = hash_type.upper().replace('-', '')
            hash_string = observation.split('=')[1].strip().strip('\'')
            if hash_type in HASHES_REGEX:
                if not re.match(HASHES_REGEX[hash_type][0], hash_string):
                    error_list.append("FAIL: '{0}' is not a valid {1} hash".
                                      format(hash_string, hash_type))
            else:
                error_list.append("FAIL: '{0}' is not a valid hash type"
                                  .format(hash_type))
    return error_list
