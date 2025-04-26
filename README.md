# Available RAM Monitor

A Python-based utility to monitor the available RAM on your system. This tool provides a simple interface to check if the available RAM is below a specified threshold and offers additional features like displaying the current RAM status in a graphical window.

## Features

- Monitor available RAM as a percentage of total RAM.
- Set and get custom thresholds for RAM monitoring.
- Retrieve available and remaining RAM in megabytes.
- Display current RAM status in a graphical window using Tkinter.
- Logging for detailed insights into RAM usage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alfredo000008/available_ram_monitor.git
   cd available_ram_monitor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install dependencies directly from the `pyproject.toml` file:
   ```bash
   pip install psutil==7.0.0
   ```

3. (Optional) Install development dependencies:
   ```bash
   pip install pipreqs==0.5.0 pytest==8.3.5 psutil==7.0.0
   ```

## Usage

### Basic Example

```python
from available_ram_monitor.monitor import RAMMonitor

# Initialize the RAM monitor with a threshold of 20%
monitor = RAMMonitor(threshold=0.2)

# Check if available RAM is below the threshold
if monitor.check_available_ram():
    print("Warning: Available RAM is below the threshold!")
else:
    print("Available RAM is sufficient.")
```

### Display Current RAM Status

```python
monitor.show_current_status(timeout=5000)  # Display status for 5 seconds
```

### Get Available and Remaining RAM

```python
available_ram = monitor.get_available_ram()
remaining_ram = monitor.get_remaining_ram()

print(f"Available RAM: {available_ram:.2f} MB")
print(f"Remaining RAM: {remaining_ram:.2f} MB")
```

## Configuration

You can customize the RAM threshold using the `set_threshold` method:

```python
monitor.set_threshold(0.1)  # Set threshold to 10%
```

Retrieve the current threshold using:

```python
current_threshold = monitor.get_threshold()
print(f"Current Threshold: {current_threshold:.2%}")
```

## Development

### Running Tests

Run the tests using `pytest`:

```bash
pytest
```

### Generating Requirements File

To regenerate the `requirements.txt` file, use `pipreqs`:

```bash
pipreqs . --force
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Developed by Alfredo Gasa ([@alfredo000008](mailto:alfredogasa8@hotmail.com)).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgments

- [psutil](https://github.com/giampaolo/psutil) for system monitoring utilities.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical interface.
