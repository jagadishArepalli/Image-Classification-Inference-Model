# Cloud Computing



### <ins>Project Demo</ins>

```sh
https://www.youtube.com/watch?v=v-UtoLRWc-c
```

### <ins>Steps to execute the code in AWS</ins>


### IAM role creation
•	Create an IAM role which has the following policies-
  * AWS S3 full access 
  * Sagemaker full access
  * AWS lambda execute permission policies.

### How to run the code in AWS SageMaker?
•	Navigate to notebook instances in the AWS sagemaker console and try to create a new notebook instance and choose an appropriate instance type for faster execution we have used ml.m5.xlarge, ml.m5.4xlarge and ml.c5.4xlarge.
•	After creating the new notebook instance open the notebook and in the left sidebar, choose the File Browser icon (   ) to display the file browser.
•	Now upload the files as it is like in this repository. (Except lambda.py)
•	Now download the dataset from https://www.kaggle.com/puneet6060/intel-image-classification/download, rename the zip file to imageclassification and upload it to the Jupyter Lab. 
•	After opening the notebook file(.ipynb) choose the kernel as conda_amazonei_pytorch_latest_p37 before execution.
Packages that need to be installed
•	Seaborn package must be installed before starting the execution.
•	!pip install seaborn

### How to run the code in AWS Lambda?
•	Create a new Lambda function in the AWS Lambda console and copy the code from the lambda_function.py and paste in the new function created.

### Creating and deploying API
•	Create a new POST API in the API gateway console and connect it to the lambda function created above.

### Results
For checking the results copy the url of the deployed API and paste it in the postman and give the json body in the below format.

#### Invoke URL


```sh
https://bveo5csfsh.execute-api.us-east-2.amazonaws.com/prod
```

#### Input parameters

```sh
{
   "url":"https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/139/015/1390157d4caaf290962de5c5fb4c42.jpg"
}

```
Or
 
Use the below curl syntax to check it in the terminal.

```sh
curl -i -X POST -d '{"url": "https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/139/136/139136bb43e41df8949f873fb44af.jpg"}' https://bveo5csfsh.execute-api.us-east-2.amazonaws.com/prod
```





