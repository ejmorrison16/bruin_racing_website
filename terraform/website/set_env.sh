#!/usr/bin/env bash

# Input env variables
# ENV

if [ -z "$ENV" ]; then
   echo "error: Environment var ENV not set" >&2
fi

export ORG=bruinracing
export APP=website
export OWNER=lisa

# export AWS_PROFILE="$ORG-$ENV"
export AWS_PROFILE="$ORG"

# S3_BUCKET=www.bruinracing.com

export TF_VAR_env=$ENV
export TF_VAR_org=$ORG
export TF_VAR_owner=$OWNER
export APP_NAME=$APP
export TF_VAR_app_name=$APP_NAME
export TF_VAR_app_name_hyphen=$APP_NAME
export TF_VAR_app_name_underscore=$(echo "$APP_NAME" | tr '-' '_')
export TF_VAR_app_name_alpha=$(echo "$APP_NAME" | tr -d -c '[a-zA-Z0-9]')
export TF_VAR_ssh_public_key=$SSH_PUBLIC_KEY
export TF_VAR_remote_state_s3_bucket_name="${ORG}-${TF_VAR_app_name_hyphen}-${ENV}-tfstate"
export TF_VAR_remote_state_s3_bucket_name_prefix="${ORG}-${TF_VAR_app_name_hyphen}"
export TF_VAR_remote_state_s3_key_prefix="${ENV}/"
#export TF_VAR_remote_state_s3_key_prefix="${TF_VAR_app_name_hyphen}/${ENV}"
if [[ $ENV = *"china"* ]]; then
  export TF_VAR_remote_state_s3_bucket_region=cn-north-1
else
  export TF_VAR_remote_state_s3_bucket_region=us-east-1
fi
# export TF_VAR_key_name=$AWS_KEYPAIR
# export SSH_PUBLIC_KEY=$(cat ~/.ssh/id_rsa.pub)

# Name of EC2 keypair to use for instances
export TF_VAR_keypair_name=$ORG-$ENV
