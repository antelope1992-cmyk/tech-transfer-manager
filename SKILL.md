# 职业经理人助手 (Tech Transfer Manager)

## 技能定义
**名称**: 职业经理人助手  
**英文名**: tech-transfer-manager  
**描述**: 一个全面系统化的 AI 智能体，旨在胜任**职业技术经理人**（Technology Transfer Officer）的全部核心工作。它覆盖从**成果挖掘、IP 评估、价值定价、供需匹配、商务谈判、合同生成**到**合规备案、政策申报**的全生命周期自动化流程。

**核心能力**:
- 🕵️ **成果挖掘与评估**: 自动扫描高校/科研院所成果，进行技术成熟度 (TRL) 和知识产权 (IP) 尽职调查。
- 💰 **价值发现与定价**: 基于成本法、市场法、收益法进行技术估值，设计许可/转让模式。
- 🤝 **供需匹配与撮合**: 精准匹配企业需求，生成潜在合作伙伴清单，辅助 NDA 签署。
- 📝 **商务谈判与合同**: 生成交易条款清单 (LOI)，起草技术许可/转让合同，辅助谈判策略。
- ⚖️ **合规与备案**: 指导技术合同登记，匹配政府政策，生成申报材料。
- 🌐 **生态资源链接**: 自动链接投融资机构、中试基地、律所等生态资源。

## 触发词
当用户提到以下关键词时，自动启用此技能：
- 技术转移
- 技术经理人
- 成果转化
- 专利许可
- 技术交易
- 成果评估
- 技术定价
- 技术合同
- 产学研合作
- 技术经纪
- 知识产权运营
- 技术商业化

## 工作流架构
本技能采用**多智能体编排 **(Multi-Agent Orchestration) 模式：
1. **Scout Agent**: 负责成果挖掘与 IP 检索。
2. **Valuator Agent**: 负责技术估值与定价策略。
3. **Matchmaker Agent**: 负责供需匹配与潜在伙伴推荐。
4. **Negotiator Agent**: 负责谈判策略与合同条款生成。
5. **Compliance Agent**: 负责合规审查、合同登记与政策匹配。
6. **Ecosystem Agent**: 负责资源链接与项目申报。

## 技术栈
- **语言**: Python 3.10+
- **核心库**: `requests`, `pandas`, `openpyxl`, `python-docx` (合同生成), `jinja2` (模板引擎)
- **数据源**: 对接专利数据库 (Google Patents/CNKI API 模拟)、企业数据库、政策库。
- **编排**: 基于 `sessions_spawn` 或内部函数调用实现智能体协作。

## 文件结构
```text
SKILLs/tech-transfer-manager/
├── SKILL.md              # 本文件
├── README.md             # 用户指南
├── main.py               # 主入口与任务编排
├── agents/
│   ├── __init__.py
│   ├── scout.py          # 成果挖掘与 IP 评估
│   ├── valuator.py       # 价值评估与定价
│   ├── matchmaker.py     # 供需匹配
│   ├── negotiator.py     # 谈判与合同
│   ├── compliance.py     # 合规与政策
│   └── ecosystem.py      # 资源链接
├── tools/
│   ├── __init__.py
│   ├── ip_search.py      # IP 检索工具
│   ├── market_analysis.py# 市场分析工具
│   ├── contract_gen.py   # 合同生成工具
│   └── policy_match.py   # 政策匹配工具
├── templates/
│   ├── nda_template.docx
│   ├── license_agreement_template.docx
│   ├── valuation_report_template.md
│   └── loi_template.md
└── data/
    ├── policies.json     # 政策库
    └── industry_reports/ # 行业报告
```

## 使用示例
```python
# 启动技能
from tech_transfer_manager.main import run_tech_transfer

# 场景 1: 评估一项高校专利
result = run_tech_transfer(
    task="评估清华大学'新型钙钛矿太阳能电池'专利的商业化潜力",
    stage="full_workflow" # 全流程
)

# 场景 2: 寻找潜在被许可方
result = run_tech_transfer(
    task="为'某新型催化剂'寻找潜在的被许可方企业",
    stage="matching"
)

# 场景 3: 生成技术许可合同
result = run_tech_transfer(
    task="起草一份'某软件系统'的独占许可合同",
    stage="contract_generation"
)
```

## 注意事项
- 本技能生成的估值报告、合同草案仅供参考，**必须**由人类专业律师或评估师审核。
- 涉及真实 IP 检索时，需配置相应的 API Key (如 Google Patents, CNKI)。
- 政策库需定期更新以匹配最新政府文件。
