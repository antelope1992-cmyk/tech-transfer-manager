"""
Ecosystem Agent - 生态资源链接智能体
负责：链接投融资、中试基地、律所、会计师事务所等生态资源
"""

class EcosystemAgent:
    """生态资源链接智能体"""
    
    def run(self, task_description: str, scout_result: dict = None):
        """
        执行生态资源链接
        
        Args:
            task_description: 任务描述
            scout_result: 来自 Scout Agent 的结果
        
        Returns:
            dict: 资源链接报告
        """
        print("🌐 Ecosystem Agent 启动...")
        
        # 1. 识别资源需求
        needs = self._identify_needs(task_description, scout_result)
        
        # 2. 匹配投融资机构
        investors = self._match_investors(needs)
        
        # 3. 匹配中试基地
        pilot_plants = self._match_pilot_plants(needs)
        
        # 4. 匹配专业服务机构
        services = self._match_professional_services(needs)
        
        # 5. 生成资源对接方案
        plan = self._generate_connection_plan(needs, investors, pilot_plants, services)
        
        # 6. 生成总结
        summary = self._generate_summary(plan)
        
        return {
            "type": "ecosystem_report",
            "needs": needs,
            "investors": investors,
            "pilot_plants": pilot_plants,
            "services": services,
            "connection_plan": plan,
            "summary": summary
        }
    
    def _identify_needs(self, task_description: str, scout_result: dict):
        """识别资源需求"""
        trl = scout_result.get("trl_score", {}).get("score", 4) if scout_result else 4
        
        needs = {
            "stage": "早期" if trl < 5 else ("中试" if trl < 7 else "产业化"),
            "needs_funding": True,
            "needs_pilot": trl < 7,
            "needs_legal": True,
            "needs_accounting": True,
            "industry": scout_result.get("keywords", ["通用"])[0] if scout_result else "通用"
        }
        return needs
    
    def _match_investors(self, needs: dict):
        """匹配投融资机构"""
        stage = needs["stage"]
        
        investors = {
            "早期": [
                {"name": "创新工场", "type": "VC", "focus": "硬科技、AI", "stage": "天使/种子"},
                {"name": "联想创投", "type": "VC", "focus": "硬科技、半导体", "stage": "天使/A 轮"},
                {"name": "真格基金", "type": "VC", "focus": "早期项目", "stage": "天使"}
            ],
            "中试": [
                {"name": "红杉中国", "type": "VC", "focus": "成长期", "stage": "A/B 轮"},
                {"name": "高瓴资本", "type": "PE/VC", "focus": "全阶段", "stage": "A 轮+"},
                {"name": "IDG 资本", "type": "VC", "focus": "硬科技", "stage": "A/B 轮"}
            ],
            "产业化": [
                {"name": "中信产业基金", "type": "PE", "focus": "成熟期", "stage": "B 轮+"},
                {"name": "厚朴投资", "type": "PE", "focus": "成熟期", "stage": "Pre-IPO"},
                {"name": "国家集成电路产业基金", "type": "政府基金", "focus": "半导体", "stage": "产业化"}
            ]
        }
        
        return investors.get(stage, investors["早期"])
    
    def _match_pilot_plants(self, needs: dict):
        """匹配中试基地"""
        industry = needs.get("industry", "通用")
        
        pilot_plants = [
            {"name": "合肥综合性国家科学中心中试基地", "location": "合肥", "focus": "新能源、新材料"},
            {"name": "上海张江生物医药中试平台", "location": "上海", "focus": "生物医药"},
            {"name": "深圳先进院中试基地", "location": "深圳", "focus": "电子、机器人"},
            {"name": "北京亦庄中试基地", "location": "北京", "focus": "智能制造、半导体"}
        ]
        
        # 简单筛选
        if "新能源" in industry or "电池" in industry:
            return [p for p in pilot_plants if "合肥" in p["location"]]
        elif "医疗" in industry:
            return [p for p in pilot_plants if "上海" in p["location"]]
        else:
            return pilot_plants[:2]
    
    def _match_professional_services(self, needs: dict):
        """匹配专业服务机构"""
        return {
            "律所": [
                {"name": "金杜律师事务所", "specialty": "知识产权、技术交易"},
                {"name": "中伦律师事务所", "specialty": "科技法律、并购"},
                {"name": "方达律师事务所", "specialty": "知识产权诉讼"}
            ],
            "会计师事务所": [
                {"name": "普华永道", "specialty": "科技行业审计、税务"},
                {"name": "德勤", "specialty": "科技行业咨询、审计"},
                {"name": "立信会计师事务所", "specialty": "国内科技型企业"}
            ],
            "知识产权服务机构": [
                {"name": "中原信达知识产权", "specialty": "专利代理、诉讼"},
                {"name": "柳沈律师事务所", "specialty": "IP 战略、海外布局"}
            ]
        }
    
    def _generate_connection_plan(self, needs: dict, investors: list, pilot_plants: list, services: dict):
        """生成资源对接方案"""
        plan = {
            "timeline": [],
            "priority_contacts": [],
            "action_items": []
        }
        
        # 根据阶段生成时间线
        if needs["stage"] == "早期":
            plan["timeline"] = [
                "1. 准备商业计划书 (BP)",
                "2. 接触天使/种子期 VC",
                "3. 完成种子轮融资",
                "4. 推进技术验证"
            ]
            plan["priority_contacts"] = investors[:2]
        elif needs["stage"] == "中试":
            plan["timeline"] = [
                "1. 选择中试基地",
                "2. 进行中试放大",
                "3. 准备 A 轮融资材料",
                "4. 接触 A 轮 VC"
            ]
            plan["priority_contacts"] = pilot_plants[:1] + investors[:2]
        else:
            plan["timeline"] = [
                "1. 规模化生产准备",
                "2. B 轮/C 轮融资",
                "3. 市场拓展",
                "4. 考虑 IPO 或并购"
            ]
            plan["priority_contacts"] = investors[:2]
        
        plan["action_items"] = [
            "准备标准 BP 和技术简介",
            "整理财务数据和 IP 清单",
            "预约律所进行 IP 尽职调查",
            "联系中试基地洽谈合作"
        ]
        
        return plan
    
    def _generate_summary(self, plan: dict):
        """生成资源链接总结"""
        summary = f"""
**生态资源链接摘要**

1. **推荐资源**:
   - **投融资机构**:
"""
        for i, inv in enumerate(plan["priority_contacts"][:3], 1):
            if isinstance(inv, dict) and "name" in inv:
                summary += f"     {i}. {inv['name']}\n"
        
        summary += f"""
   - **中试基地**: (如需要)
     - 合肥综合性国家科学中心中试基地
     - 上海张江生物医药中试平台
   
   - **专业服务机构**:
     - 律所：金杜、中伦
     - 会计所：普华永道、德勤
     - IP 机构：中原信达

2. **对接时间线**:
"""
        for item in plan["timeline"]:
            summary += f"   - {item}\n"
        
        summary += f"""
3. **下一步行动**:
   - {plan['action_items'][0]}
   - {plan['action_items'][1]}
   - {plan['action_items'][2]}

**建议**: 优先联系推荐的投融资机构，同时启动中试基地考察和专业服务机构聘请。
"""
        return summary.strip()


# 单例模式
ecosystem_agent = EcosystemAgent()
