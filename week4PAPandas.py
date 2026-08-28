import pandas as pd
import matplotlib.pyplot as plt


print("bryrol6946")

students = [
    "John",
    "Mary",
    "Richard",
    "Jane",
    "David",
    "Sarah",
    "Michael",
    "Lisa",
    "James",
    "Emily"
]

subjects = ["Math", "Science"]

index = pd.MultiIndex.from_product(
    [students, subjects],
    names=["Student", "Subject"]
)

grades = [
    85, 90,
    92, 88,
    78, 84,
    95, 91,
    82, 79,
    89, 94,
    76, 81,
    93, 96,
    87, 85,
    90, 92
]

gradeData = pd.DataFrame(
    {"Grade": grades},
    index=index
)

print("\nStudent Grades:")
print(gradeData)

subjectMean = gradeData.groupby(level="Subject").mean()

print("\nMean Grade by Subject:")
print(subjectMean)

subjectMean.plot(
    kind="bar",
    y="Grade",
    legend=False
)

plt.title("Average Grade by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.xticks(rotation=0)

plt.show()
