import pandas as pd;
step_data = [12,13,14,15,16,17]
step_counts = pd.Series(step_data,index=['a','b','c','d','e','f'])
# print(step_counts)
# print(step_counts.iloc[0])
calories = {"day1": 420, "day2": 380, "day3": 390}
p_calories = pd.Series(calories,index=['day1','day2'])
# print(p_calories)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
frame = pd.DataFrame(data)
print(frame[0])