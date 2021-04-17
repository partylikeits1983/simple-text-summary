from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")

original_text = open('/home/pi/Desktop/0.txt', 'r').read()

summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)
