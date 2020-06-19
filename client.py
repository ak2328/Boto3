import boto3
aws_mag_con = boto3.session.Session(profile_name='Amit')
iam_mag_con = aws_mag_con.client('iam', 'ap-south-1')
ec2_mag_con = aws_mag_con.client('ec2', 'ap-south-1')
s3_mag_con = aws_mag_con.client('s3', 'ap-south-1')

#List all the users using client 
print('IAM......!')
result = iam_mag_con.list_users()
for each in result['Users']:
    print(each['UserName'])

print('EC2......!')
result = ec2_mag_con.describe_instances()
for each in result['Reservations'] :
    for each_instance in each['Instances']:
        print(each_instance['Tags'][0]['Value'], each_instance['InstanceId'])

print('S3.......!')
result = s3_mag_con.list_buckets()
for each in result['Buckets']:
    print(each['Name'])       
