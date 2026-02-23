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
    assert "5.0 raised to the power of 2.0 is 25.0" in result.stdout


def test_negative_number():
    result = run_main("-3")
    assert result.returncode == 0
    assert "-3.0 raised to the power of 2.0 is 9.0" in result.stdout


def test_float_input():
    result = run_main("2.5")
    assert result.returncode == 0
    assert "2.5 raised to the power of 2.0 is 6.25" in result.stdout


def test_invalid_input():
    result = run_main("abc")
    assert result.returncode != 0
    assert "invalid float value" in result.stderr.lower() or "error" in result.stderr.lower()


def test_missing_argument():
    result = run_main()
    assert result.returncode != 0
    assert "arguments are required" in result.stderr.lower() or "usage" in result.stderr.lower()


def test_custom_power():
    result = run_main("2", "--power", "3")
    assert result.returncode == 0
    assert "2.0 raised to the power of 3.0 is 8.0" in result.stdout


def test_power_of_zero():
    result = run_main("5", "--power", "0")
    assert result.returncode == 0
    assert "5.0 raised to the power of 0.0 is 1.0" in result.stdout


def test_power_of_one():
    result = run_main("7", "--power", "1")
    assert result.returncode == 0
    assert "7.0 raised to the power of 1.0 is 7.0" in result.stdout
