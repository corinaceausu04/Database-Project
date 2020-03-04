from tkinter import *
import cx_Oracle as DB 

root = Tk()

def clear():
	list = root.grid_slaves()
	for l in list:
		l.destroy()

def comanda():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select pacienti.nume, pacienti.prenume from pacienti join medici using(id_medic) join sectii using(id_sectie) where pacienti.varsta > 30 and etaj = 5')
	text = Label(root, text = "Afisati numele si prenumele pacientilor\ncu varsta de peste 30 de ani\ncare sunt consultati de medici\ncare lucreaza intr-o sectie de la etajul 5.")
	text.grid(row = 0, column = 0, sticky = W)
	i = 1
	for p in cursor.fetchall():
		nume = Label(root, text = p[0])
		nume.grid(row = i, column = 0, sticky = W)
		prenume = Label (root, text = p[1])
		prenume.grid(row = i, column = 1)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def comanda_having():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select count(id_medic), id_sectie from medici join sectii using(id_sectie) group by id_sectie, etaj having etaj = 4')
	text = Label(root, text = "Afisati numarul de medici din fiecare\nsectie care se afla la etajul 4.")
	text.grid(row = 0, column = 0, sticky = W)
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		id_sectie = Label(root, text = p[1])
		id_sectie.grid(row = i, column = 1, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def update_asistenti():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_asis
	coloana_asis = Entry(root, width = 20)
	coloana_asis.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_asis
	expresie_asis = Entry(root, width = 20)
	expresie_asis.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID asistent de modificat: ")
	text1.grid(row = 2, column = 0)
	global id_upasis
	id_upasis = Entry(root, width = 20)
	id_upasis.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_asistenti_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_asistenti_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update asistenti set ' + coloana_asis.get() + '=' + expresie_asis.get() + 'where id_asistent = ' + a + id_upasis.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def update_pacienti():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_pac
	coloana_pac = Entry(root, width = 20)
	coloana_pac.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_pac
	expresie_pac = Entry(root, width = 20)
	expresie_pac.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID pacient de modificat: ")
	text1.grid(row = 2, column = 0)
	global id_pac
	id_pac = Entry(root, width = 20)
	id_pac.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_pacienti_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_pacienti_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update pacienti set ' + coloana_pac.get() + '=' + expresie_pac.get() + 'where id_pacient = ' + id_pac.get())
	conn.commit()
	cursor.close()
	conn.close()

def update_diagnostice():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_diag
	coloana_diag = Entry(root, width = 20)
	coloana_diag.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_diag
	expresie_diag = Entry(root, width = 20)
	expresie_diag.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID diagnostic de modificat: ")
	text1.grid(row = 2, column = 0)
	global id_diag
	id_diag = Entry(root, width = 20)
	id_diag.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_diagnostice_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_diagnostice_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update diagnostice set ' + coloana_diag.get() + '=' + expresie_diag.get() + 'where id_diagnostic = ' + a + id_diag.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def update_tratamente():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_trat
	coloana_trat = Entry(root, width = 20)
	coloana_trat.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_trat
	expresie_trat = Entry(root, width = 20)
	expresie_trat.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID tratament de modificat: ")
	text1.grid(row = 2, column = 0)
	global id_trat
	id_trat = Entry(root, width = 20)
	id_trat.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_tratamente_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_tratamente_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update tratamente set ' + coloana_trat.get() + '=' + expresie_trat.get() + 'where id_tratament = ' + a + id_trat.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def update_sectii():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana
	coloana = Entry(root, width = 20)
	coloana.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie
	expresie = Entry(root, width = 20)
	expresie.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID sectie de modificat: ")
	text1.grid(row = 2, column = 0)
	global id_up
	id_up = Entry(root, width = 20)
	id_up.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_sectii_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_sectii_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update sectii set ' + coloana.get() + '=' + expresie.get() + 'where id_sectie = ' + a + id_up.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def update_medici():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_med
	coloana_med = Entry(root, width = 20)
	coloana_med.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_med
	expresie_med = Entry(root, width = 20)
	expresie_med.grid(row = 1, column = 1)
	text1 = Label(root, text = "ID medic pentru modificat: ")
	text1.grid(row = 2, column = 0)
	global id_upmed
	id_upmed = Entry(root, width = 20)
	id_upmed.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_medici_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_medici_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update medici set ' + coloana_med.get() + '=' + expresie_med.get() + 'where id_medic = ' + id_upmed.get())
	conn.commit()
	cursor.close()
	conn.close()

def update_saloane():
	clear()
	text1 = Label(root, text = "Coloana de modificat: ")
	text1.grid(row = 0, column = 0)
	global coloana_sal
	coloana_sal = Entry(root, width = 20)
	coloana_sal.grid(row = 0, column = 1)
	text2 = Label(root, text = "Expresia cu care modificam: ")
	text2.grid(row = 1, column = 0)
	global expresie_sal
	expresie_sal = Entry(root, width = 20)
	expresie_sal.grid(row = 1, column = 1)
	text1 = Label(root, text = "Nr salon pentru modificat: ")
	text1.grid(row = 2, column = 0)
	global id_upsal
	id_upsal = Entry(root, width = 20)
	id_upsal.grid(row = 2, column = 1)
	button = Button(root, text = "Set", command = update_saloane_command)
	button.grid(row = 3, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 5, column = 0, sticky = W)

def update_saloane_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('update saloane set ' + coloana_sal.get() + '=' + expresie_sal.get() + 'where numar_salon = ' + id_upsal.get())
	conn.commit()
	cursor.close()
	conn.close()

def delete_sectii_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from sectii where id_sectie = ' + a + entry.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_sectii():
	clear()
	global entry_sectii
	entry_sectii = Entry(root, width = 20)
	entry_sectii.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_sectii_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_medici_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from medici where id_medic = ' + a + entry_medici.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_medici():
	clear()
	global entry_medici
	entry_medici = Entry(root, width = 20)
	entry_medici.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_medici_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_saloane_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from saloane where numar_salon = ' + a + entry_salon.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_saloane():
	clear()
	global entry_salon
	entry_salon = Entry(root, width = 20)
	entry_salon.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_saloane_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_asistenti_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from asistenti where id_asistent = ' + a + entry_asistenti.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_asistenti():
	clear()
	global entry_asistenti
	entry_asistenti = Entry(root, width = 20)
	entry_asistenti.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_asistenti_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_pacienti_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from pacienti where id_pacient = ' + a + entry_pacienti.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_pacienti():
	clear()
	global entry_pacienti
	entry_pacienti = Entry(root, width = 20)
	entry_pacienti.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_pacienti_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_diagnostice():
	clear()
	global entry_diag
	entry_diag = Entry(root, width = 20)
	entry_diag.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_diagnostice_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_diagnostice_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from diagnostice where id_diagnostic = ' + a + entry_diag.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def delete_tratamente():
	clear()
	global entry_trat
	entry_trat = Entry(root, width = 20)
	entry_trat.grid(row = 0, column = 0)
	button = Button(root, text = "Delete", command = delete_tratamente_command)
	button.grid(row = 1, column = 0, sticky = W)
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = 2, column = 0, sticky = W)

