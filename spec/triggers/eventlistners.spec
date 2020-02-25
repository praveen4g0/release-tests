# Verify eventlistners spec

Pre condition:
  * Operator should be installed

## Create Eventlistener
Tags: triggers, focus

This scenario helps you to create eventlistner, listens to github events by default, on each github event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener
  * Expose event listener service externally
  * Mock push event
  * Verify new pipelineRun created with labels & event-id

## Create Eventlistener with github interceptor
Tags: triggers, focus

This scenario helps you to create eventlistner with github interceptor, listens to github events, on each github event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener with github interceptor
  * Expose event listener service externally
  * Mock github pull-request event
  * Verify new pipelineRun created with labels & event-id

## Create Eventlistener with gitlab interceptor
Tags: triggers, focus

This scenario helps you to create eventlistner with gitlab interceptor, listens to gitlab events, on each event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener with gitlab interceptor
  * Expose event listener service externally
  * Mock gitlab push event
  * Verify new TaskRun created with labels & event-id

## Create EventListener with custom interceptor
Tags: triggers, focus

This scenario helps you to create eventlistner with custom interceptor, listens to custom events, on each event to custom service it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Create custom gh-validator service
  * Add Event listener with custom interceptor
  * Expose event listener service externally
  * Mock custom push event
  * Verify new pipelineRun created with labels & event-id

## Create EventListener with CEL interceptor with filter
Tags: triggers, focus

This scenario helps you to create eventlistner with CEL interceptor with filter, listens to filtered CEL events, on each event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener with CEL interceptor with filter
  * Expose event listener service externally
  * Mock CEL push/pr event
  * Verify new pipelineRun created with labels & event-id

## Create EventListener with CEL interceptor without filter
Tags: triggers, focus

This scenario helps you to create eventlistner with CEL interceptor, listens to all CEL events, on each event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, to deploy example app

Steps:
  * Create trigger bindings
  * Create trigger template
  * Create roles for resources
  * Add Event listener with CEL interceptor without filter
  * Expose event listener service externally
  * Mock CEL push/pr event
  * Verify new pipelineRun created with labels & event-id


## Create EventListener with multiple interceptors
Tags: triggers, focus

This scenario helps you to create eventlistner with multiple interceptors, listens to events forwards request to validator service -> parsed response to other validators and so on, on each event it creates/triggers 
openshift-pipeline Resources defined under triggers-template, which helps you to deploy example app

Steps:
  * Create roles for resources
  * Create trigger bindings
  * Create trigger template
  * Add Event listener with multiple interceptors
  * Expose event listener service externally
  * Mock push event
  * Verify new pipelineRun created with labels & event-id
 

