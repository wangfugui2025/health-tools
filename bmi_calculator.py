try:
    user_height = float(input("请输入你的身高（单位：米）："))
    user_weight = float(input("请输入你的体重（单位：千克）："))
    if user_height <= 0 or user_weight <= 0:
        raise ValueError("身高体重必须大于0")
except ValueError as e:
    print(f"输入错误：{e}")
    exit()
BMI = user_weight / (user_height ** 2)
if BMI < 18.5:
    category = "偏瘦"
elif 18.5 <= BMI < 24:
    category = "正常"
else:
    category = "超重"
print(f"您的BMI分类：{category}")