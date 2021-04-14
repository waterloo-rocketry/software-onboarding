import sandbox as sb


def test_add_one():
    val = 10
    assert sb.add_one(val) == 11

def test_add_two():
    val = 1
    assert sb.add_two(val) == 3

def test_add_exclamation():
	string = "sandbox"
	assert sb.add_exclamation(string) == "sandbox!"