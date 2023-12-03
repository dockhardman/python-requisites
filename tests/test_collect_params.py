from typing import Text

import requisites


def func_with_pos_or_key(var: Text) -> Text:
    return var


def func_with_var(a, b, *args, c, d=1, **kwargs) -> Text:
    return "OK"


class TestClass:
    def method_with_var(self, a, b, *args, c, d=1, **kwargs) -> Text:
        return "OK"

    @staticmethod
    def static_method_with_var(a, b, *args, c, d=1, **kwargs) -> Text:
        return "OK"

    @classmethod
    def class_method_with_var(cls, a, b, *args, c, d=1, **kwargs) -> Text:
        return "OK"


def test_collect_params_with_pos_or_key():
    # Test positional arguments
    req_args, req_kwargs = requisites.collect_params(
        func_with_pos_or_key, *("hello", "world")
    )
    assert req_args == ("hello",)  # "world" is not collected
    assert req_kwargs == {}
    assert func_with_pos_or_key(*req_args, **req_kwargs) == "hello"

    # Test positional arguments if the kwargs name is not the same as the argument name
    req_args, req_kwargs = requisites.collect_params(
        func_with_pos_or_key, *("hello",), **{"var": "world"}
    )
    assert req_args == ()
    assert req_kwargs == {
        "var": "world"
    }  # "hello" is not collected because there is a keyword argument named "var"
    assert func_with_pos_or_key(*req_args, **req_kwargs) == "world"

    # Test keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        func_with_pos_or_key, **{"var": "hello", "var2": "world"}
    )
    assert req_args == ()
    assert req_kwargs == {"var": "hello"}  # "var2" is not collected
    assert func_with_pos_or_key(*req_args, **req_kwargs) == "hello"


def test_collect_params_with_var():
    # Test at least required parameters
    req_args, req_kwargs = requisites.collect_params(
        func_with_var, args=("hello",), *("world",), c="c"
    )
    assert req_args == ("hello", "world")
    assert req_kwargs == {"c": "c", "d": 1}
    assert func_with_var(*req_args, **req_kwargs) == "OK"

    # Test with extra positional and keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        func_with_var, args=("hello",), *("world", "!"), c="c", e="e", f="f"
    )
    assert req_args == ("hello", "world", "!")
    assert req_kwargs == {"c": "c", "d": 1, "e": "e", "f": "f"}
    assert func_with_var(*req_args, **req_kwargs) == "OK"


def test_collect_params_with_var_of_object_method():
    test_obj = TestClass()

    # Test at least required parameters
    req_args, req_kwargs = requisites.collect_params(
        test_obj.method_with_var, args=("hello",), *("world",), c="c"
    )
    assert req_args == ("hello", "world")
    assert req_kwargs == {"c": "c", "d": 1}
    assert test_obj.method_with_var(*req_args, **req_kwargs) == "OK"

    # Test with extra positional and keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        test_obj.method_with_var,
        args=("hello",),
        *("world", "!"),
        c="c",
        e="e",
        f="f",
    )
    assert req_args == ("hello", "world", "!")
    assert req_kwargs == {"c": "c", "d": 1, "e": "e", "f": "f"}
    assert test_obj.method_with_var(*req_args, **req_kwargs) == "OK"


def test_collect_params_with_var_of_static_method():
    # Test at least required parameters
    req_args, req_kwargs = requisites.collect_params(
        TestClass.static_method_with_var, args=("hello",), *("world",), c="c"
    )
    assert req_args == ("hello", "world")
    assert req_kwargs == {"c": "c", "d": 1}
    assert TestClass.static_method_with_var(*req_args, **req_kwargs) == "OK"

    # Test with extra positional and keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        TestClass.static_method_with_var,
        args=("hello",),
        *("world", "!"),
        c="c",
        e="e",
        f="f",
    )
    assert req_args == ("hello", "world", "!")
    assert req_kwargs == {"c": "c", "d": 1, "e": "e", "f": "f"}
    assert TestClass.static_method_with_var(*req_args, **req_kwargs) == "OK"


def test_collect_params_with_var_of_class_method():
    # Test at least required parameters
    req_args, req_kwargs = requisites.collect_params(
        TestClass.class_method_with_var, args=("hello",), *("world",), c="c"
    )
    assert req_args == ("hello", "world")
    assert req_kwargs == {"c": "c", "d": 1}

    # Test with extra positional and keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        TestClass.class_method_with_var,
        args=("hello",),
        *("world", "!"),
        c="c",
        e="e",
        f="f",
    )
    assert req_args == ("hello", "world", "!")
    assert req_kwargs == {"c": "c", "d": 1, "e": "e", "f": "f"}
    assert TestClass.class_method_with_var(*req_args, **req_kwargs) == "OK"
