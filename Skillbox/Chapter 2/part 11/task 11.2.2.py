class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60

class Headphone:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = False

first_monitor = Monitor()
second_monitor = Monitor()
second_monitor.monitor_freq = 144
third_monitor = Monitor()
third_monitor.monitor_freq = 70
forth_monitor = Monitor()

first_headphone = Headphone()
second_headphone = Headphone()
second_headphone.headphones_micro = True
third_headphone = Headphone()