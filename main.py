from gradio_client import Client

promptinput=input()

client = Client("stabilityai/stable-diffusion-3.5-medium")
result = client.predict(
		prompt=promptinput,
		negative_prompt="",
		seed=0,
		randomize_seed=True,
		width=1024,
		height=1024,
		guidance_scale=4.5,
		num_inference_steps=40,
		api_name="/infer"
)
print(result)