def decode(data: bytes) -> str | int | list | dict:
    """
    Decode some bencoded data.

    Args:
        data: bencoded data

    Returns:
        Decoded data. Could be a str, int, list or dict depending on input.
    """
    decoded, _ = _decode(data)
    return decoded


def _decode(data: bytes) -> (any, bytes):
    # base:
    if len(data) == 0:
        return None, b""

    # handle ints
    if chr(data[0]) == "i":
        val = int(data.split(b"e")[0][1:])
        remaining = data.split(b"e", 1)[1]
        return val, remaining

    # handle strings
    if chr(data[0]).isdigit():
        length_str, remaining_after_length = data.split(b":", 1)
        length = int(length_str)
        val = remaining_after_length[:length]
        remaining = remaining_after_length[length:]
        return val, remaining

    # handle lists
    if chr(data[0]) == "l":
        return _decode_list(data, lst=[])

    if chr(data[0]) == "d":
        return _decode_dict(data, dct={})


def _decode_list(data: bytes, lst: list) -> (list, bytes):
    data = data[1:]

    while chr(data[0]) != "e":
        val, data = _decode(data)
        lst.append(val)
    return lst, data[1:]


def _decode_dict(data: bytes, dct: dict) -> (dict, bytes):
    data = data[1:]
    while chr(data[0]) != "e":
        key, data = _decode(data)
        value, data = _decode(data)
        dct[key.decode()] = value
    return dct, data[1:]
