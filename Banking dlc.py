from pathlib import Path
import json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {"Time" : self.formatTime(record, self.datefmt), "Level" : record.levelname,
                     "Owner" : record.name, "Message" : record.getMessage()}
        return json.dumps(log_entry)

# fileHandler.setFormatter(JsonFormatter(datefmt = "%H:%M:%S / %Y.%m.%d"))
# Both the class and the setFormatter should be in "Banking System". I just wanted them to be here because I collected all the changes and additions I made to the system

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
