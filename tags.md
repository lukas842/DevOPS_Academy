Action				Command
List All Tags			git tag
Latest Tag			git describe --tags --abbrev=0
Add A Tag Locally		git tag -a TAG -m MESSAGE
Add a Tag at Specific Commit	git tag -a TAG -m MESSAGE HASH
Delete a Tag Locally		git tag -d TAG
Redoing a Tag Locally		git tag -f -a TAG -m MESSAGE
Push a Tag to Remote		git push origin TAG
Push all Local Tags to Remove	git push origin --tags
Delete a Tag on Remote		git push origin :refs/tags/TAG
List Tags as References		git show-ref --tags
