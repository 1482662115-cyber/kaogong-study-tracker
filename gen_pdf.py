from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ======= 注册中文字体 =======
pdfmetrics.registerFont(TTFont('WenQuanYi', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'))
pdfmetrics.registerFont(TTFont('WenQuanYiBold', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'))

# ======= 颜色 =======
C_PRIMARY = HexColor('#2563eb')
C_ACCENT  = HexColor('#059669')
C_RED     = HexColor('#dc2626')
C_AMBER   = HexColor('#d97706')
C_BG2     = HexColor('#f1f5f9')
C_INK     = HexColor('#1a1d24')
C_MUTED   = HexColor('#6b7280')
C_RULE    = HexColor('#e5e7eb')

# ======= 样式 =======
styles = getSampleStyleSheet()

s_title = ParagraphStyle('title', fontName='WenQuanYi', fontSize=22, leading=30,
                         alignment=TA_CENTER, textColor=C_PRIMARY, spaceAfter=4*cm)
s_subtitle = ParagraphStyle('subtitle', fontName='WenQuanYi', fontSize=11, leading=18,
                            alignment=TA_CENTER, textColor=C_MUTED, spaceAfter=1.5*cm)

s_h1 = ParagraphStyle('h1', fontName='WenQuanYi', fontSize=16, leading=22,
                      textColor=C_PRIMARY, spaceBefore=18, spaceAfter=10)
s_h2 = ParagraphStyle('h2', fontName='WenQuanYi', fontSize=13, leading=20,
                      textColor=C_INK, spaceBefore=14, spaceAfter=8)
s_h3 = ParagraphStyle('h3', fontName='WenQuanYi', fontSize=11.5, leading=17,
                      textColor=C_AMBER, spaceBefore=10, spaceAfter=6)

s_body = ParagraphStyle('body', fontName='WenQuanYi', fontSize=10.5, leading=17,
                        textColor=C_INK, spaceAfter=6)
s_indent = ParagraphStyle('indent', fontName='WenQuanYi', fontSize=10.5, leading=17,
                          textColor=C_INK, leftIndent=14, spaceAfter=5)
s_tag = ParagraphStyle('tag', fontName='WenQuanYi', fontSize=9, leading=14,
                        textColor=C_RED, leftIndent=14, spaceAfter=4)
s_hint = ParagraphStyle('hint', fontName='WenQuanYi', fontSize=10, leading=16,
                        textColor=C_ACCENT, leftIndent=14, spaceAfter=6)
s_formula = ParagraphStyle('formula', fontName='WenQuanYi', fontSize=11.5, leading=18,
                            textColor=C_PRIMARY, leftIndent=20, spaceAfter=8)

# ======= 构建PDF =======
out = '/workspace/逻辑判断知识清单.pdf'
doc = SimpleDocTemplate(out, pagesize=A4,
                        leftMargin=2.2*cm, rightMargin=2.2*cm,
                        topMargin=2.2*cm, bottomMargin=2.2*cm,
                        title='逻辑判断知识清单', author='花生十三风格')

story = []

# 封面
story.append(Paragraph('逻辑判断', s_title))
story.append(Paragraph('翻译推理 + 分析推理 · 完整知识清单', s_subtitle))
story.append(Paragraph('花生十三风格 · 人话解释 · 公式口诀 · 真题踩坑', ParagraphStyle(
    'center', fontName='WenQuanYi', fontSize=11, alignment=TA_CENTER, textColor=C_MUTED)))

# ======== Part 1 总框架 ========
story.append(Paragraph('📌 总框架（花生十三分类）', s_h1))
story.append(Paragraph(
    '逻辑判断 → 翻译推理（推出类）+ 分析推理（匹配/排序/分组）', s_body))
story.append(Paragraph(
    '<b>翻译推理</b>：题干有大量"如果…那么… / 只有…才…"，选项是确定结论。', s_indent))
story.append(Paragraph(
    '<b>分析推理</b>：题干有"甲乙丙丁""北京上海"等元素对应关系。', s_indent))

# ======== Part 2 翻译推理 ========
story.append(PageBreak())
story.append(Paragraph('Part 1 · 翻译推理（推出推理）', s_h1))
story.append(Paragraph('考点定位：题干有大量"如果…那么… / 只有…才…"', s_body))

# 1.1 翻译规则
story.append(Paragraph('▶ 1.1 翻译规则（必须动笔写，别在脑子里翻！）', s_h2))

# 前推后
story.append(Paragraph('规则 1 · 前推后', s_h3))
table1 = Table([
    ['中文关键词', '翻译', '人话解释'],
    ['如果 P，那么 Q', 'P → Q', 'P 成立则 Q 必成立'],
    ['只要 P，就 Q', 'P → Q', '同上'],
    ['所有 A 都是 B', 'A → B', '每个 A 都在 B 里'],
    ['A 必须 B / A 就 B', 'A → B', 'A 的前提是 B'],
], colWidths=[4.2*cm, 3.5*cm, 6*cm])
table1.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table1)

# 后推前
story.append(Paragraph('规则 2 · 后推前（最容易翻译错！写手上！）', s_h3))
table2 = Table([
    ['中文关键词', '翻译', '人话解释'],
    ['只有 P，才 Q', 'Q → P', 'Q 成立的前提是 P'],
    ['必须 P，才 Q', 'Q → P', '同上'],
    ['除非 P，否则不 Q', 'Q → P', '等价于"只有 P 才 Q"'],
    ['不 P，不 Q', 'Q → P', '同上'],
    ['P 是 Q 的前提/必要条件', 'Q → P', 'Q 要成立必须有 P'],
], colWidths=[4.5*cm, 3.2*cm, 6*cm])
table2.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_RED),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table2)

# 且/或/否定
story.append(Paragraph('规则 3 · 且 / 或 / 否定', s_h3))
table3 = Table([
    ['中文关键词', '翻译', '人话解释'],
    ['P 并且 Q / 虽然 P 但是 Q', 'P ∧ Q', 'P 和 Q <b>同时成立</b>'],
    ['P 或者 Q / P 或 Q', 'P ∨ Q', 'P 和 Q <b>至少一个</b>'],
    ['要么 P 要么 Q', 'P ⊕ Q', '只能一个成立（考得少）'],
    ['不是 P / 没有 P / 不 P', '¬P', 'P 的否定'],
], colWidths=[4.8*cm, 3*cm, 6*cm])
table3.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_AMBER),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table3)

