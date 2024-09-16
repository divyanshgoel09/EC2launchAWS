# EC2launchAWS
A user can launch a EC2 instance on your AWS account by just clicking on a link provided by you 
Here we used AWS Lambda, AWS EC2 Instance, AWS API Gateway.

In the given python code by the help of BOTO3 library we write a code that launches a EC2 instance on the LINK provider account and when that EC2 instance get into the Running state the subscribed user (AWS account owner or we can say the concerned user that we have added in Subscription result) of SNS will receive a notification
**First we made a AWS lambda function where we used the BOTO3 library of python which launches EC2 instance on our accouunt.**
![2222](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/050822ef-a413-439d-a827-7247a0b366b1)
_The python code is avaiable in file._

**To trigger that we made a API gateway where by using that API we trigger the lambda function to LAUNCH EC2 instance.**
![4444](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/34088f72-5471-4917-bb93-5e621a153cc2)

**Also we added a SNS service which send the E-mail to AWS account owner that a Instance has been launched on their AWS account.**
![3333](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/5d203162-8c2b-4b25-aeaa-19ae1792165a)

Example of link to trigger 
![55555](https://github.com/divyanshgoel09/EC2launchAWS/assets/118998853/29cc86ae-1280-43e0-974e-4b1bc4d7c153)

