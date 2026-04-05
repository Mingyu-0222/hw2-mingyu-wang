# Report

## Business Use Case

The business workflow I chose is summarizing meetings into action items. This workflow is useful for teams that have many meetings and need a fast way to identify next steps. The input is a set of meeting notes or a meeting transcript, and the output is a structured list of action items with task, owner, and deadline when available. This task is valuable because meeting notes often include a lot of discussion, but the most important part for a team is knowing what needs to be done after the meeting.

## Model Choice

I used Google Gemini through the Google AI API. I chose this model because it was easy to access, simple to connect with Python, and worked well for short business writing tasks. I wanted a model that could quickly turn unstructured notes into a more organized format. In my testing, Gemini produced clear results for normal meeting cases and was able to identify the main tasks correctly.

## Baseline and Final Design Comparison

My baseline design used a simple prompt that asked the model to extract action items and include task, owner, and deadline. This version worked for straightforward cases, but sometimes the output included extra introductory wording before the action items. It also did not clearly separate real action items from general discussion.

After revising the prompt, I made the instructions more specific. I told the model to ignore vague discussion points, return only clear action items, and use a more consistent structure. In the final design, the output became cleaner, easier to evaluate, and more focused on concrete next steps. The prompt iteration improved the consistency of the results and reduced unnecessary text.

## Remaining Limitations and Need for Human Review

This prototype still has limitations. It works best when the meeting notes contain clear tasks and clear owners. If the notes are vague, incomplete, or highly ambiguous, the model may miss context or return action items that are too general. In some cases, there may be discussion points that sound important but do not actually represent a real task. Human review is still needed to confirm that the extracted action items are accurate and useful, especially in higher stakes business settings.

## Deployment Recommendation

I would recommend this workflow only as a support tool, not as a fully automated system. It can save time by producing a first draft of action items after a meeting, but a human should still review the results before sharing them with a team. This is especially important when meeting notes are incomplete or when deadlines and ownership are unclear. Under those conditions, I think this workflow could be valuable as a productivity tool with human oversight.
