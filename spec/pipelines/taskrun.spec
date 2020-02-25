# Verify Task Run Spec
Pre condition:
  * Operator should be installed

## Run Cluster Task
Tags: taskrun, focus

Steps:
 * Run "./testdata/taskrun/clusterTask.yaml"
 * Verify taskrun status is "successfull"

## Run Task to build, push using kaniko
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/build-push-kaniko.yaml" 
 * Verify taskrun status is "successfull"
 * Verify image stream

## Run custom-volume task
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/custom-volume.yaml"
 * Verify taskrun status is "successfull"

## Run pulling private image using docker-credentials
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/docker-cred.yaml"
 * Verify taskrun status is "successfull"

## Run side car task
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/sidecar.yaml"
 * Verify taskrun status is "successfull"

## Run task step as script
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/step-script.yaml"
 * Verify taskrun status is "successfull"


## Run workspace task
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/workspace.yaml"
 * Verify taskrun status is "successfull"

## Run podTemplate task
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/podtemplate.yaml"
 * Verify taskrun status is "successfull"

## Cancell Task Run
Tags:  taskrun, focus

Steps:
 * Run "./testdata/taskrun/cancel.yaml"
 * Cancel task run
 * Verify taskrun status is "cancelled"