import boto3                                                                                                              
from random import choice                                                                                                 
import sys                                                                                                                
import csv                                                                                                                          
                                                                                                                          
                                                                                                                          
def get_iam_client_object():                                                                                              
    session=boto3.session.Session(profile_name="root")                                                                
    iam_client=session.client(service_name="iam",region_name="us-east-1")                                                 
    return iam_client                                                                                                     
                                                                                                               
def main():                                                                                                               
   iam_client=get_iam_client_object()                                                                                     
   Iam_user_name="ak2328" 
   number = '0918273746537382992'                                                                              
                                                                                        
   PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"                                                                
   try:                                                                                                                   
      iam_client.create_user(UserName=Iam_user_name)                                                                      
   except Exception as e:                                                                                                 
      if e.response['Error']['Code']=="EntityAlreadyExists": # pylint: disable=no-member                                                          
          print("Already Iam User with {} is exist".format(Iam_user_name))                                                 
          sys.exit(0)                                                                                                     
      else:                                                                                                               
         print("Please verify the following error and retry")                                                              
         print(e)                                                                                                          
         sys.exit(0)                                                                                                      
   response = iam_client.create_access_key(UserName=Iam_user_name)                                                        
   #print("IAM User Name={}".format(Iam_user_name))                                                                         
   #print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))                                                                                                               
   iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn) 
   CSV_NAME = 'IAMCRED{}.csv'.format(choice(number))
   csv_ob=open(CSV_NAME,"w",newline='')
   csv_w= csv.writer(csv_ob)
   csv_w.writerow(["UserName","AccessKey","AccessKeyId"])
   csv_w.writerow([ Iam_user_name , response['AccessKey']['AccessKeyId'] , response['AccessKey']['SecretAccessKey']])                                                                                       
   return None                                                                                                            
                                                                                                                          
if __name__=="__main__":                                                                                                  
    main()                  