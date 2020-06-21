import  boto3
aws_mag_con = boto3.session.Session(profile_name='root')
vol_mag_con = aws_mag_con.resource('ec2','ap-south-1')
'''
#Resource
f1 = {"Name": "status" , "Values": ["available"]}
for each in vol_mag_con.volumes.filter(Filters=[f1]):
    if not each.tags:
        print(each.id, each.state, each.tags)
        print("Deleting unused and untagged volumes")
        each.delete()
print("Deleted unused and untagged volumes")                
'''

vol_mag_cli = aws_mag_con.client('ec2','ap-south-1')
for each in vol_mag_cli.describe_volumes()['Volumes']:
    if not 'Tags' in each and each['State']=='available':
        print("Deleting volume", each['VolumeId'])
        vol_mag_cli.delete_volume(VolumeId=each['VolumeId'])
print("Deleted unused and untagged volumes")        

