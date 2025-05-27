from ics import Calendar
from datetime import datetime, timezone
import json

# 读取 ICS 文件
with open("calendar.ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

# 获取当前时间
now = datetime.now(timezone.utc)

# 提取未来事件
future_events = [
    event for event in calendar.events
    if event.begin.datetime >= now
]

# 按时间排序
future_events.sort(key=lambda e: e.begin.datetime)

# 只保留 summary 和 date 字段（前 30 条）
output = [
    {
        "summary": event.name,
        "date": event.begin.date().isoformat()
    }
    for event in future_events[:30]
]

# 写入 bin_collection.json
with open("bin_collection.json", "w", encoding="utf-8") as out:
    json.dump(output, out, indent=2, ensure_ascii=False)

print(f"✅ 生成成功：{len(output)} 条写入 bin_collection.json")
