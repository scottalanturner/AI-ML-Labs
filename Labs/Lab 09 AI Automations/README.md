# Lab 08: AI Automations – Building Your First Workflow in Make.com or n8n

## Tools (All Free)

- **Make.com** – Visual no-code automation builder
- **OR n8n.io** – Open-source workflow automation tool
- **Gmail, Google Sheets, or any app** that supports triggers/actions

## Overview

In this self-paced lab, you'll become an Automation Creator by building your first workflow using Make.com or n8n. You'll connect simple tools—like Google Sheets and Gmail—to automate a process that normally requires manual effort.

This lab introduces foundational concepts behind automation pipelines, which are essential in both AI and MLOps. Whether you're automating a business process or retraining a machine learning model, the same logic applies: detect, trigger, act, and monitor.

**Note:** We won't be adding any AI nodes to these workflows. The reason is they require paid services to get API access. In the video for this module the nodes that were communicating with OpenAI/Anthropic/Gemini all had paid API access to allow them to work.

If you get stuck, use the built-in AI companion to get suggestions on how to wire things up or use ChatGPT for troubleshooting and help. You have to keep building your prompt engineering skills to get better at it.

## Learning Objectives

By the end of this lab, you will be able to:

1. Explain the purpose of triggers, actions, and workflows in automation systems.
2. Build and test a working automation using Make.com or n8n.
3. Connect multiple apps to move data automatically between them.

## Part 1: Setup

1. Create a free account on Make.com or n8n.io (or use the n8n Cloud trial).
2. Explore the dashboard: identify where to create Scenarios (Make) or Workflows (n8n).
3. Review the core automation flow:
   - **Trigger:** What starts the workflow (e.g., new row added, new email received).
   - **Action:** What happens in response (e.g., send an email, update a record).

## Part 2: Build a Simple Workflow

**Goal:** Create an automation that sends an email whenever a new row is added to a Google Sheet.

### Steps:

1. Create a new scenario/workflow.
2. Add Google Sheets as the Trigger: "When a new row is added."
3. Add Email (Gmail) or Webhook/Notification as the Action.
4. Save and run the workflow once manually to test.
5. Add a filter or conditional rule (e.g., only trigger if "Priority" = "High").
6. Activate the workflow to run automatically.

## Deliverables

**Submit:** A screenshot of your completed workflow.
