# prod.collab
Demo project for showing off collaboration practices in action.

## SETUP: 

### Python virtual environment
```bash
python3.8 -m venv <virtual_environments_folder>/prodcollab
source <virtual_environments_folder>/prodcollab/bin/activate
```

### Install
 - Configure GitHub SSH:
    https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh

 - checkout code
    ```bash
    cd <Folder/Dir of your choosing>
    git clone git@github.com:MVanderer/prod.collab.git
    cd prod.collab
    ```

 - install Python requirements
    ```bash
    PIP_CONFIG_FILE=<if_necessary_to_deal_with_proxy_settings>/pip.conf pip install -r requirements.txt
    ```

## Configuration
    - (TODO): Steps to prepare prod.collab.yaml here
    - (TODO): Steps to set up environmental variables here
    - (TODO): Additional steps to prepare secure access

## Startup

### Run prod.collab
 - start single-threaded flask appserver
    ```bash
    python src/api/application.py
    ```

 - (optional) start a multi-threaded flaks appserver with gunicorn
    ```bash
    gunicorn --workers 8 --bind=0.0.0.0:5001 --access-logfile '-' prod.collab.application:app
    ```

 - (optional) run apache
    (TODO): collect static files - setup script
    ```bash
    
