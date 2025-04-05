import re


with open("exportedData.txt", "r", encoding="utf-8") as f:
    log_data = f.read()  




pattern = re.compile(r"(started a call that lasted )((?:(\d+ hours? )?(\d+ minutes? )?)?\d+ seconds?)")


def normalize_duration(match):
    prefix = match.group(1)
    duration = match.group(2)
    if "hour"  not in duration:
        duration = "0 hours " + duration
    return prefix + duration


normalized_log = pattern.sub(normalize_duration, log_data)



with open("exportedData.txt", "w", encoding="utf-8") as f:
    f.write(normalized_log)