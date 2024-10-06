# #ladderize if statement
# temp = int(input("Enter temp: "))
# if(temp>100):
#     print("Steam")
# elif(temp==100):
#     print("Boiling Point")
# elif(temp==0):
#     print("Freezing Point")

# grade = 84
# if grade >= 95 and grade <=100:
#     print('Excellent')
# elif grade >= 90 and grade <= 94:
#     print('Outstanding')
# elif grade >= 85 and grade <= 89:
#     print('Very Good')
# elif grade >= 80 and grade <= 84:
#     print('Good')
# elif grade >=75 and grade <= 79:
#     print('Poor')
# elif grade < 75:
#     print('Failed')
grade = 4
if grade > 100:
    print('Grade out of range')
elif grade >= 95:
    print('Excellent')
elif grade >= 90:
    print('Outstanding')
elif grade >= 85:
    print('Very Good')
elif grade >= 80:
    print('Good')
elif grade >= 75:
    print('Poor')
elif grade >= 0:
    print('Failed')