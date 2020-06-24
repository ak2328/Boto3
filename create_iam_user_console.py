import boto3
from random import choice
import xlsxwriter 
import csv
import sys
import pylint

def get_iam_client_object():
    session = boto3.session.Session(profile_name='root')
    iam_client_object = session.client('iam' , 'ap-south-1')
    return iam_client_object

def get_random_password():
    len_pass = 8
    vali_car = "lffdjdikdofvovndmwlwpdpe9292887@$$#%#^&@*&*(@()@))VVFVSBBSSNWJHJEJAKMSBFMDKOUBDBBD@#$%^&**()?"
    return  "".join(choice(vali_car) for each in range(len_pass))

def main():
    iam_client = get_iam_client_object()
    Iam_User_Name = "ak2328"
    number = '0918273746537382992'
    password = get_random_password()
    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    #print(dir(iam_client))  
    try: 
        iam_client.create_user(UserName = Iam_User_Name) 
    except Exception as e:
       if  e.response['Error']['Code']=='EntityAlreadyExists': # pylint: disable=no-member
           print("Already Iam User with {} is exist".format(Iam_User_Name))                                                 
           sys.exit(0)
       else:                                                                                                               
         print("Please verify the following error and retry")                                                              
         print(e)                                                                                                          
         sys.exit(0)          
    iam_client.create_login_profile(UserName = Iam_User_Name , Password = password ,PasswordResetRequired = True )
    iam_client.attach_user_policy(UserName = Iam_User_Name , PolicyArn = PolicyArn)
    response = iam_client.create_access_key(UserName=Iam_User_Name) 
    #print("IAM User Name={} and Password={}".format(Iam_User_Name , password))
    Arn = iam_client.get_user(UserName='ak2328')['User']['Arn']
    CSV_NAME = 'IAMCRED{}.csv'.format(choice(number))
    csv_ob=open(CSV_NAME,"w",newline='')
    csv_w= csv.writer(csv_ob)
    csv_w.writerow(["UserName" , "Password" , "Arn","AccessKey","AccessKeyId"])
    csv_w.writerow([Iam_User_Name , password , Arn , response['AccessKey']['AccessKeyId'] , response['AccessKey']['SecretAccessKey']])
    print("User Created")
    return None
    

if __name__ == "__main__":
     main()       