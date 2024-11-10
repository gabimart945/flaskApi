import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:P0sgre$s1stemas@database.ctm6m1rqejhv.us-east-1.rds.amazonaws.com:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False