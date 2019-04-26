import re

HASHES_REGEX = {
    "MD5": (r"^[a-fA-F0-9]{32}$", "MD5"),
    "MD6": (r"^[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{56}|[a-fA-F0-9]{64}|[a-fA-F0-9]{96}|[a-fA-F0-9]{128}$", "MD6"),
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

    """ extract hash type and string in order to verify them """
    pattern = str(pattern).strip(']').strip('[')
    try:
        hash_search = re.findall(r':(.*?)\.', pattern)[0]
    except:
        hash_search = None
    if hash_search == 'hashes':
        hash_type = pattern[12:].split('\'')[1]
        hash_type = hash_type.upper().replace('-', '')
        hash_string = pattern.split('=')[1].strip().strip('\'')
            
        if hash_type in HASHES_REGEX:
            print "here"
            if not re.match(HASHES_REGEX[hash_type][0], hash_string):
                return "FAIL: '{0}' is not a valid {1} hash".format(hash_string, 
                hash_type)
        else:
            return "FAIL: '{0}' is not a valid hash type".format(hash_type)

