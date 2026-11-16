from pathlib import Path
from copy import deepcopy
from lxml import html, etree
import re
SOURCE=Path('.audit/localization-original.html').read_text(encoding='utf8')
original=html.fromstring(SOURCE)
norm=lambda t:' '.join(str(t).split())
texts=[]
for x in original.xpath('//body//text()[not(ancestor::script)]'):
 s=norm(x)
 if s and s not in texts:texts.append(s)
lookup={s:i for i,s in enumerate(texts)}
translations={}
def rows(s):
 for line in s.strip().splitlines():
  n,es,sr=line.split('|');translations[int(n)]={'es':es,'sr':sr}
rows('''
0|Bienvenidos a la formación SAC de PLAYMOBIL|Dobrodošli u PLAYMOBIL SAC obuku
1|Siguiente ↓|Sledeća ↓
2|Plazos de entrega y gastos de transporte|Rokovi isporuke i troškovi dostave
3|Surtido regular|Redovni asortiman
5|6–8 días hábiles|6–8 radnih dana
6|Piezas sueltas|Rezervni delovi
7|Hasta 10 semanas|Do 10 nedelja
8|↑ Anterior|↑ Prethodna
9|Gastos de envío|Troškovi dostave
10|España / Portugal|Španija / Portugal
12|Promoción de envío gratuito: consultar las condiciones aplicables a compras superiores a 60 EUR|Promocija besplatne dostave: proveriti uslove za kupovine preko 60 EUR
13|Canarias / Ceuta / Melilla|Kanarska ostrva / Seuta / Melilja
15|Envío gratuito para compras superiores a 150 EUR; consultar las condiciones|Besplatna dostava za kupovine preko 150 EUR; proveriti uslove
16|Azores / Madeira|Azorska ostrva / Madeira
17|PROCESO DE COMPRA|PROCES KUPOVINE
19|Tras realizar el pedido|Nakon poručivanja
20|El cliente recibe un correo de confirmación.|Kupac dobija potvrdu porudžbine mejlom.
22|El pedido sale del almacén|Porudžbina napušta skladište
23|El cliente recibe un correo con la factura.|Kupac dobija mejl sa fakturom.
25|La agencia de transporte recibe el pedido|Kurirska služba preuzima porudžbinu
26|DHL, CTT o UPS envía un correo con información del envío. Conviene revisar también el correo no deseado.|DHL, CTT ili UPS šalje mejl sa podacima o pošiljci. Treba proveriti i neželjenu poštu.
28|El cliente recibe el pedido|Kupac prima porudžbinu
29|Los documentos discrepan sobre el plazo de desistimiento. Consulta los Términos y Condiciones aprobados y, en caso de duda, al responsable de SAC.|Dokumenti navode različite rokove za odustanak. Proverite odobrene Uslove kupovine i, ako postoji nedoumica, obratite se odgovornoj osobi u SAC-u.
31|Devolución / cancelación|Povraćaj / otkazivanje
32|El cliente asume los gastos de devolución. PLAYMOBIL los asume si los daños se notificaron en el momento de la entrega y constan en el justificante.|Troškove povraćaja snosi kupac. PLAYMOBIL ih snosi ako je oštećenje prijavljeno pri isporuci i zabeleženo na potvrdi o isporuci.
33|Directrices generales de SAP|Opšte SAP smernice
34|Organización de ventas|Organizacija prodaje
35|España|Španija
39|Tipos de pedido|Tipovi porudžbina
41|Pedidos de piezas sueltas y DS|Porudžbine rezervnih delova i DS asortimana
43|Reclamaciones|Reklamacije
45|Abono|Knjižno odobrenje
47|Factura|Faktura
48|Métodos de pago|Načini plaćanja
50|Gratuito|Besplatno
51|(Reclamaciones)|(Reklamacije)
53|Transferencia bancaria|Bankovni prenos
54|(Pedidos por correo electrónico)|(Porudžbine mejlom)
56|Pago mediante enlace|Plaćanje putem linka
57|Reclamaciones – proceso ZTA3|Reklamacije – postupak ZTA3
58|Reclamaciones|Reklamacije
59|Recibimos un correo que comunica una pieza faltante o defectuosa.|Dobijamo mejl o delu koji nedostaje ili je neispravan.
60|Crear un ZTA3|Kreiranje ZTA3
62|Comprueba si el cliente ya existe en el sistema o si es necesario crearlo.|Proverite da li kupac već postoji u sistemu ili treba kreirati novog.
64|Introduce el pedido ZTA3.|Unesite porudžbinu ZTA3.
66|Anota y registra el número de incidencia.|Zapišite i evidentirajte broj reklamacije.
68|Responde al cliente.|Odgovorite kupcu.
69|← Anterior|← Prethodna
70|Siguiente →|Sledeća →
71|Reclamaciones – comprobar clientes existentes|Reklamacije – provera postojećih kupaca
72|Comprueba si el cliente ya existe en SAP.|Proverite da li kupac već postoji u SAP-u.
73|Importante|Važno
74|Anota el número de cliente para crear la reclamación ZTA3.|Zapišite broj kupca za kreiranje reklamacije ZTA3.
75|Reclamaciones – crear un nuevo cliente|Reklamacije – kreiranje novog kupca
76|Crear un cliente en SAP|Kreiranje kupca u SAP-u
77|Datos del cliente|Podaci o kupcu
78|• Tratamiento (Sr./Sra.)|• Oslovljavanje (gospodin/gospođa)
79|• Apellidos y nombre|• Prezime i ime
80|• Calle y dirección|• Ulica i adresa
81|• Código postal y población|• Poštanski broj i mesto
82|• País y región|• Država i region
83|• Número de identificación fiscal (DNI/CIF)|• Poreski identifikacioni broj (DNI/CIF)
84|• Teléfono|• Broj telefona
85|• Correo electrónico|• Adresa elektronske pošte
86|Crear pedido|Kreiranje porudžbine
87|Selecciona|Izaberite
88|para reclamaciones o|za reklamacije ili
89|para pedidos si vas a crear uno a continuación.|za porudžbine ako odmah zatim kreirate porudžbinu.
90|Reclamaciones – crear un ZTA3|Reklamacije – kreiranje ZTA3
91|Introduce el pedido ZTA3 en SAP|Unesite porudžbinu ZTA3 u SAP
92|Importante – paso 5|Važno – korak 5
93|Anota el número de incidencia después de grabar el ZTA3.|Zapišite broj reklamacije nakon čuvanja ZTA3.
94|Reclamaciones – registrar y responder|Reklamacije – evidentiranje i odgovor
95|Registrar la reclamación|Evidentiranje reklamacije
96|Responder al cliente|Odgovor kupcu
97|Registra la reclamación y comunica al cliente el estado de su solicitud de forma clara.|Evidentirajte reklamaciju i jasno obavestite kupca o statusu zahteva.
98|• Registra el número de incidencia.|• Evidentirajte broj reklamacije.
99|• Confirma la recepción de la solicitud.|• Potvrdite prijem zahteva.
100|• Informa al cliente de que las piezas de repuesto se han solicitado a Alemania.|• Obavestite kupca da su zamenski delovi zatraženi iz Nemačke.
101|• Facilita el número de incidencia.|• Navedite broj reklamacije.
102|• Explica que la entrega puede tardar unas semanas.|• Objasnite da isporuka može potrajati nekoliko nedelja.
103|• Pide al cliente que vuelva a contactar si las piezas no llegan en aproximadamente 20 días hábiles.|• Zamolite kupca da se ponovo javi ako delovi ne stignu za približno 20 radnih dana.
104|Pide al cliente que indique el número de incidencia cuando vuelva a contactar.|Zamolite kupca da navede broj reklamacije pri ponovnom obraćanju.
105|Pedidos por correo electrónico – crear un ZTAC|Porudžbine mejlom – kreiranje ZTAC
106|Tramitación del pedido|Obrada porudžbine
107|01. Comprueba si el cliente ya existe o si hay que crearlo.|01. Proverite da li kupac već postoji ili treba kreirati novog.
108|02. Introduce el pedido ZTAC en SAP.|02. Unesite porudžbinu ZTAC u SAP.
109|03. Envía el presupuesto al cliente.|03. Pošaljite ponudu kupcu.
110|Restricciones de los pedidos por correo electrónico|Ograničenja porudžbina mejlom
111|Máximo de 40 referencias distintas y 20 unidades de una misma referencia por pedido. No se aplican promociones.|Najviše 40 različitih šifara artikala i 20 komada iste šifre po porudžbini. Promocije se ne primenjuju.
112|Pedidos por correo electrónico – comprobar clientes existentes|Porudžbine mejlom – provera postojećih kupaca
113|Anota el número de cliente para crear el pedido ZTAC.|Zapišite broj kupca za kreiranje porudžbine ZTAC.
114|Pedidos por correo electrónico – crear un nuevo cliente|Porudžbine mejlom – kreiranje novog kupca
115|Datos necesarios del cliente|Potrebni podaci o kupcu
116|para pedidos o|za porudžbine ili
117|para reclamaciones si vas a crearlas a continuación.|za reklamacije ako odmah zatim kreirate reklamaciju.
118|Introducir el pedido ZTAC – pasos 1–5|Unos porudžbine ZTAC – koraci 1–5
119|Sigue los pasos numerados en SAP|Pratite numerisane korake u SAP-u
120|Introducir el pedido ZTAC – pasos 6–9|Unos porudžbine ZTAC – koraci 6–9
121|Continúa con los pasos numerados en SAP|Nastavite sa numerisanim koracima u SAP-u
122|Enviar el presupuesto al cliente|Slanje ponude kupcu
123|Presupuesto + Términos y Condiciones|Ponuda + Uslovi kupovine
124|Envía al cliente el presupuesto y los Términos y Condiciones.|Pošaljite kupcu ponudu i Uslove kupovine.
125|El cliente acepta el presupuesto – pago|Kupac prihvata ponudu – plaćanje
126|El cliente puede completar la compra con uno de estos dos métodos de pago.|Kupac može završiti kupovinu jednim od ova dva načina plaćanja.
127|Transferencia bancaria|Bankovni prenos
128|• Envía al cliente los datos bancarios aprobados, el presupuesto y los Términos y Condiciones.|• Pošaljite kupcu odobrene podatke za uplatu, ponudu i Uslove kupovine.
129|• Informa a|• Obavestite
130|Contabilidad|Računovodstvo
131|del ingreso previsto.|o očekivanoj uplati.
132|• Incluye el número de pedido, el número de cliente y el importe.|• Navedite broj porudžbine, broj kupca i iznos.
133|• Contabilidad confirmará por correo la recepción del ingreso.|• Računovodstvo će mejlom potvrditi prijem uplate.
134|• Solo entonces se puede quitar|• Tek tada uklonite
135|Operación por aclarar|Operación por aclarar (potrebno razjašnjenje)
136|para que se envíe el pedido.|kako bi porudžbina mogla da se pošalje.
137|Pago mediante enlace|Plaćanje putem linka
138|• Cambia la condición de pago del pedido a PBYL.|• Promenite uslov plaćanja porudžbine na PBYL.
139|• Informa al cliente de que el enlace de pago tiene una validez de|• Obavestite kupca da link za plaćanje važi
140|24 horas|24 sata
142|cuando se haya realizado el pago.|nakon izvršene uplate.
143|• Incluye el número de pedido, el número de cliente y el importe pagado.|• Navedite broj porudžbine, broj kupca i uplaćeni iznos.
144|Modificar / visualizar pedidos y reclamaciones|Izmena / pregled porudžbina i reklamacija
145|Este proceso permite modificar cantidades o eliminar artículos de un pedido manual pendiente de pago.|Ovaj postupak omogućava izmenu količina ili uklanjanje artikala iz ručne porudžbine koja čeka uplatu.
146|Importante – Operación por aclarar|Važno – Operación por aclarar (potrebno razjašnjenje)
147|Después de realizar cambios, vuelve a establecer|Nakon izmena ponovo postavite
148|Si no se establece este bloqueo, el pedido se facturará y se enviará.|Bez ove blokade porudžbina će biti fakturisana i poslata.
149|Para transferencias, quita el bloqueo solo tras la confirmación de Contabilidad. Con PBYL, la validación es automática: no lo quites manualmente.|Kod bankovnog prenosa uklonite blokadu tek nakon potvrde Računovodstva. Kod PBYL validacija je automatska: ne uklanjajte blokadu ručno.
150|Pago mediante enlace – proceso SAP|Plaćanje putem linka – postupak u SAP-u
151|Correo de pago automático|Automatski mejl za plaćanje
152|Al grabar los cambios, SAP envía automáticamente un correo al cliente para solicitar el pago.|Kada sačuvate izmene, SAP automatski šalje kupcu mejl sa zahtevom za plaćanje.
153|El pedido se valida automáticamente con el pago mediante enlace.|Porudžbina se automatski validira pri plaćanju putem linka.
154|No quites manualmente Operación por aclarar.|Ne uklanjajte ručno Operación por aclarar (potrebno razjašnjenje).
155|Cómo responder a los clientes|Kako odgovarati kupcima
156|Utiliza las plantillas del|Koristite šablone iz dokumenta
157|Manual Atención al Cliente de Playmobil Ibérica|Manual Atención al Cliente de Playmobil Ibérica (priručnik korisničke podrške)
158|Si no existe una plantilla o el caso es específico, personaliza la respuesta.|Ako nema odgovarajućeg šablona ili je slučaj poseban, prilagodite odgovor.
159|Comunica los accidentes, las situaciones de peligro y los problemas con piezas no encontradas o que no se pueden introducir en SAP al responsable de SAC:|Nesreće, opasne situacije i probleme sa delovima koji nisu pronađeni ili se ne mogu uneti u SAP prijavite odgovornoj osobi u SAC-u:
160|Responsable de SAC|Odgovorna osoba u SAC-u
161|Consulta el directorio interno aprobado.|Kontakt potražite u odobrenom internom imeniku.
162|Cuando hayas resuelto un correo, muévelo a la carpeta|Kada rešite zahtev, premestite mejl u fasciklu
163|Enviado|Enviado (poslato)
164|.|.
165|Incidencias de transporte|Problemi u transportu
166|Paquetes perdidos o no entregados, retrasos, cambios de dirección y cancelaciones|Izgubljeni ili neisporučeni paketi, kašnjenja, promene adrese i otkazivanja
168|CORREO ELECTRÓNICO|ELEKTRONSKA POŠTA
171|TELÉFONO|TELEFON
181|Notas importantes|Važne napomene
182|No se modifica una dirección confirmada. Se puede trasladar la solicitud al transportista, sin garantizar el cambio.|Potvrđena adresa se ne menja. Zahtev se može proslediti prevozniku, bez garancije da će promena biti moguća.
183|Los documentos discrepan sobre el plazo de cancelación. Consulta los Términos y Condiciones aprobados y al responsable de SAC.|Dokumenti navode različite rokove za otkazivanje. Proverite odobrene Uslove kupovine i konsultujte odgovornu osobu u SAC-u.
184|Devoluciones y reembolsos|Povraćaj robe i novca
185|Motivos de devolución|Razlozi za povraćaj
186|Error del cliente al realizar el pedido o cambio de opinión.|Greška kupca pri poručivanju ili promena odluke.
187|Error en la preparación del pedido.|Greška pri pripremi porudžbine.
188|El cliente recibe un paquete dañado.|Kupac prima oštećen paket.
189|Formulario de devolución|Obrazac za povraćaj
190|Página de devoluciones de PLAYMOBIL|PLAYMOBIL stranica za povraćaj
191|Condiciones de devolución|Uslovi povraćaja
192|• Los gastos de devolución los asume el cliente.|• Troškove povraćaja snosi kupac.
193|• Si el daño se notificó en el momento de la entrega y consta en el justificante, PLAYMOBIL IBÉRICA asume los gastos de devolución.|• Ako je oštećenje prijavljeno pri isporuci i zabeleženo na potvrdi o isporuci, PLAYMOBIL IBÉRICA snosi troškove povraćaja.
194|• Plazo de desistimiento:|• Rok za odustanak:
195|14 días hábiles|14 radnih dana
196|Consulta los Términos y Condiciones aprobados; las fuentes discrepan.|Proverite odobrene Uslove kupovine; izvori navode različite rokove.
197|• Según la formación, los reembolsos se tramitan en|• Prema materijalu za obuku, povraćaj novca obrađuje se u roku od
198|desde la llegada de la mercancía a nuestras instalaciones.|od prijema robe u našem objektu.
199|Contacta con MRW para las recogidas que paga PLAYMOBIL IBÉRICA.|Za preuzimanja koja plaća PLAYMOBIL IBÉRICA obratite se MRW-u.
200|ZG2R – abono (pasos 1–4)|ZG2R – knjižno odobrenje (koraci 1–4)
201|Importante: anota el número de documento.|Važno: zapišite broj dokumenta.
202|ZG2R – abono (pasos 5–8)|ZG2R – knjižno odobrenje (koraci 5–8)
203|Después de crear el abono|Nakon kreiranja knjižnog odobrenja
204|Anota el número de documento e informa a|Zapišite broj dokumenta i obavestite
205|Contabilidad|Računovodstvo
206|del abono.|o knjižnom odobrenju.
207|En caso de duda, consulta al responsable de SAC.|Ako postoji nedoumica, obratite se odgovornoj osobi u SAC-u.
208|Seguimiento de envíos en SAP|Praćenje pošiljki u SAP-u
209|Consultar el estado del envío|Provera statusa pošiljke
210|Tareas diarias – llamadas y correos electrónicos|Svakodnevni zadaci – pozivi i mejlovi
211|Atención telefónica y por correo electrónico|Telefonska podrška i podrška mejlom
212|Responde con educación y eficacia a las consultas por teléfono y correo electrónico, resolviendo las dudas del cliente.|Na telefonske upite i mejlove odgovarajte ljubazno i efikasno, rešavajući nedoumice kupca.
213|Conoce bien la web|Dobro upoznajte sajt
215|y consúltala con frecuencia para conocer las promociones y novedades.|i redovno ga posećujte da biste pratili promocije i nove proizvode.
216|Qué consultar en la web|Šta treba pratiti na sajtu
217|El banner principal de la página de inicio muestra la promoción principal y otras novedades.|Glavni baner početne stranice prikazuje glavnu promociju i ostale novosti.
218|Es fundamental conocer las condiciones de las promociones porque generan muchas consultas.|Važno je poznavati uslove promocija jer kupci o njima često postavljaju pitanja.
219|Las consultas pueden tratar sobre entregas, productos, promociones, piezas sueltas o devoluciones. Estos temas se desarrollan a lo largo de la formación.|Upiti mogu biti o isporuci, proizvodima, promocijama, rezervnim delovima ili povraćaju. Sve ove teme obrađene su u obuci.
220|Promociones y consultas telefónicas|Promocije i telefonski upiti
221|Normalmente las promociones no son compatibles con|Promocije se obično ne kombinuju sa
222|Piezas sueltas o de repuesto –|Pojedinačnim ili rezervnim delovima –
223|piezas sueltas y manuales de montaje|rezervni delovi i uputstva za sklapanje
224|Otras promociones y códigos de descuento|Drugim promocijama i kodovima za popust
225|Packs promocionales|Promotivnim paketima
226|Novedades lanzadas en los últimos dos meses|Novim proizvodima uvedenim u poslednja dva meseca
227|Qué no podemos hacer por teléfono|Šta ne radimo telefonom
228|Solicitar datos personales para tramitar pedidos o reclamaciones. El cliente debe utilizar|Tražiti lične podatke za obradu porudžbine ili reklamacije. Kupac mora koristiti
229|la web|sajt
230|o escribir a|ili pisati na
232|Dar precios de productos. Remite al cliente a la web.|Saopštavati cene proizvoda. Uputite kupca na sajt.
233|Dar referencias de piezas sueltas. Pide al cliente que escriba por correo o consulte los manuales de montaje de la web.|Davati šifre rezervnih delova. Zamolite kupca da pošalje mejl ili pogleda uputstva za sklapanje na sajtu.
234|Estas consultas se resuelven por correo electrónico.|Ovi upiti se rešavaju mejlom.
235|Información esencial para SAC|Najvažnije informacije za SAC
236|Entrega|Isporuka
237|Pedidos de surtido regular:|Porudžbine redovnog asortimana:
238|6–8 días hábiles|6–8 radnih dana
239|Pedidos de piezas sueltas: hasta|Porudžbine rezervnih delova: do
240|10 semanas|10 nedelja
241|Pago|Plaćanje
242|Web: tarjeta de crédito y PayPal.|Sajt: kreditna kartica i PayPal.
243|Pedidos por correo electrónico: transferencia bancaria o tarjeta mediante enlace.|Porudžbine mejlom: bankovni prenos ili kartica putem linka.
244|Devoluciones y cambios|Povraćaj i izmene
245|Plazo de desistimiento:|Rok za odustanak:
246|Consulta los Términos y Condiciones aprobados; las fuentes discrepan.|Proverite odobrene Uslove kupovine; izvori navode različite rokove.
247|No se modifican los pedidos ni las direcciones una vez confirmada la compra.|Potvrđene porudžbine i adrese ne mogu se menjati.
248|Gastos de envío|Troškovi dostave
249|Península y Baleares:|Kopneni deo Španije i Balearska ostrva:
251|; las promociones de envío gratuito para compras superiores a 60 € están sujetas a condiciones.|; promocije besplatne dostave za kupovine preko 60 € podležu uslovima.
252|Canarias, Ceuta y Melilla:|Kanarska ostrva, Seuta i Melilja:
254|; envío gratuito para compras superiores a 150 €, sujeto a condiciones.|; besplatna dostava za kupovine preko 150 €, prema uslovima.
255|Pedidos por correo electrónico|Porudžbine mejlom
256|No se aplican promociones a los pedidos por correo electrónico.|Promocije se ne primenjuju na porudžbine mejlom.
257|Piezas individuales de una figura|Pojedinačni delovi figure
258|No se pueden pedir piezas individuales de una figura, como pelucas, barbas o brazos.|Pojedinačni delovi figure, kao što su perike, brade ili ruke, ne mogu se naručiti.
259|B) Estadísticas SAC|B) SAC statistika
260|Registra a diario los correos recibidos en la carpeta:|Svakodnevno evidentirajte primljene mejlove u fascikli:
262|Correos en el buzón|Mejlovi u sandučetu
263|Anota el total de correos que aparece en el buzón a primera hora, antes de abrirlos.|Ujutru, pre otvaranja poruka, zapišite ukupan broj mejlova prikazanih u sandučetu.
264|Correos recibidos|Primljeni mejlovi
265|Anota el número de correos recibidos el día anterior mediante la búsqueda correspondiente en Outlook.|Pomoću odgovarajuće pretrage u Outlooku zapišite broj mejlova primljenih prethodnog dana.
266|Pedidos y reclamaciones|Porudžbine i reklamacije
267|Después de leer y clasificar los correos, registra cuántos corresponden a pedidos y reclamaciones.|Nakon čitanja i razvrstavanja mejlova evidentirajte koliko se odnosi na porudžbine, a koliko na reklamacije.
268|C) Consulta de pedidos bloqueados en SAP|C) Provera blokiranih porudžbina u SAP-u
269|Primera búsqueda – VA14L|Prva pretraga – VA14L
270|Utiliza la transacción SAP|Koristite SAP transakciju
272|para consultar los pedidos bloqueados por importe elevado en España y Portugal.|za proveru porudžbina blokiranih zbog visokog iznosa u Španiji i Portugalu.
273|En|U polju
274|Bloqueo de entrega cabecera|Bloqueo de entrega cabecera (blokada isporuke u zaglavlju)
275|, realiza la primera búsqueda con:|prvu pretragu izvršite sa sledećim vrednostima:
276|Bloqueo de entrega:|Blokada isporuke:
278|Organización de ventas:|Organizacija prodaje:
279|(España)|(Španija)
280|Canal de distribución:|Kanal distribucije:
282|Sector:|Sektor:
283|Pulsa el icono del reloj para mostrar los pedidos bloqueados.|Kliknite na ikonicu sata da prikažete blokirane porudžbine.
284|Eliminar el bloqueo|Uklanjanje blokade
285|Abre el pedido pulsando su número en la tabla de resultados.|Otvorite porudžbinu klikom na njen broj u tabeli rezultata.
286|En|U polju
287|Bloqueo entrega|Bloqueo entrega (blokada isporuke)
288|, quita la opción|uklonite opciju
289|Comprobación importe|Comprobación importe (provera iznosa)
290|.|.
291|Graba el pedido.|Sačuvajte porudžbinu.
292|Cierra el pedido, vuelve a la pantalla inicial y pulsa el botón verde para guardar.|Zatvorite porudžbinu, vratite se na početni ekran i kliknite na zeleno dugme za čuvanje.
293|Repite la búsqueda con Z0, además de Z1.|Ponovite pretragu sa Z0, pored Z1.
294|C) Pedidos bloqueados – consulta de Portugal|C) Blokirane porudžbine – provera za Portugal
295|Repite las mismas comprobaciones para Portugal|Ponovite iste provere za Portugal
296|Realiza las dos búsquedas de bloqueo de entrega con la organización de ventas de Portugal:|Izvršite obe pretrage blokade isporuke sa organizacijom prodaje za Portugal:
297|Z1 y Z0|Z1 i Z0
298|Resumen diario: 2090 – Z1 y Z0; 2095 – Z1 y Z0.|Dnevni pregled: 2090 – Z1 i Z0; 2095 – Z1 i Z0.
299|En cada búsqueda, pulsa el reloj, revisa los resultados y elimina el bloqueo cuando proceda.|Za svaku pretragu kliknite na sat, pregledajte rezultate i uklonite blokadu kada je to potrebno.
300|D) Informes de Contabilidad – clientes bloqueados|D) Izveštaji Računovodstva – blokirani kupci
301|Informes diarios de Contabilidad|Dnevni izveštaji Računovodstva
302|Recibimos informes automáticos de Contabilidad a diario. Dos tipos requieren actuación:|Svakodnevno dobijamo automatske izveštaje Računovodstva. Dve vrste zahtevaju postupanje:
303|Clientes que deben bloquearse por datos falsos o incorrectos en sus pedidos, que incumplen los Términos y Condiciones.|Kupci koje treba blokirati zbog lažnih ili netačnih podataka u porudžbinama, čime su prekršeni Uslovi kupovine.
304|Informes de cancelaciones y abonos de pedidos devueltos a Alemania.|Izveštaji o otkazivanjima i knjižnim odobrenjima za porudžbine vraćene u Nemačku.
305|Archiva los demás informes en la carpeta Contabilidad de Outlook.|Ostale izveštaje arhivirajte u fascikli Contabilidad (Računovodstvo) u Outlooku.
306|Bloquear un cliente|Blokiranje kupca
307|Abre el correo y revisa el PDF adjunto con los clientes que deben bloquearse.|Otvorite mejl i pregledajte priloženi PDF sa kupcima koje treba blokirati.
308|Si aparece|Ako se pojavi poruka
310|, escribe al equipo de|, pišite timu
311|para solicitar el bloqueo de los clientes.|i zatražite blokiranje kupaca.
312|Informa por correo a los clientes afectados de que sus cuentas están deshabilitadas.|Obavestite pogođene kupce mejlom da su im nalozi deaktivirani.
313|Conserva el correo del día anterior en Contabilidad como no leído. Reenvíalo con todos los clientes y SAC en copia oculta (CCO).|Mejl od prethodnog dana ostavite u fascikli Contabilidad kao nepročitan. Prosledite ga sa svim kupcima i SAC-om u skrivenoj kopiji (BCC).
314|D) Informes de cancelaciones y abonos|D) Izveštaji o otkazivanjima i knjižnim odobrenjima
315|Comprobar la cancelación|Provera otkazivanja
316|Abre el informe de cancelaciones y abonos enviado por Alemania.|Otvorite izveštaj o otkazivanjima i knjižnim odobrenjima iz Nemačke.
317|En SAP, ejecuta|U SAP-u pokrenite
319|con el número de cliente.|sa brojem kupca.
320|Amplía el periodo de búsqueda a los dos meses anteriores.|Proširite period pretrage na prethodna dva meseca.
321|Comprueba si el cliente tiene el pedido|Proverite da li kupac ima odgovarajuću porudžbinu
323|correspondiente y la devolución|i povraćaj
325|creada por Alemania.|koji je kreirala Nemačka.
326|Qué comunicar a Contabilidad|Šta prijaviti Računovodstvu
327|Si el ZTAI y la devolución RE son correctos y no hay una compensación previa, reenvía el informe a Contabilidad y solicita el reembolso.|Ako su ZTAI i povraćaj RE ispravni i nije bilo prethodne nadoknade, prosledite izveštaj Računovodstvu i zatražite povraćaj novca.
328|Si existe un|Ako postoji
329|con el mismo contenido y la mercancía se ha enviado gratuitamente, no corresponde ese reembolso.|sa istim sadržajem i roba je već besplatno poslata, taj povraćaj novca nije opravdan.
330|Si ya se ha enviado la reclamación, indica a Contabilidad que no debe reembolsar al|Ako je roba po reklamaciji već poslata, obavestite Računovodstvo da ne izvrši povraćaj za
331|cliente afectado|pogođenog kupca
332|; se emitirá una factura|; izdaće se faktura
333|para compensar su cuenta.|za poravnanje njegovog računa.
334|Consulta el procedimiento L2 en|Postupak za L2 pogledajte u
335|J) Rectificación de abonos – Facturas L2 (y sección 37)|J) Rectificación abonos – Facturas L2 (ispravka knjižnih odobrenja; i odeljak 37)
336|y registra la operación en|i evidentirajte postupak u
338|Prioridades SAC – Navidad|SAC prioriteti – božićni period
339|Objetivos generales: dar soluciones rápidas y de calidad, informar del estado de los envíos y garantizar el servicio posventa.|Opšti ciljevi: brzo i kvalitetno rešavanje zahteva, obaveštavanje o statusu pošiljki i obezbeđivanje postprodajne podrške.
340|Noviembre – enero|Novembar – januar
341|Durante el periodo navideño, las prioridades son:|U božićnom periodu prioriteti su:
342|Prioridad 1|Prioritet 1
343|Pedidos y entregas|Porudžbine i isporuke
344|Consultas de pedidos y entregas, seguimiento, promociones y ofertas.|Upiti o porudžbinama i isporuci, praćenju pošiljki, promocijama i ponudama.
345|Prioridad 2|Prioritet 2
346|Servicio posventa|Postprodajna podrška
347|Piezas faltantes o defectuosas, pedidos de piezas de repuesto y devoluciones.|Delovi koji nedostaju ili su neispravni, porudžbine rezervnih delova i povraćaji.
348|Prioridad 3|Prioritet 3
349|Otras solicitudes|Ostali zahtevi
350|Todas las demás solicitudes de clientes.|Svi ostali zahtevi kupaca.
351|Prioridades SAC – resto del año|SAC prioriteti – ostatak godine
352|De febrero a octubre, el servicio posventa es la prioridad principal.|Od februara do oktobra postprodajna podrška ima prednost.
353|Febrero – octubre|Februar – oktobar
354|¡Gracias por vuestra atención!|Hvala na pažnji!
355|Diseño de Bojan Dj.|Dizajn: Bojan Dj.
356|Volver al inicio|Nazad na početak
357|☰ Secciones|☰ Odeljci
358|Secciones|Odeljci
''')
EN={0:'Welcome to PLAYMOBIL SAC training',3:'Regular assortment',5:'6–8 working days',6:'Spare parts',10:'Spain / Portugal',12:'Free-shipping promotion: check conditions for purchases over EUR 60',13:'Canary Islands / Ceuta / Melilla',15:'Free shipping for purchases over EUR 150; check conditions',26:'DHL, CTT or UPS emails shipment information. Also check the spam folder.',29:'The sources disagree on the withdrawal deadline. Check approved Terms & Conditions and ask the SAC supervisor if uncertain.',32:'The customer pays return costs. PLAYMOBIL pays when damage was reported on delivery and recorded on the delivery receipt.',104:'Ask customers to quote their claim reference when contacting us again.',111:'Maximum 40 different references and 20 units of the same reference per order. No promotions apply.',128:'• Email the customer the approved bank details, quotation and Terms & Conditions.',129:'• Inform',130:'Accounting',133:'• Accounting will confirm receipt of payment by email.',135:'Operación por aclarar (operation to be clarified)',138:'• Change the order payment terms to PBYL.',145:'Use this process to change quantities or remove items from a manual order awaiting payment.',146:'Important – Operación por aclarar',149:'For bank transfers, remove the block only after Accounting confirms payment. PBYL validates automatically: do not remove it manually.',153:'Payment-link orders validate automatically.',154:'Do not manually remove Operación por aclarar.',159:'Report accidents, dangerous situations and problems with parts not found or unavailable for SAP entry to the SAC supervisor:',160:'SAC supervisor',161:'Use the approved internal contact directory.',163:'Enviado (Sent)',164:'.',182:'Confirmed addresses cannot be changed. Forward a request to the carrier without guaranteeing a change.',183:'The sources disagree on the cancellation deadline. Check approved Terms & Conditions and ask the SAC supervisor.',194:'• Withdrawal deadline:',196:'Check approved Terms & Conditions; the sources disagree.',197:'• The training describes refund processing within',205:'Accounting',207:'If uncertain, ask the SAC supervisor.',243:'Email orders: bank transfer or card via payment link.',245:'Withdrawal deadline:',246:'Check approved Terms & Conditions; the sources disagree.',251:'; free-shipping promotions for purchases over €60 are subject to conditions.',254:'; free shipping for purchases over €150, subject to conditions.',274:'Bloqueo de entrega cabecera (header delivery block)',287:'Bloqueo entrega (delivery block)',289:'Comprobación importe (amount check)',304:'Cancellation and credit-note reports for orders returned to Germany.',310:'appears, email the',311:'team to request the customer blocks.',327:'If the ZTAI order and RE return are correct and no earlier compensation exists, forward the report to Accounting and request the refund.',329:'exists with the same contents and the free replacement has been dispatched, this refund is not appropriate.',330:'If the claim shipment has already been sent, tell Accounting not to refund the',331:'affected customer',332:'; issue an',335:'J) Rectificación abonos – Facturas L2 (and section 37)'}
NEW={
37:{'source':'Manual · 27–29; 9',
'en':['L2 invoices – correcting a credit note',
['When to use L2','L2 corrects an incorrect or duplicate credit note so the customer receives only the appropriate refund.','If a free ZTA3 replacement with the same contents was dispatched, tell Accounting not to refund and follow the L2 correction procedure. Record the correction in ABONOS CONTABILIDAD_01.'],
['Documented sequence','1. In Crear pedido (create order), select L2. Choose Crear con referencia (create with reference) and enter the original purchase invoice.','2. Choose Tomar (copy). Set Motivo de pedido (order reason) to Razón devolución desconocida (unknown return reason), then save.','3. Record the generated document number. Open it in Modificar pedido (change order) and save to obtain the invoice number. Coordinate the correction with Accounting.']],
'es':['Facturas L2 – rectificar un abono',
['Cuándo utilizar L2','L2 rectifica un abono incorrecto o duplicado para que el cliente reciba únicamente el reembolso que corresponde.','Si se ha enviado un ZTA3 gratuito con el mismo contenido, indica a Contabilidad que no realice el reembolso y sigue el procedimiento L2. Registra la rectificación en ABONOS CONTABILIDAD_01.'],
['Secuencia documentada','1. En Crear pedido, selecciona L2. Pulsa Crear con referencia e introduce la factura original de la compra.','2. Pulsa Tomar. En Motivo de pedido, selecciona Razón devolución desconocida y graba.','3. Anota el número de documento generado. Ábrelo en Modificar pedido y graba para obtener el número de factura. Coordina la rectificación con Contabilidad.']],
'sr':['Fakture L2 – ispravka knjižnog odobrenja',
['Kada se koristi L2','L2 ispravlja pogrešno ili duplirano knjižno odobrenje kako bi kupac dobio samo opravdani povraćaj novca.','Ako je besplatna zamena ZTA3 sa istim sadržajem već poslata, obavestite Računovodstvo da ne izvrši povraćaj i primenite postupak L2. Ispravku evidentirajte u ABONOS CONTABILIDAD_01.'],
['Dokumentovani redosled','1. U Crear pedido (kreiranje porudžbine) izaberite L2. Kliknite na Crear con referencia (kreiranje sa referencom) i unesite originalnu fakturu kupovine.','2. Kliknite na Tomar (preuzmi). Za Motivo de pedido (razlog porudžbine) izaberite Razón devolución desconocida (nepoznat razlog povraćaja) i sačuvajte.','3. Zapišite broj kreiranog dokumenta. Otvorite ga u Modificar pedido (izmena porudžbine) i sačuvajte da dobijete broj fakture. Uskladite ispravku sa Računovodstvom.']]},
38:{'source':'Manual · 36–37; Formación 2026 · 16',
'en':['Demandware – an order is missing from SAP',
['Investigate the order','Use advanced search in Demandware / Salesforce and search by the customer’s email to review their order history.','ERROR and CREADO orders were not recorded correctly and cannot be processed or dispatched. Check whether the customer is blocked in SAP or whether billing details differ between earlier orders.'],
['Explain and escalate','If the account is blocked, explain that the order cannot be dispatched. If there is a system error without an account block, offer a manual quotation and payment by transfer or link.','Financial handling is unresolved in the manual: page 36 requests a refund, while page 37 describes an authorization hold. Ask Accounting to verify the actual payment status; do not promise a refund or its timing.','Manual recovery mentions website conditions, but the newer training excludes promotions on email orders. Escalate any promotion exception before promising it.']],
'es':['Demandware – un pedido no aparece en SAP',
['Investigar el pedido','Utiliza la búsqueda avanzada de Demandware / Salesforce y busca por el correo del cliente para revisar su historial de pedidos.','Los pedidos ERROR y CREADO no se han grabado correctamente y no pueden tramitarse ni enviarse. Comprueba si el cliente está bloqueado en SAP o si los datos de facturación difieren entre pedidos anteriores.'],
['Explicar y escalar','Si la cuenta está bloqueada, explica que no se puede enviar el pedido. Si se trata de un fallo del sistema sin bloqueo, ofrece un presupuesto manual y el pago por transferencia o enlace.','El manual no aclara el tratamiento del pago: la página 36 solicita un reembolso y la 37 describe una retención. Pide a Contabilidad que compruebe el estado real del pago; no prometas un reembolso ni su plazo.','La recuperación manual menciona las condiciones de la web, pero la formación más reciente excluye promociones en pedidos por correo. Escala cualquier excepción antes de prometerla.']],
'sr':['Demandware – porudžbina se ne prikazuje u SAP-u',
['Provera porudžbine','Koristite naprednu pretragu u Demandware / Salesforce i pretražite istoriju porudžbina prema adresi elektronske pošte kupca.','Porudžbine ERROR i CREADO nisu pravilno evidentirane i ne mogu se obraditi niti poslati. Proverite da li je kupac blokiran u SAP-u ili se podaci za fakturisanje razlikuju u prethodnim porudžbinama.'],
['Objašnjenje i prosleđivanje','Ako je nalog blokiran, objasnite da porudžbina ne može biti poslata. Ako je u pitanju sistemska greška bez blokade, ponudite ručnu ponudu i plaćanje bankovnim prenosom ili linkom.','Priručnik ne razjašnjava postupanje sa uplatom: strana 36 traži povraćaj, a strana 37 opisuje rezervaciju sredstava. Računovodstvo treba da proveri stvarni status uplate; ne obećavajte povraćaj ni rok.','Postupak ručnog oporavka pominje uslove sajta, ali novija obuka isključuje promocije za porudžbine mejlom. Svaki izuzetak prosledite nadležnima pre nego što ga obećate.']]},
39:{'source':'Manual · 38',
'en':['Reactivating a discount code',
['Check the specific situation','A single-use code may become inactive after an attempted order that was not confirmed. This procedure is for that documented situation.','In Demandware, open Pedidos (orders) and search using the customer’s email. Review the order history.'],
['Reactivate and save','Open the latest relevant order marked ERROR or CREADO.','In ESTADO DE PEDIDO (order status), select error and save. This reactivates the code in the documented case.','Do not apply this procedure to a completed purchase or promise that a code is eligible for every product. Check the promotion conditions.']],
'es':['Reactivar un código de descuento',
['Comprobar el caso concreto','Un código de un solo uso puede quedar inactivo tras un intento de pedido que no se confirmó. Este procedimiento se aplica a ese caso documentado.','En Demandware, abre Pedidos y busca con el correo del cliente. Revisa el historial.'],
['Reactivar y guardar','Abre el último pedido correspondiente que figure como ERROR o CREADO.','En ESTADO DE PEDIDO, selecciona error y guarda. Así se reactiva el código en el caso documentado.','No apliques este procedimiento a una compra completada ni prometas que el código sirve para todos los productos. Revisa las condiciones de la promoción.']],
'sr':['Ponovno aktiviranje koda za popust',
['Provera konkretnog slučaja','Kod za jednokratnu upotrebu može postati neaktivan posle pokušaja poručivanja koji nije potvrđen. Ovaj postupak odnosi se na taj dokumentovani slučaj.','U Demandware otvorite Pedidos (porudžbine) i pretražite prema mejlu kupca. Pregledajte istoriju.'],
['Aktiviranje i čuvanje','Otvorite poslednju odgovarajuću porudžbinu sa statusom ERROR ili CREADO.','U polju ESTADO DE PEDIDO (status porudžbine) izaberite error i sačuvajte. Time se kod ponovo aktivira u dokumentovanom slučaju.','Ne primenjujte ovaj postupak na završenu kupovinu i ne obećavajte da kod važi za svaki proizvod. Proverite uslove promocije.']]},
40:{'source':'Manual · 14, 22, 24, 31, 38; Formación 2026 · 3, 28–30',
'en':['Order validation and operational exceptions',
['Validate according to payment method','Bank transfer: wait for Accounting confirmation, then open Modificar pedido (change order), remove Operación por aclarar and save.','Payment link (PBYL): validation is automatic. Do not remove Operación por aclarar manually. Restore the block after editing an unpaid manual order.'],
['Check the exceptions','Claims usually cannot be changed after saving. A change may still be possible immediately after saving, before the delivery document is processed.','A customer number beginning 130 belongs to a shop (B2B); do not use it for a consumer claim. Check for the appropriate consumer account before creating a new one.','For a blocked customer requiring a credit note, ask Accounting to remove the block temporarily and to restore it afterwards. Surprise-bag spare parts cannot be ordered.','Webshops are B2C for Spain and Portugal. Handle consumer claims submitted through shops; route other B2B claims to Sales Administration.']],
'es':['Validación de pedidos y excepciones operativas',
['Validar según el método de pago','Transferencia: espera la confirmación de Contabilidad; después, abre Modificar pedido, quita Operación por aclarar y graba.','Enlace de pago (PBYL): la validación es automática. No quites Operación por aclarar manualmente. Restablece el bloqueo tras modificar un pedido manual pendiente de pago.'],
['Comprobar las excepciones','Las reclamaciones normalmente no pueden modificarse tras grabarlas. Puede existir una posibilidad inmediatamente después, antes de que se procese el albarán.','Un número de cliente que comienza por 130 corresponde a una tienda (B2B); no lo utilices para una reclamación de consumidor. Busca primero la cuenta de consumidor adecuada antes de crear otra.','Si un cliente bloqueado necesita un abono, pide a Contabilidad que quite el bloqueo temporalmente y que lo restablezca después. No se pueden pedir piezas sueltas de sobres sorpresa.','Las tiendas online son B2C para España y Portugal. Atiende las reclamaciones de consumidores tramitadas por tiendas y remite las demás reclamaciones B2B a Administración de Ventas.']],
'sr':['Validacija porudžbina i operativni izuzeci',
['Validacija prema načinu plaćanja','Bankovni prenos: sačekajte potvrdu Računovodstva, zatim otvorite Modificar pedido (izmena porudžbine), uklonite Operación por aclarar i sačuvajte.','Link za plaćanje (PBYL): validacija je automatska. Ne uklanjajte Operación por aclarar ručno. Vratite blokadu nakon izmene ručne porudžbine koja čeka uplatu.'],
['Provera izuzetaka','Reklamacije se uglavnom ne mogu menjati posle čuvanja. Izmena može biti moguća odmah nakon čuvanja, pre obrade otpremnice.','Broj kupca koji počinje sa 130 pripada prodavnici (B2B); ne koristite ga za reklamaciju potrošača. Pre kreiranja novog naloga proverite da li postoji odgovarajući potrošački nalog.','Ako je blokiranom kupcu potrebno knjižno odobrenje, zatražite od Računovodstva privremeno uklanjanje blokade i njeno vraćanje nakon postupka. Delovi iz kesica iznenađenja ne mogu se naručiti pojedinačno.','Internet prodavnice namenjene su potrošačima u Španiji i Portugalu. Obradite reklamacije potrošača koje proslede prodavnice; ostale B2B reklamacije uputite Administraciji prodaje.']]}}
ALTS={
18:['SAP customer search process','Búsqueda de clientes en SAP','Pretraga kupaca u SAP-u'],
19:['SAP new customer creation','Creación de un cliente en SAP','Kreiranje novog kupca u SAP-u'],
20:['SAP ZTA3 claim creation','Creación de una reclamación ZTA3 en SAP','Kreiranje reklamacije ZTA3 u SAP-u'],
21:['Claim register and customer reply example','Registro de reclamaciones y ejemplo de respuesta','Evidencija reklamacija i primer odgovora kupcu'],
22:['Customer email requesting products','Correo de un cliente con productos solicitados','Mejl kupca sa traženim proizvodima'],
23:['SAP customer search for a ZTAC order','Búsqueda de clientes para un pedido ZTAC','Pretraga kupaca za porudžbinu ZTAC'],
24:['SAP new customer form','Formulario de creación de clientes en SAP','Obrazac za kreiranje kupca u SAP-u'],
25:['SAP ZTAC order entry, steps 1–5','Introducción de ZTAC en SAP, pasos 1–5','Unos ZTAC u SAP-u, koraci 1–5'],
26:['SAP ZTAC order entry, steps 6–9','Introducción de ZTAC en SAP, pasos 6–9','Unos ZTAC u SAP-u, koraci 6–9'],
27:['Quotation email with Terms and Conditions','Correo de presupuesto con Términos y Condiciones','Mejl sa ponudom i Uslovima kupovine'],
29:['SAP order modification process','Modificación de pedidos en SAP','Postupak izmene porudžbine u SAP-u'],
30:['SAP payment-link procedure','Procedimiento de enlace de pago en SAP','Postupak za link za plaćanje u SAP-u'],
34:['SAP ZG2R credit note, steps 1–4','Abono ZG2R en SAP, pasos 1–4','Knjižno odobrenje ZG2R u SAP-u, koraci 1–4'],
35:['SAP ZG2R credit note, steps 5–8','Abono ZG2R en SAP, pasos 5–8','Knjižno odobrenje ZG2R u SAP-u, koraci 5–8'],
36:['SAP shipment and carrier tracking','Consulta de envíos y seguimiento del transportista en SAP','Pregled pošiljki i praćenje prevoznika u SAP-u']}

