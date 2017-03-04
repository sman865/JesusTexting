# JesusTexting
Wake up to a text that gives you something spiritually productive to do each day. Uses AWS SNS texting service.

## About
If you use this service you will recieve 7 texts with the following items to do each week:

* 2 Bible chapters to read
* 2 things to pray about
* 1 person to do a good deed for
* 1 thing to listen to/watch (video/podcast/song of your choice)
* 1 day of rest

## Setup/Dependencies
* python3
* [boto3](https://github.com/boto/boto3). Use their installation instructions or just `pip install boto3`
* A linux server that supports cron
* An Amazon AWS account

## Instructions
### Main setup
1. `mkdir ~/JesusTexting`
1. Add `JesusTexting.py` and `JTSetup.sh` to the above directory
1. Edit the `PhoneNumber` line in JesusTexting.py to the phone number you want to text
1. Edit your crontab with `crontab -e` and add the following lines:

        needs
        to be
        added
1. You should now receive daily texts. The order will be randomized each Sunday night.

### AWS setup example (you just need these two files in ~/.aws)
1. Edit to use your region

        $ cat ~/.aws/config
        [default]
        region=us-west-2
1. Get credentials from: aws console->click your name at the top right of the page->security credentials

        $ cat ~/.aws/credentials
        [default]
        aws_access_key_id = YOURS_HERE
        aws_secret_access_key = YOURS_HERE
