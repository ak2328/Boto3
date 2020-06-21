import boto3
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')
ec2_mag_cli = aws_mag_con.client('ec2','ap-south-1')

sts_mag_con = aws_mag_con.client('sts','ap-south-1')
result = sts_mag_con.get_caller_identity()
sts = result['UserId']
# Resource Method
f_size = {"Name":"volume-size", "Values":['8']}
f1 = {"Name": "tag:Name" , "Values":["Ansible"]}
for each in ec2_mag_con.snapshots.filter(OwnerIds=[sts] , Filters = [f_size,f1]):
    print(each)

# Client Method
f_size = {"Name":"volume-size", "Values":['8']}
f1 = {"Name": "tag:Name" , "Values":["Ansible"]}
print("Using client Object")
for each in ec2_mag_cli.describe_snapshots( Filters = [f_size,f1], OwnerIds=[sts])['Snapshots']:
    print(each['SnapshotId'])
    
