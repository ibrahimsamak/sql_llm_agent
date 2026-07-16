import gradio as gr

from agent import SQLAgent

agent = SQLAgent()


def ask(question):
    if not question or not question.strip():
        return "", "Please enter a question."
    try:
         sql, result = agent.answer(question)
         return  sql, result
    except Exception as e:
        return "", f"Error: {type(e).__name__}: {e}"


with gr.Blocks(title="SQL Agent") as demo:
    gr.Markdown("# SQL Agent\nAsk a question about the school database in plain English.")

    question = gr.Textbox(
        label="Question",
        placeholder="e.g. How many students do we have?",
        lines=2,
    )
    submit = gr.Button("Ask", variant="primary")
    with gr.Row():
        with gr.Column():
            answer = gr.Textbox(label="Answer", lines=6)
        with gr.Column():
            sql_box = gr.Code(label="Sql Query:", language="sql")
       

    gr.Examples(
        examples=[
            "How many students do we have?",
            "What is the average age of students?",
            "List all student names.",
        ],
        inputs=question,
    )

    submit.click(fn=ask, inputs=question, outputs=[sql_box, answer])
    question.submit(fn=ask, inputs=question, outputs=[sql_box, answer])


if __name__ == "__main__":
    demo.launch()
