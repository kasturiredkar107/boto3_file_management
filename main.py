import boto3

s3=boto3.client('s3')

def  create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': s3.meta.region_name}
                     )
        print(f"Bucket {bucket_name} created successfully")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"{bucket_name} already owned by you")
    except Exception as e:
        print("Error creating bucket",e)

def upload_file(bucket_name,files,s3file_name):
    try:
        s3.upload_file(files,bucket_name,s3file_name)
        print(f"{files} uploaded successfully in {bucket_name} as {s3file_name}")
    except Exception as e:
        print("Exception reached",e)

def list_files(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in response:
            print("Yes its present")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print("No files found")
    except Exception as e:
        print("Exception listing",e)

def download_file(bucket_name, key_name, download_path):
    try:
        s3.download_file(bucket_name, key_name, download_path)
        print(f"file {key_name} downloaded to {download_path}")
    except Exception as e:
        print("error in downloading",e)

if __name__=="__main__":
    bucket_name = "kasturiboto3project"
    files = "textfile.txt"

    #create a test file
    with open(files,"w") as file:
        file.write("Inside using boto3")

    create_bucket(bucket_name)
    upload_file(bucket_name,files,"boto3_test.txt")
    list_files(bucket_name)
    download_file(bucket_name,"boto3_test.txt","C:\\Users\\LIC\\Downloads\\downloaded_s3file")
    
