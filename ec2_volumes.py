import boto3
from pprint import pprint
aws_mag_con = boto3.session.Session(profile_name='Amit')
ec2_mag_con = aws_mag_con.client('ec2','ap-south-1')

result = ec2_mag_con.describe_volumes()
for each_item in result['Volumes']:
            print('--------')
            print("The volume id is: {}\nThe AvailabilityZone is: {}\nThe VolumeType is: {}".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))
