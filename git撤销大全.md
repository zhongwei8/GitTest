# 1. 场景：撤销推向远程的推送
## 1.1 命令
```git
git revert <sha>
// sha 是 commit 的 hash 值，通过 git log 命令可以查看到
```
## 1.2 做了什么
`git revert` 创建了一个与 `sha` 所代表的 `commit` 的 "相反" 的 commit，这个新的 commit 会将
`sha commit` 所做的一切撤销。
