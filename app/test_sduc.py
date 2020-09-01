import sduc


def test_format():
    element1 = sduc.Element("E1", "/")
    for resutl, size in [
        ("0 B", 0),
        ("1 B", 1),
        ("1023 B", 2 ** 10 - 1),
        ("1.0 kB", 2 ** 10),
        ("1023.0 kB", 2 ** 20 - 2 ** 10),
        ("1.0 MB", 2 ** 20),
        ("1023.0 MB", 2 ** 30 - 2 ** 20),
        ("1.0 GB", 2 ** 30),
    ]:
        element1.size = size
        assert str(element1) == "E1 " + resutl