def delete_tratamente_command():
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	a = "'"
	cursor.execute('delete from tratamente where id_tratament = ' + a + entry_trat.get() + a)
	conn.commit()
	cursor.close()
	conn.close()

def afis_sectie():
	root.geometry("300x320")
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from sectii')
	i = 1
	for p in cursor.fetchall():
		id_sectie = Label(root, text = p[0])
		id_sectie.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		etaj = Label(root, text = p[2])
		etaj.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare dupa id", command = sectii_sort_id)
	button_sort.grid(row = i, column = 1)
	button_sort_den = Button(root, text = "Sortare dupa denumire", command = sectii_sort_den)
	button_sort_den.grid(row = i+1, column = 0)
	button_sort_den = Button(root, text = "Sortare dupa etaj", command = sectii_sort_et)
	button_sort_den.grid(row = i+1, column = 1)
	button8 = Button(root, text = "Stergere sectie dupa id", command = delete_sectii)
	button8.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update sectie dupa id", command = update_sectii)
	button_up.grid(row = i+2, column = 1)

def sectii_sort_id():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from sectii order by id_sectie')
	i = 1
	for p in cursor.fetchall():
		id_sectie = Label(root, text = p[0])
		id_sectie.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		etaj = Label(root, text = p[2])
		etaj.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def sectii_sort_den():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from sectii order by denumire')
	i = 1
	for p in cursor.fetchall():
		id_sectie = Label(root, text = p[0])
		id_sectie.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		etaj = Label(root, text = p[2])
		etaj.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def sectii_sort_et():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from sectii order by etaj')
	i = 1
	for p in cursor.fetchall():
		id_sectie = Label(root, text = p[0])
		id_sectie.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		etaj = Label(root, text = p[2])
		etaj.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_medici():
	clear()
	root.geometry("820x520")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort_id = Button(root, text = "Sortare dupa id", command = medici_sort_id)
	button_sort_id.grid(row = i, column = 1)
	button_sort = Button(root, text = "Sortare dupa nume", command = medici_sort_nume)
	button_sort.grid(row = i, column = 2)
	button_sort_prenume = Button(root, text = "Sortare dupa prenume", command = medici_sort_prenume)
	button_sort_prenume.grid(row = i, column = 3)
	button_sort_email = Button(root, text = "Sortare dupa email", command = medici_sort_email)
	button_sort_email.grid(row = i, column = 4)
	button_sort_tel = Button(root, text = "Sortare dupa nr telefon", command = medici_sort_nrtel)
	button_sort_tel.grid(row = i, column = 4)
	button_sort_varsta = Button(root, text = "Sortare dupa varsta", command = medici_sort_varsta)
	button_sort_varsta.grid(row = i+1, column = 0)
	button_sort_sectie = Button(root, text = "Sortare dupa is sectie", command = medici_sort_idsectie)
	button_sort_sectie.grid(row = i+1, column = 1)
	button_del = Button(root, text = "Stergere medic dupa id medic", command = delete_medici)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update medic dupa id", command = update_medici)
	button_up.grid(row = i+2, column = 1)

