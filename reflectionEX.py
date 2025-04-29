import os
import anthropic


# Economist Chatbot
def economist(query, max_tokens, llm, model_name, role):

    full_query = f"\nUser: {query}"

    chain = llm.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        system=f"{role}",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": full_query
                    }
                ]
            }
        ]
    )

    result = chain.content[0].text

    return result



def reflection(query, max_tokens, llm, model_name, reflection_content):

    full_query = f"\nUser: {query}"


    chain = llm.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        system=f"{reflection_content}",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": full_query
                    }
                ]
            }
        ]
    )

    result = chain.content[0].text

    return result


def final_reflection(query, max_tokens, llm, model_name, reflection_content):

    full_query = f"\nUser: {query}"

    chain = llm.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        system=f"{reflection_content}",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": full_query
                    }
                ]
            }
        ]
    )

    result = chain.content[0].text

    return result