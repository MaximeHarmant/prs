This is how job market will change !

# Environment installation
    pip install virtualenv
    pip install virtualenvwrapper

# Add to your shell startup file
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

# Create virtualenv and install required packages
    mkvirtualenv django
    pip install -Ur requirements.txt

# Later to use your workspace
    workon django

# Later to close your workspace
    deactivate