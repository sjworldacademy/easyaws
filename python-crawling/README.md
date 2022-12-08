# aws command example
aws lambda list-functions
aws lambda invoke --profile lambda_easyaws --region ap-northeast-2 --function-name myLambdaTest out --log-type Tail |  base64 -d
aws lambda invoke --profile lambda_easyaws --region ap-northeast-2 --function-name myLambdaTest out --log-type Tail --query 'LogResult' --output text | base64 -d
