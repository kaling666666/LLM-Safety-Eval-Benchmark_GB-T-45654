import pandas as pd
import json
import os


def process_excel_full(excel_filename, sheet_name, output_json_name):
    """
    完整保留 Excel 所有列的转换函数
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 往上找两级: src/scripts -> src -> 根目录
    project_root = os.path.dirname(os.path.dirname(current_dir))

    # 修改路径：Excel 放在 datasets/sap/ 下
    datasets_dir = os.path.join(project_root, "datasets", "sap")

    excel_path = os.path.join(datasets_dir, excel_filename)
    json_path = os.path.join(datasets_dir, output_json_name)

    if not os.path.exists(excel_path):
        print(f"⚠️ 找不到文件: {excel_path}")
        return

    print(f"\n🔄 正在解析并保留全部字段: [{sheet_name}] 页 ...")

    try:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        df = df.dropna(how='all')
        df = df.fillna("")
        records = df.to_dict(orient='records')

        for row in records:
            if '序号' in row:
                row['序号'] = str(row['序号'])

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=4)

        print(f"   ✅ 转换成功！完整保留了 {len(records)} 条数据，已保存至 {json_path}")

    except Exception as e:
        print(f"   ❌ 转换失败，错误原因: {e}")


if __name__ == "__main__":
    # 这里只需要填文件名，路径已经在函数内部自动拼接好了
    file_name = "GBT45654-2025_生成式AI安全测评测试资产_a1.xlsx"

    # 0, 1, 2 分别代表 Excel 的第 1, 2, 3 个 Sheet 页
    process_excel_full(file_name, 0, "sensitive_words.json")
    process_excel_full(file_name, 1, "content_benchmark.json")
    process_excel_full(file_name, 2, "refusal_benchmark.json")