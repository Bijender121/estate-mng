
from os import getenv, path

from dotenv import load_dotenv

from .base import *  # noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)




# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-xeoad(j+!#^mwrmfnr#4ebc)(+s(nsd^pgt#@mv93f$+6vf0%$'

SECRET_KEY = getenv("DJANGO_SECRET_KEY")




ALLOWED_HOSTS = []

  
ADMINS =[("Bijender Nagar", "api.", "api.bijendernagar@gmail.com"),]