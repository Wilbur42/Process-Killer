from threading import Thread
import os
import wmi
import pythoncom

def terminate_all():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    while True:
        processList = list(c.Win32_Process())
        for process in processList:
            try:
                if process.name not in ['Discord.exe', 'new.py', 'Code.exe', 'python.exe', 'py.exe', 'cmd.exe', 'conhost.exe', 'bash.exe']:
                    print(f'Terminating process: {process.name}.')
                    process.terminate()
                    os.system(f"taskkill /F /IM {process.name}")
            except:
                print(f'Error: {process.name} could not be terminated.')

            # if 'svchost.exe' in process.name:
            #     continue # When relaunched, restarts explorer.exe
            # if 'explorer.exe' in process.name:
            #     os.system('TASKKILL /IM explorer.exe /F')

if __name__ == '__main__':

    thread_count = 2

    for i in range(thread_count):
        Thread(target=terminate_all).start()
        print(f'Started thread {i} successfully.')
