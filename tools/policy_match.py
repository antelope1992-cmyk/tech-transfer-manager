"""
Policy Matcher Tool - 政策匹配工具
匹配科技成果转化相关政策
"""

class PolicyMatcher:
    """政策匹配工具"""
    
    def match(self, task_description: str):
        """
        匹配相关政策
        
        Args:
            task_description: 任务描述
        
        Returns:
            list: 匹配的政策列表
        """
        # 模拟政策库
        policies = [
            {
                "name": "促进科技成果转化法",
                "level": "国家法律",
                "key_benefits": [
                    "科研人员可获得不低于 50% 的转化收益",
                    "高校可自主决定成果转化方式",
                    "不纳入国有资产评估管理"
                ],
                "url": "http://www.npc.gov.cn"
            },
            {
                "name": "技术合同增值税减免政策",
                "level": "国家税收",
                "key_benefits": [
                    "技术转让、许可免征增值税",
                    "技术开发免征增值税",
                    "需办理技术合同登记"
                ],
                "url": "http://www.chinatax.gov.cn"
            },
            {
                "name": "高新技术企业认定管理办法",
                "level": "国家政策",
                "key_benefits": [
                    "企业所得税减按 15% 征收",
                    "研发费用加计扣除",
                    "优先支持申报科技项目"
                ],
                "url": "http://www.most.gov.cn"
            },
            {
                "name": "科技创新券管理办法",
                "level": "地方政策",
                "key_benefits": [
                    "最高 50 万元补贴",
                    "可用于购买技术服务",
                    "支持中试、检测等服务"
                ],
                "url": "当地科技局网站"
            },
            {
                "name": "首台（套）重大技术装备保险补偿",
                "level": "国家政策",
                "key_benefits": [
                    "保险费用补贴 80%",
                    "支持首台套装备推广",
                    "降低企业创新风险"
                ],
                "url": "http://www.miit.gov.cn"
            }
        ]
        
        return policies


# 单例模式
policy_matcher = PolicyMatcher()
