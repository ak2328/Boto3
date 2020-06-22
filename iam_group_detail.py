import boto3
import datetime
aws_mag_con = boto3.session.Session(profile_name='root')
iam_mag_con = aws_mag_con.resource('iam', 'ap-south-1')
'''
#Get details of any iam group

iam_group_ob = iam_mag_con.Group("Permissions")
#print(dir(iam_group_ob))
print(iam_group_ob.group_name , iam_group_ob.group_id , iam_group_ob.arn , iam_group_ob.create_date.strftime("%d-%m-%Y"))
'''

# Get details of all iam users

for iam_group_ob in iam_mag_con.groups.all():
    print(iam_group_ob.group_name , iam_group_ob.group_id , iam_group_ob.arn , iam_group_ob.create_date.strftime("%d-%m-%Y"))
   