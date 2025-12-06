from pathlib import Path

Log_dir = Path("C:\\Users\\kevha\\OneDrive\\Dokumente\\Desktop\\Logs") / "banklog.txt"
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

        self.logger = logging.getLogger(self.owner) # Hier einen Check machen, ob ein Logger bereits mit dem gleichen Namen existiert
        self.logger.setLevel(logging.INFO) # Sonst könnten Logs zweimal geschrieben werden
        self.logger.addHandler(fileHandler)

    def deposit(self, amount): # Müsstest mal fragen, was hier das self macht
        self.balance += float(amount)
        self.logger.info(f"{amount} erfolgreich auf das Konto von {self.owner} geladen")

    def check(self, amount):
        if self.balance < amount:
            return False
        else:
            return True # Du kannst stattdessen auch "return self.balance >= amount" machen
    def withdraw(self, amount):
        if not self.check(amount):
            self.logger.warning("Fehlgeschlagene Abhebung")
            return "Vorgang nicht möglich, zu wenig Guthaben"
        else:
            self.balance -= float(amount)
            self.logger.info(f"{amount} erfolgreich von {self.owner} aus dem Konto genommen")
            return "Vorgang erfolgreich"

    def __str__(self):
        return f"Konto von {self.owner} - Guthaben: {self.balance}"

    def test(self):
        return self.balance

# Dictionary für jeden Nutzer mit seiner Pin -> hier maybe später in so Sicherheit, log in Systeme gehen?!




