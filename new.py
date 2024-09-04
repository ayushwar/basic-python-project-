from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def summarize_paragraph(paragraph):
    # Summarize the input paragraph
    summary = summarizer(paragraph, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Function to summarize the original and student's answers
def summarize_answers(original_ans, student_ans):
    summarized_original = summarize_paragraph(original_ans)
    summarized_student = summarize_paragraph(student_ans)
    
    return summarized_original, summarized_student

# Input the original and student's answers (as strings)
original_ans = input("Enter the original answer: ")
student_ans = input("Enter the student's answer: ")

# Get the summarized versions
summarized_original, summarized_student = summarize_answers(original_ans, student_ans)

print("\nSummarized Original Answer:\n", summarized_original)
print("\nSummarized Student Answer:\n", summarized_student)
