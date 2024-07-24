import string, secrets

alphabet = string.ascii_letters + string.digits + "!#$%&'*+-.^_`|~"
test = ''.join(secrets.choice(alphabet) for i in range(64))

print(test)

