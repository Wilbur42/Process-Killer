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

    terminate_all()
