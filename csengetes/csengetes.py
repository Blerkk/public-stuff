import sys
import os
mappa = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(mappa, 'config.txt')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import csengetes_support

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def vp_start_gui():
    global val, w, root, top
    root = tk.Tk()
    top = Toplevel1 (root)
    beolvasas()
    csengetes_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root, top
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    csengetes_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

sorok = []
def beolvasas():
    global top
    with open(config, 'r+') as f:
        lines = [line.rstrip().split(';') for line in f]
        for i in range(0,len(lines)):
            top.betolt(lines[i][0], lines[i][2], lines[i][1])

def szerkesztes():
    szerkeszt = tk.Tk()
    szerkeszt.wm_title("Letrehozas")
    szerkeszt.geometry("220x100")
    szerkeszt.minsize(120, 1)
    szerkeszt.maxsize(3844, 1061)
    szerkeszt.resizable(1, 1)
    Label1 = tk.Label(szerkeszt)
    Label1.place(relx=0.273, rely=0.15, height=23, width=104)
    Label1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Nap kivalasztasa')

    Spinbox1 = tk.Spinbox(szerkeszt, from_=1, to=31)
    Spinbox1.place(relx=0.355, rely=0.513, relheight=0.162, relwidth=0.159)
    Spinbox1.configure(activebackground="#f9f9f9", background="white", buttonbackground="#d9d9d9", disabledforeground="#a3a3a3", font="TkDefaultFont", foreground="black",
                        highlightbackground="black", highlightcolor="black", insertbackground="black", selectbackground="blue", selectforeground="white")

    Spinbox1_2 = tk.Spinbox(szerkeszt, from_=1.0, to=100.0)
    Spinbox1_2.place(relx=0.505, rely=0.513, relheight=0.16292, relwidth=0.159)
    Spinbox1_2.configure(activebackground="#f9f9f9", background="white", buttonbackground="#d9d9d9", disabledforeground="#a3a3a3", font="TkDefaultFont", foreground="black",
                         highlightbackground="black", highlightcolor="black", insertbackground="black", selectbackground="blue", selectforeground="white")
    
    def lekeres():
        ora = "00"
        perc = "00"
        if(int(Spinbox1.get()) < 10):
            ora = "0" + str(Spinbox1.get())
        else:
            ora = str(Spinbox1.get())
        if(int(Spinbox1_2.get()) < 10):
            perc = "0" + str(Spinbox1_2.get())
        else:
            perc = str(Spinbox1_2.get())
        ujErt= ora + ":" + perc
        print(ujErt)

    Button1 = tk.Button(szerkeszt, command = lekeres)
    Button1.place(relx=0.364, rely=0.769, height=24, width=65)
    Button1.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", 
                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='Kovetkezo')
    szerkeszt.mainloop()

def letrehozas():
    letrehozNap = tk.Tk()
    letrehozNap.wm_title("Letrehozas")
    letrehozNap.geometry("220x100")
    letrehozNap.minsize(120, 1)
    letrehozNap.maxsize(3844, 1061)
    letrehozNap.resizable(1, 1)
    Label1 = tk.Label(letrehozNap)
    Label1.place(relx=0.273, rely=0.15, height=23, width=104)
    Label1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Nap kivalasztasa')

    comboNapok = ['Hetfo', 'Kedd', 'Szerda', 'Csutortok', 'Pentek']
    TCombobox1 = ttk.Combobox(letrehozNap, values=comboNapok, state='readonly')
    TCombobox1.set('Hetfo')
    TCombobox1.place(relx=0.182, rely=0.5, relheight=0.2188, relwidth=0.65)
    print(TCombobox1.get())

    Button1 = tk.Button(letrehozNap, command = letrehozNap.destroy)
    Button1.place(relx=0.364, rely=0.769, height=24, width=65)
    Button1.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                     highlightcolor="black", pady="0", text='Kovetkezo')
    letrehozNap.mainloop()

