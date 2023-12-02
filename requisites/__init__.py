import inspect
from types import MappingProxyType
from typing import Any, Dict, Optional, Text, Tuple

from .version import VERSION

__version__ = VERSION

ArgsType = Tuple[Any, ...]
KwargsType = Dict[Text, Any]


def collect_params(
    fun: MappingProxyType[Text, "inspect.Parameter"],
    *args,
    kwargs: Optional[Dict[Text, Any]] = None,
    **extra_kwargs,
) -> Tuple[ArgsType, KwargsType]:
    signature_parameters: MappingProxyType[
        Text, "inspect.Parameter"
    ] = inspect.signature(fun).parameters

    collected_args = []
    collected_kwargs = {}
    args_idx = 0
    visited_names = set()

    for param_name, param_meta in signature_parameters.items():
        if param_meta.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            if kwargs and param_name in kwargs and param_name not in visited_names:
                collected_args.append(kwargs[param_name])
            elif param_name in extra_kwargs and param_name not in visited_names:
                collected_args.append(extra_kwargs[param_name])
            elif args_idx < len(args):
                collected_args.append(args[args_idx])
                args_idx += 1
            elif param_meta.default != inspect.Parameter.empty:
                collected_kwargs[param_name] = param_meta.default
            else:
                raise TypeError(f"Missing required positional argument: '{param_name}'")

        elif param_meta.kind == inspect.Parameter.VAR_POSITIONAL:
            collected_args.extend(args[args_idx:])
            args_idx = len(args)

        elif param_meta.kind == inspect.Parameter.KEYWORD_ONLY:
            if kwargs and param_name in kwargs and param_name not in visited_names:
                collected_kwargs[param_name] = kwargs[param_name]
            elif param_meta.default != inspect.Parameter.empty:
                collected_kwargs[param_name] = param_meta.default
            elif param_name in extra_kwargs and param_name not in visited_names:
                collected_kwargs[param_name] = extra_kwargs[param_name]
            else:
                raise TypeError(f"Missing required keyword argument: '{param_name}'")

        elif param_meta.kind == inspect.Parameter.VAR_KEYWORD:
            if kwargs:
                for k, v in kwargs.items():
                    if k not in collected_kwargs and k not in visited_names:
                        collected_kwargs[k] = v
            if extra_kwargs:
                for k, v in extra_kwargs.items():
                    if k not in collected_kwargs and k not in visited_names:
                        collected_kwargs[k] = v

        elif param_meta.kind == inspect.Parameter.POSITIONAL_ONLY:
            collected_args.append(args[args_idx])
            args_idx += 1

        else:
            raise TypeError(f"Unsupported parameter type: '{param_meta.kind}'")

        visited_names.add(param_name)

    return (tuple(collected_args), collected_kwargs)
