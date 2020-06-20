import boto3
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')
f1 = {"Name": "instance-state-name" , "Values":["running","stopped"]}
f2 = {"Name": "instance-type" , "Values":["t2.micro"]}
f3 = {"Name": "tag:Name" , "Values":["Ansible", "Jenkins-Project"]}
for each in ec2_mag_con.instances.filter(Filters=[f1,f2,f3]):
    print(each)