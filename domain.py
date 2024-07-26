import google.generativeai as genai
import json
import streamlit as st

st.title("Roadmap Generator")

def generate_roadmap(domain):
    """Generates a Roadmap based on given parameter.

    Args:
        domain: Type of Domain as per user's requirement 

    Returns:
        A dictionary containing the Roadmap, or None if an error occurs.
    """
    try:
        # Configure API key
        genai.configure(api_key="AIzaSyDWZkP2r17QA3Q_zWxbv70LoEsXYufLeY0")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are an expert in coding. and you would like to learn new technologies for that you need a roadmap for the particular domain",
        )

        # Construct the prompt
        prompt = f"Im a B.tech i want to learn {domain} so for that could you please create a clean Roadmap for {domain}."

        # Generate the recipe
        response = model.generate_content(prompt)
        recipe_text = response.text

        # Basic recipe formatting (you can enhance this)
        recipe_dict = {"roadmap": [], "instructions": []}
        current_section = "roadmap"
        for line in recipe_text.split("\n"):
            if line.startswith("Roadmap:"):
                current_section = "roadmap"
            
            else:
                recipe_dict[current_section].append(line)

        return recipe_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
domain =st.text_input(label="Enter any Domain") 

roadmap = generate_roadmap(domain)
print(roadmap)
if st.button("Generate Roadmap"):
    roadmap = generate_roadmap(domain)
    if roadmap:
        st.header("Roadmap for " + domain)
        st.write("### Short-term goals (next 6-12 months):")
        for item in roadmap["roadmap"]:
            st.write("- " + item)
        
    else:
        st.error("Error generating roadmap. Please try again!")