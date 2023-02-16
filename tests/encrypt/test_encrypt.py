import pytest
from challenges.challenge_encrypt_message import encrypt_message

INVALID_TYPE_MESSAGE = 8
INVALID_TYPE_KEY = "INVALID"
ODD_KEY = 2
EVEN_KEY = 3
MESSAGE = "PYETRA É LINDA"
RESPONSE_ODD = "ADNIL É ARTE_YP"
RESPONSE_EVEN = "EYP_ADNIL É ART"
RESPONSE_ZERO = "ADNIL É ARTEYP"


def test_encrypt_message():
    response = encrypt_message(MESSAGE, ODD_KEY)
    assert response == RESPONSE_ODD

    response = encrypt_message(MESSAGE, EVEN_KEY)
    assert response == RESPONSE_EVEN

    response = encrypt_message(MESSAGE, 0)
    assert response == RESPONSE_ZERO

    with pytest.raises(TypeError) as error:
        encrypt_message(INVALID_TYPE_MESSAGE, ODD_KEY)
        assert str(error.value) == "tipo inválido para message"

    with pytest.raises(TypeError) as error:
        encrypt_message(MESSAGE, INVALID_TYPE_KEY)
        assert str(error.value) == "tipo inválido para key"
