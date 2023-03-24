import openai

# TODO: Modularize this into a class -> keep it consistent with other nns
prompt_template = """Here is a video transcription from a meeting:
{transcription}
----
You are to act as a programming manager. Your task is to take this transcription above and create a task for a developer. The task should include a title, the task. You must infer the main task and sub-task if they exist. Provide it into a nice format with markdown text separating the title, and task. This ticket will then be sent to a developer to perform the task. Think through step by step, as a product manager to engineers."""

# prompt_template = """Here is a video transcription from a meeting:
# {transcription}
# ----
# You are to act as a programming manager. Your task is to take this transcription above and create a task for a developer. The task should include a title, the task. You must infer the main task and sub-task if they exist. Provide it into a nice format separating the title, and task. This ticket will then be sent to a developer to perform the task. Think through step by step, as a product manager to engineers. Write the ticket in chinese, talk in mandarin"""

def parse_response(response): 
    return response['choices'][0]['message']['content']

def format_prompt(transcription, prompt_template):
    return prompt_template.format(transcription=transcription)

def project_manager(transcription, prompt_template=prompt_template):
    """chatGPT acting as a project manager"""
    formatted_prompt = format_prompt(transcription, prompt_template)
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a programming manager whom works with a team of engineers to build new features. You are to take a transcription of a meeting and then formulate a ticket for your engineers to flesh out bugs and features. You are also to ignore all other conversations that are not related to the feature you are working on."},
            {"role": "user", "content": formatted_prompt},
        ],
    temperature=0.2,
    )
    return parse_response(res)