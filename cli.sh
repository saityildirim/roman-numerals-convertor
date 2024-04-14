aws ec2 run-instances \
   --image-id $(aws ssm get-parameters --names "//aws\service\ami-amazon-linux-latest\al2023-ami-kernel-default-x86_64" --query \
   'Parameters[0].[Value]' --output text) \
   --count 1 \
   --instance-type t2.micro\
   --key-name firstkey\
   --security-group-ids sg-0c83196c8fee225d4 \
   --user-data file://userdata.sh