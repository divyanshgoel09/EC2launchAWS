import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    myec2 = boto3.resource(
        service_name="ec2", #give service name here
        aws_access_key_id=" #enter your access key id ",  #we can also add access key id and secret access key in environment variable instead of giving the here as setting up in environment variable is a good practice
        aws_secret_access_key=" #enter your secret access key ", 
        region_name="ap-south-1"
    )
    mysns = boto3.client("sns")
    
    myos = myec2.create_instances(
        ImageId="ami-00fa32593b478ad6e",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
    )
    
    instance = myos[0]
    instance.wait_until_running()
    instance.reload()

    if instance.state['Name'] == 'running':
        mysns.publish(
            TopicArn='arn:aws:sns:ap-south-1:654654630405:TestSNS',
            Message=f'Hi, an instance on your AWS account launched with Instance ID: {instance.id}',
            Subject='EC2 launched on your Account'
        )
    
    print(instance.id)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello! EC2 Launched Successfully!!!! {instance.id}')
    }
