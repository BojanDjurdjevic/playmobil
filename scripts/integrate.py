"""One-time presentation integration, kept for review; not a runtime dependency."""
from pathlib import Path
from lxml import html, etree

GALLERY = {
29:[('sac-statistics',3,('SAC statistics: record inbox, received, order and claim counts.','Estadísticas SAC: registra el buzón, los recibidos, los pedidos y las reclamaciones.','SAC statistika: beleži poruke u sandučetu, primljene poruke, porudžbine i reklamacije.')),('outlook-previous-day-search',4,('Outlook: use the Ayer filter to count messages received yesterday.','Outlook: utiliza el filtro Ayer para contar los mensajes del día anterior.','Outlook: koristi filter Ayer (juče) za broj poruka primljenih prethodnog dana.'))],
30:[('va14l-command',4,('Enter transaction VA14L.','Introduce la transacción VA14L.','Unesi transakciju VA14L.')),('va14l-search-parameters',4,('VA14L: Z1, sales organization 2090, channel 01 and division 01.','VA14L: Z1, organización de ventas 2090, canal 01 y sector 01.','VA14L: Z1, organizacija prodaje 2090, kanal 01 i sektor 01.')),('va14l-blocked-orders',5,('Review blocked orders; customer data is redacted.','Revisa los pedidos bloqueados; los datos de clientes están ocultados.','Pregled blokiranih porudžbina; podaci kupaca su trajno uklonjeni.')),('va14l-remove-delivery-block',5,('Bloqueo entrega: remove Comprobación importe after reviewing the order.','Bloqueo entrega: elimina Comprobación importe tras revisar el pedido.','Bloqueo entrega (blokada isporuke): ukloni Comprobación importe (provera iznosa) nakon provere.')),('va14l-save-modified-order',5,('Save the modified order and return using the indicated control.','Graba el pedido modificado y vuelve con el control indicado.','Sačuvaj izmenjenu porudžbinu i vrati se pomoću označene kontrole.'))],
31:[('va14l-portugal-z0',6,('Portugal: organization 2095, Z0 example. Repeat the check for Z1.','Portugal: organización 2095, ejemplo Z0. Repite la consulta con Z1.','Portugal: organizacija 2095, primer Z0. Ponovi proveru i za Z1.'))],
32:[('accounting-report-inbox',6,('Daily Accounting report types; private sender and date data removed.','Tipos de informes diarios de Contabilidad; remitentes y fechas privados eliminados.','Vrste dnevnih računovodstvenih izveštaja; privatni podaci pošiljalaca i datumi su uklonjeni.')),('accounting-block-report',7,('Counterparty error report: request the customer block from Accounting.','Informe de error de la contraparte: solicita el bloqueo del cliente a Contabilidad.','Izveštaj o grešci druge ugovorne strane: zatraži blokadu kupca od računovodstva.'))],
33:[('cancellation-report',8,('Cancellation report: verify the documents before requesting any refund.','Informe de cancelaciones: verifica los documentos antes de solicitar un reembolso.','Izveštaj o otkazivanjima: proveri dokumente pre zahteva za refundaciju.')),('va05-cancellation-check',8,('Use VA05 and extend the search to the previous two months.','Utiliza VA05 y amplía la búsqueda a los dos meses anteriores.','Koristi VA05 i proširi pretragu na prethodna dva meseca.')),('va05-refund-verification',9,('Compare ZTAI and RE with the replacement and credit history.','Compara ZTAI y RE con el historial de sustituciones y abonos.','Uporedi ZTAI i RE sa istorijom zamenskih pošiljki i knjižnih odobrenja.'))]}

for lang,filename in [('en','index.html'),('es','es.html'),('sr','sr.html')]:
    index=['en','es','sr'].index(lang)
    doc=html.fromstring(Path(filename).read_text(encoding='utf8'))
    main=doc.find('.//main');main.attrib.clear();main.set('class','h-dvh overflow-y-auto scroll-smooth');main.set('id','training')
    for node in main.iter():
        for attr in list(node.attrib):
            if attr.startswith('@') or attr in ['x-init','x-data']:del node.attrib[attr]
        if node.tag=='a' and node.get('target')=='_blank':node.set('rel','noopener noreferrer')
    for section,images in GALLERY.items():
        parent=main.get_element_by_id(f'section-{section}')
        for old in parent.xpath('./div[@class="gallery"]'):parent.remove(old)
        gallery=etree.Element('div',attrib={'class':'gallery'})
        for name,page,captions in images:
            figure=etree.SubElement(gallery,'figure',attrib={'data-reveal':''})
            caption=captions[index]
            etree.SubElement(figure,'img',src=f'assets/manual/{name}.png',alt=caption,loading='lazy',width='900',height='450')
            etree.SubElement(figure,'figcaption').text=caption+' '+['Manual, page ','Manual, página ','Priručnik, strana '][index]+str(page)+'.'
        parent.insert(len(parent)-1,gallery)
    title=['SAC Training Center','Centro de formación SAC','SAC centar za obuku'][index]
    result=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>PLAYMOBIL · {title}</title>
<link rel="stylesheet" href="css/tailwind.css"><link rel="stylesheet" href="css/center.css"><link rel="stylesheet" href="css/presentation.css">
<script defer src="js/i18n.js"></script><script defer src="js/presentation.js"></script><script defer src="js/vendor/alpine-3.15.8.min.js"></script></head>
<body class="presentation bg-gray-800 text-white" x-data="{{showContext:false}}">
{html.tostring(main,encoding='unicode')}
<noscript>JavaScript is required / Se necesita JavaScript / Potreban je JavaScript.</noscript>
</body></html>'''
    Path(filename).write_text(result,encoding='utf8')
print('Integrated 3 presentations and 13 shared screenshot references per language.')
