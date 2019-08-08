### Exercise 102 
##### git rebase interactive: `git rebase -i`
##### GitHub Pull Request, PR Check, PR Merge


1. Run init script to create a feature branch with 2 commits
	```$ git flow feature start git102```
	```$ touch changes/git102```
	```$ git add .```
	```$ git commit -m 'adding new file'```
	```$ echo "adding content" >> changes/git102```
	```$ git add .```
	```$ git commit -m 'adding content'```

2. Rebase to combine 2 commits into one with proper comment:
	```$ git rebase -i develop```
	Follow the instruction, and the new commit should have comment exactly:
	`feature/git102 rebase practice`
	Note: you can run rebase many times to practice
	The comment will be validated later during automatic PR check 

3. Publish changes to remote:
	```$ git flow feature publish git102```

4. Create a Pull Request on Github, you can use the url in the termial after running #3 similar:
	https://github.com/.../pull/new/feature/git102

5. Submit PR, and you will see a check is running, which is a CircleCI job has triggered
	If everything is correct (PR only has 1 commit and proper comment), a slackbot will notify you on slack and also PR check is marked completed.
	If it's not correct, slackbot will nofity error.

6. Merge PR on GitHub and delete remote feature branch to complete exercise
