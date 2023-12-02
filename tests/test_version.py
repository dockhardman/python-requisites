import tomli

from requisites import __version__


def test_version():
    with open("pyproject.toml", "rb") as f:
        pyproject_data = tomli.load(f)
    assert __version__ == pyproject_data["tool"]["poetry"]["version"]
