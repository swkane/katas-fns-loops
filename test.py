import inspect
from main import add, multiply, power, factorial, fibonacci


def implementation_test_helper(function):
    illegal_operators = ["+", "/", "*"]
    source = inspect.getsource(function)
    return not any(x in source for x in illegal_operators)


class TestAdd:
    def test_answer(self):
        assert add(2, 2) == 4
        assert add(2, 3) == 5
        assert add(0, 0) == 0


class TestMultiply:
    def test_answer(self):
        assert multiply(0, 10) == 0
        assert multiply(3, 3) == 9
        assert multiply(3, 1) == 3

    def test_implementation(self):
        assert implementation_test_helper(multiply)


class TestPower:
    def test_answer(self):
        assert power(1, 2) == 1
        assert power(3, 2) == 9
        assert power(2, 3) == 8

    def test_implementation(self):
        assert implementation_test_helper(power)


class TestFactorial:
    def test_answer(self):
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_implementation(self):
        assert implementation_test_helper(factorial)


class TestFibonacci:
    def test_answer(self):
        assert fibonacci(8) == 13
        assert fibonacci(12) == 89
        assert fibonacci(15) == 377
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1

    def test_implementation(self):
        assert implementation_test_helper(fibonacci)
