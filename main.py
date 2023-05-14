from threading import Thread
import psutil
# import os

def terminate_all():
    while True:
        for proc in psutil.process_iter():
            try:
                if proc.name() not in ['Discord.exe', 'new.py', 'Code.exe', 'python.exe', 'py.exe', 'cmd.exe', 'conhost.exe', 'bash.exe']:
                    print(f'Terminating process: {proc.name()}.')
                    proc.terminate()
                    # os.system(f"taskkill /F /IM {proc.name()}")
            except psutil.AccessDenied:
                print(f'Access denied to process: {proc.name()}.')
            except psutil.NoSuchProcess:
                print(f'Process not found: {proc.name()}.')

            # if 'svchost.exe' in proc.name():
            #     continue # When relaunched, restarts explorer.exe
            # if 'explorer.exe' in proc.name():
            #     os.system('TASKKILL /F /IM explorer.exe')

if __name__ == '__main__':

    thread_count = 2

    for i in range(thread_count):
        Thread(target=terminate_all).start()
        print(f'Started thread {i} successfully.')
