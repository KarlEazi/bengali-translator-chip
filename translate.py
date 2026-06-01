from deep_translator import GoogleTranslator

def translate(text: str, source_lang: str = "auto") -> str:
    """
    যেকোনো ভাষা থেকে বাংলায় ট্রান্সলেট করে।
    source_lang = "auto" রাখলে নিজে থেকে ডিটেক্ট করে।
    """
    try:
        translator = GoogleTranslator(source=source_lang, target="bn")
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"
