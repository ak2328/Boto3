import boto3
import sys
aws_mag_con = boto3.session.Session(profile_name='root')
ec2_mag_con = aws_mag_con.resource('ec2','ap-south-1')
while True:
    print("The script performs following actions on ec2")
    print("""
              1. start
              2. stop
              3. reboot
              4. Terminate
              5. Exit""")
    opt= int(input("Enter Your Choice: "))
    if opt==1:
        instance_id=input("Enter your Instance Id: ")
        instance_obj = ec2_mag_con.Instance(instance_id)
        print("Starting Instance")
        instance_obj.start()
    elif opt==2:
        instance_id=input("Enter your Instance Id: ")
        instance_obj = ec2_mag_con.Instance(instance_id)
        print("Stopping Instance")
        instance_obj.stop()
    elif opt==3:
       instance_id=input("Enter your Instance Id: ")
       instance_obj = ec2_mag_con.Instance(instance_id)
      # print(dir(instance_obj))
       print("Rebooting Instance: ")
       instance_obj.reboot()
    elif opt==4:
        instance_id=input("Enter your Instance Id: ")
        instance_obj = ec2_mag_con.Instance(instance_id)
        print("Terminating Instance")
        instance_obj.terminate() 
    elif opt==5:
        print("Thank You")
        sys.exit(0)
    else:
        print("Option is invalid")                           