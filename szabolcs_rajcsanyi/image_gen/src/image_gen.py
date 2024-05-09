import os
from dotenv import load_dotenv

import cv2
from skimage import io

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def create_chain():
    llm = OpenAI(
        temperature=0.4,
        max_tokens=1000
    )
    prompt_template = PromptTemplate(
        input_variables=["description"],
        template="Generate a prompt to generate an image based on the following description: {description}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain

def generate_image(description):
    chain = create_chain()
    image_url = DallEAPIWrapper().run(chain.run(description))
    image = io.imread(image_url)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV compatibility
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert back to RGB for displaying
    return image

