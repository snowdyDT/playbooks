import os

from dotenv import find_dotenv, load_dotenv

env_file_ = find_dotenv(rf'assets\.env.{os.getenv("ENV", "development")}')
env_file = env_file_ if env_file_ else find_dotenv(f'.env.{os.getenv("ENV", "development")}')
load_dotenv(env_file)

hosts = os.getenv('HOSTS', 'localhost')
python_venv_path = os.getenv('PYTHON_VENV_PATH')
python_library = os.getenv('PYTHON_LIBRARY', 'python-dotenv')

playbook_path = '/project/install_python_library.yml'
