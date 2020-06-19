import boto3

#aws_mag_con = boto3.session.Session(profile_name= "root")

iam_mag_con = boto3.resource('iam','ap-south-1') #only when we have some default entry without profile tag

iam_mag_con_2= boto3.client('iam','ap-south-1')

for each_user in iam_mag_con.users.all():
    print(each_user.name)

#print(aws_mag_con.get_available_resources())

print(type(iam_mag_con_2.list_users()['Users']))

print(iam_mag_con_2.list_users()['Users'][0]['UserName'])


