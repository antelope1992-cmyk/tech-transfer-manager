"""
Scout Agent - 成果挖掘与 IP 评估智能体
负责：技术成熟度评估、IP 尽职调查、竞争技术分析
"""

import re
from tools.ip_search import ip_search_tool

class ScoutAgent:
    """成果挖掘与评估智能体"""
    
    def run(self, task_description: str):
        """
        执行成果挖掘与评估
        
        Args:
            task_description: 任务描述，如 "评估'新型钙钛矿太阳能电池'专利"
        
        Returns:
            dict: 评估报告
        """
        print("🕵️ Scout Agent 启动...")
        
        # 1. 提取关键技术关键词
        keywords = self._extract_keywords(task_description)
        print(f"   提取关键词：{keywords}")
        
        # 2. IP 尽职调查
        ip_report = self._conduct_ip_dd(keywords)
        
        # 3. 技术成熟度 (TRL) 评估
        trl_score = self._assess_trl(task_description)
        
        # 4. 竞争技术分析
        competition_report = self._analyze_competition(keywords)
        
        # 5. 生成总结
        summary = self._generate_summary(ip_report, trl_score, competition_report)
        
        return {
            "type": "scout_report",
            "keywords": keywords,
            "ip_report": ip_report,
            "trl_score": trl_score,
            "competition_report": competition_report,
            "summary": summary
        }
    
    def _extract_keywords(self, task_description: str):
        """从任务描述中提取技术关键词"""
        # 简单提取：去除"评估"、"分析"等动词，保留核心技术名词
        # 实际应用中可使用 NLP 模型提取
        keywords = re.findall(r'["\']([^"\']+)["\']', task_description)
        if not keywords:
            # 如果没有引号，尝试提取技术名称（简单规则）
            keywords = task_description.split()[-3:]  # 取最后几个词作为关键词
        return keywords
    
    def _conduct_ip_dd(self, keywords: list):
        """进行 IP 尽职调查"""
        # 调用 IP 检索工具
        ip_data = ip_search_tool.search(keywords)
        
        return {
            "patent_count": ip_data.get("count", 0),
            "status": ip_data.get("status", "需人工确认"),
            "ownership": ip_data.get("ownership", "需确认权属"),
            "risk_level": ip_data.get("risk_level", "中等"),
            "details": ip_data.get("details", [])
        }
    
    def _assess_trl(self, task_description: str):
        """评估技术成熟度 (TRL)"""
        # 基于任务描述中的线索进行简单评估
        # 实际应用中需结合详细技术文档
        
        trl_mapping = {
            "实验室": 3,
            "中试": 6,
            "量产": 9,
            "原型": 5,
            "概念": 2
        }
        
        score = 4  # 默认值
        for keyword, trl in trl_mapping.items():
            if keyword in task_description:
                score = trl
                break
        
        trl_descriptions = {
            1: "基本原理研究",
            2: "技术概念形成",
            3: "实验室环境验证",
            4: "组件在相关环境验证",
            5: "组件在模拟环境验证",
            6: "系统原型在相关环境演示",
            7: "系统原型在真实环境演示",
            8: "系统完成并通过测试",
            9: "系统实际运行"
        }
        
        return {
            "score": score,
            "level": trl_descriptions.get(score, "未知"),
            "recommendation": "建议进行中试放大" if score < 6 else "具备商业化条件"
        }
    
    def _analyze_competition(self, keywords: list):
        """分析竞争技术"""
        # 模拟竞争分析
        return {
            "main_competitors": ["技术 A", "技术 B", "技术 C"],
            "market_share": "需进一步调研",
            "advantage": "本技术在效率/成本方面具有潜力",
            "disadvantage": "稳定性需验证"
        }
    
    def _generate_summary(self, ip_report, trl_score, competition_report):
        """生成评估总结"""
        summary = f"""
**成果评估摘要**

1. **IP 状态**: 
   - 专利数量：{ip_report['patent_count']}
   - 风险等级：{ip_report['risk_level']}
   - 权属状态：{ip_report['ownership']}

2. **技术成熟度 **(TRL):
   - 当前等级：{trl_score['score']} / 9
   - 阶段描述：{trl_score['level']}
   - 建议：{trl_score['recommendation']}

3. **竞争分析**:
   - 主要竞争者：{', '.join(competition_report['main_competitors'])}
   - 优势：{competition_report['advantage']}
   - 劣势：{competition_report['disadvantage']}

**综合建议**: 该技术{'具备' if trl_score['score'] >= 6 else '暂不具备'}商业化条件，建议{'优先推进' if ip_report['risk_level'] == '低' else '进一步 IP 尽职调查'}。
"""
        return summary.strip()


# 单例模式
scout_agent = ScoutAgent()
