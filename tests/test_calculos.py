from teste_ie.calculos import soma, subtracao, multiplicacao, divisao


def test_soma():
    a = 1
    b = 2
    res = 3

    assert soma(a,b) == res


def test_subtracao():
    a = 1
    b = 2
    res = 1

    assert subtracao(a,b) == res


def test_multiplicacao():
    a = 2
    b = 2
    res = 4

    assert multiplicacao(a,b) == res


def test_divisao():
    a = 6
    b = 2
    res = 3

    assert divisao(a,b) == res
