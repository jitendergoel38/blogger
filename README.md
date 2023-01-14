




Following steps:
    1. Move settings to settings folder and create different settings viz., base, local, production
    2. Set local if debug is true else production
    3. from django.core.management.utils import get_random_secret_key
    4. import python-dotenv... 
        1. .env file is created which has all the environment variables which are then imported into settings... more at the time of deployement
    5. import pytest...
        1. for testing purpose
        2. ```pytest``` in the terminal runs the pytest.
        3. create pytest.ini file
        4.
