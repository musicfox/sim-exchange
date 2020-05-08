#! /bin/bash

# BERGLAS
export PROJECT_ID=musicfox
export BUCKET_ID=sim-exchange-backend-secrets
export KMS_KEY=projects/${PROJECT_ID}/locations/global/keyRings/berglas/cryptoKeys/berglas-key
PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export SA_EMAIL=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
export BUCKET_LOCATION=us-central1

# BERGLAS BOOTSTRAPPING
/home/jason/go/bin/berglas bootstrap --project $PROJECT_ID --bucket $BUCKET_ID --bucket-location $BUCKET_LOCATION

# BERGLAS container creation
/home/jason/go/bin/berglas create ${BUCKET_ID}/MFDB_USER "postgres" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/MFDB_NAME "postgres" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/MFDB_PASSWORD "my-secret-db-password" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/APP_SECRET "jlEL2oPGX7MFtHWd7SV5zA" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/REDIS_HOST "redis-12643.c124.us-central1-1.gce.cloud.redislabs.com" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/REDIS_PASSWORD "my-secret-redis-password" --key ${KMS_KEY}
/home/jason/go/bin/berglas create ${BUCKET_ID}/REDIS_PORT "12643" --key ${KMS_KEY}

# BERGLAS add cloud run env var permissions
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:${SA_EMAIL} --role roles/run.viewer
# BERGLAS permissions
/home/jason/go/bin/berglas grant ${BUCKET_ID}/MFDB_USER --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/MFDB_NAME --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/MFDB_PASSWORD --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/APP_SECRET --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/REDIS_HOST --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/REDIS_PORT --member serviceAccount:${SA_EMAIL}
/home/jason/go/bin/berglas grant ${BUCKET_ID}/REDIS_PASSWORD --member serviceAccount:${SA_EMAIL}
