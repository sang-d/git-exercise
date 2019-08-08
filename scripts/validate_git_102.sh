!#/bin/bash


GIT_BRANCH=$(git branch | grep \* | cut -d ' ' -f2)

CIRCLE_USERNAME=$CIRCLE_USERNAME