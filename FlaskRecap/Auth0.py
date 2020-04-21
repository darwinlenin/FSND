import json
from jose import jwt
from urllib.request import urlopen

# Configuration
# UPDATE THIS TO REFLECT YOUR AUTH0 ACCOUNT
AUTH0_DOMAIN = 'zoegeop.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'image'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

        # PASTE YOUR OWN TOKEN HERE
        # MAKE SURE THIS IS A VALID AUTH0 TOKEN FROM THE LOGIN FLOW
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJyWWZGMFZydllVWGd4bjVxWmNwOSJ9.eyJpc3MiOiJodHRwczovL3pvZWdlb3AuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOGEyYTkzNjU5NTExMGMxMGNmZjI4ZCIsImF1ZCI6InpvZWdlb3AiLCJpYXQiOjE1ODYxMTMxNzIsImV4cCI6MTU4NjEyMDM3MiwiYXpwIjoiN0ExS1E3amJCNkcwS3R6Vk5RTkdyb3EyTWtCbVlUVTciLCJzY29wZSI6IiJ9.fQx53qonRG5NqjTcGJPxSObvzrJxvKTK22BJVy6D7dfA6KJ-9EfuDkSEYB-IOp8v9oh0eYjiixm2jDR3FPAP-9P59pLhBRkm_6bGGYEcCLS23CUpMQwhUUCfGguwWacF9krdFlXBBRg1rOK0khMhOM67AGtWh0IuGhqcAsH2c83-6mLfUaWq6w9CAnGdKv1SgDi_qAuQfRHi3mUV3bEp18QM4FrXlevjueH8buWTJGsG9aU4lRZ8xMokqqawWjK9qDvexOJzDabvQh-yEtLsn9myRo4TcbWL1-f7Wp0nXa0LpYMHzopYZeWIz2cteLyvNLyBeveU9peRwPnfI17hDA"

    ## Auth Header
    def verify_decode_jwt(token):
        # GET THE PUBLIC KEY FROM AUTH0
        jsonurl = urlopen(f'https://zoegeop.auth0.com/.well-known/jwks.json')
        jwks = json.loads(jsonurl.read())

        # GET THE DATA IN THE HEADER
        unverified_header = jwt.get_unverified_header(token)

        # CHOOSE OUR KEY
        rsa_key = {}
        if 'kid' not in unverified_header:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }, 401)

        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }

        # Finally, verify!!!
        if rsa_key:
            try:
                # USE THE KEY TO VALIDATE THE JWT
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer='https://' + AUTH0_DOMAIN + '/'
                )
                print(payload)

                return payload

            except jwt.ExpiredSignatureError:
                raise AuthError({
                    'code': 'token_expired',
                    'description': 'Token expired.'
                }, 401)

            except jwt.JWTClaimsError:
                raise AuthError({
                    'code': 'invalid_claims',
                    'description': 'Incorrect claims. Please, check the audience and issuer.'
                }, 401)
            except Exception:
                raise AuthError({
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentication token.'
                }, 400)
        raise AuthError({
            'code': 'invalid_header',
                    'description': 'Unable to find the appropriate key.'
        }, 400)
