import boto3
print('From root user')
aws_mag_con = boto3.session.Session(profile_name='root')
sts_mag_con = aws_mag_con.client('sts','ap-south-1')
result = sts_mag_con.get_caller_identity()
print(result)
print(result['UserId'])
print('From IAM user')
aws_mag_con = boto3.session.Session(profile_name='Amit')
sts_mag_con = aws_mag_con.client('sts','ap-south-1')
result = sts_mag_con.get_caller_identity()
print(result)
print(result['UserId'])
