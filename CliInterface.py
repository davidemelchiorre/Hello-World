import subprocess

while 1:
    comando = input(">")

    if comando=="start":
        print()
        print("-----------------Start routine-----------------")
        try:
            if proc is None:
                print("Info>> Starting program...")
                proc=subprocess.Popen(["python","attesa.py"])
            else:
                print("Info>> Program is already running")
        except NameError:
            print("Info>> Starting program...")
            proc=subprocess.Popen(["python","attesa.py"])
        print("-----------------------------------------------")
        print()
  
    if comando=="stop":
        print()
        print("-----------------Stop routine------------------")
        try:
            if proc is not None:
                print(proc)
                print("Info>> Stopping program...")
                proc.kill()
                proc=None
            else:
                print("Info>> Program is not running")
        except NameError:
            print("Info>> Program is not running")
        print("-----------------------------------------------")
        print()
