# COMMUNICATION-BRIDGE-FOR-WEBSITE-DEVELOPMENT-TEAM

## Introduction

The Communication Bridge for Website Development Team is an automation system designed to streamline communication between the Meetly Team and Website Team using n8n, AWS Bedrock (Claude 3.5 Sonnet), and AWS DynamoDB.

This workflow automatically extracts website requirements from meeting transcripts, structures them into standardized JSON, sends them to the Website Team, gathers image and voice script requests, emails the results to the Meetly Team, and logs all activities in AWS DynamoDB for auditing and tracking purposes.

## Project Overview

The project eliminates manual dependency in communication between multiple teams by using AI and workflow
automation.

## Features

✅ Automatic Gmail trigger for new transcripts
✅ AI-based transcript analysis (AWS Bedrock – Claude 3.5 Sonnet)
✅ Converts outputs to structured “website instruction JSON”
✅ Sends structured data to Website Team via Webhook
✅ Converts website team responses (images/voice scripts) into plain text email
✅ Sends formatted email back to Meetly Team
✅ Logs entire execution (AI output, metadata, timestamps) into AWS DynamoDB

## Technologies and Tools Used

| Category                | Technology / Tool               | Purpose                                            |
| ----------------------- | ------------------------------- | -------------------------------------------------- |
| Artificial Intelligence | AWS Bedrock (Claude 3.5 Sonnet) | Transcript analysis and structured JSON generation |
| Workflow Automation     | n8n                             | Workflow orchestration and automation              |
| Email Automation        | Gmail API                       | Sending and receiving email communication          |
| Cloud Storage           | AWS DynamoDB                    | Storing execution logs                             |
| Serverless Compute      | AWS Lambda                      | Writing logs into DynamoDB                         |
| API Management          | AWS API Gateway                 | Providing HTTP endpoint for logging                |
| Scripting               | JavaScript, Python (within n8n) | Data transformation and parsing                    |
| Testing                 | webhook.site, n8n Cloud URLs    | Testing webhook endpoints                          |

## System Architecture

```
            +-------------------+
            |    Meetly Team    |
            | (Sends Transcript)|
            +---------+---------+
                      |
                      v
         +--------------------------+
         | Gmail Trigger (n8n)      |
         | Fetches Email & JSON File|
         +-----------+--------------+
                     |
                     v
        +---------------------------+
        | Move Binary Data (to JSON)|
        | & Validate JSON Structure |
        +-----------+---------------+
                    |
                    v
       +----------------------------------------+
       | AI Agent – Analyze Transcript/JSON     |
       | (Claude 3.5 Sonnet via AWS Bedrock)    |
       +------------------+---------------------+
                          |
                          v
       +----------------------------------------+
       | Clean & Parse AI JSON                  |
       | Extracts website_type, sections, etc.  |
       +------------------+---------------------+
                          |
                          v
       +----------------------------------------+
       | Send to Website API                    |
       | Forwards instructions to Website Team  |
       +------------------+---------------------+
                          |
                          v
       +----------------------------------------+
       | Convert JSON to Plain Text             |
       | Formats Website Team Response          |
       +------------------+---------------------+
                          |
                          v
       +----------------------------------------+
       | Send Email to Meetly Team              |
       | Summarizes images/scripts needed       |
       +------------------+---------------------+
                          |
                          v
       +----------------------------------------+
       | Log to AWS DynamoDB                    |
       | Via Lambda + API Gateway Endpoint      |
       +----------------------------------------+
```

## Prerequisites

Before running this project, ensure the following are set up:

* n8n Cloud or Self-Hosted Instance
* AWS Account with access to Bedrock, DynamoDB, Lambda, and API Gateway
* Gmail Account (with OAuth2 credentials connected to n8n)
* Basic understanding of workflow automation and cloud configuration

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/communication-bridge-workflow.git
cd communication-bridge-workflow

### Step 2: Import Workflow in n8n

Open n8n.io

Go to Workflows → Import from File

Select and import workflows/v6.json

Ensure all nodes are connected as per the provided flow

### Step 3: Configure Environment Variables

In n8n:

Open the Workflow Config node

Set:

websiteApiUrl → Your Website Team webhook URL

logApiUrl → Your AWS API Gateway endpoint URL

Example:

{
  "websiteApiUrl": "https://your-n8n-cloud.webhook/receive-usecase",
  "logApiUrl": "https://your-api-gateway.amazonaws.com/prod/logs"
}

### Step 4: Connect Required Credentials

Gmail Trigger → Connect Gmail OAuth2 account

AWS Bedrock Chat Model → Configure AWS credentials

Region: us-east-1 (or your region)

Model ID: anthropic.claude-3-5-sonnet-20240620-v1:0

### Step 5: AWS Setup for Logging

1. Create a DynamoDB Table

Table Name: WorkflowLogs

Primary Key: executionId (String)

2. Create AWS Lambda Function

Upload aws/lambda_logger.py script

Add necessary IAM permissions for DynamoDB PutItem

3. Create an API Gateway

Create a POST endpoint that triggers your Lambda function

Copy the API Gateway endpoint URL

Paste it into n8n → Workflow Config → logApiUrl

### step 6: Running the Workflow

Once the setup is complete:

1. Activate the workflow in n8n (Active switch on top-right).

2. Send a JSON transcript email to the connected Gmail inbox from the Meetly team.

3. Observe the automated execution:

Transcript is analyzed → AI generates JSON → Data sent to Website API

Website response → Converted to plain text → Email sent to Meetly team

Execution details logged to AWS DynamoDB

You can view logs either in:

AWS DynamoDB Table

Or via your API Gateway test logs


### Developed by: Sujitha

```
