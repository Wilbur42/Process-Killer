from threading import Thread
import wmi
import pythoncom

def terminate_all():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    processList = c.Win32_Process()
    for process in processList:
        try:
            # if process.name not in ['Discord.exe', 'new.py', 'Code.exe', 'python.exe', 'cmd.exe']:
            process.Terminate()
            print(f'Terminated process: {process.name} successfully.')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':

    thread_count = 2

    for i in range(thread_count):
        Thread(target=terminate_all).start()
        print(f'Started thread {i} successfully.')
