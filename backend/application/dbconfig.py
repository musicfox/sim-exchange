"""Configuration for postgreSQL database hosted with avien"""
# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
import os


def set_uri(
    user,
    pswd,
    dbname,
    ip="pgdb-musicfox-musicfox-083b.aivencloud.com",
    port=25398,
    extras="sslmode=require",
):
    """
    Set the database uri given credential data and others.

    This works for our databases at aiven.io.

    """
    if not user:
        raise AttributeError("You need to set your MFDB_USER env variable.")

    if not pswd:
        raise AttributeError(
            "You need to set your MFDB_PASSWORD env variable."
        )

    return f"postgres+psycopg2://{user}:{pswd}@{ip}:{port}/{dbname}?{extras}"


# set environment variables set in google cloud bucket using berglas
# or for testing via `source .env`
USER = os.environ.get("MFDB_USER")
PASSWORD = os.environ.get("MFDB_PASSWORD")
DBNAME = os.environ.get("MFDB_NAME")

DATABASE_URI = set_uri(USER, PASSWORD, dbname=DBNAME)
