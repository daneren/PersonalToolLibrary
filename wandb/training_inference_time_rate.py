import wandb
import pandas as pd # 引入 pandas 进行数据处理

# 假设您的项目名称是 'my-ml-project'
# 替换为您的实际项目路径： 'entity/project-name'
api = wandb.Api()
project_path = "lr-experiment/DAPO-FP8-ROLLOUT"

# 替换为您的两次实验的完整路径或 Run ID
run1_path = f"lr-experiment/DAPO-FP8-ROLLOUT/svp0p3rf" 
run2_path = f"lr-experiment/DAPO-FP8-ROLLOUT/q6ibz7ti" 

# 要计算平均值的指标
metric_key1 = "timing_s/step"
metric_key2 = "timing_s/gen"

# --- 新增的 Step 范围参数 ---
START_STEP = 0
END_STEP = 20
# -----------------------------

def calculate_mean_metric_in_range(run_path, metric, start_step, end_step):
    """
    从 W&B Run 中获取指定指标在 [start_step, end_step] 范围内的平均值。
    """
    try:
        run = api.run(run_path)
        # 获取包含 metric 和 _step 的所有历史数据
        history = run.history(keys=[metric, '_step'], samples=1000) 
        
        # 1. 检查数据是否存在
        if metric not in history or history.empty:
            print(f"⚠️ 实验 {run.name}: 找不到指标 {metric} 的数据。")
            return None

        # 2. 筛选 Step 范围
        # 使用 W&B 自动生成的 _step 列进行筛选
        filtered_history = history[
            (history['_step'] >= start_step) & 
            (history['_step'] <= end_step)
        ]

        # 3. 计算平均值
        if not filtered_history.empty:
            mean_value = filtered_history[metric].mean()
            std_value = filtered_history[metric].std() 
            count = len(filtered_history)

            print(f"✅ 实验 {run.name}: (Step {start_step} to {end_step}, 共 {count} 个点)")
            print(f"   范围平均 {metric}: {mean_value:.2f}")
            print(f"   范围标准差 {metric}: {std_value:.2f}")
            return mean_value
        else:
            print(f"⚠️ 实验 {run.name}: 在 Step {start_step} 到 {end_step} 范围内没有找到数据。")
            return None
            
    except Exception as e:
        print(f"❌ 运行 {run_path} 发生错误: {e}")
        return None

print(f"--- 计算指标: {metric_key1} vs {metric_key2} 在 Step {START_STEP} 到 {END_STEP} 范围内的平均值 ---")
mean1 = calculate_mean_metric_in_range(run1_path, metric_key1, START_STEP, END_STEP)
mean2 = calculate_mean_metric_in_range(run1_path, metric_key2, START_STEP, END_STEP)

print(f"mean1: {mean1}")
print(f"mean2: {mean2}")
mean_train = mean1-mean2
print(f"mean1-mean2: {mean_train:.2f}")
print(f"mean2 / (mean1-mean2): {mean2 / mean_train:.2f}")



print(f"--- 计算指标: {metric_key1} vs {metric_key2} 在 Step {START_STEP} 到 {END_STEP} 范围内的平均值 ---")
mean1 = calculate_mean_metric_in_range(run2_path, metric_key1, START_STEP, END_STEP)
mean2 = calculate_mean_metric_in_range(run2_path, metric_key2, START_STEP, END_STEP)

print(f"mean1: {mean1}")
print(f"mean2: {mean2}")
mean_train = mean1-mean2
print(f"mean1-mean2: {mean_train:.2f}")
print(f"mean2 / (mean1-mean2): {mean2 / mean_train:.2f}")