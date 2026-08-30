---
title: "20ms把PDF变成Markdown！开源OCR神器快了近300倍"
source: 量子位
url: https://www.qbitai.com/2026/08/481075.html
date: 2026-08-30
published_at: 2026-08-29T12:26:49+00:00
tag: 工具开源
item_id: 6dba216035658442
---
# 20ms把PDF变成Markdown！开源OCR神器快了近300倍

3秒可处理200份PDF

##### 文婷 发自 凹非寺

量子位 | 公众号 QbitAI

**曾经只能手动摘取PDF文字、结果乱码一堆、LLM还看不懂的苦逼日子——**

**终于要结束了！**

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/2616afffa2efaf61b3d1b5bb0dff317a.webp)

Y Combinator孵化的明星项目Firecrawl团队最近放了个大招：

其联合创始人兼CTO Nicolas Camara宣布，他们最新开发的**OCR It**可以**在20ms内**将一份不可复制的PDF文件内的所有文字内容提炼完，并将其转化成清晰的Markdown格式，AI读完马上就能看懂。

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/0849fa29f26e18e18251e2d2ce568b7e.webp)

20ms是什么概念？

相当于**你刚点完确定还没眨完眼，一份处理好的Markdown文件就已经清清爽爽地交到你手上了。**

而且它还不需要联网，可以**100%Offline via Bundled Tesseract**。

这个刚刚开源的OCR工具才刚发布，就**在GitHub上获得了热门关注。**

Nicolas Camara骄傲地表示，**在处理质量与Docling旗鼓相当的前提下，OCR It的处理速度比Docling快了近300倍！**

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/9d67062d14b0c48c67ac3b151dafedcf.webp)

小伙伴们测完也纷纷在X上留言：

**快，确实快得很啊！![👍](https://i.qbitai.com/wp-content/uploads/2026/08/564d3c3de1ce231cff1295da7dcf2420.webp)**


![图片](https://i.qbitai.com/wp-content/uploads/2026/08/1de757ff02f510e70a8bb45070e71921.webp)

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/134fef2acc74192662d4436804a103f8.webp)


![图片](https://i.qbitai.com/wp-content/uploads/2026/08/acbb82a08e133af5c94cb8c26ee36c5b.webp)


## OCR It怎么用

首先，OCR It是一款**适用于Chrome和Firefox**的免费浏览器插件。

你只需框选一次区域，之后每按一次快捷键（或开启自动模式），它就能把整本书或整个文档变成完整且可编辑的纯文本，方便你直接喂给AI进行总结或提问。

期间，**OCR It会默认在连续识别到两张相同页面、无法继续翻页、OCR失败或达到300页上限时自动停止**，避免在末页无限重复抓取。

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/14516053cf570840bed453367bd34312.webp)

具体而言，手动和自动档可以分别按以下的几个步骤操作：

*（注：用Windows和Linux的小伙伴们需将option键替换为Alt）*

1、手动档：

- **框选和识别：**

**首先按Option+Shift+R**选定需要识别的文字区域，**确认无误后按Enter保存**；

完成第一步框选文字区域之后，按一次Option+Shift+S，OCR It就会开始识别当前页面，并在识别完成后会自动翻到下一页。

接下来你只需要重复这个操作直到整份文档识别完毕就好了。

如果你希望进一步节省时间的话，**你也可以一边翻页一边在每一页按一次Option+Shift+S，系统会立即截图并在后台自动排队执行识别任务。**

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/36d8fb10dc7c3f64d0beb2ae0667469d.webp)

- **检查：**
 全部识别完成后，你可以在插件面板中检查、修改文本，也可以重新识别单独某一页，最后选择 **“Copy all”** 或**“Download .txt”** 导出全文，整个任务就完成啦！

![](https://i.qbitai.com/wp-content/uploads/2026/08/2d34718d98247077249cdaad3d0e1fa8.webp)

2、**自动档**：

自动挡的话就简单多了，你只需要按下**Option+Shift+A或点击Start auto-run**，OCR It便会自动循环执行“截图—OCR—翻页”，直至文档结束。

**如果你想中途结束任务的话，按ESC就行**，检查流程几乎和手动档一致。

此外，OCR It仓库界面显示，**它既不需要API Key、联网、安装时也不需要索取任何网站权限，它只会在需要自动运行或操作跨域iframe时才按需申请当前站点的权限。**

另外，浏览器内置PDF阅读器目前也还暂时不支持自动翻页，所以大家在处理这类PDF时，还是尽量用手动档处理吧。

## 处理复杂任务时还不太稳定

不过，OCR It虽然看起来又快又方便，但**还远没有到“以后把所有PDF都丢给它，就能高枕无忧”的程度。**

![图片](https://i.qbitai.com/wp-content/uploads/2026/08/26914102c54dbcea01dd05a35ae74e56.webp)

网友们通过实测达成的一个共识是：

OCR It目前可以相当顺手地处理版式简单、文字清晰的PDF文档，但它**还不太能处理一些标题、脚注、表格、数学公式和正文段落混排的复杂页面**，所以它还有不小的提升空间。


![图片](https://i.qbitai.com/wp-content/uploads/2026/08/7589bababe54be54669a44c4555f2999.webp)

让我们期待一下团队后续的更新吧！

感兴趣的小伙伴们可以点进文末第二个链接看看，欢迎跟我们分享你的测试结果～
![👇](https://i.qbitai.com/wp-content/uploads/2026/08/75b112db7f2dc512ef221e3a2d9cc558.webp)


参考链接：

[1]https://x.com/nickscamara_/status/2083295265793212827

[2]https://github.com/thiagotigaz/ocr-it

[3]https://www.firecrawl.dev/about

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


![](http://www.qbitai.com/wp-content/themes/liangziwei/imagesnew/head.jpg)

- [100%开源！吴恩达做了个个人桌面Agent](https://www.qbitai.com/2026/07/460892.html)*2026-07-25*
- [OpenAI官方教你8招玩透ChatGPT！](https://www.qbitai.com/2026/07/452611.html)*2026-07-17*
