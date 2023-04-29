import pyotp

# Create a secret key
secret = pyotp.random_base32()

# Generate a TOTP object
# global totp
totp = pyotp.TOTP(secret)


def create_code():
    # Get the current TOTP code
    totp_code = totp.now()

    return totp_code