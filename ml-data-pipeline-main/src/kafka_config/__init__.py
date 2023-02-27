
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# API_KEY = os.getenv('API_KEY',None)
API_KEY = "5UEQUUNCQLR2QDG5"

# ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-lzvd0.ap-southeast-2.aws.confluent.cloud"

# API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
API_SECRET_KEY = "LcW0ELkMw/+kgJAtMPl79B48d3UqfN1kwjNTKqH0PFathLpe0JQ9XIYQwB1vpkO7"
# BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"


# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

# SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_KEY = "4XMLRZSWW3BZLZVW"

# SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
SCHEMA_REGISTRY_API_SECRET = "WapvplgSMgDIYDhnZQfEOnKIyFBvmUnsvsOYn2ONg51dbBiDj+y0URhqsDKmi3uj"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

