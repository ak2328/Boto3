import boto3
aws_mag_con = boto3.session.Session(profile_name='root')
iam_mag_con = aws_mag_con.resource('iam', 'ap-south-1')
ec2_mag_con = aws_mag_con.resource('ec2', 'ap-south-1')
s3_mag_con = aws_mag_con.resource('s3', 'ap-south-1')

result = iam_mag_con.users
for each in result.limit(2):
    print(each.name)