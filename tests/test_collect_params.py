from typing import Text

import requisites


def func_with_pos_or_key(var: Text) -> Text:
    return var


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
