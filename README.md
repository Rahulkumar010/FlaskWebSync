# sample-flask-app

Hosting a Flask application in PythonAnywhere with Continuous Integration:

1. Create the Flask application and push it to Github, use "pipreqs ..\sample-flask-app --savepath requirements.txt" to get project requirements.
2. Create PythonAnywhere account here - https://www.pythonanywhere.com/
3. Open the bash terminal in PythonAnywhere and clone the repo
4. Setup the web app in PythonAnywhere, follow the instructions provided
5. Added the "./git_update" as part of main script here in this case it's server.py and created Webhook on the same Endpoint like https://{username|custom_domain}.pythonanywhere.com/git_update.
6. Create a file with name "post-merge" with following contents under "./git/hooks" folder of Git repo cloned in PythonAnywhere.
```
#!/bin/sh
touch {path to WSGI configuration file} 
```
path looks like "/var/www/{your web aplication domain}_wsgi.py"
--> found here - https://www.pythonanywhere.com/user/{username}/webapps/  under WSGI configuration file

7. Provide the execution permission to the bash script created above using --> chmod +x post-merge
8. Please follow the guide here - https://help.pythonanywhere.com/pages/Virtualenvs, to install addtional dependencies with respect to WebApp and update the configuration accordingly as mentioned.
9. Now, whenever any update in code has been commited, the Webhook triggers and updates repo in PythonAnywhere, where "post-merge" would execute to reload the Web Application, ensuring Continuous Deployment.