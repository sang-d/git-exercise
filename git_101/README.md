### Exercise 101 
##### git basic opration: `git add` `git status` `git commit`
##### using git flow to create and publish and finish feature branch


1. Create a new feature branch with format: feature/git101
	There are 2 ways to do:
	```$ git flow feature start git101```
	Or
	```$ git checkout -b feature/git101```

2. Adding a new file:
	```$ touch changes/hello.txt```

3. Add changes to git staging:
	```$ git add .```

4. Commit with proper comment"
	```$ git commit -m "feature/git101 git practice"```

5. Publish your branch to remote origin
	There are 2 ways to do:
	```$ git flow feature publish git101```
	Or
	```$ git push --set-upstream origin feature/git101```

After complete this, a slack bot `git-x` will notify you on Slack if it has been done correctly.

6. Clean your branch (delete local and remote branch)
	There are 2 ways to do:
	```$ git flow feature finish git101```
	```$ git reset origin/develop --hard```

	Or
	```$ git push origin --delete feature/git101```
	```$ git checkout develop```
	```$ git branch -D feature/git101```
	