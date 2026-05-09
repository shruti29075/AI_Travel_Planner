def get_chat_response(llm, itinerary_context: str, user_message: str):
    """
    Handles interactive chat with the AI Co-pilot using the itinerary as context.
    """
    if not llm:
        return "⚠️ Chat Assistant unavailable. Please check API Key."
        
    try:
        from langchain_core.prompts import ChatPromptTemplate
        
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are the AI Travel Co-Pilot. You have generated this trip itinerary:\n\n{context}\n\n"
                       "Answer the user's questions about this trip, suggest nearby food, or adjust the plan dynamically. "
                       "Keep responses friendly, helpful, and concise."),
            ("human", "{message}")
        ])
        
        messages = chat_prompt.format_messages(context=itinerary_context, message=user_message)
        resp = llm.invoke(messages)
        return resp.content if hasattr(resp, "content") else str(resp)
    except Exception as e:
        return f"Sorry, I encountered an error answering that: {str(e)}"
