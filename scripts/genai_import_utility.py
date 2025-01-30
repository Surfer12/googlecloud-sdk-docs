from google import genai
from google.genai import types
import base64

def generate():
    client = genai.Client(
        vertexai=True,
        project="credible-datum-447120-p2",
        location="us-central1"
    )

    # Add a default prompt to ensure parts field is populated
    contents = [
        types.Content(
            role="user", 
            parts=[types.Part.from_text("Provide a summary of your capabilities.")]
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=2,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
            )
        ]
    )

    try:
        for chunk in client.models.generate_content_stream(
            model="gemini-2.0-flash-exp",
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk, end="")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate()