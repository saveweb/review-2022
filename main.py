import os

flag = 0
markdown = """# 2022年终总结

> 2021 年的年终总结见：[saveweb/review-2021](https://github.com/saveweb/review-2021)

本项目将长期维护（直到2024年初），因为[以往的经验](https://t.me/blogrsslist/269)告诉我——有些博主的年终总结可能要[拖拉个半年才写得完](https://idealclover.top/archives/627/)，还有些博主明明都年中了才写完了上一年的年终总结，又觉得不好意思[而自己把文章发布时间改成年初](https://github.com/saveweb/review-2021/commit/558ba32ef42025dd1bf2da31c2c1fb60e05e2524)，掩耳盗铃。有趣有趣……

链接后面的数字是我们对每个博客分配的博客ID，有什么用呢？自行探索其它仓库。

**想要添加您的年终总结？请发 Issue 或编辑 metadata.md 发PR（不需要填写博客ID）。**

---

### 相关链接:
| [Save The Web's Telegram Channel](https://t.me/saveweb) | [独立博客&播客全订阅's Telegram Channel](https://t.me/blogrsslist) | [Github Org](https://github.com/saveweb)
| --- | --- | --- |

### 友情链接:
- 待确定

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
