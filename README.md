---
title: README
categories:
  - Life
abbrlink: 77cd4175
tags:
---


# Book_arrangement
Hexo博客：[博客](https://booka.wasteland.ink/)

预览网址：[Alist (ics.ink)](https://alist.ics.ink/Edge01/Book_arrangement)

Github：[wasteland-institute/Book_arrangement](https://github.com/wasteland-institute/Book_arrangement)



书籍整理，扫书推书，部分内容来自网络。

## Front-matter 
Front-matter 是文件最上方以 --- 分隔的区域，用于指定文件变量，举例来说：
```text
---
title: README
categories:
- YY向
tags:
- 后宫
- 日常
---
```

只有文章支持分类和标签，您可以在 Front-matter 中设置。在其他系统中，分类和标签听起来很接近，但是在 Hexo 中两者有着明显的差别：分类具有顺序性和层次性，也就是说 `Foo, Bar` 不等于 `Bar, Foo`；而标签没有顺序和层次。

<table><tbody><tr><td><pre class="hljs css">categories:- Diarytags:- PS3- Games</pre></td></tr></tbody></table>

> **分类方法的分歧**
> 
> 如果您有过使用 WordPress 的经验，就很容易误解 Hexo 的分类方式。WordPress 支持对一篇文章设置多个分类，而且这些分类可以是同级的，也可以是父子分类。但是 Hexo 不支持指定多个同级分类。下面的指定方法：
> 
> `categories:  - Diary  - Life`
> 
> 会使分类`Life`成为`Diary`的子分类，而不是并列分类。因此，有必要为您的文章选择尽可能准确的分类。
> 
> 如果你需要为文章添加多个分类，可以尝试以下 list 中的方法。
> 
> `categories:- [Diary, PlayStation]- [Diary, Games]- [Life]`
> 
> 此时这篇文章同时包括三个分类： `PlayStation` 和 `Games` 分别都是父分类 `Diary` 的子分类，同时 `Life` 是一个没有子分类的分类。
