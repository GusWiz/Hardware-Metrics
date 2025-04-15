import psutil 
# a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)
import GPUtil 
# Library for NVIDIA GPUs using the nvidia-smi command-line utility. It allows users to identify available GPUs, monitor their utilization, 
# and manage GPU resources within Python applications.
import time 
# Time is used for disk IO counter intervals

class MetricsFetcher:
    def __init__(self):
        pass
    def get_cpu_usage(self):
        pass
    def get_memory_info(self):
        pass
    def get_disk_info(self):
        pass
    def get_network_io(self):
        pass
    def get_gpu_info(self):
        pass