# 1.2 推理规则
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('▶ 1.2 推理规则（花生十三锁死顺序：逆否→否定肯定→连锁→两难）', s_h2))

# 规则1 逆否
story.append(Paragraph('🥇 规则 1 · 逆否等价（90% 的翻译推理要用）', s_h3))
story.append(Paragraph(
    '<b>P → Q  ⟺  ¬Q → ¬P</b>', s_formula))
story.append(Paragraph(
    '人话版："下雨 → 地湿" = "地没湿 → 没下雨"', s_indent))
story.append(Paragraph(
    '❌ <b>高频坑</b>：P→Q  ≠  ¬P→¬Q（否命题不等价，只有逆否才等价！）', s_tag))
story.append(Paragraph(
    '⚡ 秒杀口诀：<b>逆否就是「前后换，全都加非」</b>', s_hint))

# 规则2 肯前/否后
story.append(Paragraph('🥈 规则 2 · 肯前 / 否后（别脑补，按规则来）', s_h3))
table4 = Table([
    ['已知', '能推出', '不能推出（坑！）'],
    ['P→Q，P 成立', '✅ Q 必成立', '—'],
    ['P→Q，¬Q 成立', '✅ ¬P 必成立', '—'],
    ['P→Q，¬P 成立', '❌ 啥也推不出！', '¬Q（脑补！）'],
    ['P→Q，Q 成立', '❌ 啥也推不出！', 'P（脑补！）'],
], colWidths=[5*cm, 3.5*cm, 5.2*cm])
table4.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table4)

# 规则3 否定肯定
story.append(Paragraph('🥉 规则 3 · 选言命题否定肯定式（练到条件反射）', s_h3))
story.append(Paragraph(
    '<b>A ∨ B  ⟺  ¬A → B  ⟺  ¬B → A</b>', s_formula))
story.append(Paragraph(
    '人话版："要么考国考要么考省考"，没考国考 → 一定考了省考', s_indent))

# 规则4 连锁
story.append(Paragraph('🏅 规则 4 · 连锁推理（串成一条链）', s_h3))
story.append(Paragraph(
    '<b>P → Q，Q → R  ⇒  P → R</b>', s_formula))
story.append(Paragraph(
    '人话版："下雨 → 地湿 → 人滑" = "下雨 → 人滑"', s_indent))

