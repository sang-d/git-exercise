### Exercise 101 
##### git basic opration: `git add` `git status` `git commit`
##### using git flow to create and publish and finish feature branch


1. Create a new feature branch with format: feature/git101
	There are 2 ways to do:
	```$ git flow feature start {your-wizeline-user-name}```
	```$ git checkout -b feature/{your-wizeline-user-name}```

2. Adding a new file:
	```$ touch git_101/hello.txt```

3. Add changes to git staging:
	```$ git add .```

4. Commit with proper comment"
	```$ git commit -m "feature/{your-wizeline-user-name} git 101 practice"```

5. Publish your branch to remote origin
	There are 2 ways to do:
	```$ git flow feature publish {your-wizeline-user-name}```
	```$ git push --set-upstream origin feature/{your-wizeline-user-name}```

After complete this, a slack bot `git-x` will notify you if it has been done correctly.

6. Clean your branch (delete local and remote branch)
	There are 2 ways to do:
	```$ git flow feature finish {your-wizeline-user-name}```
	```$ git reset origin/develop --hard```

	Or
	```$ git push origin --delete feature/{your-wizeline-user-name}```
	```$ git checkout develop```
	```$ git branch -D feature/{your-wizeline-user-name}```
	
#### Note: you need to complete #6 to practice git_102
