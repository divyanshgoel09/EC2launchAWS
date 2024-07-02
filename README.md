# EC2launchAWS
A user can launch a EC2 instance on your AWS account by just clicking on a link provided by you 

A first we made a AWS lambda function where we used the BOTO3 library of python which launches EC2 instance on our accouunt.
![2222](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/050822ef-a413-439d-a827-7247a0b366b1)
The python code is avaiable in file.

To trigger that we made a API gateway where by using that API we trigger the lambda function to LAUNCH EC2 instance.
![4444](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/5c2b45f4-1a57-4113-95d6-c5f3996fa21e)

Also we added a SNS service which send the E-mail to AWS account owner that a Instance has been launched on their AWS account.
![3333](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/5d203162-8c2b-4b25-aeaa-19ae1792165a)
