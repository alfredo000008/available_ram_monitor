import pytest
import threading
import time
from unittest.mock import patch
from available_ram_monitor.monitor import RAMMonitor

@pytest.fixture
def ram_monitor():
    return RAMMonitor(threshold=0.2)

@patch("available_ram_monitor.monitor.psutil.virtual_memory")
def test_check_available_ram_below_threshold(mock_virtual_memory, ram_monitor):
    mock_virtual_memory.return_value = type(
        "VirtualMemory", (object,), {"available": 1 * 1024 ** 3, "total": 10 * 1024 ** 3}
    )()
    assert ram_monitor.check_available_ram() is True

@patch("available_ram_monitor.monitor.psutil.virtual_memory")
def test_check_available_ram_above_threshold(mock_virtual_memory, ram_monitor):
    mock_virtual_memory.return_value = type(
        "VirtualMemory", (object,), {"available": 3 * 1024 ** 3, "total": 10 * 1024 ** 3}
    )()
    assert ram_monitor.check_available_ram() is False

def test_set_and_get_threshold(ram_monitor):
    ram_monitor.set_threshold(0.3)
    assert ram_monitor.get_threshold() == 0.3

@patch("available_ram_monitor.monitor.psutil.virtual_memory")
def test_get_available_ram(mock_virtual_memory, ram_monitor):
    mock_virtual_memory.return_value = type(
        "VirtualMemory", (object,), {"available": 2 * 1024 ** 3}
    )()
    assert ram_monitor.get_available_ram() == 2048.0

@patch("available_ram_monitor.monitor.psutil.virtual_memory")
def test_get_remaining_ram(mock_virtual_memory, ram_monitor):
    mock_virtual_memory.return_value = type(
        "VirtualMemory", (object,), {"total": 10 * 1024 ** 3, "used": 8 * 1024 ** 3}
    )()
    assert ram_monitor.get_remaining_ram() == 2048.0

def test_str_representation(ram_monitor):
    assert str(ram_monitor) == "RAMMonitor(threshold=20.00%)"

def test_repr_representation(ram_monitor):
    assert repr(ram_monitor) == "RAMMonitor(threshold=10.00%)"

    