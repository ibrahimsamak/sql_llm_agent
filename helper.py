import re

def clean_sql(text: str) -> str:
    # remove ```sql ... ``` fences
    text = re.sub(r"```(?:sql)?", "", text, flags=re.IGNORECASE).strip()
    # drop a leading "SQLQuery:" label if present
    if "SQLQuery:" in text:
        text = text.split("SQLQuery:", 1)[1]
    # keep only the first statement (cut off SQLResult:/Answer:/extra ;)
    text = text.split(";")[0].strip() + ";"
    return text
