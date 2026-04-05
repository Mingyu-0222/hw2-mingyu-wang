# HW2 Mingyu Wang

## Project Overview

This project builds a simple GenAI workflow for summarizing meeting notes into action items.

The goal is to help teams quickly identify what needs to be done after a meeting. The system takes meeting notes as input and produces a structured list of action items as output. When possible, the output includes the task, the owner, and the deadline.

## Business Workflow

The workflow I chose is summarizing meetings into action items.

The user is a business professional or team member who attends meetings and needs a fast way to understand the next steps after the meeting.

The input to the system is a set of meeting notes or a meeting transcript, which may be unstructured and contain extra discussion.

The output of the system is a clear list of action items, including tasks, owners, and deadlines if that information is available.

This task is valuable because meetings often produce a large amount of information, but the most useful part is knowing what actions need to be taken. Automating part of this process can save time and improve team efficiency.

## Files in This Repository

1. `README.md`  
   This file explains the project and includes the video link.

2. `app.py`  
   A simple Python prototype that uses Google Gemini to turn meeting notes into action items.

3. `prompts.md`  
   This file shows the initial prompt and the revised versions.

4. `eval_set.md`  
   This file contains the evaluation cases used to test the workflow.

5. `report.md`  
   This file explains the business use case, model choice, prompt revision process, limitations, and deployment recommendation.

## How to Run the Prototype

1. Install the required package:

```bash
pip install google-genai
