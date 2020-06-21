import boto3
import datetime
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')


sts_mag_con = aws_mag_con.client('sts','ap-south-1')
result = sts_mag_con.get_caller_identity()
sts = result['UserId']
today = datetime.datetime.now()
start_time = str(datetime.datetime(today.year , today.month , 21, 20,28,19))
#print(start_time)
for each in ec2_mag_con.snapshots.filter(OwnerIds=[sts]):
    if each.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time:
        print(each.id , each.start_time.strftime("%Y-%m-%d %H:%M:%S"))


