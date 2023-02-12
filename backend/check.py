from typing import Any
from mypy import api
import polygon


def enable_typing(lib: Any) -> None:  # type: ignore
    open(lib.__path__[0] + "/py.typed", 'a').close()


enable_typing(polygon)


[success, error, exit_code] = api.run(["."])
if success:
    print('\nType checking report:\n')
    print(success)

if error:
    print('\nError report:\n')
    print(error)

print('\nExit status:', exit_code)
quit(exit_code)
