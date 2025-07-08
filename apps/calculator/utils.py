import google.generativeai as genai
import ast
import json
import re
from PIL import Image
from constants import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def extract_first_list(text):
    """Extract the first top-level Python list from Gemini response."""
    match = re.search(r'\[.*?\]', text, re.DOTALL)
    return match.group(0) if match else "[]"

def analyze_image(img: Image, dict_of_vars: dict):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    dict_of_vars_str = json.dumps(dict_of_vars, ensure_ascii=False)

    prompt = (
        f"You have been given an image with some mathematical expressions, equations, or graphical problems, and you need to solve them. "
        f"Note: Use the PEMDAS rule for solving mathematical expressions. PEMDAS stands for Parentheses, Exponents, Multiplication and Division (L-R), Addition and Subtraction (L-R). "
        f"For example: "
        f"Q. 2 + 3 * 4 → (3 * 4) = 12 → 2 + 12 = 14. "
        f"Q. 2 + 3 + 5 * 4 - 8 / 2 → 20 + 5 - 4 = 21. "
        f"YOU CAN HAVE FIVE TYPES OF EQUATIONS/EXPRESSIONS IN THIS IMAGE, AND ONLY ONE CASE SHALL APPLY EVERY TIME: "
        f"1. Simple math: Return format → [{{'expr': '...', 'result': ...}}] "
        f"2. Set of equations (x, y): Return format → [{{'expr': 'x', 'result': ..., 'assign': True}}, ...] "
        f"3. Variable assignment: Return format → [{{'expr': 'x', 'result': ..., 'assign': True}}] "
        f"4. Graphical math problems (trigonometry, collisions, cricket runs, etc): Return format → [{{'expr': '...', 'result': ...}}] "
        f"5. Abstract drawing concepts: Return format → [{{'expr': '...', 'result': 'concept'}}] "
        f"IMPORTANT RULES:\n"
        f"• Only return a single list of properly quoted Python dictionaries.\n"
        f"• Do NOT use markdown or backticks.\n"
        f"• Do NOT write labels like 'Answer:', just return the list.\n"
        f"• Use double quotes for all keys and string values.\n"
        f"Here is a dictionary of user-assigned variables you must use if referenced: {dict_of_vars_str} "
    )

    response = model.generate_content([prompt, img])

    print("📥 Raw Gemini Response:\n", response.text)

    cleaned_response = extract_first_list(response.text.strip())
    print("🧪 Cleaned for Parsing:\n", cleaned_response)

    answers = []
    try:
        answers = ast.literal_eval(cleaned_response)
    except Exception as e:
        print(f"❌ Error parsing Gemini response: {e}")

    # Normalize structure
    for answer in answers:
        if 'assign' not in answer:
            answer['assign'] = False

    print("✅ Final parsed answers:", answers)
    return answers
