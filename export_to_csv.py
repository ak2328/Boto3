import boto3
import csv
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="ap-south-1")
ec2_mag_cli = aws_mag_con.client('ec2','ap-south-1')
cnt=1
vol_id = []
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
for each__vol_id in ec2_mag_cli.describe_volumes()['Volumes']:
               vol_id.append(each__vol_id['VolumeId'])
for each in ec2_con_re.instances.all():
	print(cnt,vol_id[cnt],each,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
	csv_w.writerow([cnt,vol_id[cnt],each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

	cnt+=1
csv_ob.close()
