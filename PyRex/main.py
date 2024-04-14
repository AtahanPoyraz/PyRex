import argparse
from os import system
from platform import system as sys

from module.ftp import FTP_BRUTEFORCE
from module.ssh import SSH_BRUTEFORCE
from module.telnet import TELNET_BRUTEFORCE

class Main:
    def __init__(self) -> None:
        self.clear()
        print("""
   ▄███████▄ ▄██   ▄      ▄████████    ▄████████ ▀████    ▐████▀ 
  ███    ███ ███   ██▄   ███    ███   ███    ███   ███▌   ████▀  
  ███    ███ ███▄▄▄███   ███    ███   ███    █▀     ███  ▐███    
  ███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄▄██▀  ▄███▄▄▄        ▀███▄███▀    
▀█████████▀  ▄██   ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀        ████▀██▄     
  ███        ███   ███ ▀███████████   ███    █▄    ▐███  ▀███    
  ███        ███   ███   ███    ███   ███    ███  ▄███     ███▄  
 ▄████▀       ▀█████▀    ███    ████  ██████████ ████       ███▄ By Atahan Poyraz.
""")
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-m", "--module", required=True, choices=['ftp', 'ssh', 'telnet'], help="Select a module: ftp, ssh, or telnet.")
        self.parser.add_argument("-t", "--target", required=True, help="Enter the IP or Domain.")
        self.parser.add_argument("-u", "--user", required=True, help="Username for login attempt.")
        self.parser.add_argument("-to", "--timeout", required=True, type=int, help="Timeout per connection attempt for ssh and telnet module.")
        self.parser.add_argument("-w", "--wordlist", required=True, help="Location of the file with passwords.")

        args = self.parser.parse_args()

        self.module = args.module
        self.target = args.target
        self.user = args.user
        self.wordlist = args.wordlist
        self.timeout = args.timeout

        self.run(module=self.module, target=self.target, username=self.user, wordlist=self.wordlist, timeout=self.timeout)

    def run(self, *c, module : str, target : str, username : str, wordlist : str, timeout : int = 3) -> None:
        match module.lower():
            case "ftp":
                if target != "" and username != "" and wordlist != "":
                    FTP_BRUTEFORCE(target=target, username=username, wordlist=wordlist).start()

                else:
                    print("Missing Input Value!")

            case "ssh":
                if target != "" and username != "" and wordlist != "":
                    SSH_BRUTEFORCE(target=target, username=username, timeout=timeout, wordlist=wordlist).start()

                else:
                    print("Missing Input Value!")

            case "telnet":
                if target != "" and username != "" and wordlist != "":
                    TELNET_BRUTEFORCE(target=target, username=username, timeout=timeout, wordlist=wordlist).start()

                else:
                    print("Missing Input Value!")

            case _:
                print("Missing Module Name Try: (ftp, ssh, telnet)")

    def clear(self)  -> None:
        if sys().lower() == "windows":
            system("cls")
        
        else:
            system("clear")

if __name__ == "__main__":
    Main()