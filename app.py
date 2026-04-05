import os
from google import genai

PROMPT_TEMPLATE = """
You are a helpful assistant that turns meeting notes into action items.

Instructions:
1. Extract only clear action items from the meeting notes.
2. For each action item, include:
   - Task
   - Owner
   - Deadline
3. If owner or deadline is missing, write "Not specified".
4. If there are no clear action items, say "No clear action items found."
5. Keep the output concise and easy to read.

Meeting notes:
{notes}
"""

def summarize_meeting(notes: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    prompt = PROMPT_TEMPLATE.format(notes=notes)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def main():
    sample_notes = """
    Team meeting notes:
    - John will finish the report by Friday
    - Sarah will prepare slides for the presentation
    - Marketing team needs to draft the social media plan by next Wednesday
    - Follow up meeting is next Monday
    """

    print("=== INPUT MEETING NOTES ===")
    print(sample_notes)

    print("\n=== GENERATED ACTION ITEMS ===")
    result = summarize_meeting(sample_notes)
    print(result)

if __name__ == "__main__":
    main()