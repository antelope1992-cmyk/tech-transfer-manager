"""
职业经理人助手 (Tech Transfer Manager) - 主入口
负责任务编排、智能体调度与结果汇总
"""

import sys
import os
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from agents.scout import scout_agent
from agents.valuator import valuator_agent
from agents.matchmaker import matchmaker_agent
from agents.negotiator import negotiator_agent
from agents.compliance import compliance_agent
from agents.ecosystem import ecosystem_agent

class TechTransferManager:
    """技术转移全流程管理器"""
    
    def __init__(self):
        self.report = {
            "task": "",
            "stage": "",
            "scout_result": None,
            "valuation_result": None,
            "matching_result": None,
            "contract_result": None,
            "compliance_result": None,
            "ecosystem_result": None,
            "summary": ""
        }
    
    def run_full_workflow(self, task_description: str):
        """运行全流程"""
        print(f"🚀 启动全流程任务：{task_description}")
        self.report["task"] = task_description
        self.report["stage"] = "full_workflow"
        
        # 1. 成果挖掘与评估
        print("🕵️ 正在执行成果挖掘与 IP 评估...")
        self.report["scout_result"] = scout_agent.run(task_description)
        
        # 2. 价值评估与定价
        print("💰 正在执行价值评估与定价...")
        self.report["valuation_result"] = valuator_agent.run(task_description, self.report["scout_result"])
        
        # 3. 供需匹配
        print("🤝 正在执行供需匹配...")
        self.report["matching_result"] = matchmaker_agent.run(task_description, self.report["scout_result"])
        
        # 4. 商务谈判与合同
        print("📝 正在生成谈判策略与合同草案...")
        self.report["contract_result"] = negotiator_agent.run(task_description, self.report["valuation_result"], self.report["matching_result"])
        
        # 5. 合规与政策
        print("⚖️ 正在执行合规审查与政策匹配...")
        self.report["compliance_result"] = compliance_agent.run(task_description, self.report["contract_result"])
        
        # 6. 生态资源链接
        print("🌐 正在链接生态资源...")
        self.report["ecosystem_result"] = ecosystem_agent.run(task_description, self.report["scout_result"])
        
        # 生成总结
        self._generate_summary()
        
        return self.report
    
    def run_stage(self, task_description: str, stage: str):
        """运行指定阶段"""
        self.report["task"] = task_description
        self.report["stage"] = stage
        
        if stage == "scout":
            self.report["scout_result"] = scout_agent.run(task_description)
        elif stage == "valuation":
            self.report["valuation_result"] = valuator_agent.run(task_description, self.report.get("scout_result"))
        elif stage == "matching":
            self.report["matching_result"] = matchmaker_agent.run(task_description, self.report.get("scout_result"))
        elif stage == "contract":
            self.report["contract_result"] = negotiator_agent.run(task_description, self.report.get("valuation_result"), self.report.get("matching_result"))
        elif stage == "compliance":
            self.report["compliance_result"] = compliance_agent.run(task_description, self.report.get("contract_result"))
        elif stage == "ecosystem":
            self.report["ecosystem_result"] = ecosystem_agent.run(task_description, self.report.get("scout_result"))
        else:
            raise ValueError(f"未知阶段：{stage}")
        
        return self.report
    
    def _generate_summary(self):
        """生成综合报告总结"""
        summary = []
        summary.append("## 📊 技术转移全流程综合报告")
        summary.append(f"### 任务：{self.report['task']}")
        summary.append("")
        
        if self.report["scout_result"]:
            summary.append("### 1. 成果评估摘要")
            summary.append(self.report["scout_result"].get("summary", "无"))
            summary.append("")
        
        if self.report["valuation_result"]:
            summary.append("### 2. 价值评估摘要")
            summary.append(self.report["valuation_result"].get("summary", "无"))
            summary.append("")
        
        if self.report["matching_result"]:
            summary.append("### 3. 匹配结果摘要")
            summary.append(self.report["matching_result"].get("summary", "无"))
            summary.append("")
        
        if self.report["contract_result"]:
            summary.append("### 4. 合同与谈判摘要")
            summary.append(self.report["contract_result"].get("summary", "无"))
            summary.append("")
        
        if self.report["compliance_result"]:
            summary.append("### 5. 合规与政策摘要")
            summary.append(self.report["compliance_result"].get("summary", "无"))
            summary.append("")
        
        if self.report["ecosystem_result"]:
            summary.append("### 6. 生态资源摘要")
            summary.append(self.report["ecosystem_result"].get("summary", "无"))
            summary.append("")
        
        self.report["summary"] = "\n".join(summary)


def run_tech_transfer(task: str, stage: str = "full_workflow"):
    """
    对外暴露的主函数
    
    Args:
        task: 任务描述
        stage: 运行阶段 ("full_workflow" 或具体阶段名)
    
    Returns:
        报告字典
    """
    manager = TechTransferManager()
    if stage == "full_workflow":
        return manager.run_full_workflow(task)
    else:
        return manager.run_stage(task, stage)


if __name__ == "__main__":
    # 测试运行
    test_task = "评估'新型钙钛矿太阳能电池'专利的商业化潜力并寻找潜在合作伙伴"
    result = run_tech_transfer(test_task, "full_workflow")
    print("\n" + "="*50)
    print(result["summary"])
    print("="*50)
