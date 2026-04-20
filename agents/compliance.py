"""
Compliance Agent - 合规审查与政策申报智能体
负责：合规审查、技术合同登记、政策匹配与申报
"""

from tools.policy_match import policy_matcher

class ComplianceAgent:
    """合规审查与政策申报智能体"""
    
    def run(self, task_description: str, contract_result: dict = None):
        """
        执行合规审查与政策匹配
        
        Args:
            task_description: 任务描述
            contract_result: 来自 Negotiator Agent 的结果
        
        Returns:
            dict: 合规与政策报告
        """
        print("⚖️ Compliance Agent 启动...")
        
        # 1. 合规审查
        compliance_check = self._conduct_compliance_check(contract_result)
        
        # 2. 技术合同登记指导
        registration_guide = self._generate_registration_guide(task_description)
        
        # 3. 政策匹配
        policies = self._match_policies(task_description)
        
        # 4. 申报材料清单
        materials = self._generate_materials_list(policies)
        
        # 5. 生成总结
        summary = self._generate_summary(compliance_check, registration_guide, policies)
        
        return {
            "type": "compliance_report",
            "compliance_check": compliance_check,
            "registration_guide": registration_guide,
            "policies": policies,
            "materials_list": materials,
            "summary": summary
        }
    
    def _conduct_compliance_check(self, contract_result: dict):
        """进行合规审查"""
        issues = []
        
        # 检查合同关键条款
        if contract_result:
            contract = contract_result.get("contract", {})
            # 模拟检查
            issues.append({
                "item": "知识产权归属",
                "status": "需明确",
                "recommendation": "明确约定改进技术的归属"
            })
            issues.append({
                "item": "保密条款",
                "status": "完整",
                "recommendation": "保持现有条款"
            })
            issues.append({
                "item": "违约责任",
                "status": "需细化",
                "recommendation": "明确违约金计算方式"
            })
        
        return {
            "overall_status": "需修改",
            "issues": issues,
            "legal_review_required": True,
            "recommendations": [
                "聘请专业律师审核",
                "补充不可抗力条款",
                "明确争议解决方式（仲裁/诉讼）"
            ]
        }
    
    def _generate_registration_guide(self, task_description: str):
        """生成技术合同登记指南"""
        guide = {
            "registration_type": "技术许可合同登记",
            "authority": "当地科技主管部门",
            "required_documents": [
                "技术合同登记申请表",
                "技术合同原件（一式三份）",
                "双方营业执照/身份证复印件",
                "知识产权证明文件",
                "技术说明材料",
                "发票或付款凭证（如已付款）"
            ],
            "process": [
                "1. 准备上述材料",
                "2. 登录'全国技术合同认定登记系统'",
                "3. 在线提交申请",
                "4. 提交纸质材料至登记点",
                "5. 审核通过后获取《技术合同认定登记证明》"
            ],
            "timeline": "通常 10-15 个工作日",
            "benefits": [
                "享受增值税减免",
                "作为高新技术企业认定依据",
                "申请科技项目支持"
            ]
        }
        return guide
    
    def _match_policies(self, task_description: str):
        """匹配相关政策"""
        # 调用政策匹配工具
        matched_policies = policy_matcher.match(task_description)
        
        # 模拟政策库
        policies = [
            {
                "name": "科技成果转化奖励政策",
                "level": "国家",
                "benefit": "科研人员可获得不低于 50% 的转化收益",
                "deadline": "长期有效",
                "apply_url": "http://www.most.gov.cn"
            },
            {
                "name": "技术合同增值税减免",
                "level": "国家",
                "benefit": "技术转让、许可免征增值税",
                "deadline": "长期有效",
                "apply_url": "http://www.chinatax.gov.cn"
            },
            {
                "name": "高新技术企业认定",
                "level": "国家",
                "benefit": "企业所得税减按 15% 征收",
                "deadline": "每年分批",
                "apply_url": "http://www.most.gov.cn"
            },
            {
                "name": "科技创新券",
                "level": "地方",
                "benefit": "最高 50 万元补贴",
                "deadline": "按季度",
                "apply_url": "当地科技局网站"
            }
        ]
        
        return policies
    
    def _generate_materials_list(self, policies: list):
        """生成申报材料清单"""
        materials = []
        for policy in policies[:3]:  # 取前 3 个政策
            materials.append({
                "policy": policy["name"],
                "required_materials": [
                    f"{policy['name']}申请表",
                    "营业执照/法人证书",
                    "技术合同认定登记证明",
                    "财务报表",
                    "知识产权清单",
                    "其他专项材料"
                ]
            })
        
        return materials
    
    def _generate_summary(self, compliance_check, registration_guide, policies):
        """生成合规与政策总结"""
        summary = f"""
**合规审查与政策申报摘要**

1. **合规审查**:
   - 总体状态：{compliance_check['overall_status']}
   - 需关注问题:
     - {compliance_check['issues'][0]['item']}: {compliance_check['issues'][0]['recommendation']}
     - {compliance_check['issues'][2]['item']}: {compliance_check['issues'][2]['recommendation']}
   - 建议：{compliance_check['recommendations'][0]}

2. **技术合同登记**:
   - 类型：{registration_guide['registration_type']}
   - 所需材料：{len(registration_guide['required_documents'])} 项
   - 办理时限：{registration_guide['timeline']}
   - 主要优惠：{registration_guide['benefits'][0]}

3. **匹配政策 **(Top 3):
"""
        for i, policy in enumerate(policies[:3], 1):
            summary += f"   {i}. **{policy['name']}** ({policy['level']})\n"
            summary += f"      - 优惠：{policy['benefit']}\n"
        
        summary += f"""
4. **下一步行动**:
   - 完成合同修改与律师审核
   - 准备技术合同登记材料
   - 提交登记申请
   - 根据登记证明申报相关政策

**提示**: 技术合同登记是享受税收优惠和政策支持的前提，建议优先办理。
"""
        return summary.strip()


# 单例模式
compliance_agent = ComplianceAgent()