def medici_sort_nume():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by nume')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_id():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by id_medic')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_prenume():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by prenume')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_email():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by email')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_nrtel():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by nr_telefon')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_varsta():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by varsta')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def medici_sort_idsectie():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from medici order by id_sectie')
	i = 1
	for p in cursor.fetchall():
		id_medic = Label(root, text = p[0])
		id_medic.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		varsta = Label(root, text = p[5])
		varsta.grid(row = i, column = 5, sticky = W)
		id_sectie = Label(root, text = p[6])
		id_sectie.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_saloane():
	clear()
	root.geometry("430x400")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from saloane')
	i = 1
	for p in cursor.fetchall():
		nr_salon = Label(root, text = p[0])
		nr_salon.grid(row = i, column = 0, sticky = W)
		tip = Label (root, text = p[1])
		tip.grid(row = i, column = 1, sticky = W)
		nr_locuri = Label(root, text = p[2])
		nr_locuri.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare dupa nr salon", command = saloane_sort)
	button_sort.grid(row = i, column = 1, sticky = W)
	button_sort_nrlocuri = Button(root, text = "Sortare nr locuri", command = saloane_sort_nrlocuri)
	button_sort_nrlocuri.grid(row = i, column = 2, sticky = W)
	button_del = Button(root, text = "Stergere salon dupa numar salon", command = delete_saloane)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update salon dupa numar", command = update_saloane)
	button_up.grid(row = i+2, column = 1)

def saloane_sort():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from saloane order by numar_salon')
	i = 1
	for p in cursor.fetchall():
		nr_salon = Label(root, text = p[0])
		nr_salon.grid(row = i, column = 0, sticky = W)
		tip = Label (root, text = p[1])
		tip.grid(row = i, column = 1, sticky = W)
		nr_locuri = Label(root, text = p[2])
		nr_locuri.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def saloane_sort_nrlocuri():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from saloane order by nr_locuri')
	i = 1
	for p in cursor.fetchall():
		nr_salon = Label(root, text = p[0])
		nr_salon.grid(row = i, column = 0, sticky = W)
		tip = Label (root, text = p[1])
		tip.grid(row = i, column = 1, sticky = W)
		nr_locuri = Label(root, text = p[2])
		nr_locuri.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_asistenti():
	clear()
	root.geometry("710x300")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from asistenti')
	i = 1
	for p in cursor.fetchall():
		id_asistent = Label(root, text = p[0])
		id_asistent.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		data_ang = Label(root, text = p[5])
		data_ang.grid(row = i, column = 5, sticky = W)
		nr_salon = Label(root, text = p[6])
		nr_salon.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare Asistenti", command = asistenti_sort)
	button_sort.grid(row = i, column = 1)
	button_del = Button(root, text = "Stergere asistent dupa id", command = delete_asistenti)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update asistent dupa id", command = update_asistenti)
	button_up.grid(row = i+2, column = 1)

