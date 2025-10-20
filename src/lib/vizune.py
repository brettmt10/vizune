from openai import OpenAI
import json

client = OpenAI()

# openAI wrapper tailored to Vizune
class VizuneAI():
    def __init__(self, data):
        self.input_data = data
    
    def format_input(self, df):
        data = df.to_dict(orient='records')
        if len(data) > 100:
            return json.dumps(data)
        return json.dumps(data, indent=2)
    
    def send_response(self, data):  
        response = client.responses.create(
            model="gpt-5-nano",
            input=f"Summarize this data: {data}."
        )
        return response
    
    def vizune(self):
        data_f = self.format_input(df=self.input_data)
        return self.send_response(data_f)
