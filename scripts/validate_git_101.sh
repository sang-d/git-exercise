#!/bin/bash

LAST_COMMIT_ID=$(git log --format="%H" -n 1)

EMAIL=$(git log --format='%ae' ${LAST_COMMIT_ID}^! )
EMAIL=$(echo $EMAIL | tr '[:upper:]' '[:lower:]')

clean_git101() 
{
	# git push origin --delete $CIRCLE_BRANCH
	python scripts/slack.py $EMAIL "$CIRCLE_BRANCH is now deleted"
}

NUMBER_COMMIT=$(git log --oneline $CIRCLE_BRANCH ^origin/develop | wc -l)
echo "number commit" $NUMBER_COMMIT
if [[ $NUMBER_COMMIT != 1 ]]; then
	msg="Git101 Failed, there are more than 1 commit"
	python scripts/slack.py $EMAIL $msg
	# clean remote branch
	clean_git101
	exit 1
fi

COMMENT=$(git log -1 --pretty=%B)
echo "comment content", $COMMENT
if [[ $COMMENT != "feature/git101 git practice" ]]; then
	echo 'Git101 Failed, comment should be "feature/git101 git practice"'
	clean_git101
	exit 1
fi 

msg="Congratulation you have completed git 101"
python scripts/slack.py $EMAIL $msg
clean_git101
exit 0