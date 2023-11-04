import streamlit as st
import openai
import requests
from PIL import Image

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define function to generate images using DALL-E
def generate_images(prompt):
    response = openai.Completion.create(
        engine="image-alpha-001",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.5,
    )
    image_url = response.choices[0].text.strip()
    image = Image.open(requests.get(image_url, stream=True).raw)
    return image

# Define Streamlit app function
def app():
    st.title("DALL-E Image Generator")

    # Define form inputs
    prompt1 = st.text_input("Prompt 1")
    prompt2 = st.text_input("Prompt 2")
    prompt3 = st.text_input("Prompt 3")
    prompt4 = st.text_input("Prompt 4")
    prompt5 = st.text_input("Prompt 5")
    prompt6 = st.text_input("Prompt 6")
    prompt7 = st.text_input("Prompt 7")

    # Generate images using DALL-E
    if st.button("Generate Images"):
        image1 = generate_images(prompt1)
        image2 = generate_images(prompt2)
        image3 = generate_images(prompt3)
        image4 = generate_images(prompt4)
        image5 = generate_images(prompt5)
        image6 = generate_images(prompt6)
        image7 = generate_images(prompt7)

        # Display generated images
        st.image([image1, image2, image3, image4, image5, image6, image7], width=200)

# Run Streamlit app
if __name__ == "__main__":
    app()
