# 1. 从远端拉去分支到本地
```git
git checkout --track origin/[branch-name]
```
这时会在本地新建一个分支，名为 branch-name，会自动追踪远程的同名分支 branch-name
# 2. 向远程推送新的本地分支
```git
git push --set-upstream origin [branch-name]
```
这时会在远程新建一个 branch-name 分支并与本地的 branch-name 
# 3. 建立追踪关系，在本地现有分支与指定的远程分支之间
```git
git branch --set-upstream [branch-name] [remote-branch-name]
```
（在本地创建和远程分支对应的分支，本地和远程分支的名称最爱好一致：
git checkout -b dev origin/dev