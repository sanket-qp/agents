import time
import gradio as gr

def update_textbox(inputs):
    countdown = list(reversed([str(i) for i in range(inputs + 1)]))
    countdown[-1] = "Time is up!"
    for i in countdown:
        yield gr.update(value=i)
        time.sleep(1)

with gr.Blocks() as demo:
    inputs = gr.Number(label="Enter the time in secs")
    text = gr.Textbox(label="Remaining time in secs", lines=1, interactive=True)
    btn = gr.Button("start")
    btn.click(fn=update_textbox, inputs=[inputs], outputs=text)

demo.launch()