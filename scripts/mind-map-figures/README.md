# 408 思维导图配图

`content/docs/408/mind-maps/` 中的配图全部由本目录的脚本生成为 SVG（部分图改写为 Markdown 表格 / 代码直接写进导图）。

- `svgkit.py`：统一的视觉语言（白色圆角卡片、锌灰色系 + 少量柔和强调色、1.5px 线宽、系统中文字体），提供框、箭头、表格、树、图、数组等基础元素。
- `common.py`：多张图共用的组合部件（B 树结点、链表、败者树、数据通路、时序波形、帧格式等）。
- `figs/<id>.py`：一张图的源码，`LABEL` 为无障碍描述，`F` 为画布；`DW` 可覆盖导图中的显示宽度（默认 ≤ 300）。
- `figs/<id>.md`：用 Markdown 代替图片的内容，构建时会替换导图中的 `<img>` 节点。
- `figs/<id>.alias`：内容与另一张图相同，直接复用其 SVG。

修改后在仓库根目录运行：

```bash
python3 scripts/mind-map-figures/build.py
```

脚本会重新生成 `public/images/408-mind-maps/*.svg`，并同步更新 MDX 中 `<img>` 的路径和宽高。
