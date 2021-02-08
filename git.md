[https://www.cnblogs.com/wulixia/p/12732488.html](git 分支管理)
1. 创建本地分支
```git
git branch [branch-name]
```
2. 新建分支并切换到该分支
```git
git checkout -b [branch-name]
git switch -b [branch-name]
```
3. 列出本地所有分支
```git
git branch
```
4. 列出所有远程分支
```git
git branch -r
```
5. 列出所有本地和远程分支
```git
git branch -a
```
6. 新建一个分支与指定的远程分支建立追踪关系
```git
git branch --track [branch-name] [remote-branch-name]
```
7. 切换到指定分支
```git
git checkout/switch [branch-name]
```
8. 删除本地分支
```git
git branch -d [branch-name]
```
9. 删除远程分支
```git
git branch -r -d origin/[branch-name]
```
10. 追踪远程的新分支
```git
git checkout --track origin/[branch-name]

// 这时，本地会新建一个分支，名为 branch-name，会自动追踪远程的
// 同名分支 branch-name
```
11. 建立链接
```git
git push --set-upstream origin [branch-name]
// 这时会在远程新建一个 branch-name 分支并与本地的 branch-name
// 关联，后面 push pull 就会同步

```
12. 建立本地分支与远程分支的追踪关系
```git
git branch --set-upstream [branch-name] [remote-branch-name]
// 将本地分支链接到远程分支
```






```git
git branch --set-upstream-to=origin/remote_branch your_branch

其中，origin/remote_branch 是本地分支对应的远程分支;
your_branch 是当前的本地分支
```

