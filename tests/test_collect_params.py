from typing import Text

import requisites


def func_with_var(var: Text) -> Text:
    return var


def test_collect_params():
    # Test positional arguments
    req_args, req_kwargs = requisites.collect_params(func_with_var, *("hello", "world"))
    assert req_args == ("hello",)  # "world" is not collected
    assert req_kwargs == {}
    assert func_with_var(*req_args, **req_kwargs) == "hello"

    # Test positional arguments if the kwargs name is not the same as the argument name
    req_args, req_kwargs = requisites.collect_params(
        func_with_var, *("hello",), **{"var": "world"}
    )
    assert req_args == (
        "world",
    )  # "hello" is not collected because there is a keyword argument named "var"
    assert req_kwargs == {}
    assert func_with_var(*req_args, **req_kwargs) == "world"

    # Test keyword arguments
    req_args, req_kwargs = requisites.collect_params(
        func_with_var, **{"var": "hello", "var2": "world"}
    )
    assert req_args == ()
    assert req_kwargs == {"var": "hello"}  # "var2" is not collected
    assert func_with_var(*req_args, **req_kwargs) == "hello"
