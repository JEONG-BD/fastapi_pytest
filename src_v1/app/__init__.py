from dotenv import load_dotenv
import os

# one
load_dotenv()

# multi
# dotenv_files = [
#     os.path.join('env', '.env.dev'),
#     os.path.join('env', '.env.test')
# ]
# for dotenv_file in dotenv_files:
#     print(dotenv_file)
#     print(dotenv_file)
#     print(dotenv_file)
#     load_dotenv(dotenv_file, override=False)
#     print("DEV_DATABASE_URL:", os.getenv("DEV_DATABASE_URL"))
#     print("TEST_DATABASE_URL:", os.getenv("TEST_DATABASE_URL"))
