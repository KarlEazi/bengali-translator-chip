# Bengali Translator Chip

**Description**: Any language → Bengali translation skill.  
**Input**: 
- text (string)
- source_lang (string, optional, default: "auto")

**Output**: Bengali text

**Usage example**:
```python
from translate import translate
result = translate("Hello world", "en")
print(result)  # "হ্যালো ওয়ার্ল্ড"
