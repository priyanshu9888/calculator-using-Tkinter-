# custom made buttons for tkinter
import tkinter as tk
 
 
counter = 0
crow = 0
mem1 = ""
mem2 = ""
mop = ""
 
 
def setEntry(value):
    global esv
    global mem1
    global mem2
    global mop
 
    print(value)
 
    if value == "C":
        esv.set("")
    else:
        v = esv.get()
        v += value
        esv.set(v)
 
        # when you press this... you must put the value in mem1
        # but you must not add other values
        if value in "+-x:":
            mop = value
            print("mop", mop)
            mem1 = v.replace(value, "")
            esv.set("")
 
        elif value == "=":
            mem2 = v.replace("=", "")
            print("mem", mop)
            if mop == "x":
                mop = "*"
            if mop == ":":
                mop = "/"
            result = eval(f"{float(mem1)} {mop} {float(mem2)}")
            esv.set(result)
            mem1 = result
        # Here is when user digit a number
        else:
            # it is the first number, mem it and show it
            if mem1 == "":
                mem1 = value
                esv.set(value)
            # the second number show the first and the second, memorize it
            elif mop == "":
                value = str(mem1) + value
                mem1 = value
                esv.set(value)
            if mem1 == mem2:
                value = str(mem2) + value
                mem2 = value
                esv.set(value)
 
 
def Button(text):
    global counter
    global crow
    global entry
    global esv
 
    # b = button(1, 10, text, "black", None)
    b = tk.Button(root, text=text)
    b["bg"] = "black"
    b["fg"] = "white"
    b["font"] = "arial 30"
    root.columnconfigure(counter, weight=1)
    root.rowconfigure(crow, weight=1)
    b["command"] = lambda: setEntry(b["text"])
    if b["text"] in "-+:x":
        b["bg"] = "black"
    if b["text"] in "C":
        b["fg"] = "white"
    if b["text"] == "=":
        b["bg"] = "black"
        b.grid(
            row=1 + crow, column=counter,
            columnspan=3, sticky="nswe", ipady=0, ipadx=0)
    else:
        b.grid(row=1 + crow, column=counter, sticky="nswe", ipady=0, ipadx=0)
    counter += 1
    if counter > 2:
        crow += 1
        counter = 0
    return b
 
 
def main():
    global root
    global esv
    root = tk.Tk()
    root.title("Calculator")
    esv = tk.StringVar()
    entry = tk.Entry(root, textvariable=esv, justify="right")
    entry["font"] = "arial 30"
    entry["bg"] = "white"
    entry.grid(row=0, column=0, columnspan=3, sticky="nswe")
    for but in [7, 8, 9, 4, 5, 6,
                1, 2, 3, 0, "+", "-",
                "C", "x", ":", "="]:
        Button(str(but))
    root.mainloop()
 
 
main()