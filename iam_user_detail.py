import boto3
import datetime
aws_mag_con = boto3.session.Session(profile_name='root')
iam_mag_con = aws_mag_con.resource('iam', 'ap-south-1')
'''
#Get details of any iam user

iam_user_ob = iam_mag_con.User("Amit")
#print(dir(iam_user_ob))
print(iam_user_ob.user_name , iam_user_ob.user_id , iam_user_ob.arn , iam_user_ob.create_date.strftime("%d-%m-%Y"))
'''

# Get details of all iam users

for iam_user_ob in iam_mag_con.users.all():
    print(iam_user_ob.user_name , iam_user_ob.user_id , iam_user_ob.arn , iam_user_ob.create_date.strftime("%d-%m-%Y"))
    