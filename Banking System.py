from pathlib import Path

Log_dir = Path("x") / "banklog.txt"
if not Log_dir.exists():
    Log_dir.touch(exist_ok = True)

import logging

fileHandler = logging.FileHandler(Log_dir, encoding = "utf-8")
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt = "%H:%M:%S / %Y.%m.%d"))

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = float(balance)

        self.logger = logging.getLogger(self.owner) 
        self.logger.setLevel(logging.INFO) 
        self.logger.addHandler(fileHandler)

    def deposit(self, amount): 
        self.balance += float(amount)
        self.logger.info(f"{amount} successfully loaded onto {self.owner}")

    def check(self, amount):
        if self.balance < amount:
            return False
        else:
            return True 
    def withdraw(self, amount):
        if not self.check(amount):
            self.logger.warning("Withdrawing went wrong")
            return "Process not possible"
        else:
            self.balance -= float(amount)
            self.logger.info(f"{amount} succesfully deducted from {self.owner}")
            return "Process succesfull"

    def __str__(self):
        return f"Account of {self.owner} - Balance: {self.balance}"

    def test(self):
        return self.balance