class Toplevel1:
    def __init__(self, top=None):
        global lines
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.cascadeMenu = tk.Menu(self.menubar,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.menubar.add_cascade(label="File", menu=self.cascadeMenu)
        self.cascadeMenu.add_command(label="Uj letrehozasa")
        self.cascadeMenu.add_command(label="Mentes")
        self.cascadeMenu.add_command(label="Betoltes")
        self.cascadeMenu.add_separator()
        self.cascadeMenu.add_command(label="Kilepes", command=top.quit)

        top.geometry("750x500")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("Csengetes")
        top.configure(background="#d9d9d9")

        self.Button1 = tk.Button(top, command=letrehozas)
        self.Button1.place(relx=0.837, rely=0.318, height=24, width=67)
        self.Button1.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", 
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='Szerkesztes')

        self.Button2 = tk.Button(top, command=letrehozas)
        self.Button2.place(relx=0.837, rely=0.451, height=24, width=67)
        self.Button2.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='Letrehozas')

        self.Button3 = tk.Button(top, command=self.kivalTorol)
        self.Button3.place(relx=0.837, rely=0.584, height=24, width=67)
        self.Button3.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='Torles')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.788, rely=0.265, relheight=0.443)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.050, rely=0.133, relwidth=0.716)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.055, rely=0.053, height=18, width=65)
        self.Label1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Hetfo')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.205, rely=0.053, height=18, width=64)
        self.Label2.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Kedd')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.360, rely=0.053, height=18, width=54)
        self.Label3.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Szerda')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.505, rely=0.053, height=18, width=63)
        self.Label4.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Csutortok')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.650, rely=0.053, height=18, width=61)
        self.Label5.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='Pentek')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.049, rely=0.159, relheight=0.743, relwidth=0.125)
        self.Scrolledlistbox1.configure(background="white", cursor="xterm", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="black", highlightbackground="#d9d9d9",
                                        highlightcolor="#d9d9d9", selectbackground="blue", selectforeground="white")

        self.Scrolledlistbox2 = ScrolledListBox(top)
        self.Scrolledlistbox2.place(relx=0.197, rely=0.159, relheight=0.743, relwidth=0.123)
        self.Scrolledlistbox2.configure(background="white", cursor="xterm", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="black", highlightbackground="#d9d9d9",
                                        highlightcolor="#d9d9d9", selectbackground="blue", selectforeground="white")

        self.Scrolledlistbox3 = ScrolledListBox(top)
        self.Scrolledlistbox3.place(relx=0.345, rely=0.159, relheight=0.743, relwidth=0.123)
        self.Scrolledlistbox3.configure(background="white", cursor="xterm", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="black", highlightbackground="#d9d9d9",
                                        highlightcolor="#d9d9d9", selectbackground="blue", selectforeground="white")

        self.Scrolledlistbox4 = ScrolledListBox(top)
        self.Scrolledlistbox4.place(relx=0.493, rely=0.159, relheight=0.743, relwidth=0.125)
        self.Scrolledlistbox4.configure(background="white", cursor="xterm", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="black", highlightbackground="#d9d9d9",
                                        highlightcolor="#d9d9d9", selectbackground="blue", selectforeground="white")

        self.Scrolledlistbox5 = ScrolledListBox(top)
        self.Scrolledlistbox5.place(relx=0.64, rely=0.159, relheight=0.743, relwidth=0.123)
        self.Scrolledlistbox5.configure(background="white", cursor="xterm", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="black", highlightbackground="#d9d9d9",
                                        highlightcolor="#d9d9d9", selectbackground="blue", selectforeground="white")

    def betolt(self, nap, ora, tipus):
        if(nap == 'hetfo'):
            self.Scrolledlistbox1.insert(tk.END, tipus)
            self.Scrolledlistbox1.insert(tk.END, ora)
            self.Scrolledlistbox1.insert(tk.END, " ")
        elif(nap == 'kedd'):
            self.Scrolledlistbox2.insert(tk.END, tipus)
            self.Scrolledlistbox2.insert(tk.END, ora)
            self.Scrolledlistbox2.insert(tk.END, " ")
        elif(nap == 'szerda'):
            self.Scrolledlistbox3.insert(tk.END, tipus)
            self.Scrolledlistbox3.insert(tk.END, ora)
            self.Scrolledlistbox3.insert(tk.END, " ")
        elif(nap == 'csutortok'):
            self.Scrolledlistbox4.insert(tk.END, tipus)
            self.Scrolledlistbox4.insert(tk.END, ora)
            self.Scrolledlistbox4.insert(tk.END, " ")
        elif(nap == 'pentek'):
            self.Scrolledlistbox5.insert(tk.END, tipus)
            self.Scrolledlistbox5.insert(tk.END, ora)
            self.Scrolledlistbox5.insert(tk.END, " ")

    def kivalTorol(self):
        self.Scrolledlistbox1.delete(tk.ANCHOR)
        self.Scrolledlistbox2.delete(tk.ANCHOR)
        self.Scrolledlistbox3.delete(tk.ANCHOR)
        self.Scrolledlistbox4.delete(tk.ANCHOR)
        self.Scrolledlistbox5.delete(tk.ANCHOR)

class AutoScroll(object):
    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                    | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                    + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()