## HISTOGRAM
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import style

ml_student_age = np.random.randint(18,45,(100))
py_student_age = np.random.randint(20,40,(100))
print(ml_student_age)
print()
print(py_student_age)
bins = [15,20,25,30,35,40,45,50]
plt.figure(figsize=(15,7))
style.use("ggplot")
plt.hist([ml_student_age, py_student_age], bins, rwidth=0.8, histtype="bar",orientation="vertical",
         color=["green","Orange"], label=["ML Students","Python Students"])

# plt.hist(py_student_age, bins, rwidth=0.8, histtype="bar",orientation="vertical",
#          color="orange", label="Python Students")

plt.legend(loc=2)
plt.title("Ml Students Age Histogram")
plt.xlabel("Age Category")
plt.ylabel("Number of Students")
plt.grid(color="blue",linestyle="--", linewidth=2)
plt.show()

