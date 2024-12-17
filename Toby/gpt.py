import openai

API = "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"

openai.api_key = API

model = 'text-davinci-003'

resp = openai.Completion.create(


		prompt = 'What are the rewards for guiness book of record',
		model = model,
		max_tokens=1000,
		temperature=0.9
		
	)

print(resp.choices[0].text)
print(resp.usage.total_tokens)