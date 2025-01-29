import threading
from internet_check import is_Online
from Alert import Alert
from DATA.dlg_data import online_dlg, offline_dlg
import random
from co_brain import jarvis
from TTS.ttsB import speak
from Automation.battery import check_plug
from Time_Operations.Throw_Alert import check_schedule, check_Alarm

alarm_path = r"C:\Users\shrig\Downloads\ADVANCED-JARVIS-main\ADVANCED-JARVIS-main\Alarm_data.txt"
file_path = r"C:\Users\shrig\Downloads\ADVANCED-JARVIS-main\ADVANCED-JARVIS-main\schedule.txt"

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg) 

def wish(): 
    """Initiates the wish functionality."""
    t1 = threading.Thread(target=speak, args=(ran_online_dlg,))
    t2 = threading.Thread(target=Alert, args=(ran_online_dlg,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    """Main function to control the program flow."""
    if is_Online():
        wish()
        threads = [
            threading.Thread(target=check_plug),
            threading.Thread(target=check_schedule, args=(file_path,)),
            threading.Thread(target=jarvis),
            threading.Thread(target=check_Alarm, args=(alarm_path,))
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    else:
        Alert(ran_offline_dlg)

if __name__ == "__main__":
    main()