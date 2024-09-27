# flask-template

Template for bootstrapping a new flask app

use (say)

`npx degit github:arabidopsis/flask-template my-new-website`

To create a simple layout for a new flask website.


## Install dependencies

```bash
# activate a suitable python
micromamba activate py312
# create an isolated virtual environment
python -m venv .venv
micromamba deactivate
# now activate the virtual environment
source .venv/bin/activate
# install python dependencies
poetry install --without=dev
# ** for development ** don't exclude dev
# pre-commit install

# run the flask app
flask run
```

You should have a fully running flask website.

## push new code to github

See [here](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github).

First remove anything you don't want or need.

```bash
# create a empty new repo {my-new-repo} on github. Then ...
git clone git@github.com:{user}/my-new-repo.git
# copy everything including hidden files
cp -rT /path/to/my-new-website/ my-new-repo/
cd my-new-repo
git add . && git commit -m "initial commit"
git push
```