# 规则5 两难
story.append(Paragraph('🏆 规则 5 · 两难推理（简单构成式）', s_h3))
story.append(Paragraph(
    '<b>P → Q，¬P → Q  ⇒  Q 必真</b>', s_formula))
story.append(Paragraph(
    '人话版："考100分买玩具，没考100分也买玩具" → 不管考不考，玩具都有', s_indent))
story.append(Paragraph(
    '🎯 识别标志：两个假言命题的前件完全矛盾（P 和 ¬P），后件完全相同', s_hint))
story.append(Paragraph(
    '⚡ 秒杀口诀：<b>多假言，扫前件，有矛盾，揪后件，后件同，直接选</b>', s_hint))

# 规则6 德摩根
story.append(Paragraph('💎 规则 6 · 德摩根定律（考得少但出现过）', s_h3))
story.append(Paragraph('¬(A ∧ B)  ⟺  ¬A ∨ ¬B', s_formula))
story.append(Paragraph('¬(A ∨ B)  ⟺  ¬A ∧ ¬B', s_formula))

# 做题步骤
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('▶ 1.3 翻译推理做题流程（强制执行）', s_h2))
story.append(Paragraph('Step 1 扫题干 → 找"如果/只有/除非/才能" → 判定翻译推理', s_indent))
story.append(Paragraph('Step 2 动笔翻译 → 写成 P→Q 形式（别脑补！）', s_indent))
story.append(Paragraph('Step 3 写逆否 → 每个 P→Q 立刻写 ¬Q→¬P', s_indent))
story.append(Paragraph('Step 4 连锁 → 首尾相接串成一条链', s_indent))
story.append(Paragraph('Step 5 选答案 → 符合链/两难/否定肯定', s_indent))
story.append(Paragraph('Step 6 验选项 → 代入题干验一遍（能省3分！）', s_indent))

# ======== Part 3 分析推理 ========
story.append(PageBreak())
story.append(Paragraph('Part 2 · 分析推理（匹配/排序/分组）', s_h1))
story.append(Paragraph('⚠️ 花生十三铁律：必须纸上作业，绝不允许在脑子里干想！', ParagraphStyle(
    'warn', fontName='WenQuanYi', fontSize=10.5, leading=16,
    textColor=C_RED, leftIndent=10)))

# 2.1 匹配
story.append(Paragraph('▶ 2.1 匹配型（元素对应 · 最常考）', s_h2))
story.append(Paragraph('特征：多个元素（甲乙丙丁）+ 多个对应位置（四个城市）', s_body))
table5 = Table([
    ['优先级', '解法', '适用场景', '人话解释'],
    ['🥇', '假设代入法', '选项信息充分（全列了）', '直接代入选项，10秒出答案'],
    ['🥈', '最大信息优先', '选项信息不充分', '提到次数最多的元素先确定'],
    ['🥉', '确定信息优先', '有直接给的确定条件', '先锁死确定项，再推其他人'],
], colWidths=[1.6*cm, 2.8*cm, 4*cm, 4.5*cm])
table5.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_ACCENT),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table5)
story.append(Paragraph('⚡ 秒杀口诀：<b>选项全就直接代；选项缺就找最常提；有确定就先锁死</b>', s_hint))

# 2.2 排序
story.append(Paragraph('▶ 2.2 排序型（谁在前谁在后）', s_h2))
story.append(Paragraph('特征：N 个元素按顺序排（谁排第一、谁和谁相邻）', s_body))
story.append(Paragraph('解法（必须画图！）', s_indent))
story.append(Paragraph('① 画数轴：从左到右标位置（1、2、3、4、5）', s_indent))
story.append(Paragraph('② 捆绑法：必须相邻的用括号绑一起（甲乙相邻 → (甲,乙)）', s_indent))
story.append(Paragraph('③ 插空法：必须不相邻的先放其他人再插空隙', s_indent))
story.append(Paragraph('④ 条件代入：每条条件标到数轴上', s_indent))

# 2.3 分组
story.append(Paragraph('▶ 2.3 分组型（把人分几堆）', s_h2))
story.append(Paragraph('特征：N 个元素分成 M 组，每组有数量限制', s_body))
story.append(Paragraph('解法（先满足最少，再自由分配）', s_indent))
story.append(Paragraph('① 先分配最少名额：甲≥3、乙≥2 → 先各分 3、2，用掉 9 个', s_indent))
story.append(Paragraph('② 剩余名额自由分配：隔板法 C(n+m-1, m-1)', s_indent))
story.append(Paragraph('③ 条件锁定：先满足"必同组/必不同组/必在某组"', s_indent))

