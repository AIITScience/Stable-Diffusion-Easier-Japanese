# coding: shift-jis

from gradio_client import Client

promptinput=input()

client = Client("AIITScience/stable-diffusion-3.5-medium")
result = client.predict(
		param_0=promptinput,
		api_name="/predict"
)
print(result)
