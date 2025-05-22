import psutil 
# a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)
import GPUtil 
# Library for NVIDIA GPUs using the nvidia-smi command-line utility. It allows users to identify available GPUs, monitor their utilization, 
# and manage GPU resources within Python applications.
import time 
# Time is used for disk IO counter intervals

class MetricsFetcher:
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1) # returns the cpu percentage out of 100%
    def get_memory_info(self):
        # sets varaiable from psutil library that contains informaiton about memory
        memory = psutil.virtual_memory()
        # returns the memory varaibles by a dictionary
        return {
            'total': memory.total,
            'available': memory.available,
            'used': memory.used,
            'percentage': memory.percent
        }
    def get_disk_info(self):
        disk = psutil.disk_usage('/') # start of all directories.
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percentage': disk.percentage
        }
    def get_network_io(self):
        net_io = psutil.net_connections()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv
        }
    def get_gpu_info(self):
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            return {
                'id': gpu.id,
                'name': gpu.name,
                'load': gpu.load * 100,
                'memory_total': gpu.memoryTotal,
                'memory_used': gpu.memoryUsed,
                'memory_free': gpu.memoryFree
            }
        else:
            return None
        

