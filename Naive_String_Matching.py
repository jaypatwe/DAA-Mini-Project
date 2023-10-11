import tkinter as tk

def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

def search_pattern():
    text = text_entry.get()
    pattern = pattern_entry.get()
    matches = naive_string_matching(text, pattern)
    
    if matches:
        result_label.config(text=f"Pattern found at positions: {matches}")
    else:
        result_label.config(text="Pattern not found in the text.")


window = tk.Tk()
window.title("String Matching")


text_label = tk.Label(window, text="Enter the text:")
text_label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

pattern_label = tk.Label(window, text="Enter the pattern to search:")
pattern_label.pack()
pattern_entry = tk.Entry(window)
pattern_entry.pack()

search_button = tk.Button(window, text="Search Pattern", command=search_pattern)
search_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()