def asistenti_sort():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from asistenti order by nume')
	i = 1
	for p in cursor.fetchall():
		id_asistent = Label(root, text = p[0])
		id_asistent.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		email = Label(root, text = p[3])
		email.grid(row = i, column = 3, sticky = W)
		nr_telefon = Label(root, text = p[4])
		nr_telefon.grid(row = i, column = 4, sticky = W)
		data_ang = Label(root, text = p[5])
		data_ang.grid(row = i, column = 5, sticky = W)
		nr_salon = Label(root, text = p[6])
		nr_salon.grid(row = i, column = 6, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_pacienti():
	clear()
	root.geometry("730x300")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from pacienti')
	i = 1
	for p in cursor.fetchall():
		id_pacient = Label(root, text = p[0])
		id_pacient.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		varsta = Label(root, text = p[3])
		varsta.grid(row = i, column = 3, sticky = W)
		gen = Label(root, text = p[4])
		gen.grid(row = i, column = 4, sticky = W)
		nr_telefon = Label(root, text = p[5])
		nr_telefon.grid(row = i, column = 5, sticky = W)
		adresa = Label(root, text = p[6])
		adresa.grid(row = i, column = 6, sticky = W)
		id_medic = Label(root, text = p[7])
		id_medic.grid(row = i, column = 7, sticky = W)
		id_diagnostic = Label(root, text = p[8])
		id_diagnostic.grid(row = i, column = 8, sticky = W)
		nr_salon = Label(root, text = p[9])
		nr_salon.grid(row = i, column = 9, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare Pacienti", command = pacienti_sort)
	button_sort.grid(row = i, column = 1)
	button_del = Button(root, text = "Stergere pacient dupa id", command = delete_pacienti)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update pacient dupa id", command = update_pacienti)
	button_up.grid(row = i+2, column = 1)

def pacienti_sort():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from pacienti order by nume')
	i = 1
	for p in cursor.fetchall():
		id_pacient = Label(root, text = p[0])
		id_pacient.grid(row = i, column = 0, sticky = W)
		nume = Label (root, text = p[1])
		nume.grid(row = i, column = 1, sticky = W)
		prenume = Label(root, text = p[2])
		prenume.grid(row = i, column = 2, sticky = W)
		varsta = Label(root, text = p[3])
		varsta.grid(row = i, column = 3, sticky = W)
		gen = Label(root, text = p[4])
		gen.grid(row = i, column = 4, sticky = W)
		nr_telefon = Label(root, text = p[5])
		nr_telefon.grid(row = i, column = 5, sticky = W)
		adresa = Label(root, text = p[6])
		adresa.grid(row = i, column = 6, sticky = W)
		id_medic = Label(root, text = p[7])
		id_medic.grid(row = i, column = 7, sticky = W)
		id_diagnostic = Label(root, text = p[8])
		id_diagnostic.grid(row = i, column = 8, sticky = W)
		nr_salon = Label(root, text = p[9])
		nr_salon.grid(row = i, column = 9, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_diagnostice():
	clear()
	root.geometry("550x200")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from diagnostice')
	i = 1
	for p in cursor.fetchall():
		id_diagnostic = Label(root, text = p[0])
		id_diagnostic.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		id_tratament = Label(root, text = p[2])
		id_tratament.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare dupa denumire", command = diagnostice_sort)
	button_sort.grid(row = i, column = 1)
	button_sort_iddiag = Button(root, text = "Sortare dupa id diagnostic", command = diagnostice_sort_iddiag)
	button_sort_iddiag.grid(row = i, column = 2)
	button_sort_idtrat = Button(root, text = "Sortare dupa id tratament", command = diagnostice_sort_idtrat)
	button_sort_idtrat.grid(row = i+1, column = 0)
	button_del = Button(root, text = "Stergere diagnostic dupa id", command = delete_diagnostice)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update diagnostic dupa id", command = update_diagnostice)
	button_up.grid(row = i+2, column = 1)

def diagnostice_sort():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from diagnostice order by denumire')
	i = 1
	for p in cursor.fetchall():
		id_diagnostic = Label(root, text = p[0])
		id_diagnostic.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		id_tratament = Label(root, text = p[2])
		id_tratament.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def diagnostice_sort_iddiag():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from diagnostice order by id_diagnostic')
	i = 1
	for p in cursor.fetchall():
		id_diagnostic = Label(root, text = p[0])
		id_diagnostic.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		id_tratament = Label(root, text = p[2])
		id_tratament.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def diagnostice_sort_idtrat():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from diagnostice order by id_tratament')
	i = 1
	for p in cursor.fetchall():
		id_diagnostic = Label(root, text = p[0])
		id_diagnostic.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		id_tratament = Label(root, text = p[2])
		id_tratament.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def afis_tratamente():
	clear()
	root.geometry("550x300")
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from tratamente')
	i = 1
	for p in cursor.fetchall():
		id_tratament = Label(root, text = p[0])
		id_tratament.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		cantitate = Label(root, text = p[2])
		cantitate.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)
	button_sort = Button(root, text = "Sortare dupa denumire", command = tratamente_sort)
	button_sort.grid(row = i, column = 1)
	button_sort1 = Button(root, text = "Sortare dupa id tratament", command = tratamente_sort_idtrat)
	button_sort1.grid(row = i, column = 2)
	button_sort2 = Button(root, text = "Sortare dupa cantitate", command = tratamente_sort_cantit)
	button_sort2.grid(row = i+1, column = 0)
	button_del = Button(root, text = "Stergere tratament dupa id", command = delete_tratamente)
	button_del.grid(row = i+2, column = 0)
	button_up = Button(root, text = "Update tratament dupa id", command = update_tratamente)
	button_up.grid(row = i+2, column = 1)

def tratamente_sort():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from tratamente order by denumire')
	i = 1
	for p in cursor.fetchall():
		id_tratament = Label(root, text = p[0])
		id_tratament.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		cantitate = Label(root, text = p[2])
		cantitate.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def tratamente_sort_idtrat():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from tratamente order by id_tratament')
	i = 1
	for p in cursor.fetchall():
		id_tratament = Label(root, text = p[0])
		id_tratament.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		cantitate = Label(root, text = p[2])
		cantitate.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def tratamente_sort_cantit():
	clear()
	conn = DB.connect('corinaceausu/Corinac04@localhost:1521/cc04')
	cursor = conn.cursor()
	cursor.execute('select * from tratamente order by cantitate')
	i = 1
	for p in cursor.fetchall():
		id_tratament = Label(root, text = p[0])
		id_tratament.grid(row = i, column = 0, sticky = W)
		denumire = Label (root, text = p[1])
		denumire.grid(row = i, column = 1, sticky = W)
		cantitate = Label(root, text = p[2])
		cantitate.grid(row = i, column = 2, sticky = W)
		i = i + 1
	cursor.close()
	conn.close()
	back_button = Button(root, text = "Back", command = MainMeniu)
	back_button.grid(row = i, column = 0, sticky = W)

def MainMeniu():
	clear()
	root.geometry("340x270")
	space = Label(root, text = " ")
	space.grid(row = 0, column = 0)
	button = Button(root, text = "Sectii", command = afis_sectie)
	button.grid(row = 1, column = 0,  padx = 90)
	button2 = Button(root, text = "Medici", command = afis_medici)
	button2.grid(row = 2, column = 0, padx = 90)
	button3 = Button(root, text = "Saloane", command = afis_saloane)
	button3.grid(row = 3, column = 0, padx = 90)
	button4 = Button(root, text = "Asistenti", command = afis_asistenti)
	button4.grid(row = 4, column = 0, padx = 90)
	button5 = Button(root, text = "Pacienti", command = afis_pacienti)
	button5.grid(row = 5, column = 0, padx = 90)
	button6 = Button(root, text = "Diagnostice", command = afis_diagnostice)
	button6.grid(row = 6, column = 0, padx = 90)
	button7 = Button(root, text = "Tratamente", command = afis_tratamente)
	button7.grid(row = 7, column = 0, padx = 90)
	button8 = Button(root, text = "Cerere select din 3 tabele", command = comanda)
	button8.grid(row = 8, column = 0, padx = 90)
	button9 = Button(root, text = "Cerere care foloseste functii grup", command = comanda_having)
	button9.grid(row = 9, column = 0, padx = 90)
	
MainMeniu()

root.mainloop()