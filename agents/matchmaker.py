"""
Matchmaker Agent - 供需匹配与撮合智能体
负责：精准匹配潜在合作伙伴、生成推荐清单
"""

class MatchmakerAgent:
    """供需匹配与撮合智能体"""
    
    def run(self, task_description: str, scout_result: dict = None):
        """
        执行供需匹配
        
        Args:
            task_description: 任务描述
            scout_result: 来自 Scout Agent 的结果
        
        Returns:
            dict: 匹配报告
        """
        print("🤝 Matchmaker Agent 启动...")
        
        # 1. 提取技术/需求特征
        features = self._extract_features(task_description)
        
        # 2. 搜索潜在合作伙伴
        candidates = self._search_candidates(features)
        
        # 3. 匹配度评分
        ranked_candidates = self._score_matches(candidates, features)
        
        # 4. 生成推荐清单
        recommendation = self._generate_recommendation(ranked_candidates)
        
        # 5. 生成总结
        summary = self._generate_summary(recommendation)
        
        return {
            "type": "matching_report",
            "features": features,
            "candidates": candidates,
            "ranked_list": ranked_candidates,
            "recommendation": recommendation,
            "summary": summary
        }
    
    def _extract_features(self, task_description: str):
        """提取技术或需求特征"""
        # 简单提取：根据任务描述判断是"技术供给"还是"企业需求"
        if "寻找" in task_description or "引进" in task_description:
            mode = "需求方"
            # 提取需求关键词
            keywords = task_description.replace("寻找", "").replace("引进", "").strip()
        else:
            mode = "供给方"
            # 提取技术关键词
            import re
            keywords = re.findall(r'["\']([^"\']+)["\']', task_description)
            keywords = keywords[0] if keywords else task_description
        
        return {
            "mode": mode,
            "keywords": keywords,
            "industry": self._infer_industry(keywords),
            "stage": self._infer_stage(task_description)
        }
    
    def _infer_industry(self, keywords: str):
        """推断所属行业"""
        industry_map = {
            "电池": "新能源",
            "光伏": "新能源",
            "AI": "人工智能",
            "医疗": "医疗健康",
            "芯片": "半导体",
            "软件": "软件互联网"
        }
        for keyword, industry in industry_map.items():
            if keyword in keywords:
                return industry
        return "其他"
    
    def _infer_stage(self, task_description: str):
        """推断技术阶段"""
        if "量产" in task_description:
            return "产业化"
        elif "中试" in task_description:
            return "中试"
        elif "实验室" in task_description:
            return "实验室"
        else:
            return "早期"
    
    def _search_candidates(self, features: dict):
        """搜索潜在合作伙伴"""
        # 模拟数据库查询
        industry = features.get("industry", "其他")
        
        candidates = {
            "新能源": [
                {"name": "阳光电源", "type": "企业", "location": "合肥", "match_reason": "光伏领域龙头"},
                {"name": "宁德时代", "type": "企业", "location": "宁德", "match_reason": "电池技术领先"},
                {"name": "隆基绿能", "type": "企业", "location": "西安", "match_reason": "光伏制造巨头"}
            ],
            "人工智能": [
                {"name": "百度", "type": "企业", "location": "北京", "match_reason": "AI 研发实力强"},
                {"name": "商汤科技", "type": "企业", "location": "上海", "match_reason": "计算机视觉领先"},
                {"name": "科大讯飞", "type": "企业", "location": "合肥", "match_reason": "语音 AI 龙头"}
            ],
            "医疗健康": [
                {"name": "迈瑞医疗", "type": "企业", "location": "深圳", "match_reason": "医疗器械龙头"},
                {"name": "联影医疗", "type": "企业", "location": "上海", "match_reason": "医学影像设备"},
                {"name": "药明康德", "type": "企业", "location": "上海", "match_reason": "CRO 龙头"}
            ],
            "半导体": [
                {"name": "中芯国际", "type": "企业", "location": "上海", "match_reason": "晶圆代工龙头"},
                {"name": "华为海思", "type": "企业", "location": "深圳", "match_reason": "芯片设计"},
                {"name": "紫光展锐", "type": "企业", "location": "上海", "match_reason": "移动通信芯片"}
            ],
            "软件互联网": [
                {"name": "腾讯", "type": "企业", "location": "深圳", "match_reason": "软件生态强大"},
                {"name": "阿里巴巴", "type": "企业", "location": "杭州", "match_reason": "云计算与 AI"},
                {"name": "字节跳动", "type": "企业", "location": "北京", "match_reason": "算法与数据"}
            ]
        }
        
        return candidates.get(industry, [{"name": "待匹配", "type": "未知", "location": "-", "match_reason": "需进一步调研"}])
    
    def _score_matches(self, candidates: list, features: dict):
        """对候选者进行匹配度评分"""
        ranked = []
        for i, candidate in enumerate(candidates):
            # 模拟评分：基于行业匹配度、规模、地理位置等
            base_score = 80 + (i * 5)  # 简单模拟
            ranked.append({
                **candidate,
                "score": min(base_score, 100),
                "contact_info": "需进一步获取"
            })
        
        # 按分数降序排序
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked
    
    def _generate_recommendation(self, ranked_candidates: list):
        """生成推荐方案"""
        top_3 = ranked_candidates[:3]
        
        actions = []
        for i, candidate in enumerate(top_3, 1):
            actions.append(f"{i}. **{candidate['name']}** (匹配度：{candidate['score']}分)\n   - 理由：{candidate['match_reason']}\n   - 建议：安排技术对接会")
        
        return {
            "top_candidates": top_3,
            "next_steps": [
                "准备技术简介材料 (1-2 页)",
                "签署 NDA 后提供详细技术文档",
                "安排线上/线下技术交流会",
                "准备初步报价方案"
            ],
            "nda_template": "templates/nda_template.docx"
        }
    
    def _generate_summary(self, recommendation):
        """生成匹配总结"""
        top = recommendation["top_candidates"][0]
        summary = f"""
**供需匹配摘要**

1. **匹配对象**: {top['name']}
   - 匹配度：{top['score']}分
   - 推荐理由：{top['match_reason']}

2. **推荐清单 **(Top 3):
"""
        for i, candidate in enumerate(recommendation["top_candidates"], 1):
            summary += f"   {i}. {candidate['name']} ({candidate['score']}分)\n"
        
        summary += f"""
3. **下一步行动**:
   - {recommendation['next_steps'][0]}
   - {recommendation['next_steps'][1]}
   - {recommendation['next_steps'][2]}

**建议**: 优先联系 {top['name']}，其匹配度最高且行业契合。
"""
        return summary.strip()


# 单例模式
matchmaker_agent = MatchmakerAgent()
