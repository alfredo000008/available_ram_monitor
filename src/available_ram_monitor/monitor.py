"""
This module contains the logic for monitoring available RAM on the system.
It provides a function to check if the available RAM is below a specified threshold.
"""

import psutil
import logging
import tkinter as tk
from tkinter import messagebox

class RAMMonitor:
    """
    A class to monitor the available RAM on the system.
    """

    def __init__(self, threshold: float = 0.2):
        """
        Initialize the RAMMonitor with a specified threshold.

        :param threshold: The threshold for available RAM as a fraction of total RAM (default is 0.2).
        """
        self.threshold = threshold
        logging.info(f"RAMMonitor initialized with threshold: {self.threshold:.2%}")

    def check_available_ram(self) -> bool:
        """
        Check if the available RAM is below the specified threshold.

        :return: True if available RAM is below the threshold, False otherwise.
        """
        ram = psutil.virtual_memory()
        available_ram = ram.available / ram.total
        logging.info(f"Available RAM: {available_ram:.2%}")

        if available_ram < self.threshold:
            logging.warning("Available RAM is below the threshold.")
            return True
        else:
            logging.info("Available RAM is above the threshold.")
            return False
    
    def set_threshold(self, threshold: float):
        """
        Set a new threshold for available RAM.

        :param threshold: The new threshold for available RAM as a fraction of total RAM.
        """
        self.threshold = threshold
        logging.info(f"Threshold updated to: {self.threshold:.2%}")
    
    def get_threshold(self) -> float:
        """
        Get the current threshold for available RAM.

        :return: The current threshold for available RAM as a fraction of total RAM.
        """
        return self.threshold
    
    def get_available_ram(self) -> float:
        """
        Get the current available RAM in Megabytes.

        :return: The current available RAM in Megabytes.
        """
        ram = psutil.virtual_memory()
        available_ram_mb = ram.available / (1024 ** 2)
        logging.info(f"Available RAM: {available_ram_mb:.2f} MB")
        return available_ram_mb
    
    def get_remaining_ram(self) -> float:
        """
        Get the remaining RAM in Megabytes.

        :return: The remaining RAM in Megabytes.
        """
        ram = psutil.virtual_memory()
        remaining_ram_mb = ram.total / (1024 ** 2) - ram.used / (1024 ** 2)
        logging.info(f"Remaining RAM: {remaining_ram_mb:.2f} MB")
        return remaining_ram_mb
    
    def show_current_status(self, timeout: int = 4000) -> None:
        """
        This function will show a small tkinter window with the current status of the RAM.
        It will show the total, available RAM, and the threshold. The window will close automatically after a timeout.

        :param timeout: The time in milliseconds before the window closes automatically (default is 5000ms).
        """
        ram = psutil.virtual_memory()
        total_ram_mb = ram.total / (1024 ** 2)
        available_ram_mb = ram.available / (1024 ** 2)

        root = tk.Tk()
        root.withdraw()

        # Create a new top-level window
        status_window = tk.Toplevel(root)
        status_window.title("Current RAM Status")
        status_window.geometry("300x150")

        # Add the RAM status information
        label = tk.Label(
            status_window,
            text=(
                f"Total RAM: {total_ram_mb:.2f} MB\n"
                f"Available RAM: {available_ram_mb:.2f} MB\n"
                f"Threshold: {self.threshold:.2%}"
            ),
            justify="left",
        )
        label.pack(pady=10)

        # Close the window after the timeout
        root.after(ms = timeout, func = status_window.destroy)
        root.mainloop()

    def __str__(self) -> str:
        """
        Return a string representation of the RAMMonitor object.

        :return: A string representation of the RAMMonitor object.
        """
        return f"RAMMonitor(threshold={self.threshold:.2%})"
    
    def __repr__(self) -> str:
        """
        Return a string representation of the RAMMonitor object for debugging.

        :return: A string representation of the RAMMonitor object for debugging.
        """
        return f"RAMMonitor(threshold={self.threshold:.2%})"
    

    
