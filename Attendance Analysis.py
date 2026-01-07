from pathlib import Path
import pandas as pd

Path_basic = Path("x")
File = Path_basic / "Exam_Score_Prediction.csv"

Reader = pd.read_csv(File)

scores = {"0": [], "10": [], "20": [], "30": [], "40": [], "50": [], "60": [], "70": [], "80": [], "90": []}
grades = Reader["exam_score"].tolist()
times = Reader["class_attendance"].tolist()

for i in range(len(times)):
    t = float(times[i])
    g = float(grades[i])
    if 0 < t <= 10:
        scores["0"].append(g)
    elif 10 < t <= 20:
        scores["10"].append(g)
    elif 20 < t <= 30:
        scores["20"].append(g)
    elif 30 < t <= 40:
        scores["30"].append(g)
    elif 40 < t <= 50:
        scores["40"].append(g)
    elif 50 < t <= 60:
        scores["50"].append(g)
    elif 60 < t <= 70:
        scores["60"].append(g)
    elif 70 < t <= 80:
        scores["70"].append(g)
    elif 80 < t <= 90:
        scores["80"].append(g)
    elif 90 < t < 100:
        scores["90"].append(g)

scores_clean = []
for key in scores:
    try:
        scores_clean.append(round(sum(scores[key]) / len(scores[key]), 2))
    except ZeroDivisionError:
        scores_clean.append(0)

grade_list = []
for i in range(len(scores_clean)):
    grade_list.append(i)

import matplotlib.pyplot as plt

plt.bar(grade_list, scores_clean)
plt.xticks(grade_list) 
plt.yticks(scores_clean)
plt.show()

# What if it was just the facility rating?

Dict_ratings = {"low": 0, "medium": 0, "high": 0}
Ratings_high = Reader[Reader["class_attendance"] >= 80].to_dict(orient = "list")

for i in range(len(Ratings_high["exam_score"])):
    if Ratings_high["exam_score"][i] >= 67:
        if Ratings_high["facility_rating"][i] == "low":
            Dict_ratings["low"] += 1
        elif Ratings_high["facility_rating"][i] == "medium":
            Dict_ratings["medium"] += 1
        elif Ratings_high["facility_rating"][i] == "high":
            Dict_ratings["high"] += 1

Ratings2 = {"low": 0, "medium": 0, "high": 0}
Ratings_low = Reader[Reader["class_attendance"] <= 50].to_dict(orient = "list")

for i in range(len(Ratings_low["exam_score"])):
    if Ratings_low["exam_score"][i] <= 60:
        if Ratings_low["facility_rating"][i] == "low":
            Ratings2["low"] += 1
        elif Ratings_low["facility_rating"][i] == "medium":
            Ratings2["medium"] += 1
        elif Ratings_low["facility_rating"][i] == "high":
            Ratings2["high"] += 1

width = 0.35
x = [0, 1, 2]

plt.bar([i-width/2 for i in x], list(Dict_ratings.values()), width = width, color = "orange", label = "High Attendance")
plt.bar([i+width/2 for i in x], list(Ratings2.values()), width = width, color = "purple", label = "Low Attendance")

plt.xticks(x, list(Ratings2.keys())) 
plt.legend()
plt.tight_layout()
plt.show()

# People with higher attendance and therefore better grades are more likely to be found in a high-rated facility. Whereas people who have a lower attendance and therefore worse grades are more likely to be found in low-rated places

# Just for more: how much does the course affect the sleep? 

Sleep = Reader.groupby("course")["sleep_hours"].mean()
Sleep.plot(kind = "bar")
plt.ylim(6.5, None)
plt.show()

# So we see: there is no severe difference in sleep between the courses
