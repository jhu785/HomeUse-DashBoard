from ics import Calendar
from datetime import datetime
import json

# 读取 ICS 文件
with open(r"C:\Users\ji.hu\Downloads\calendar.ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

# 获取所有未来或历史事件
all_events = []

for event in calendar.events:
    all_events.append({
        "summary": event.name,
        "date": event.begin.date().isoformat()
    })

# 按日期排序
all_events.sort(key=lambda x: x["date"])

# 写入为 JSON 文件
with open("bin_collection_all.json", "w", encoding="utf-8") as out:
    json.dump(all_events, out, indent=2, ensure_ascii=False)

print(f"✅ 成功写入 bin_collection_all.json，共导出 {len(all_events)} 条事件")
