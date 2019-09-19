# git_config.sh

# add the source remote
git remote add upstream 'https://github.com/captechconsulting/aaml-tc01-mnist.git'
git fetch upstream master
git pull upstream master

# create and checkout new branch for student to work on 
git checkout -b develop
git push origin develop

# protect against master commits
[ -d ".git/hooks" ] && exit 0
mkdir .git/hooks
mv git-hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
rmdir git-hooks