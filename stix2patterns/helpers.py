import string


def leading_characters(s, length):
    """
    Returns non-whitespace leading characters

    :param str s: The string to process
    :param int length: The number of characters to return
    :return: The non-whitespace leading characters
    :rtype: str or None
    """
    if s is None:
        return None

    stripped = []
    for char in s:
        if char not in string.whitespace:
            stripped.append(char)

    upper_bound = min(length, len(stripped))
    return ''.join(stripped[:upper_bound])
