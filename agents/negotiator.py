"""
Negotiator Agent - 商务谈判与合同生成智能体
负责：谈判策略制定、LOI 生成、合同草案起草
"""

from tools.contract_gen import contract_generator

class NegotiatorAgent:
    """商务谈判与合同生成智能体"""
    
    def run(self, task_description: str, valuation_result: dict = None, matching_result: dict = None):
        """
        执行谈判与合同生成
        
        Args:
            task_description: 任务描述
            valuation_result: 来自 Valuator Agent 的结果
            matching_result: 来自 Matchmaker Agent 的结果
        
        Returns:
            dict: 谈判与合同报告
        """
        print("📝 Negotiator Agent 启动...")
        
        # 1. 制定谈判策略
        strategy = self._formulate_strategy(valuation_result, matching_result)
        
        # 2. 生成 LOI (条款清单)
        loi = self._generate_loi(task_description, valuation_result)
        
        # 3. 起草合同
        contract = self._draft_contract(task_description, valuation_result, matching_result)
        
        # 4. 风险审查
        risks = self._review_risks(contract)
        
        # 5. 生成总结
        summary = self._generate_summary(strategy, loi, contract, risks)
        
        return {
            "type": "negotiation_report",
            "strategy": strategy,
            "loi": loi,
            "contract": contract,
            "risks": risks,
            "summary": summary
        }
    
    def _formulate_strategy(self, valuation_result: dict, matching_result: dict):
        """制定谈判策略"""
        # 提取估值信息
        value = valuation_result.get("final_valuation", {}).get("weighted_value", 1000000) if valuation_result else 1000000
        
        strategy = {
            "opening_offer": value * 1.3,  # 开局报价上浮 30%
            "target_price": value,  # 目标价格
            "walk_away_price": value * 0.7,  # 底线价格
            "key_leverage_points": [
                "技术的独特性和专利保护",
                "市场增长潜力",
                "先发优势"
            ],
            "concession_plan": [
                {"item": "许可费率", "initial": "8%", "target": "5%", "final": "3%"},
                {"item": "独家性", "initial": "独占", "target": "排他", "final": "普通"},
                {"item": "付款周期", "initial": "一次性", "target": "分期", "final": "分期 + 提成"}
            ],
            "negotiation_tips": [
                "强调技术的长期价值而非短期收益",
                "准备多个备选方案",
                "保持灵活但坚守底线"
            ]
        }
        return strategy
    
    def _generate_loi(self, task_description: str, valuation_result: dict):
        """生成 LOI (意向书/条款清单)"""
        value = valuation_result.get("final_valuation", {}).get("weighted_value", 1000000) if valuation_result else 1000000
        
        loi = {
            "title": "技术许可/转让意向书 (LOI)",
            "parties": {
                "licensor": "技术持有方",
                "licensee": "意向被许可方"
            },
            "key_terms": {
                "transaction_type": "技术许可",
                "scope": "独占许可",
                "territory": "中国大陆",
                "duration": "5 年",
                "financial_terms": {
                    "upfront_fee": value * 0.3,
                    "royalty_rate": "5%",
                    "minimum_annual_royalty": value * 0.1
                },
                "milestones": [
                    "签署合同后 30 日内支付入门费",
                    "技术交付后 60 日内完成验收",
                    "每年按销售额支付提成"
                ]
            },
            "validity": "本 LOI 有效期 30 天",
            "confidentiality": "双方需签署 NDA",
            "next_steps": "签署正式合同"
        }
        return loi
    
    def _draft_contract(self, task_description: str, valuation_result: dict, matching_result: dict):
        """起草合同"""
        # 调用合同生成工具
        contract_content = contract_generator.generate(
            contract_type="技术许可合同",
            licensor="技术持有方",
            licensee=matching_result.get("top_candidates", [{}])[0].get("name", "意向方") if matching_result else "意向方",
            valuation=valuation_result.get("final_valuation", {}).get("weighted_value", 1000000) if valuation_result else 1000000
        )
        
        return {
            "type": "contract_draft",
            "title": "技术许可合同 (草案)",
            "content": contract_content,
            "file_path": "output/contract_draft.docx",
            "sections": [
                "第一条 定义",
                "第二条 许可范围",
                "第三条 许可费用",
                "第四条 技术交付",
                "第五条 保密义务",
                "第六条 知识产权归属",
                "第七条 违约责任",
                "第八条 争议解决",
                "第九条 合同期限与终止"
            ]
        }
    
    def _review_risks(self, contract: dict):
        """风险审查"""
        risks = [
            {
                "type": "法律风险",
                "description": "需确认 IP 权属清晰，无侵权纠纷",
                "severity": "高",
                "mitigation": "进行完整的 IP 尽职调查"
            },
            {
                "type": "商业风险",
                "description": "技术商业化失败风险",
                "severity": "中",
                "mitigation": "设置里程碑付款，与商业化进展挂钩"
            },
            {
                "type": "财务风险",
                "description": "被许可方支付能力不足",
                "severity": "中",
                "mitigation": "要求银行保函或分期付款担保"
            },
            {
                "type": "技术风险",
                "description": "技术交付后无法达到预期效果",
                "severity": "中",
                "mitigation": "明确验收标准，设置技术支持期"
            }
        ]
        return {
            "risk_assessment": risks,
            "overall_risk_level": "中等",
            "recommendations": [
                "聘请专业律师审核合同",
                "购买知识产权保险",
                "设置履约保证金"
            ]
        }
    
    def _generate_summary(self, strategy, loi, contract, risks):
        """生成谈判与合同总结"""
        summary = f"""
**商务谈判与合同摘要**

1. **谈判策略**:
   - 开局报价：¥{strategy['opening_offer']:,.0f}
   - 目标价格：¥{strategy['target_price']:,.0f}
   - 底线价格：¥{strategy['walk_away_price']:,.0f}
   - 关键筹码：{', '.join(strategy['key_leverage_points'][:2])}

2. **LOI 核心条款**:
   - 交易类型：{loi['key_terms']['transaction_type']}
   - 许可范围：{loi['key_terms']['scope']}
   - 入门费：¥{loi['key_terms']['financial_terms']['upfront_fee']:,.0f}
   - 提成率：{loi['key_terms']['financial_terms']['royalty_rate']}

3. **合同草案**:
   - 文件：{contract['title']}
   - 主要章节：{len(contract['sections'])} 条

4. **风险审查**:
   - 总体风险等级：{risks['overall_risk_level']}
   - 主要风险：
     - {risks['risk_assessment'][0]['type']}: {risks['risk_assessment'][0]['description']}
     - {risks['risk_assessment'][1]['type']}: {risks['risk_assessment'][1]['description']}

**建议**: 
- 按 LOI 条款推进谈判
- 聘请专业律师审核正式合同
- 重点关注 IP 权属和支付保障条款
"""
        return summary.strip()


# 单例模式
negotiator_agent = NegotiatorAgent()
