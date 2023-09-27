import os

flag = 0
markdown = """# 2022年终总结

- 2021 年的年终总结见：[saveweb/review-2021](https://github.com/saveweb/review-2021)
- 2022 年：就是这里啦！
- 2023 年的年终总结见：[saveweb/review-2021](https://github.com/saveweb/review-2023)

与去年一样，本项目将长期维护（直到2024年初）。

**想要添加您的年终总结？请发 Issue 或编辑 metadata.md 发PR（不需要填写博客ID）。**

仓库维护/贡献者：

[yzqzss](https://github.com/yzqzss)、[taranakineko](https://github.com/taranakineko)、[cronfox](https://github.com/cronfox)、[gledos](https://github.com/gledos)

---

### 相关链接

| [Save The Web's Telegram Channel](https://t.me/saveweb) | [独立博客&播客全订阅's Telegram Channel](https://t.me/blogrsslist) | [Github Org](https://github.com/saveweb)
| --- | --- | --- |

### 广告

[我们给 1700 多个中文独立博客做了每日备份](https://blog.save-web.org/blog/2022/07/19/震惊，stwp-竟然给-1700-多个中文独立博客做了每日备份/)  

> 实际频率是 每几天/每一两周 推送一次链接。

---

"""

with open('metadata.md', 'r') as f:
  file = f.read()
lines = file.splitlines()
header = lines[0:2]
# print(header)
# import sys
# sys.exit(0)
lines = set(lines[2:])
lines.discard('')
lines = list(lines)
lines.sort()

# with open('metadata.md', 'w') as f:
#   for line in header:
#     f.write(line+'\n')    
#   for line in lines:
#     f.write(line+'\n')

with open('README.md', 'w') as f:
  f.write(markdown+'计数: '+str(len(lines))+' 篇。\n\n')
  for line in header:
    f.write(line+'\n')
  lines = set(lines)
  for line in lines:
    f.write(line+'\n')
