import boto3
import time
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')
ec2_mag_cli = aws_mag_con.client('ec2','ap-south-1')

'''
#This can be used for Method 1 and Method 2 , Method 3 and Method 4 has their own way
I = input("Enter Instance Id: ")
my_instance_ob = ec2_mag_con.Instance(I)
print("Starting the instance..")
my_instance_ob.start()
'''

'''
#Method 1
# This is a normal method for waiting
while True:
    my_instance_ob = ec2_mag_con.Instance(I)
    print("The current state of Instance is: " + my_instance_ob.state["Name"])
    if my_instance_ob.state["Name"] == "running":
        break
    else:
        print("waiting for running status...")
        time.sleep(5) 
print("Now your instance is running")           

'''

'''
#Method 2
#This is a method for function wait_until_running
my_instance_ob.wait_until_running() #This will wait for 200 seconds (Waiter resource will check 40 times)
print("Now your Instance is running") 
'''
'''
#Method 3
#This is the method to use waiters function itself( can be only used with client)
I = input("Enter Instance Id: ")
ec2_mag_cli.start_instances(InstanceIds=[I])
print("Starting Instance...")
waiter = ec2_mag_cli.get_waiter('instance_running')
print("Waiting for instance to run...")
waiter.wait(InstanceIds=[I]) #This will recheck everything in every 15 seconds (40 times)
print("Now your instance is running")
'''

#Method 4
#This is the hybrid method where we create object and start instance with resource and waiter will be of client object
I = input("Enter Instance Id: ")
my_instance_ob = ec2_mag_con.Instance(I)
print("Starting the instance..")
my_instance_ob.start()
waiter = ec2_mag_cli.get_waiter('instance_running')
print("Waiting for instance to run...")
waiter.wait(InstanceIds=[I]) #This will recheck everything in every 15 seconds (40 times)
print("Now your instance is running")