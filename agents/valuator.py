"""
Valuator Agent - 价值评估与定价智能体
负责：技术估值、定价策略、许可模式设计
"""

class ValuatorAgent:
    """价值评估与定价智能体"""
    
    def run(self, task_description: str, scout_result: dict = None):
        """
        执行价值评估与定价
        
        Args:
            task_description: 任务描述
            scout_result: 来自 Scout Agent 的评估结果
        
        Returns:
            dict: 估值报告
        """
        print("💰 Valuator Agent 启动...")
        
        # 1. 选择估值方法
        methods = self._select_valuation_methods(scout_result)
        
        # 2. 成本法评估
        cost_value = self._cost_approach(task_description)
        
        # 3. 市场法评估
        market_value = self._market_approach(task_description)
        
        # 4. 收益法评估
        income_value = self._income_approach(task_description)
        
        # 5. 综合估值
        final_valuation = self._synthesize_valuation(cost_value, market_value, income_value)
        
        # 6. 定价策略与许可模式
        pricing_strategy = self._design_pricing_strategy(final_valuation)
        
        # 7. 生成总结
        summary = self._generate_summary(final_valuation, pricing_strategy)
        
        return {
            "type": "valuation_report",
            "methods_used": methods,
            "cost_approach": cost_value,
            "market_approach": market_value,
            "income_approach": income_value,
            "final_valuation": final_valuation,
            "pricing_strategy": pricing_strategy,
            "summary": summary
        }
    
    def _select_valuation_methods(self, scout_result):
        """根据技术特点选择估值方法"""
        methods = ["成本法", "市场法", "收益法"]
        # 如果 TRL 较低，减少收益法权重
        if scout_result and scout_result.get("trl_score", {}).get("score", 5) < 5:
            methods.remove("收益法")
        return methods
    
    def _cost_approach(self, task_description: str):
        """成本法评估"""
        # 模拟成本计算
        r_and_d_cost = 500000  # 假设研发成本 50 万
        protection_cost = 50000  # 专利保护成本
        total_cost = r_and_d_cost + protection_cost
        
        return {
            "method": "成本法",
            "rd_cost": r_and_d_cost,
            "protection_cost": protection_cost,
            "total_value": total_cost,
            "currency": "CNY"
        }
    
    def _market_approach(self, task_description: str):
        """市场法评估"""
        # 模拟市场对比
        comparable_deals = [
            {"tech": "类似技术 A", "price": 800000},
            {"tech": "类似技术 B", "price": 1200000},
            {"tech": "类似技术 C", "price": 1000000}
        ]
        avg_price = sum(d["price"] for d in comparable_deals) / len(comparable_deals)
        
        return {
            "method": "市场法",
            "comparable_deals": comparable_deals,
            "average_value": avg_price,
            "currency": "CNY"
        }
    
    def _income_approach(self, task_description: str):
        """收益法评估"""
        # 模拟收益预测
        annual_revenue = 2000000  # 假设年营收 200 万
        royalty_rate = 0.05  # 5% 许可费率
        duration = 5  # 5 年
        total_income = annual_revenue * royalty_rate * duration
        
        return {
            "method": "收益法",
            "annual_revenue": annual_revenue,
            "royalty_rate": royalty_rate,
            "duration_years": duration,
            "total_value": total_income,
            "currency": "CNY"
        }
    
    def _synthesize_valuation(self, cost_value, market_value, income_value):
        """综合估值"""
        # 简单加权平均
        weights = {"cost": 0.3, "market": 0.3, "income": 0.4}
        
        total = (
            cost_value["total_value"] * weights["cost"] +
            market_value["average_value"] * weights["market"] +
            income_value["total_value"] * weights["income"]
        )
        
        return {
            "weighted_value": total,
            "value_range": {
                "low": total * 0.8,
                "high": total * 1.2
            },
            "currency": "CNY",
            "confidence": "中等",
            "assumptions": [
                "基于当前市场数据",
                "假设技术能顺利商业化",
                "未考虑未来技术迭代风险"
            ]
        }
    
    def _design_pricing_strategy(self, valuation: dict):
        """设计定价策略与许可模式"""
        base_value = valuation["weighted_value"]
        
        strategies = {
            "一次性买断": {
                "price": base_value * 1.2,
                "description": "适合技术成熟度高、买方资金充足的情况"
            },
            "入门费 + 提成": {
                "upfront": base_value * 0.3,
                "royalty_rate": 0.05,
                "description": "适合长期合作、降低买方初期风险"
            },
            "作价入股": {
                "equity_percentage": "5-10%",
                "description": "适合深度绑定、共享长期收益"
            }
        }
        
        return {
            "recommended_mode": "入门费 + 提成",
            "options": strategies,
            "negotiation_tips": [
                "强调技术的独特性和竞争优势",
                "提供详细的收益预测数据",
                "考虑设置里程碑付款"
            ]
        }
    
    def _generate_summary(self, valuation, pricing):
        """生成估值总结"""
        summary = f"""
**价值评估与定价摘要**

1. **估值方法**:
   - 使用了：{', '.join(pricing.get('recommended_mode', ['多方法综合']))}
   - 综合估值：¥{valuation['weighted_value']:,.0f}
   - 估值区间：¥{valuation['value_range']['low']:,.0f} - ¥{valuation['value_range']['high']:,.0f}

2. **定价策略**:
   - 推荐模式：{pricing['recommended_mode']}
   - 可选方案:
     - 一次性买断：¥{pricing['options']['一次性买断']['price']:,.0f}
     - 入门费 + 提成：入门费 ¥{pricing['options']['入门费 + 提成']['upfront']:,.0f} + {pricing['options']['入门费 + 提成']['royalty_rate']*100}% 提成
     - 作价入股：{pricing['options']['作价入股']['equity_percentage']} 股权

3. **谈判建议**:
   - {pricing['negotiation_tips'][0]}
   - {pricing['negotiation_tips'][1]}

**重要提示**: 本估值仅供参考，正式交易前请咨询专业评估机构。
"""
        return summary.strip()


# 单例模式
valuator_agent = ValuatorAgent()
