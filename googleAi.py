import google.generativeai as genai

genai.configure(api_key="AIzaSyAgMzpIabJ9lXecA1dckC-ExZIT5-M0338")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)