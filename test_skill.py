"""
职业经理人助手 - 测试脚本
用于验证 Skill 的各项功能
"""
import sys
import io
# 设置标准输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pathlib import Path

# 添加 Skill 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "tech-transfer-manager"))

from main import run_tech_transfer

def test_full_workflow():
    """测试全流程"""
    print("="*60)
    print("[测试] 开始测试：全流程技术转移")
    print("="*60)
    
    task = "评估'新型钙钛矿太阳能电池'专利的商业化潜力并寻找潜在合作伙伴"
    result = run_tech_transfer(task, "full_workflow")
    
    print("\n" + result["summary"])
    print("\n" + "="*60)
    print("[完成] 测试完成")
    print("="*60)

def test_single_stage():
    """测试单阶段功能"""
    print("="*60)
    print("[测试] 开始测试：单阶段功能")
    print("="*60)
    
    task = "评估'某 AI 医疗影像系统'的技术价值"
    
    # 测试评估阶段
    print("\n--- 测试：成果评估 ---")
    result = run_tech_transfer(task, "scout")
    print(result["scout_result"]["summary"])
    
    # 测试估值阶段
    print("\n--- 测试：价值评估 ---")
    result = run_tech_transfer(task, "valuation")
    print(result["valuation_result"]["summary"])
    
    # 测试匹配阶段
    print("\n--- 测试：供需匹配 ---")
    result = run_tech_transfer(task, "matching")
    print(result["matching_result"]["summary"])
    
    print("\n" + "="*60)
    print("[完成] 单阶段测试完成")
    print("="*60)

if __name__ == "__main__":
    # 运行全流程测试
    test_full_workflow()
    
    # 运行单阶段测试
    # test_single_stage()
