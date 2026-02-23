# square-demo

A simple CLI tool that raises a number to a power (default: 2).

## Usage

```sh
uv run main.py <number> [--power POWER]
```

### Arguments

| Argument   | Required | Description                                  |
|------------|----------|----------------------------------------------|
| `number`   | Yes      | The number to raise                          |
| `--power`  | No       | The power to raise the number to (default: 2)|

### Examples

```sh
$ uv run main.py 5
5.0 raised to the power of 2.0 is 25.0

$ uv run main.py -3
-3.0 raised to the power of 2.0 is 9.0

$ uv run main.py 2 --power 3
2.0 raised to the power of 3.0 is 8.0

$ uv run main.py 5 --power 0
5.0 raised to the power of 0.0 is 1.0
```

## Development

### Run tests

```sh
uv run pytest
```
