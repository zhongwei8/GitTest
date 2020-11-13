1. 建立本地仓库并建立与远程仓库的连接
```git
$ git init                              # 建立本地仓库
$ git add .                             # 将代码提交到本地仓库
$ git commit -m 'new branch commit'
$ git remote add origin git@...         # 建立关联：建立本地仓库与远程仓库的连接
```
2. 把本地代码提交到远程仓库
```git
$ git branch hello_git_branch           # 建立本地分支
$ git checkout hello_git_branch         # 切换到本地分支
$ git push origin hello_git_branch      # 推送到远程仓库，origin 为远程仓库的别名
$ git push origin hello_git_branch:master   # 推送到指定分支 master 上

# 把远程仓库的 master 与本地的当前分支 hello_git_branch 合并
$ git pull origin hello_git_branch:master   # 把远程仓库的 master 与 本地的 hello_git_branch 分支合并(本地当前分支为 hello_git_branch)

# 将远程仓库的 master 分支合并下来。如果本地没有 master 分支，本地就新建一个 master 分支
$ git pull master
```


1. 本地新建分支并切换到该分支
```git
$ git branch test_name        # 本地新建分支的名称
$ git checkout test_name      # checkout 命令切换到指定分支
```
2. 查看分支
```git
$ git branch                    # 查看分地分支
$ git branch -a                 # 查看所有分支，包括远程分支和本地分支

```
3. 推送本地分支到服务器
1) 新建远程分支，并将本地分支推送上去
```git
$ git push origin local_branch:remote_branch    # 本地已经切换到 local_branch
```
2) 将本地当前分支推送到远程已有分支
```git
$ git push                      # 将本地当前分支推送到远程已有分支
```
3) 关联 + 推送(先将**远程分支**和**当前分支**关联起来，再将本地分支 **推送** 到远程分支)
```git
$ git push -u origin/remote_branch  # 

```



1. 关联分支并 `push` 代码
```git
$ git push -u origin/remote_branch  # 远程已有 remote_branch 分支，但未关联本地分支 local_branch 
$                                   # 并且本地已经切换到 local_branch 分支
```


```git
$ git branch -d xxx                 # 删除本地分支
$ git remote -v                     # 查看远程分支
$ git branch -a                     # 查看所有分支

$ git pull --rebase origin master
$ git merge dev
$ git push origin master


```


```git
$ git pull <远程主机><远程分支>:<本地分支>
$ git pull origin master:my_test    # 将 origin 厂库的 master 分支拉取并合并到本地的 my_test 分支上
$ git pull origin master            # 省略本地分支，自动合并到当前所在分支



$ git clone <远程仓库>              # 克隆远程仓库
$ git remote add <远程仓库>         # 添加远程仓库
$ git pull <远程仓库>master:master  # 从远程仓库的 master 分支拉取最新的对性，合并到本地 master 分支
$ git checkout yyyy                # 切换到 yyyy 分支
$ git branch develop;git checkout develop   # 在当前分支的基础上创建一个开发分支，并切换到该分支，
$ git add .                         # 将修改保存到索引区
$ git commit -a                     # 将修改提交到本地分区
$ git push origin my_test:my_test   # 将本地分支 my_test 提交到远程仓库的 my_test 分支上

```


# 2 git pull 命令
取回远程主机某个分支的更新，再与本地的指定分支合并
```git
$ git pull <远程主机名><远程分支名>:<本地分支名>
$ git pull origin next:master       # 取回 origin 主机的 next 分支，与本地的 master 分支合并
$ git pull origin next              # 取回 origin/next 分支，再与当前分支合并(省略本地分支名，则默认为当前分支)


# 某些场合，Git会自动在本地分支与远程分支之间，建立一种追踪关系(tracking)。
# 比如，在 git clone 的时候，所有本地分支默认与远程主机的同名分支，建立追踪关系
# 也就是说，本地的 master 分支自动追踪 origin/master 分支
$ git fetch origin
$ git merge origin/next

# 手动建立 本地 master 分支与 远程 next 分支的追踪关系 
$ git branch --set upstream master origin/next
# 如果 当前分支与远程分支存在追踪关系，可以省略远程和本地分支名

$ git pull origin


# 如果当前分支只有一个追踪分支，连远程主机名都可以省略
$ git pull

$ git pull --rebase <远程主机名><远程分支名>:<本地分支名>
```

