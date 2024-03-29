# Deployment

[Click here for Readme file](/README.md#deployment)

## GitHub

The program was built using GitHub repository. GitHub clone and GitHub branch methods could be used although were not needed for this project.

Repository may be forked in the following steps:
1. Go to GitHub repository,
2. Click Fork button (top right).

Steps for cloning repository:
1. Go to GitHub repository,
2. Click Code button (top right above files list),
3. Select cloning method option: HTTPS, SSH or GitHub CLI and click Copy button (right side of the text box) to copy URL to clipboard,
4. Open Git Bash (Git Bash can be downloaded from https://git-scm.com/downloads),
5. In Git Bash change working directory to the desired destination for the clone,
6. Type "git clone", paste URL for SSH method from the clipboard and press Enter.

During part of production process both [GitPod](https://gitpod.io/) and the program [Visual Studio Code](https://code.visualstudio.com) were used. The latter was not strictly necessary but provided smoother production in times of poor Internet connection and provided extra level of assurance in form of local copy of all files.

## Heroku

This application is deployed from GitHub using Heroku in following steps:

1. Create an account at [Heroku](https://id.heroku.com/).

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_signup.jpg)
    </details>

2. Create new app by clicking "New" and then "Create new app".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_create_new_app.jpg)
    </details>

3. Add app name and region and click on "Create app".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_create_name_region.jpg)
    </details>

4. Choose "Settings".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_settings.jpg)
    </details>

5. Under "Config Vars" add credentials, e.g. creds.json, secret key.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_config_vars.jpg)
    </details>

6. Set buildpacks by selecting "Add buildpacks" (I then chose "Python") and "Save changes".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_buildpacks.jpg)
    </details>

7. Go to "Deploy", at "Deployment method" click "Connect to GitHub" and confirm.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_deploy.jpg)
    </details>

8. Enter repository name, click on it when it appears below.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_connect_repo.jpg)
    </details>

9. Select the branch for building the app.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_branch.jpg)
    </details>

10. Clicking "Enable Automatic Deploys" will keep the app updated with GitHub repository. This feature is not used for this project.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](../readme/docs/images/testing/deployment/heroku_automatic.jpg)
    </details>

Ad. 5. Config Vars and coresponding keys in project files for this project:

| Config Vars in Heroku             | env.py                           | settings.py                                                     |
| --------------------------------- | -------------------------------- | --------------------------------------------------------------- |
| CLOUDINARY\_URL =  cloudinary://… | CLOUDINARY\_URL = cloudinary://… | \-                                                              |
| DATABASE\_URL = postgres://…      | DATABASE\_URL = postgres://…     | \-                                                              |
| SECRET\_KEY                       | SECRET\_KEY                      | SECRET\_KEY = os.environ.get('SECRET\_KEY')                     |
| DEBUG = 0                         | DEBUG = 1                        | DEBUG = os.environ.get('DEBUG', '1') == '1'                     |
| EMAIL\_HOST\_PASSWORD             | EMAIL\_HOST\_PASSWORD            | EMAIL\_HOST\_PASSWORD = os.environ.get('EMAIL\_HOST\_PASSWORD') |
| EMAIL\_HOST\_USER                 | EMAIL\_HOST\_USER                | EMAIL\_HOST\_USER = os.environ.get('EMAIL\_HOST\_USER')         |
| DISABLE\_COLLECTSTATIC = 0        | \-                               | \-                                                              |
| PORT = 8000                       | \-                               | \-                                                              |
 
 