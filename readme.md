```sh
aws --endpoint-url=http://localhost:4566 s3 ls --profile localstack
aws --endpoint-url=http://localhost:4566 s3 ls s3://eu-docker-klarna-data-eu --recursive
aws --endpoint-url=http://localhost:4566 s3 ls s3://eu-docker-klarna-data-eu --recursive

aws --endpoint-url=http://localhost:4566 s3api get-bucket-notification --bucket eu-docker-klarna-data-eu --profile localstack
# get all sqs
aws --endpoint-url=http://localhost:4566 sqs list-queues --profile localstack
# get arn of sqs
aws --endpoint-url=http://localhost:4566 sqs get-queue-attributes --queue-url "http://localhost:4566/000000000000/validation-service-s3-import-docker"  --attribute-names QueueArn |jq .Attributes.QueueArn -r
# recive all messages
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url "http://localhost:4566/000000000000/bookkeeping-events-validation-s3-import-docker.fifo"  --attribute-names All --message-attribute-names All --max-number-of-messages 10
```
```sh
#### All cloudforamtion
aws --endpoint-url=http://localhost:4566  cloudformation list-stacks
# check if success occured
aws --endpoint-url=http://localhost:4566 cloudformation describe-stacks --stack-name bi-framework-docker
aws --endpoint-url=http://localhost:4566  cloudformation list-exports
```

aws --region eu-west-1 --endpoint-url=http://localhost:4566 cloudformation validate-template --template-body file://cfn-lambda.yaml


aws --region eu-west-1 --endpoint-url=http://localhost:4566 cloudformation create-stack \
   --stack-name test5 \
   --template-body file://cfn-lambda.yaml \
   --parameters \
		ParameterKey=Environment,ParameterValue="docker" \
		ParameterKey=ServiceName,ParameterValue="bi-frame"
   aws --region eu-west-1 --endpoint-url=http://localhost:4566  cloudformation wait stack-create-complete \
		--stack-name test5



```sh
aws --endpoint-url=http://localhost:4566 lambda list-functions
aws --endpoint-url=http://localhost:4566 \
lambda list-event-source-mappings \
    --function-name test16-primer-ac104961

aws --endpoint-url=http://localhost:4566 \
lambda get-event-source-mapping \
    --uuid "06cd0097-46e6-4aec-9a3f-a2414afdc69b"

aws --endpoint-url=http://localhost:4566 iam list-roles 

 aws --endpoint-url=http://localhost:4566 \
 sns publish --topic-arn "arn:aws:sns:eu-west-1:000000000000:bookkeeping-events-validation-internal-notifications-docker.fifo" \
 --message-group-id 123 \
 --message "test message for pub-sub-test topic"
aws --endpoint-url=http://localhost:4566 sns get-topic-attributes \
--topic-arn "arn:aws:sns:eu-west-1:000000000000:bookkeeping-events-validation-internal-notifications-docker.fifo"
aws --endpoint-url=http://localhost:4566 sns list-subscriptions
aws --endpoint-url=http://localhost:4566 sns get-subscription-attributes \
--subscription-arn "arn:aws:sns:eu-west-1:000000000000:bookkeeping-events-validation-internal-notifications-docker.fifo:9c866066-cfe2-4c11-90db-668bc1d40f9a"
```