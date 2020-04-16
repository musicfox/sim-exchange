# A `berglas` how to
Though well designed and ultimately easy to use, `berglas` has it's quirks and is somewhat byzantine. 

Here's how to set it up w/links to the right docs for quick reference. 

## Setup

First of all, run the following (until you're adding code to an application) on the google cloud console. It's just easier and all setup.

Rather than rehash specifically, get setup, in the google cloud console (using docker):

[https://github.com/GoogleCloudPlatform/berglas](https://github.com/GoogleCloudPlatform/berglas)

Specifically,
```bash
docker pull gcr.io/berglas/berglas:latest
docker images
# get the image hash
echo "image-hash" >> .bash_profile && source .bash_profile
berglas [blah blah]
```

## Using `berglas`
Once setup, auto loading environment variables using the Goog's encryption/security/beefy-engineers, is fantastic.

If stuck be sure to read the docs at the bottom of this page.

### Reference syntax
```bash
berglas://[BUCKET]/[SECRET]?[OPTIONS]#[GENERATION]
```
[Reference syntax documentation](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md)

### Key management & Google Cloud Run deployments
First, you'll need some environment variables to create or issue account access for new keys. 

#### `berglas` env variables
Set the following to get going.
```
export PROJECT_ID=my-project
export BUCKET_ID=my-bucket
export KMS_KEY=projects/${PROJECT_ID}/locations/global/keyRings/berglas/cryptoKeys/berglas-key

PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export SA_EMAIL=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
```
#### How to create a key
```
berglas create ${BUCKET_ID}/my-key-name "my-key-name-value" \
--key ${KMS_KEY}
```

#### How to give service account access
The following assumes you've already granted the service account read access to the cloud deployment's env variables. Check the docs if you need to do this.
```
berglas grant ${BUCKET_ID}/my-key-name --member serviceAccount:${SA_EMAIL}
```

#### How to update your build scripts with environment variables
To your `cloudbuild-*.yaml` file, add this to the last deploy section as arguments in the list:
```
"--set-env-vars"
"my-key-name=berglas://${BUCKET_ID}/my-key-name?destination=tempfile",
"--allow-unauthenticated"
```

### Links

[Cloud Run Github](https://github.com/GoogleCloudPlatform/berglas/tree/master/examples/cloudrun/python)

[`berglas` Github](https://github.com/GoogleCloudPlatform/berglas/blob/master/README.md)

[Google Cloud suggestions](https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-secrets-credentials)