import google.generativeai as genai

API_KEY = "AQ.Ab8RN6KKNK5st-hydVzU3NQxXu7et_3FOHE7PNbf1i6cfc31Bw"

print(API_KEY[:10])

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Hello")
print(response.text)