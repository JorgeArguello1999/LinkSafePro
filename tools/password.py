import random
import string

def generate_password(length: int) -> str:
  """Generates a random password of the specified length."""

  # Define the characters that can be used in the password.
  characters = string.ascii_letters + string.digits + string.punctuation

  # Generate a random password.
  password = ''.join(random.choice(characters) for i in range(length))

  # Return the password.
  return password