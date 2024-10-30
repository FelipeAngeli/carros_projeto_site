import openai
import os
from dotenv import load_dotenv

load_dotenv()



def get_car_ai_bio(model, brand, year):
 
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        prompt = "Monte uma descrição de venda para o carro {} {} ano {}. Esta descrição deve ter no máximo 255 caracteres e deve incluir informações específicas do carro para impressionar os possíveis clientes.".format(brand, model, year)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60
        )
        return response.choices[0].message['content']
    
    except Exception as e:
        return "Carro em excelente estado, único dono, sem detalhes, venha conferir!"

