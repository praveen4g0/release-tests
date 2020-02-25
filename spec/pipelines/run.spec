# Verify Pipeline Run

Pre condition:
  * Operator should be installed

## Run sample pipeline
Tags: e2e, integration, pipelines, focus

Run a sample pipeline that has 2 tasks:
  1. create a file
  2. read file content created by above task
and verify that it runs succesfully


Steps:
  * Create sample pipeline
  * Run sample pipeline
  * Verify sample pipelinerun is successfull


## Run conditional pipeline
Tags: e2e, integration, pipelines, focus  

Steps:
  * Run "./testdata/pipelinerun/conditional-pr.yaml"
  * Verify pipelinerun status is "successfull"

## Cancel Pipeline Run
Tags: e2e, integration, pipelines, focus  

Steps:
  * Run "./testdata/pipelinerun/conditional-pr.yaml"
  * Cancel pipeline run
  * Verify pipelinerun status is "successfull"

## Run pipeline with pipeline spec
Tags: e2e, integration, pipelines, focus  

Steps:
  * Run "./testdata/pipelinerun/pr-with-pipelinespec.yaml"
  * Verify pipelinerun status is "successfull"

## Run pipeline with resource spec
Tags: e2e, integration, pipelines, focus  

Steps:
  * Run "./testdata/pipelinerun/pr-with-resourcespec.yaml"
  * Verify pipelinerun status is "successfull"
