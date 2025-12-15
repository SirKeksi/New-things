from pathlib import Path
import json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {"Time" : self.formatTime(record, self.datefmt), "Level" : record.levelname,
                     "Owner" : record.name, "Message" : record.getMessage()}
        return json.dumps(log_entry)

# fileHandler.setFormatter(JsonFormatter(datefmt = "%H:%M:%S / %Y.%m.%d"))

Path = Path("bank.json")

Datap = {}
Datam = {}


with Path.open("r", encoding = "utf-8") as b:
    for line in b:
        Entry = json.loads(line)
        if Entry.get("Level") == "INFO":
            if "Deposited" in Entry.get("Message"):
                if Entry.get("Owner") not in Datap:
                    Datap[Entry.get("Owner")] = int(Entry.get("Message")[10:])
                elif Entry.get("Owner") in Datap:
                    Datap[Entry.get("Owner")] += int(Entry.get("Message")[10:])

            elif "Deducted" in Entry.get("Message"):
                if Entry.get("Owner") not in Datam:
                    Datam[Entry.get("Owner")] = int(Entry.get("Message")[9:])
                elif Entry.get("Owner") in Datam:
                    Datam[Entry.get("Owner")] += int(Entry.get("Message")[9:])