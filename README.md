# DJANGO SQS CELERY EXAMPLE

## About

This is just a basic example of how to set up django with celery and SQS as a broker

### Requirements

1. Docker installed

### HOW TO

1. Create SQS on AWS
2. Add required information in your environment - for developing I suggest to create
.env file and add required information there
3. Run:
    ```shell
    make buld
   ```
   this command will create django and celery containers
4. To run django app run:
     ```shell
   make run-app
   ```
5. Open your browser and go to http://localhost:8000/ and test. 
You should see running tasks in your terminal logs, and events in AWS SQS
   