def translate_main(lang):
 main=deepcopy(original.xpath('//main')[0])
 for x in main.xpath('.//text()'):
  parent=x.getparent()
  if isinstance(parent,etree._Comment):continue
  s=norm(x)
  if s not in lookup:continue
  i=lookup[s]
  translated=EN.get(i,s) if lang=='en' else translations.get(i,{}).get(lang,s)
  if x.is_text:parent.text=' '+translated+' '
  elif x.is_tail:parent.tail=' '+translated+' '
 # Deadline numbers in withdrawal contexts must not remain; refund interval is distinct.
 for section in ['section-22','section-28']:
  root=main.get_element_by_id(section)
  for strong in root.xpath('.//strong | .//b'):
   if norm(strong.text) in ['14 working days','14 días hábiles','14 radnih dana']:
    # first matching numerical interval belongs to cancellation/withdrawal
    strong.text=''
    break
 # Fix missing navigation, preserve original section IDs and closing slide.
 prev={'en':'← Previous','es':'← Anterior','sr':'← Prethodna'}[lang]
 nxt={'en':'Next →','es':'Siguiente →','sr':'Sledeća →'}[lang]
 end=main.get_element_by_id('section-24').xpath('./div[last()]')[0]
 a=etree.SubElement(end,'a',href='#section-25',attrib={'class':'bg-gray-800 hover:bg-emerald-800 px-6 py-3 rounded-xl transition'});a.text=nxt
 link=main.get_element_by_id('section-35').xpath('.//a[@href="#section-36"]')[0];link.set('href','#section-37')
 closing=main.get_element_by_id('section-36')
 for num,record in NEW.items():
  content=record[lang]
  section=etree.Element('section',id=f'section-{num}',attrib={'class':'h-dvh snap-start snap-always flex flex-col bg-gradient-to-r from-[#202124] via-[#292633] to-[#49316C]'})
  top=etree.SubElement(section,'div',attrib={'class':'flex-none text-center py-6 px-4'})
  etree.SubElement(top,'h1',attrib={'class':'text-2xl md:text-4xl font-bold'}).text=content[0]
  grid=etree.SubElement(section,'div',attrib={'class':'grid md:grid-cols-2 gap-5 px-6 pb-5 flex-1 min-h-0'})
  for card in content[1:]:
   article=etree.SubElement(grid,'article',attrib={'class':'bg-gray-900 rounded-2xl p-6 shadow-lg','data-reveal':''})
   etree.SubElement(article,'h2',attrib={'class':'text-2xl font-bold mb-4'}).text=card[0]
   for para in card[1:]:etree.SubElement(article,'p',attrib={'class':'text-base mt-4'}).text=para
  source=etree.SubElement(section,'p',attrib={'class':'text-sm text-gray-300 px-6 pb-3'})
  source.text={'en':'Source: ','es':'Fuente: ','sr':'Izvor: '}[lang]+record['source'].replace('Manual',{'en':'January 2026 manual, pages','es':'Manual de enero de 2026, páginas','sr':'Priručnik, januar 2026, strane'}[lang]).replace('Formación 2026',{'en':'October 2026 training, pages','es':'Formación de octubre de 2026, páginas','sr':'Obuka, oktobar 2026, strane'}[lang]).replace(' · ',' ')
  nav=etree.SubElement(section,'div',attrib={'class':'flex justify-between p-5'})
  etree.SubElement(nav,'a',href='#section-'+str(35 if num==37 else num-1),attrib={'class':'bg-indigo-700 hover:bg-indigo-600 px-5 py-3 rounded-lg'}).text=prev
  etree.SubElement(nav,'a',href='#section-'+str(36 if num==40 else num+1),attrib={'class':'bg-indigo-700 hover:bg-indigo-600 px-5 py-3 rounded-lg'}).text=nxt
  main.insert(main.index(closing),section)
 for img in main.xpath('.//img'):
  n=int(re.search(r'page-(\d+)',img.get('src')).group(1))
  img.set('alt',ALTS[n][['en','es','sr'].index(lang)])
  img.set('data-preserved-click', 'openLightbox($event.currentTarget.src)')
  img.set('title',{'en':'Click to enlarge','es':'Pulsa para ampliar','sr':'Kliknite za uvećanje'}[lang])
 # Staff contact links become roles, not broken mailto links.
 for a in main.xpath('.//a[starts-with(@href,"mailto:")]'):
  if any(s in a.get('href','').lower() for s in ['anabel','maria_gomez']):
   a.tag='span';a.attrib.pop('href',None)
 # Complete SAP order-type reference with the type used in cancellation review.
 types=main.get_element_by_id('section-5').xpath('.//div[p[normalize-space(.)="ZTAC"]]')[0].getparent()
 extra=etree.SubElement(types,'div',attrib={'class':'w-full bg-gray-800 rounded-xl p-4'})
 etree.SubElement(extra,'p',attrib={'class':'text-2xl font-bold text-purple-200'}).text='ZTAI'
 etree.SubElement(extra,'p',attrib={'class':'text-lg mt-1'}).text={'en':'Regular assortment, DS and spare parts','es':'Surtido regular, DS y piezas sueltas','sr':'Redovni asortiman, DS i rezervni delovi'}[lang]
 # Explain the interface without requiring learners to decipher screenshots alone.
 notes={14:{'en':'Enter order type ZTAC, sales organization 2090 (Spain) or 2095 (Portugal), distribution channel 01 and division 01. Complete customer, payment terms, order reason, material references and quantities. Before saving, select Tratar → Modificación rápida → Motivo de Rechazo → Operación por aclarar to prevent unpaid dispatch.','es':'Introduce ZTAC, organización de ventas 2090 (España) o 2095 (Portugal), canal 01 y sector 01. Completa cliente, condiciones de pago, motivo, materiales y cantidades. Antes de grabar, selecciona Tratar → Modificación rápida → Motivo de Rechazo → Operación por aclarar para evitar un envío sin pago.','sr':'Unesite ZTAC, organizaciju prodaje 2090 (Španija) ili 2095 (Portugal), kanal 01 i sektor 01. Popunite kupca, uslove plaćanja, razlog, šifre artikala i količine. Pre čuvanja izaberite Tratar → Modificación rápida → Motivo de Rechazo → Operación por aclarar (potrebno razjašnjenje) kako roba ne bi bila poslata bez uplate.'},15:{'en':'After saving, retain the order number. Open Detalles → Mensajes → Cabecera → Tratar, configure Datos Adicionales and Medios de comunicación as shown, then save to receive the quotation PDF. Send it with the Terms and Conditions.','es':'Tras grabar, anota el número de pedido. Abre Detalles → Mensajes → Cabecera → Tratar, configura Datos Adicionales y Medios de comunicación como se muestra y graba para recibir el PDF del presupuesto. Envíalo con los Términos y Condiciones.','sr':'Nakon čuvanja zapišite broj porudžbine. Otvorite Detalles → Mensajes → Cabecera → Tratar, podesite Datos Adicionales (dodatni podaci) i Medios de comunicación (sredstva komunikacije) kao na prikazu i sačuvajte da dobijete PDF ponude. Pošaljite ga sa Uslovima kupovine.'},19:{'en':'Before validation, change Condición de pago from DE01 to PBYL. Open Detalles → Cabecera → Tratar, select the last message, choose Repetir mensaje, review Medios de Comunicación and Dar salida, then return and save.','es':'Antes de validar, cambia Condición de pago de DE01 a PBYL. Abre Detalles → Cabecera → Tratar, selecciona el último mensaje, pulsa Repetir mensaje, revisa Medios de Comunicación y Dar salida, vuelve y graba.','sr':'Pre validacije promenite Condición de pago (uslov plaćanja) sa DE01 na PBYL. Otvorite Detalles → Cabecera → Tratar, izaberite poslednju poruku i Repetir mensaje (ponovi poruku), proverite Medios de Comunicación i Dar salida (izlaz), zatim se vratite i sačuvajte.'}}
 for number,localized in notes.items():
  sec=main.get_element_by_id('section-'+str(number))
  p=etree.Element('p',attrib={'class':'text-sm text-gray-200 px-8 pb-4'});p.text=localized[lang]
  sec.insert(len(sec)-1,p)
 # Apply the newer customer tone, retaining the Spanish official signature.
 section=main.get_element_by_id('section-20')
 note=etree.Element('p',attrib={'class':'text-base text-gray-200 px-8 pb-4'})
 note.text={'en':'Use a professional, friendly tone. In Spanish, address the customer as tú and sign Tu equipo PLAYMOBIL (your PLAYMOBIL team).','es':'Utiliza un tono profesional, amable y cercano. Dirígete al cliente de tú y firma como Tu equipo PLAYMOBIL.','sr':'Koristite profesionalan, ljubazan i pristupačan ton. Na španskom se kupcu obraćajte sa tú (ti), a potpis je Tu equipo PLAYMOBIL (vaš PLAYMOBIL tim).'}[lang]
 section.insert(len(section)-1,note)
 return html.tostring(main,encoding='unicode',method='html').replace('data-preserved-click=', '@click.stop=')

for lang,file in [('en','index.html'),('es','es.html'),('sr','sr.html')]:
 current=Path(file).read_text(encoding='utf8')
 current=re.sub(r'<main\b[\s\S]*?</main>',lambda _:translate_main(lang),current,count=1)
 Path(file).write_text(current,encoding='utf8')
 print(file,'40 synchronized sections')
