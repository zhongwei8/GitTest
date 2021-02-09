[http://www.voidcn.com/article/p-ubypsqbj-b.html](reset checkout revert 的区别)
1. reset, checkout, revert 可以撤销 repo 的一些操作，他们既可以作用于 commit 级别，也可以作用于 file 级别。
2. git repo 的三大 components
    + working directory：代码仓库
    + staged snapshot：快照，add 的缓存库
    + commit history
# 1 commit 级别的操作
传递给 reset 和 checkout 的参数会决定命令的作用范围，当命令不包含一个文件路径时，命令作用于整个 commit。
## 1.1 reset
git reset 命令移动 HEAD 到当前分支的一个 commit，这可以用来撤销当前分支的一些 commit。
```git
git reset HEAD~2
```
HEAD 向前移动两个 commit，这意味着在下一次 git 提交时被作为垃圾删除掉，换句话说这两次提交会被抛弃。
git reset 用于撤销未被提交到远端的改动。除了可以移动当前分支的 HEAD，你可以通过不同的标记选择修改 staged snapshot 或者 working directory。
+ --soft： 缓存和工作目录都未被改变，建议在命令执行后，再 git status 查看状态
+ -- mixed: 缓存被更新，工作目录未被更改
+ -- hard：缓存和工作目录都将回退
--hard 很危险，它会回退到你之前的修改，使用前，可以实现保持 commit id。

这些标记经常和 HEAD 一起使用。例如 git reset --mixed HEAD 可撤销所有缓存改动，但是保留他们在工作目录下。
git reset --hard HEAD 可彻底删除没有提交的改动。

# 1.2 checkout branch-name
```git
git checkout hotfix
```
切换 HEAD 到不同的分支，并且更新当前的 working directory 去匹配。因为会覆盖当前的本地更改，所以更换分支前 git 强制你彻底放弃或提交存储当前的更改。      
不同于 git reset， git checkout 不会废弃任何分支或提交。

# 1.3 git checkout commit_id / HEAD~2