import openai
import os

from dotenv import load_dotenv


load_dotenv()

from  openai import AzureOpenAI


def call_api_openai(prompt, mode, lang):
    openai.api_key = os.getenv("AZURE_OPENAPI_KEY")
    openai.api_base = os.getenv("AZURE_OPENAPI_ENDPOINT")
    # "# your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_type = 'azure'
    openai.api_version = '2023-09-01-preview' # this might change in the future

    deployment_name='y8257gcre7d76fenfm6f92337yw5p98m' #This will correspond to the custom name you chose for your deployment when you deployed a model.

    # Send a completion call to generate an answer
    print('Sending a test completion job')
    start_phrase = prompt + ";; change the code and the theme of the css to make a joke or quote depending in the mood, choose a movie title, prevent that the color of bg is different than the movie title color about the css : "+ mode + " genre about random movie and the style also to fit the movie story, answer only html page! replace the text in the language : " + lang
    messages = [
        {'role': 'user', 'content': start_phrase}
    ]
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAPI_KEY"),
        api_version='2023-09-01-preview',
        azure_endpoint=os.getenv("AZURE_OPENAPI_ENDPOINT"),
    )
    response = client.chat.completions.create(model=deployment_name, max_tokens=750, messages=messages)
    print(response.choices)
    return response.choices[0].message.content      

