# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# studentInfo = {
#     "Mamun": {
#         "Name": "Mamun",
#         "Location": "Pabna",
#         "Study": "Student",
#         "Subject": "Social Sciences",
#         "Roll": 20,
#         "Age": 18,
#         "Gender": "Male",
#         "Year": 1999,
#     }
# }
# print(studentInfo)

# Python - Access Dictionary Items
# print(studentInfo["Mamun"]["Year"])

# x = studentInfo.get("Mamun")
# print(x)
# x = studentInfo.keys()
# print(x)
# print(studentInfo.values())

# studentInfo["Year"] = 2005
# print(studentInfo["Year"])

# Update the "year" of the car by using the update() method:
# studentInfo.update({"Shishir":"He is an CSE Student"})
# print(studentInfo["Shishir"])
# Python - Add Dictionary Items
# studentInfo.pop("Mamun")
# print(studentInfo)
#
# x = {'type': 'fruit', 'name': 'banana'}
#
# print(x)
# for a in studentInfo1:
#     print(a)
# for x in studentInfo1.values():
#     print(x)
# studentInfo1 = {
#     "Shishir": {
#         "Name": "Mamun",
#         "Location": "Pabna",
#         "Study": "Student",
#         "Subject": "Social Sciences",
#         "Roll": 20,
#         "Age": 18,
#         "Gender": "Male",
#         "Year": 1999,
#     }
# }
# Studentid = {
#     "Sum1" : 20,
#     "Sum2" : 30,
#     "Sum3" : 40
# }
# print(Studentid)
# myDict = Studentid.copy()
print(Studentid)

x = dict(Studentid)
print(x)
