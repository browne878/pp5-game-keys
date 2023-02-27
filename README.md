# **Game Keys**

You can see the live
website [here](https://browne878-game-keys.herokuapp.com/).

The purpose of this website is to make games widely available to the public. This website is meant to be used by anyone who
is looking for a new game to play. Games should be cheap and easy to find.

My aim for Game Keys is to bring low cost games to everyone. I want to make them easily accessible to everyone.

## **Table of Contents**

- ### [Planning]()

- ### [Features]()

- ### [Models]()

- ### [Future Development]()

- ### [Testing]()

- ### [Bugs]()
    - [Unfixed Bugs]()
    - [Fixed Bugs]()

- ### [Deployment](https://github.com/browne878/CodeSprint-Portfolio-Project-4#deployment-1)
    - [Cloning/Forking Repository](https://github.com/browne878/CodeSprint-Portfolio-Project-4#cloning--forking-repository)
    - [Local Deployment](https://github.com/browne878/CodeSprint-Portfolio-Project-4#local-deployment)
    - [Remote Deployment](https://github.com/browne878/CodeSprint-Portfolio-Project-4#remote-deployment)

- ### [Credits](https://github.com/browne878/CodeSprint-Portfolio-Project-4#credits-1)

## **Planning**

## **Features**

## **Models**

## **Future Development**

## **Testing**

## **Bugs**

### Unfixed Bugs

### Fixed Bugs

## **Deployment**

### Cloning / Forking Repository

In order to Fork the Repository, please follow the instructions below.

1. Navigate to [this](https://github.com/browne878/pp5-game-keys) repository.
2. Next, in the top left of the page, click the fork button.
3. If you are a member of a team, you may need to choose where to Fork the repository too.

Once you have forked the Repository, you can then clone it to your local machine. To do so, please follow the
instructions below.

1. Navigate to your Forked repository.
2. Click the green Code button above the repositories files.
3. Copy the URL in the dropdown window.
4. Next, open command prompt.
5. After this, navigate to the directory you would like to clone the repository too with the following command.

 ```
cd <clone location>
 ```

6. Then, run the following command.

 ```
git clone <URL>
 ```

You have now forked and cloned the repository.

### Local Deployment

### Remote Deployment

The following instructions will guide you the deployment process for Heroku. I will assume you already have
a [Heroku](https://www.heroku.com/) account.

1. First, follow the instructions to clone the repository to your GitHub.
2. On Heroku, login and navigate to your dashboard.
3. In the top right, click `New` and select `Create a new app`.
4. Next, name your app and select your region and click `Create app`.
5. After this, under the deployment method, select GitHub and link your account with GitHub.
6. Then, search for your cloned repository and click `Connect`.
7. Under the `Automatic deploys` section, ensure the main branch is selected and click the `Enable Automatic Deploys`.
8. Also, under the main branch is selected in the `Manual deploy` section.
9. Next, at the top of the page, navigate to the settings page.
10. After this, go to the resources tab on heroku and search for `Heroku Postgres` under the add-ons tab.
11. Then, you will need to go
    to [Cloudinary](https://cloudinary.com/console/c-e41e529a42f687f55f451d5505dfd8/getting-started) and sign up.
12. Once you have signed up, go to the dashboard and copy the `API Environment variable`.
13. After this, under the `Config Vars` section, click the `Reveal Config Vars` button and enter the
    following:
    - `SECRET_KEY` : `Generate this yourself but make it random so it is secure`.
    - `AWS_ACCESS_KEY_ID`:
    - `AWS_SECRET_ACCESS_KEY`:
    - `DEBUG`: This can be added if you want to develop the application further. It will provide debug messages
        in the console. Set this to `True` if you want to use it.
    - `EMAIL_HOST_PASS`:
    - `EMAIL_HOST_USER`:
    - `STRIPE_PUBLIC_KEY`:
    - `STRIPE_SECRET_KEY`:
    - `USE_AWS`:
14. Then, in the section below (`Buildpacks`), click `Add buildpack` and select python.
15. Repeat the previous step, but this time, select NodeJS.
16. Once this is done, ensure that the python build-pack is at the top of the list. (You can drag them to move them).
17. Then, at the top of the page, navigate back to the deployment section.
18. Finally, you can scroll to the bottom of the page and click the `Deploy Branch` button under the `Manual deploy`
    section.
19. Once the deployment is complete, you can click the `Open app` button at the top right of the page. This will open
    the deployed app in a new tab.

## **Credits**

This app was built using only the documentation from Bootstrap, Django and JQuery.
