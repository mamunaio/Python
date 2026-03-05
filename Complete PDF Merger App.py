import tkinter as tk
from tkinter import filedialog, messagebox # messagebox যোগ করেছি পপ-আপের জন্য
import PyPDF2

# আমরা যেই ফাইলগুলো সিলেক্ট করব, সেগুলো এই লিস্টে জমা থাকবে
selected_files = []

def select_pdfs():
    global selected_files # global ব্যবহার করেছি যেন অন্য ফাংশনও এই লিস্ট দেখতে পায়
    selected_files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if selected_files:
        status_label.config(text=f"Selected {len(selected_files)} files", fg="green")

def merge_pdfs():
    # যদি ইউজার ফাইল সিলেক্ট না করেই Merge বাটনে চাপ দেয়
    if not selected_files:
        messagebox.showwarning("Warning", "Please select PDF files first!")
        return

    # নতুন ফাইলটি কোথায় সেভ হবে তা জিজ্ঞেস করা
    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        title="Save Merged PDF As",
        filetypes=[("PDF Files", "*.pdf")]
    )

    # যদি ইউজার সেভ করার জায়গা সিলেক্ট করে
    if save_path:
        merger = PyPDF2.PdfMerger()

        # ফাইলগুলো জোড়া লাগানো হচ্ছে
        for pdf in selected_files:
            merger.append(pdf)

        merger.write(save_path)
        merger.close()

        # সফলতার মেসেজ!
        messagebox.showinfo("Success", "PDFs merged successfully!")
        status_label.config(text="Merge Complete!", fg="blue")

# --- GUI Setup (আপনার আগের কোড) ---
root = tk.Tk()
root.title("My PDF Merger App")
root.geometry("400x250")

# হেডিং
label = tk.Label(root, text="PDF Merger App", font=("Arial", 16, "bold"))
label.pack(pady=10)

# বাটন ১: ফাইল সিলেক্ট করার জন্য
btn_select = tk.Button(root, text="1. Select PDFs", bg="orange", font=("Arial", 12), command=select_pdfs)
btn_select.pack(pady=5)

# স্ট্যাটাস লেবেল
status_label = tk.Label(root, text="No file selected", fg="gray", font=("Arial", 10))
status_label.pack(pady=5)

# বাটন ২: ফাইল মার্জ করার জন্য
btn_merge = tk.Button(root, text="2. Merge & Save", bg="lightgreen", font=("Arial", 12), command=merge_pdfs)
btn_merge.pack(pady=10)

root.mainloop()