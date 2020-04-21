# sim-exchange-backend 

## Overview

sim-exchange-backend is a Python Flask-based application setup with build
triggers, a continuous deployment pipeline, and a Dockerized Python Flask
application.

### Architecture
We use `Flask` under the hood, as it's robust and easily deployable, pretty
much anywhere in space that can house Python.

`gunicorn` is our actual production webserver and we run it behind Google's Cloud Run offering, which auto-load balances and scales up to 1000 instances.

`Docker` containerizes everything. Magical.

### Google Cloud

Products utilized:

- Cloud Run
- Cloud Build
- Container Registry
- Cloud Compute Engine (other apps)
- Google Kubernetes Engine (future, if necessary, here)
#### Get Setup on Google Cloud

1. create and connect to this repo in Cloud Build with name sim-exchange-backend
in project `musicfox`.

### Google PostgreSQL database

- name: `sim-exchange-backend`
- user: `sim-exchange-backend-user`

### cookiecutter & `git`
3. run `cookiecutter app-template` from the directory in which `app-template`
resides
    - follow the prompts and be sure to copy-pasta the database user name

4. `cd sim-exchange-backend`

### environment

First get your python environment in your `application` directory:

5. `pipenv install`

6. `pipenv lock -r > requirements.txt`

7. `pip freeze > application/requirements.txt`

8. `git init && git remote add origin git@github.com:musicfox/sim-exchange-backend`

9. `git add . && git commit -m "initial commit"`

10. `git push -u origin master`

11. `git flow init -d # use the defaults`

12. `git push -u origin develop`

### BERGLAS

Now it's time to jump onto a browser or local machine using `berglas` and
the `gcloud` CLI.

Run the following `./build-cicd.sh` and then  `rm -rf build-cicd.sh`.

#### :guitar: Commit build and deploy :guitar:
`git add . && git commit -m "my first commit" && git push`

#### ACTION REQUIRED LATER - you need to manually add secrets using the 
[berglas](berglas.md) instructions for deployment.  Obviously real
database credentials per company policy need to be kept from any written,
remotely public, unencrypted access.

And here, we post the test credentials
as they don't have write or create commands and are separate from production
credentials. Just don't do this with live db credentials and report it right
away if you do.


### Admin Dashboards

- Cloud offering management: [GCP](https://console.cloud.com)
- DNS and domain-specific: [Domain Admin](domains.google.com)
- GSuite and corp admin: [Musicfox Google Admin](admin.google.com)

## Dev Ops in use

Our development operations, environments, and workflow.
### Environments

- Production: latest `master` branch that builds and passes all tests
  - `release` branches from the `git-flow` model above merge into this, in addition to `hotfix` branches
  - `[custom domain]` domains
- Testing: latest `develop` branch that builds and passes all tests
  -[custom domain].musicfox.dev` domains
- Development: latest pushed/built `feature/\*` branch

-[custom domain].active.musicfox.dev` domains

#### Local development, pre-commit
For local pre-commit testing it is recommended to port-forward the
$PORT environment variable value, running flask locally. **$PORT is set to
5009 for this application** by defualt.

To set local testing environment variables:
```bash
source application/.env # testing env vars
```  

To run the application:
```bash
cd application
flask run
```

In `vscode` type the following:

1. `ctrl+shift+p` or `cmd+shift+p`
2. `forward port`
3. press `return`
3. `5009` 
4. press `return`
5. press `return`

### Continuous Integration, Testing, and Deployment

Using [Google Build](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build) with Build Triggers allows us the convenience of automated testing, building, and even deployment.

Hands off, as they say in the business.

#### Manually run test suite

We use `py.test`, as with all our Python software for testing. For checking
links we use the Flask provided `test_client` object, as a fixture in
`test/app_test.py`.

Run the test suite from the **application directory**, in `application/`:

```bash
python -m pytest -vv --ignore=dev # extra verbosity
```

### `git flow`

We use the standard `git flow` workflow. Read more [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
and [here](https://danielkummer.github.io/git-flow-cheatsheet/).

#### Typical working branch: `develop`

Everything branches _from_ the `develop` branch.

#### Something new? An Experiment? `git flow start feature GIVEMEANAME`

Start a new feature with the `start feature` command set in git-flow.

Finish it with `git flow feature finish` which will merge the feature into the develop branch, and start the autobuild process in Google Cloud.

#### Time for a release? `git flow release start vX.X.X`

When it's time for a release use the above to branch off of `develop` and start the release.

Once ready, finish with `git flow release finish vX.X.X` and push it with `git push origin --tags`

#### Other branches we use and where to get instructions

- `hotfix` for fixing deployed releases
- [cheat sheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [original post](https://nvie.com/posts/a-successful-git-branching-model/)


### Secrets, stored at Google using Berglas

We store our application environment variables in the cloud using Google's
open source containerization and deployment secret software, Berglas.

Here's a Musicfox [how-to](/berglas.md).
)
