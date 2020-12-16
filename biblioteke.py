from osv import osv
from osv import fields
from datetime import datetime

class regjistrimi_librit(osv.osv):
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['ref1'], context=context)
        res = []
        for record in reads:
            if record['ref1']:
                name = record['ref1']
            res.append((record['id'], name))
        return res

    _name='regjistrimi.librit'
    _description='Modul i Ri'
    _columns={
       'autor':fields.text('Autor',required=True, select=True),
       'titull':fields.char('Titull',size=64,required=True, select=True),
       'kategori': fields.char('Kategori',size=64,required=True, select=True),
       'status': fields.selection([('i disponueshem', 'I disponueshem'),('i padisponueshem', 'I padisponueshem'),('mungese','Mungese')], 'Status'),
       'kopje': fields.boolean('Kopje',required=True, select=True),
       'employee': fields.many2one('stafi.punonjes','Punonjesi'),
       'ref1': fields.char('Ref1',size=5, required=True, select=True),
       'ref2': fields.char('Ref2',size=5, required=True, select=True),
}
    

regjistrimi_librit()

class dhenie_libri(osv.osv):
 
    
    _name='dhenie.libri'
    _description='Shperndarja'
    _columns={
        'autor':fields.char('Autor',size=15,required=True, select=True),
        'titull':fields.char('Titull',size=64,required=True, select=True),
        'lexues':fields.many2one('lexues.libra','Lexuesi',required=True, select=True),
        'dataKerkeses':fields.date('Data Kerkeses',required=True, select=True),
        'dataDorezimit':fields.date('Data Dorezimit',required=True, select=True),
        'lexim_salle': fields.boolean('Lexim ne Salle', required=True, select=True),
        'employee2': fields.char('Punonjesi',size=15, required=True, select=True),
        'status1': fields.selection([('e re', 'E Re'),('arkiv', 'Arkiv'),('miratuar','I Miratuar'),('refuzuat', 'I refuzuar'),('perfunduar','I Perfunduar')], 'Status'),
        'ref3': fields.many2one('regjistrimi.librit','Ref1', required=True, select=True),
        'ref4': fields.char('Ref2',size=5, required=True, select=True),
    }

    def onchange_ref3(self, cr, uid, ids, ref3, context=None):
        value = {'autor': False}
        value1 = {'titull': False}
        value2 = {'ref4': False}
        value3 = {'employee2': False}

        if ref3:
            obj = self.pool.get('regjistrimi.librit').browse(cr, uid, ref3)
            value['autor'] = obj.autor
            value['titull'] = obj.titull
            value['ref4'] = obj.ref2
            value['employee2'] = obj.employee.emri+' '+obj.employee.mbiemri
        return {'value': value}
        return {'value1': value}
        return {'value2': value}
        return {'value3': value}
                

class lexues_libra(osv.osv):
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['emri','mbiemri'], context=context)
        res = []
        for record in reads:
            if record['mbiemri']:
                name = record['emri']+' '+  record['mbiemri']
            res.append((record['id'], name))
        return res
        
    _name='lexues.libra'
    _description='Lexuesit'
    _columns={
        'emri':fields.char('Emri',size=15,required=True, select=True),
        'mbiemri':fields.char('Mbiemri',size=15,required=True, select=True),
        'datelindje':fields.date('Datelindje',required=True, select=True),
        'data_regjistrimit':fields.date('Data Regjistrimit',required=True, select=True),
        'data_skadences':fields.date('Data Skandences',required=True, select=True),
        'aktiv': fields.boolean('Aktiv', required=True, select=True),
}

class stafi_punonjes(osv.osv):

    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['emri','mbiemri'], context=context)
        res = []
        for record in reads:
            if record['mbiemri']:
                name = record['emri']+' '+  record['mbiemri']
            res.append((record['id'], name))
        return res

    _name='stafi.punonjes'
    _description='Stafi'
    _columns={
        'emri':fields.char('Emri',size=15,required=True, select=True),
        'mbiemri':fields.char('Mbiemri',size=15,required=True, select=True),
        'roli':fields.char('Roli',size=15,required=True, select=True),

}

