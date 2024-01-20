import subprocess
import speedtest
import tkinter as tk
import platform
import os
import multiprocessing
import GPUtil
import psutil
import pygetwindow as gw
import math
import uuid
import requests
import platform


def get_installed_software():
    try:
        result = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        software_list = result.decode('utf-8').split('\n')[1:-1]  
        return [software.strip() for software in software_list]
    except Exception as e:
        return f"Error: {e}"

installed_software = get_installed_software()
if isinstance(installed_software, list):
    for software in installed_software:
        print(software)
else:
    print(installed_software)


def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000  
    return download_speed, upload_speed

download_speed, upload_speed = get_internet_speed()


def get_screen_resolution():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

screen_width, screen_height = get_screen_resolution()


def get_cpu_model():
    try:
        system_info = platform.processor()
        return system_info
    except Exception as e:
        return f"Error: {e}"

cpu_model = get_cpu_model()


def get_cpu_info():
    try:
        num_cores = os.cpu_count()  
        num_threads = multiprocessing.cpu_count() 

        return num_cores, num_threads
    except Exception as e:
        return f"Error: {e}"

cores, threads = get_cpu_info()


def get_gpu_model():
    try:
        gpu_list = GPUtil.getGPUs()
        if gpu_list:
            gpu_model = gpu_list[0].name
            return gpu_model
        else:
            return "No GPU detected"
    except Exception as e:
        return f"Error: {e}"

gpu_model = get_gpu_model()


def get_ram_size():
    try:
        ram_info = psutil.virtual_memory()
        ram_size_gb = ram_info.total / (1024 ** 3) 
        return ram_size_gb
    except Exception as e:
        return f"Error: {e}"

ram_size = get_ram_size()


def get_screen_size():
    try:
        screen = gw.getWindowsWithTitle('')[0]  
        width, height = screen.width, screen.height
        diagonal_size = math.sqrt(width * 2 + height * 2)
        diagonal_size_inches = diagonal_size / gw.screenInfo.pixelDensity()

        return diagonal_size_inches
    except Exception as e:
        return f"Error: {e}"

screen_size = get_screen_size()


def get_mac_addresses():
    try:
        wifi_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2,6)][::-1])
        ethernet_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(6,12)][::-1])

        return wifi_mac, ethernet_mac
    except Exception as e:
        return f"Error: {e}"

wifi_mac, ethernet_mac = get_mac_addresses()


def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json()['origin']
        return public_ip
    except Exception as e:
        return f"Error: {e}"

public_ip = get_public_ip()


def get_windows_version():
    try:
        windows_version = platform.version()
        return windows_version
    except Exception as e:
        return f"Error: {e}"

windows_version = get_windows_version()


print("Details :----->")
print(f" 2:- Download Speed: {download_speed:.2f} Mbps")
print(f" 2:- Upload Speed: {upload_speed:.2f} Mbps")
print(f" 3:- Screen Resolution: {screen_width}x{screen_height}")
print(f" 4:- CPU Model: {cpu_model}")
print(f" 5:- Number of CPU Cores: {cores}")
print(f" 5:- Number of CPU Threads: {threads}")
print(f" 6:- GPU Model: {gpu_model}")
print(f" 7:- RAM Size: {ram_size:.2f} GB")
print(" 8:- Estimated Screen Size: {screen_size:.2f} inches")
print(f" 9:- Wi-Fi MAC Address: {wifi_mac}")
print(f" 9- Ethernet MAC Address: {ethernet_mac}")
print(f" 10:- Public IP Address: {public_ip}")
print(f" 11:- Windows Version: {windows_version}")
