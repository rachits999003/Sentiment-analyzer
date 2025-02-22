import tkinter as tk
from textblob import TextBlob
from tkinter import messagebox

def analyze_sentiment():
    text = entry.get()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        result_label.config(text="Sentiment: Positive", fg="green")
    elif sentiment < 0:
        result_label.config(text="Sentiment: Negative", fg="red")
    else:
        result_label.config(text="Sentiment: Neutral", fg="blue")

#GUI setup
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("400x300")

label = tk.Label(root, text="Enter text to analyze:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()