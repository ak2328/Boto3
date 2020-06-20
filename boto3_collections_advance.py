import boto3
import time
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')
ec2_mag_cli = aws_mag_con.client('ec2','ap-south-1')

'''
all_instances_ids = []
for each in ec2_mag_con.instances.all():
    all_instances_ids.append(each.id)
#print(dir(ec2_man_con.instances)
waiter = ec2_mag_cli.get_waiter('instance_running')
print("Starting all instances")
ec2_mag_con.instances.start()
print("Waiting for instance to run...")
waiter.wait(InstanceIds=all_instances_ids)
print("Your all instances are up and running")
'''
'''
name_ids = []
f1 = {"Name": "tag:Name" , "Values":["Ansible"]}
for each in ec2_mag_con.instances.filter(Filters=[f1]):
    name_ids.append(each.id)
print(name_ids) 
print("Starting intances with ids of : ",name_ids)
ec2_mag_cli.start_instances(InstanceIds=name_ids)
waiter=ec2_mag_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=name_ids)
print("Your instances are up and running....")
'''
name_ids = []
f1 = {"Name": "tag:Name" , "Values":["Ansible"]}
for each in ec2_mag_cli.describe_instances(Filters=[f1])['Reservations']:
    for each_in in each['Instances']:
            name_ids.append(each_in['InstanceId'])
print(name_ids) 
print("Starting intances with ids of : ",name_ids)
ec2_mag_cli.start_instances(InstanceIds=name_ids)
waiter=ec2_mag_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=name_ids)
print("Your instances are up and running....")    