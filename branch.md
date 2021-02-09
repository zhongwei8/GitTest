# 1. 将本地的新分支推送到远程
```git
git push --set-upstream origin learn_git
```
# 2. 查看所有分支详细信息
```git
git branch -vv
```
# 3. 本地关联远程分支
```git
git branch --set-upstream-to=origin/remote_branch your_local_branch
```
# 4. 推送
```git
git pull <remote> <branch>
```
# 5. 创建新分支
```git
git branch [branch-name]
```
# 6. 新建分支并切换到该分支
```git
git checkout -b [branch-name]
// git switch -c [branch-name]
```
# 7. 新建一个分支并与指定的远程分支建立追踪关系(前提是对应的远程分支存在)
```git
git branch --track [branch-name] [remote-branch-name]
```
# 8. 切换到指定分支
```git
git checkout/switch [branch-name]
```
# 9. 切换到新建的分支
```git
git checkout -b [branch-name]
```
# 10. 将新的远程分支拉去到本地
```git
git checkout --track origin/[branch-name]
// 本地会新建一个分支，名为 branch-name, 会自动追踪远程同名的分支 branch-name
```
# 11. 将新的本地分支推送到远程
```git
git push --set-upstream origin [branch-name]
// 在远程新建一个 branch-name 分支并与本地的 branch-name 关联，后面 git pull 就会同步
```
# 12. 建立追踪关系，在本地现有分支与指定的远程分支之间
```git
git branch --set-upstream [local-branch-name] [remote-branch-name]
// 在本地创建和远程分支对应的分支，本地和远程分支的名称最好一致
```
# 13. 合并到 master 分支上
```git
git checkout master         // 1. 切换到 master 分支上
git pull origin master      // 2. 把远程的 master 拉取下来，保持本地和远程的一致
git merge dev               // 3. 将 dev 分支代码合并到 master 上 
git push                    // 4. 将 合并后的代码 提交到远程
```
# 14. 撤销向远程的提交
```git
git revert -m l <commit-hash>
git commit -m "Reverting the last commit which messed the repo."
git push -u origin master
// <commit-hash> 是要还原的合并的提交哈希，-m l 表示想还原到
// 第一个父级的树，合并。
// git commit ... 行实质上是你的更改，而第三行则通过
// 将更改推送到远程分支来公开更改。
```
# 15. log 和 reflog
## 1. log：显示所有提交过的版本信息
## 2. reflog：查看所有分支的所有操作记录
包括 commit 和 reset 的操作，包括已经被删除的 commit 记录，
git log 则不能查看已经删除了的 commit 记录。
# 16. HEAD 值
HEAD 表示提交的最新版本，HEAD^ 表示上一个版本，HEAD^^ 表示上上个版本，
HEAD～100 表示往上 100 个版本
# 17. reset 命令
+ reset： 撤销(回退)一个提交
```git
git reset --hard HEAD^  // 回退到 HEAD 的上一个版本
```
# 18. reflog
```git
git reflog

// dae675a HEAD@{0}: reset: moving to HEAD^
// 8e27eb6 HEAD@{1}: commit: append GPL
// dae675e HEAD@{2}: commit add distributedd

git reset --hard 8e27eb6

// log reflog reset 可以在各个版本之间自由移动

```