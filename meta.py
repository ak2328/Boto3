#Changing resource object into client object
import boto3
aws_mag_con = boto3.session.Session(profile_name='root')
regions_re = aws_mag_con.resource('ec2')

for each in regions_re.meta.client.describe_regions()['Regions']:
    print(each['RegionName'])