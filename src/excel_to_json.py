import pandas as pd
import json
import os


def process_excel_full(excel_filename, sheet_name, output_json_name):
    """
    完整保留 Excel 所有列的转换函数
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    datasets_dir = os.path.join(project_root, "datasets")

    excel_path = os.path.join(datasets_dir, excel_filename)
    json_path = os.path.join(datasets_dir, output_json_name)

    if not os.path.exists(excel_path):
        print(f"⚠️ 找不到文件: {excel_path}")
        return

    print(f"\n🔄 正在解析并保留全部字段: [{sheet_name}] 页 ...")

    try:
        # 读取指定的 Sheet
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # 去除完全空白的行
        df = df.dropna(how='all')

        # 将 NaN (空单元格) 替换为空字符串，防止 JSON 序列化报错
        df = df.fillna("")

        # 核心：直接将 DataFrame 转换为字典列表 (每一行是一个字典，包含所有列)
        records = df.to_dict(orient='records')

        # 如果“序号”列是数字，转为字符串确保格式统一
        for row in records:
            if '序号' in row:
                row['序号'] = str(row['序号'])

        # 保存为 JSON 文件
        with open(json_path, 'w', encoding='utf-8') as f:
            # indent=4 让 JSON 格式化，方便阅读
            json.dump(records, f, ensure_ascii=False, indent=4)

        print(f"   ✅ 转换成功！完整保留了 {len(records)} 条数据，已保存至 datasets/{output_json_name}")

    except Exception as e:
        print(f"   ❌ 转换失败，错误原因: {e}")


if __name__ == "__main__":
    # ⚠️ 请替换为你真实的 Excel 文件名
    file_name = "GBT45654-2025_生成式AI安全测评测试资产_a1.xlsx"

    # 0, 1, 2 分别代表你的 Excel 里的第 1, 2, 3 个 Sheet 页
    # 关键词库
    process_excel_full(file_name, 0, "sensitive_words.json")
    # 生成内容测试题库
    process_excel_full(file_name, 1, "content_benchmark.json")
    # 拒答测试题库
    process_excel_full(file_name, 2, "refusal_benchmark.json")