# 2.4 交叉考点
story.append(Paragraph('▶ 2.4 交叉考点（翻译 + 分析混合 · 真题高频）', s_h2))
story.append(Paragraph('特征：分析推理条件里藏翻译推理！', s_body))
story.append(Paragraph('解法：先把所有条件里的假言命题<b>翻译</b>出来，再结合匹配/排序/分组<b>纸上作业</b>推。两步结合，别混！', s_hint))

# 做题流程
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('▶ 分析推理做题流程（强制执行）', s_h2))
story.append(Paragraph('Step 1 定类型（匹配/排序/分组）', s_indent))
story.append(Paragraph('Step 2 列表格 / 画数轴（强制！！！）', s_indent))
story.append(Paragraph('Step 3 找最大信息 / 确定信息', s_indent))
story.append(Paragraph('Step 4 锁死确定项，排除不可能项', s_indent))
story.append(Paragraph('Step 5 推不出就假设代入（选项全就直接代）', s_indent))
story.append(Paragraph('Step 6 验答案（符合所有条件）', s_indent))

# ======== 补充讲义 ========
story.append(PageBreak())
story.append(Paragraph('🎁 补充讲义（花生十三没讲全但真题考过的）', s_h1))

story.append(Paragraph('1. 翻译推理的"蕴含前件为假则整个命题必真"', s_h3))
story.append(Paragraph('已知 P→Q 为真：', s_body))
story.append(Paragraph('若 P 为真 → Q 必为真', s_indent))
story.append(Paragraph('若 Q 为假 → P 必为假', s_indent))
story.append(Paragraph('若 P 为假 → 无论 Q 真假，P→Q 都为真（真题考过！）', s_indent))
story.append(Paragraph('若 Q 为真 → 无论 P 真假，P→Q 都为真', s_indent))

story.append(Paragraph('2. 分析推理：选项信息充分 vs 不充分', s_h3))
table6 = Table([
    ['选项类型', '例子', '解法'],
    ['充分', 'A. 张-王-李-赵（全列了）', '假设代入法（10秒）'],
    ['不充分', 'A. 张选了（只给一个）', '自己推（最大信息优先）'],
], colWidths=[3.5*cm, 5.5*cm, 4.5*cm])
table6.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table6)

story.append(Paragraph('3. 真假推理的矛盾/反对关系', s_h3))
table7 = Table([
    ['关系', '含义', '例子'],
    ['矛盾关系', '必有一真一假', '甲获奖 vs 甲没获奖'],
    ['反对关系', '可以同假，不能同真', '甲获奖 vs 乙获奖'],
    ['下反对关系', '可以同真，不能同假', '甲没获奖 vs 乙没获奖'],
], colWidths=[3*cm, 5*cm, 5.5*cm])
table7.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_AMBER),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table7)

# ======== 错题对应 ========
story.append(PageBreak())
story.append(Paragraph('🔴 你的错题对应知识点（别再犯了！）', s_h1))
table8 = Table([
    ['你的错题', '错在哪个知识点', '补啥'],
    ['P1Q86（拖欠会费）', '逆否等价写反了', '练逆否：前后换，全都加非'],
    ['P3Q86（政绩观）', '"只有…才…"翻译错了', '后推前！写手上！'],
    ['P2Q91（5选3选派）', '假言连锁没连起来+分组条件漏看', '先翻译再连锁，别在脑子里干想'],
    ['P1Q91/Q92（中药材）', '分析推理没列表格', '强制列表！'],
    ['P1Q47（11本书分3支部）', '隔板法公式不熟', 'C(n+m-1,m-1) 背下来'],
], colWidths=[4.5*cm, 5.5*cm, 4.5*cm])
table8.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'WenQuanYi'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('BACKGROUND', (0,0), (-1,0), C_RED),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('GRID', (0,0), (-1,-1), 0.4, C_RULE),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(table8)

# ======== 终极口诀 ========
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('⚡ 终极秒杀口诀（小抄版）', s_h1))
story.append(Paragraph(
    '<b>翻译推理</b>：前推后、后推前，逆否等价最常用，选言否定肯定式，两难后件直接选', s_formula))
story.append(Paragraph(
    '<b>分析推理</b>：选项全就直接代，选项缺就找最常提，有确定就先锁死，绝不允许脑中转', s_formula))

doc.build(story)
print('✅ PDF 生成成功：', out)
