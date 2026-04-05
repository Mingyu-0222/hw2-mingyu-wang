# Evaluation Set

## Case 1: Normal Meeting

Input:
Team meeting notes:
- Discussed project timeline
- John will finish the report by Friday
- Sarah will prepare slides for presentation
- Next meeting scheduled for next Monday

Expected Output:
- John: complete the report by Friday
- Sarah: prepare presentation slides
- Team: attend next meeting on Monday

---

## Case 2: Messy Notes

Input:
Meeting notes:
We talked about the new product launch. Marketing needs to do social media. Also design team maybe update the logo. Not sure about deadline. Oh and follow up next week.

Expected Output:
- Marketing team: create social media content for product launch
- Design team: update the logo
- Team: follow up next week

---

## Case 3: Missing Information

Input:
Meeting notes:
- Need to improve customer service response time
- Someone should look into automation tools

Expected Output:
- Team: improve customer service response time
- Team: research automation tools

Note: No specific owner or deadline provided.

---

## Case 4: Potential Failure / Ambiguous

Input:
Meeting notes:
- Maybe we can reduce costs somehow
- Think about improving performance
- Could assign tasks later

Expected Output:
- No clear action items or very general suggestions

Note: Model should not hallucinate specific tasks or deadlines.

---

## Case 5: Longer Meeting

Input:
Meeting notes:
- Reviewed quarterly sales performance
- Sales team to follow up with top clients
- Finance to prepare budget report by end of month
- HR to organize training session next week
- Discussed hiring plan

Expected Output:
- Sales team: follow up with top clients
- Finance team: prepare budget report by end of month
- HR team: organize training session next week
