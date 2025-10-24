from openai import OpenAI
import json
from src.lib.responses import ChartResponseOptionSchemas
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

PROMPT_ID = os.getenv('PROMPT_ID')

# openAI wrapper tailored to Vizune
class VizuneAI():
    def __init__(self, data, meta_d):
        self.input_data = data
        self.meta_d = meta_d
        self.client = OpenAI()
    
    def format_input(self, df):
        df.columns = df.columns.str.lower()
        data = df.to_dict(orient='records')
        if len(data) > 100:
            return json.dumps(data)
        return json.dumps(data, indent=2)
    
    def send_response(self, data, meta_d: dict):
        response = self.client.responses.parse(
            model="gpt-5-nano",
            prompt={
                "id": PROMPT_ID,
                "version": "5",
                "variables": {
                    "data": str(data),
                    "meta_d": str(meta_d)
                }
            },
            input=[],
            reasoning={},
            store=True,
            include=[
                "reasoning.encrypted_content",
                "web_search_call.action.sources"
            ],
            text_format=ChartResponseOptionSchemas,
        )
        return response
        
    def vizune(self):
        data_f = self.format_input(df=self.input_data)
        return self.send_response(data_f, self.meta_d)
