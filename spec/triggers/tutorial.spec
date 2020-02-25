# Verify triggers tutorial

Pre condition:
  * Operator should be installed

## Run Triggers tutorial (by Automatically configuring webhook to git repo)
Tags: e2e, integration, triggers, focus

This scenario helps you to configure webhook & listens to github events, on each github event it creates/triggers 
openshift-pipeline Resources which helps you to deploy application (vote-app)

Steps:
  * Setup openshift-pipeline resources to create vote-app
  * Create Trigger bindings, template
  * Add Event listener with github interceptor
  * Expose event listener service externally
  * Configure webhook
     |GitHubOrg |GitUser   |GitRepo |SecretName    |
     |----------|----------|--------|--------------|
     |praveen4g0|praveen4g0|vote-api|webhook-secret|
     |praveen4g0|praveen4g0|vote-ui |webhook-secret|
  * Mock Github push event
     |body                                                                                                                  |
     |----------------------------------------------------------------------------------------------------------------------|
     |{"head_commit":{"id": "master"},"repository":{"url": "https://github.com/praveen4g0/vote-api.git","name": "vote-api"}}|
     |{"head_commit":{"id": "master"},"repository":{"url": "https://github.com/praveen4g0/vote-ui.git","name": "vote-ui"}}  |
  * Verify resources creation defined under triggers-template with labels & eventid
  * Verify application status is successfull