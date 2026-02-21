import subprocess
import sys


def run_main(*args):
    result = subprocess.run(
        [sys.executable, "main.py", *args],
        capture_output=True,
        text=True,
    )
    return result


def test_positive_number():
    result = run_main("5")
    assert result.returncode == 0
    assert "5.0 squared is 25.0" in result.stdout


def test_negative_number():
    result = run_main("-3")
    assert result.returncode == 0
    assert "-3.0 squared is 9.0" in result.stdout


def test_float_input():
    result = run_main("2.5")
    assert result.returncode == 0
    assert "2.5 squared is 6.25" in result.stdout


def test_invalid_input():
    result = run_main("abc")
    assert result.returncode == 1
    assert "not a valid number" in result.stderr + result.stdout


def test_missing_argument():
    result = run_main()
    assert result.returncode == 1
    assert "Usage:" in result.stderr + result.stdout
