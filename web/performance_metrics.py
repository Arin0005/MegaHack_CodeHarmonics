import psutil
import platform
from datetime import datetime

def system_metrics():
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_total = round(memory.total / (1024 ** 3), 2)  # Convert to GB
    memory_used = round(memory.used / (1024 ** 3), 2)
    memory_percent = memory.percent

    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_total = round(disk.total / (1024 ** 3), 2)  # Convert to GB
    disk_used = round(disk.used / (1024 ** 3), 2)
    disk_percent = disk.percent

    # Network Information
    net_io = psutil.net_io_counters()
    bytes_sent = round(net_io.bytes_sent / (1024 ** 2), 2)  # Convert to MB
    bytes_recv = round(net_io.bytes_recv / (1024 ** 2), 2)

    # Boot Time
    boot_time = psutil.boot_time()
    boot_time_formatted = datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")

    # System Information
    system_info = platform.system()
    node_name = platform.node()
    release = platform.release()
    version = platform.version()

    # Battery Information
    battery = psutil.sensors_battery()
    if battery:
        battery_percent = battery.percent
        is_plugged = battery.power_plugged
        battery_time_left = battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Unknown"
    else:
        battery_percent = "N/A"
        is_plugged = "N/A"
        battery_time_left = "N/A"

    # Print Metrics
    print("===== System Metrics Analysis =====")
    print(f"CPU Usage: {cpu_usage}% (Logical CPUs: {cpu_count})")
    print(f"Memory Usage: {memory_used} GB / {memory_total} GB ({memory_percent}%)")
    print(f"Disk Usage: {disk_used} GB / {disk_total} GB ({disk_percent}%)")
    print(f"Network: Sent={bytes_sent} MB, Received={bytes_recv} MB")
    print(f"System Boot Time: {boot_time_formatted}")
    print(f"System Info: {system_info} {node_name} {release} {version}")
    print(f"Battery: {battery_percent}% (Plugged In: {is_plugged}, Time Left: {battery_time_left} seconds)")
    print("==================================")

    # Return metrics as a dictionary for the virtual assistant to speak
    metrics = {
        "cpu_usage": cpu_usage,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "bytes_sent": bytes_sent,
        "bytes_recv": bytes_recv,
        "boot_time": boot_time_formatted,
        "battery_percent": battery_percent,
        "is_plugged": is_plugged,
        "battery_time_left": battery_time_left,
    }
    return metrics