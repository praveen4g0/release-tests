# Verify Triggers with cronJob 

Pre condition:
  * Operator should be installed

## Create Triggers using k8s cronJob
Tags: triggers, focus, ignore

This scenario helps you to Trigger pipelineRun, using a k8s CronJob, to implement a basic cron trigger that runs every minute

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener
  * Expose event listener service externally
  * Create Cron Job that triggers eventlistener, every 1 minute
  * Verify new pipelineRun created with labels & event-id
