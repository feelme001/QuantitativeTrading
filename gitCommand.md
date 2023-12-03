## Pull code from git
- Go to repository: https://github.com/feelme001/QuantitativeTrading
- code -> HTTPS -> copy "https://github.com/feelme001/QuantitativeTrading.git"
- cd into your local folder you planning to work on the project
  - inside the folder run command ```git clone https://github.com/feelme001/QuantitativeTrading.git``` 
  - login your github account if needed

## Push code to git
- Go to your local folder
- Create your test branch
  - config the git so that it look good
    - ```git config --global alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit --all"```
  - create a test branch named myTestBranch also track the head from current main```git checkout -b myTestBranch -t```
- create a test file push to your branch
  - ```vim testFile```
  - click ```i``` to enable make change to the file
  - type some sample text
  - click ```ESC``` to exit the edit model
  - ```shift``` then type ```:wq``` to indicate you want to write and quit save the new vim file you created
  - commit the change
    - ```git status``` you should see your change in red color means it havn't been saved to git yet
    - ```git add .``` add the file to git repostory
    - ```git status``` now you can see the color change to yellow which means it is ready to commit
    - ```git commit -m "This is my testFile"``` commit the change in local with a message
    - ```git lol``` now you can see your commint along with the main branch
    - ```git push origin myTestBranch``` push the myTestBranch to git online repo
    - It will ask you to login
        - user name: your user name
        - password: your token
- now you should see your change in the online git repository