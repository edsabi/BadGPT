from flask import Flask, request, render_template_string
from openai import OpenAI
import os
app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = "use your own key"

@app.route('/')
def index():

    

    prompt = request.args.get('prompt', '')
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        }
    	]
	)



    content = (completion.choices[0].message.content)
    print(content)
    template = '''
    <html>
       <head><title>Corporate OpenAI workaround</title></head>
       <body>
          <p>Ask me anything!</p>
          {}
       </body>
    </html>
    '''.format(content)
    
    return render_template_string(template)

if __name__ == "__main__":
    # Run the Flask app on port 50050
    app.run(host='0.0.0.0', port=50050)
