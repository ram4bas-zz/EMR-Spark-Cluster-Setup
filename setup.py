$ aws emr create-cluster --name "Ram Spark Cluster" --release-label \
   emr-4.3.0 --applications Name=Spark Name=Zeppelin-Sandbox \
   --ec2-attributes KeyName=cloudacademy-keypair --instance-type m3.xlarge \
   --instance-count 3 --use-default-roles
{
    "ClusterId": "Ram-1234567890"
}

#After issuing the aws emr create-cluster command, AWS will return the cluster ID. This cluster ID can be used in all the subsequent aws emr commands.
# We can view the details of the clusters using the aws emr describe-cluster command.

aws emr describe-cluster --cluster-id Ram-1234567890

### SSH to the master node
# we can issue the aws emr ssh command.

aws emr ssh --cluster-id Ram-1234567890 \
   --key-pair-file ./ramkeypair-keypair.pem
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=10 \
   -i ./amkeypair-keypair.pem hadoop@ec2-[hostname_name].compute-1.amazonaws.com
   
  
  
  
  
  #For Scala, we can use the spark-shell interpreter.
  $spark-shell
  
  
  
  #For pyspark, we can use the spark-shell interpreter.
  $pyspark
  
  
