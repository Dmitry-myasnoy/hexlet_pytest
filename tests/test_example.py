from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert('') == ''

def test_reverse():
    # Чтение исходного текста
    with open('tests/fixtures/input_text.txt', 'r', encoding='utf8') as f:
        input_text = f.read().strip()

    # Чтение ожидаемого результата
    with open('tests/fixtures/expected_output.txt', 'r', encoding='utf8') as f:
        expected_output = f.read().strip()

    # Проверка работы функции reverse
    assert reverse(input_text) == expected_output
