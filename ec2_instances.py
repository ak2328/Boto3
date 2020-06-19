import boto3
from pprint import pprint
aws_mag_con = boto3.session.Session(profile_name='Amit')
ec2_mag_con = aws_mag_con.client('ec2','ap-south-1')

result = ec2_mag_con.describe_instances()
for each in result['Reservations']:
        for each_item in each['Instances']:
            print('--------')
            print("Then name of instance: {}\n The Image id is: {}\n The instance id is: {}\n The instance launch time is: {}\n The Hypervisor is: {}\n The current state of instance is: {}".format(each_item['Tags'][0]['Value'],each_item['ImageId'],each_item['InstanceId'],each_item['LaunchTime'].strftime("%d-%m-%Y"),each_item['Hypervisor'],each_item['State']['Name']))


