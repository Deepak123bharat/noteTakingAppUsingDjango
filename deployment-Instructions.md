# noteTakingAppUsingDjango
* Add requirment.txt file to your project main directory
* Add Procfile to the main directory
* In setting.py change ALLOWED_HOSTS

```ruby
      ALLOWED_HOSTS=[*]
```

* [Add an existing project to GitHub
](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)
## Run following command in terminal

```bash
$ heroku create
$ heroku git:remote -a gentle-island-49857
```

gentle-island-49857 may be different in your cases
```bash
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ git push heroku master
```
