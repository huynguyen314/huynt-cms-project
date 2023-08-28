import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

<<<<<<< HEAD
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmshuystorageaccount2908'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '+VTol3Ni86npuygp/PQrgPU9BEU24mu+L1AwHXVr6OXmZua7OsLb58isQ3OjGqUn/0ZtfyDU3+w5+ASt92s9Yw=='
=======
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmshuystorageaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'PiBowwlKCXQs9dq2LgaMEXEoJK8WFIqysBv7BV+K3AQBr6TNSl1s0HCT5v6Cjgiu7dPjIoAckvGU+AStV4E/LQ=='
>>>>>>> 906628e11459359bb87ac9196ff2b8ac1bddee75
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-huyserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-project-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'huyadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@assword2719'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
<<<<<<< HEAD
    CLIENT_SECRET = "p1S8Q~Zic9CannLRcnz5Ozc0y_0EYHbymzRxHcK6"
=======
    CLIENT_SECRET = "rZF8Q~IGqxwpkSU_za3ru8yd9V80iPRVzy_4DcBD"
>>>>>>> 906628e11459359bb87ac9196ff2b8ac1bddee75
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

<<<<<<< HEAD
    CLIENT_ID = "7ca6c40e-8da7-4afa-9de6-c3bb28c958aa"
=======
    CLIENT_ID = "b4974548-ec41-4332-9fb0-1d17dce28354"
>>>>>>> 906628e11459359bb87ac9196ff2b8ac1bddee75

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session