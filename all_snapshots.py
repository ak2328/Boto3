import boto3
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')

sts_mag_con = aws_mag_con.client('sts','ap-south-1')
result = sts_mag_con.get_caller_identity()
sts = result['UserId']

for each in ec2_mag_con.snapshots.filter(OwnerIds=[sts]):
    print(each)
