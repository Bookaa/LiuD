# LiuTaoTao github.com/Bookaa/LiuD

from libforgen import *

def GenPython01(mod):
    assert isinstance(mod, LiuD_Module)
    visit = Visit_Gen01()
    mod.walkabout(visit)
    grmlst = visit.AllLst()
    return grmlst, visit.sample_text

class Visit_Gen02(LiuD_sample_visitor_01):
    def __init__(self, cur_syntax, arglst, grmlst):
        self.grmlst = grmlst
        self.nouse_cur_syntax = cur_syntax
        self.arglst = arglst
        self.argno = 0
        self.flgcomment = False
        self.savno = 1
        self.retv = 'None'
    def skipcomment(self):
        outp = OutP(2)
        #if self.flgcomment and self.cur_syntax != '-':
        #    outp.prtln('self.SkipComments(self.ignore_%s)' % self.cur_syntax)
        if not hasattr(self, 'cmtsts'):
            pass
        if self.flgcomment and self.cmtsts.getskipn() != -1:
            outp.prtln('self.Skip(%d)' % self.cmtsts.getskipn())
        self.flgcomment = True

    def skipcmt(self, n):
        if self.flgcomment and self.cmtsts.getskipn() != -1:
            OutP(n).prtln('self.Skip(%d)' % self.cmtsts.getskipn())
        self.flgcomment = True
    def Skipcmt(self, n, s = ''):
        skipn = self.cmtsts.getskipn(s)
        if skipn != -1:
            OutP(n).prtln('self.Skip(%d)' % skipn)

    def visit_dot_syntax(self, node):
        assert False
    def visit_set_linecomment(self, node):
        assert False
    def visit_set_blockcomment(self, node):
        assert False
    def visit_name_prefix(self, node):
        assert False
    def visit_string_def(self, node):
        assert False
    def visit_sample_text(self, node):
        assert False

    def visit_stmt_tax(self, node):
        node.v.walkabout(self)
    def visit_jiad(self, node):
        outp = OutP()
        outp.down(); outp.down()
        self.skipcomment()

        savname = 'sav%d' % self.savno; self.savno += 1
        assert isinstance(node.v1, LiuD_LitName)
        assert isinstance(node.v4, (LiuD_LitString, LiuD_ident, LiuD_basestrn, LiuD_LitName))
        vname, vtyp, vtyp2 = self.arglst[self.argno]; self.argno += 1
        outp.prtln('%s = []' % vname)
        outp.prtln('%s = self.getpos()' % savname)
        outp.prtln('while True:')
        outp.prtln('    v3 = %s' % self.handle_LitName(node.v1))
        outp.prtln('    if v3 is None:')
        outp.prtln('        break')
        outp.prtln('    %s.append(v3)' % vname)
        outp.prtln('    %s = self.getpos()' % savname)
        if node.v2q:
            outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v2q.n)
        else:
            self.Skipcmt(3)
        if isinstance(node.v4, LiuD_LitString):
            outp.prtln('    if not self.handle_OpChar(%s):' % PythonString(node.v4.s))
        elif isinstance(node.v4, LiuD_LitName):
            outp.prtln('    %s = %s' % (sav2name, self.handle_LitName(node.v4)))
            outp.prtln('    if %s is None:' % sav2name)
        elif isinstance(node.v4, LiuD_basestrn):
            assert isinstance(node.v4.v, LiuD_LitName)
            outp.prtln('    if %s is None:' % self.handle_LitName(node.v4.v))
        else:
            outp.prtln('    if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(node.v4.s), self.cur_syntax))
        outp.prtln('        break')
        if node.v3q:
            outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v3q.s)
        else:
            self.Skipcmt(3)
        outp.prtln('self.setpos(%s)' % savname)
    def handle_LitName(self, node):
        assert isinstance(node, LiuD_LitName)
        if self.grmlst.ifinline(node.n):
            return 'self.hdl_%s()' % node.n
        return 'self.handle_%s()' % node.n
    def visit_jiap(self, node):
        outp = OutP()
        outp.down(); outp.down()
        self.skipcomment()

        savname = 'sav%d' % self.savno; self.savno += 1
        assert isinstance(node.v1, LiuD_LitName)
        assert isinstance(node.v4, (LiuD_LitString, LiuD_ident, LiuD_basestrn, LiuD_LitName))
        vname, vtyp, vtyp2 = self.arglst[self.argno]; self.argno += 1
        outp.prtln('%s = []' % vname)
        sav2name = None
        if isinstance(node.v4, LiuD_LitName):
            #assert node.v4.n in base_def
            v2name = self.arglst[self.argno][0]; self.argno += 1
            outp.prtln('%s = []' % v2name)
            sav2name = 'tmp%d' % self.savno; self.savno += 1
            outp.prtln('%s = None' % sav2name)

        outp.prtln('%s = self.getpos()' % savname)
        outp.prtln('while True:')
        outp.prtln('    v3 = %s' % self.handle_LitName(node.v1))
        outp.prtln('    if v3 is None:')
        outp.prtln('        break')
        outp.prtln('    %s.append(v3)' % vname)
        if sav2name is not None:
            outp.prtln('    if %s is not None:' % sav2name)
            outp.prtln('        %s.append(%s)' % (v2name, sav2name))
        outp.prtln('    %s = self.getpos()' % savname)
        if node.v2q:
            outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v2q.n)
        else: #if self.cur_syntax != '-':
            self.skipcmt(3)
        if isinstance(node.v4, LiuD_LitString):
            outp.prtln('    if not self.handle_OpChar(%s):' % PythonString(node.v4.s))
        elif isinstance(node.v4, LiuD_LitName):
            outp.prtln('    %s = %s' % (sav2name, self.handle_LitName(node.v4)))
            outp.prtln('    if %s is None:' % sav2name)
        elif isinstance(node.v4, LiuD_basestrn):
            assert isinstance(node.v4.v, LiuD_LitName)
            outp.prtln('    if %s is None:' % self.handle_LitName(node.v4.v))
        else:
            outp.prtln('    if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(node.v4.s), self.cur_syntax))
        outp.prtln('        break')
        if node.v3q:
            outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v3q.s)
        else:
            self.skipcmt(3)
        outp.prtln('if not %s:' % vname)
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        outp.prtln('self.setpos(%s)' % savname)

    def visit_LitName(self, node):
        outp = OutP(2)
        self.skipcomment()

        s = node.n

        if self.argno >= len(self.arglst):
            assert False
        vname, vtyp, vtyp2 = self.arglst[self.argno]; self.argno += 1
        if self.grmlst.ifinline(node.n):
            outp.prtln('%s = self.hdl_%s()' % (vname, node.n))
        else:
            outp.prtln('%s = self.handle_%s()' % (vname, node.n))
        outp.prtln('if %s is None:' % vname)
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return %s' % self.retv)

    def visit_syntaxdef(self, node):
        if node.n != '-':
            print '        self.SkipComments(self.ignore_%s)' % node.n
        self.flgcomment = False

    def visit_noskip(self, node):
        self.flgcomment = False

    def visit_itemq(self, node):
        if isinstance(node.v, LiuD_basestrn):
            v2 = node.v.v
            if isinstance(v2, LiuD_LitName):
                self.Skipcmt(2)
                OutP(2).prtln('%s' % self.handle_LitName(v2))
                return
        outp = OutP(2)
        savflg = self.flgcomment
        if self.flgcomment:
            savname = 'sav%d' % self.savno; self.savno += 1
            outp.prtln('%s = self.getpos()' % savname)
            self.skipcmt(2)
        self.flgcomment = True

        if isinstance(node.v, LiuD_LitName):
            vname = self.arglst[self.argno][0]; self.argno += 1
            outp.prtln('%s = %s' % (vname, self.handle_LitName(node.v)))
            if savflg:
                outp.prtln('if %s is None:' % vname)
                outp.prtln('    self.setpos(%s)' % savname)
        elif isinstance(node.v, LiuD_basestrn):
            v2 = node.v.v
            if isinstance(v2, LiuD_stringchoice):
                vname = self.arglst[self.argno][0]; self.argno += 1
                no = 0
                for s in v2.slst:
                    if no == 0:
                        outp.prtln('%s = self.%s' % (vname, Word_or_Symbol(s)))
                    else:
                        outp.prtln('if %s is None:' % vname)
                        outp.prtln('    %s = self.%s' % (vname, Word_or_Symbol(s)))
                    no += 1
            elif isinstance(v2, LiuD_LitString):
                vname = self.arglst[self.argno][0]; self.argno += 1
                outp.prtln('%s = self.%s' % (vname, Word_or_Symbol(v2.s)))
            elif isinstance(v2, LiuD_LitName):
                assert False
            else:
                assert False
            if savflg:
                outp.prtln('if %s is None:' % vname)
                outp.prtln('    self.setpos(%s)' % savname)
        elif isinstance(node.v, LiuD_ident):
            outp.prtln('self.handle_Ident(%s, self.ignore_%s)' % (node.v.s, self.cur_syntax))
        elif isinstance(node.v, LiuD_LitString):
            outp.prtln('self.%s' % Word_or_Symbol(node.v.s))
        else:
            assert False
    def visit_itemd(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcmt(2)

        if isinstance(node.v, LiuD_LitName):
            vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
            savname = 'sav%d' % self.savno; self.savno += 1
            outp.prtln('%s = []' % vname)
            outp.prtln('%s = self.getpos()' % savname)
            outp.prtln('while True:')
            outp.prtln('    v3 = %s' % self.handle_LitName(node.v))
            outp.prtln('    if v3 is None:')
            outp.prtln('        break')
            outp.prtln('    %s.append(v3)' % vname)
            outp.prtln('    sav1 = self.getpos()')
            self.skipcmt(3)
            outp.prtln('self.setpos(%s)' % savname)
        elif isinstance(node.v, LiuD_basestrn):
            if isinstance(node.v.v, LiuD_LitName):
                if self.cur_syntax == '-':
                    outp.prtln('while self.handle_%s() is not None:' % node.v.v.s)
                    outp.prtln('    pass')
                else:
                    savname = 'sav%d' % self.savno; self.savno += 1
                    outp.prtln('%s = self.getpos()' % savname)
                    outp.prtln('while True:')
                    outp.prtln('    v3 = self.handle_%s()' % node.v.v.s)
                    outp.prtln('    if v3 is None:')
                    outp.prtln('        break')
                    outp.prtln('    %s = self.getpos()' % savname)
                    self.skipcmt(3)
                    outp.prtln('self.setpos(%s)' % savname)
                pass
            else:
                assert False
        else:
            assert False

    def visit_itemp(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()

        savname = 'sav%d' % self.savno; self.savno += 1
        assert isinstance(node.v, LiuD_LitName)
        vname, vtyp, vtyp2 = self.arglst[self.argno]; self.argno += 1
        outp.prtln('%s = []' % vname)
        outp.prtln('%s = self.getpos()' % savname)
        outp.prtln('while True:')
        outp.prtln('    v3 = %s' % self.handle_LitName(node.v))
        outp.prtln('    if v3 is None:')
        outp.prtln('        break')
        outp.prtln('    %s.append(v3)' % vname)
        outp.prtln('    %s = self.getpos()' % savname)
        self.skipcmt(3)
        outp.prtln('if not %s:' % vname)
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        outp.prtln('self.setpos(%s)' % savname)

    def visit_optgroup(self, node):
        outp = OutP(); outp.down(); outp.down()
        savname = 'sav%d' % self.savno; self.savno += 1
        outp.prtln('flag = True')
        outp.prtln('%s = self.getpos()' % savname)
        self.skipcomment()

        lst = []
        no = False
        for v in node.vlst:
            if isinstance(v, LiuD_LitString):
                if no:
                    outp.prtln('if flag:')
                    outp.down()
                    self.skipcmt(3)

                outp.prtln('if self.%s is None:' % Word_or_Symbol(v.s))
                outp.prtln('flag = False', 1)
                if no:
                    outp.up()
            elif isinstance(v, LiuD_LitName):
                vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
                lst.append(vname)
                if no:
                    outp.prtln('%s = None' % vname)
                    outp.prtln('if flag:')
                    outp.down()
                    self.skipcmt(3)
                outp.prtln('%s = %s' % (vname, self.handle_LitName(v)))
                outp.prtln('if %s is None:' % vname)
                outp.prtln('flag = False', 1)
                if no:
                    outp.up()
            elif isinstance(v, LiuD_ident):
                outp.prtln('if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(v.s), self.cur_syntax))
                outp.prtln('flag = False', 1)
            else:
                assert False
            no = True
        outp.prtln('if not flag:')
        for vname in lst:
            outp.prtln('    %s = None' % vname)
        outp.prtln('    self.setpos(%s)' % savname)

    def visit_LitString(self, node):
        outp = OutP(2)
        self.skipcomment()

        outp.prtln('if self.%s is None:' % Word_or_Symbol(node.s))
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return %s' % self.retv)
    def visit_bracechoice(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()

        vname = None
        first = True
        for v in node.vlst:
            if isinstance(v, LiuD_LitName):
                pass
                if first:
                    vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
                    outp.prtln('%s = %s' % (vname, self.handle_LitName(v)))
                else:
                    outp.prtln('if %s is None:' % vname)
                    outp.prtln('    %s = %s' % (vname, self.handle_LitName(v)))

            elif isinstance(v, LiuD_inline):
                if first:
                    vname = self.arglst[self.argno]; self.argno += 1
                    outp.prtln('%s = self.handle_%s()' % (vname, v.v.s))
                else:
                    outp.prtln('if %s is None:' % vname)
                    outp.prtln('    %s = self.handle_%s()' % (vname, v.v.s))
            elif isinstance(v, LiuD_basestrn):
                if isinstance(v.v, LiuD_LitString):
                    if first:
                        vname = self.arglst[self.argno]; self.argno += 1
                        outp.prtln('%s = self.%s' % (vname, Word_or_Symbol(v.v.s)))
                    else:
                        outp.prtln('if %s is None:' % vname)
                        outp.prtln('    %s = self.%s' % (vname, Word_or_Symbol(v.v.s)))
                else:
                    assert False
            else:
                assert False
            first = False
        if vname is not None:
            outp.prtln('if %s is None:' % vname)
            outp.prtln('    self.setpos(sav0)')
            outp.prtln('    return None')
    def visit_BoolChoice(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()
        vname = self.arglst[self.argno][0]; self.argno += 1
        outp.prtln('%s = False' % vname)
        outp.prtln('if self.handle_OpChar(%s) is not None:' % PythonString(node.s1))
        outp.prtln('    %s = True' % vname)
        outp.prtln('elif self.handle_OpChar(%s) is None:' % PythonString(node.s2))
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
    def visit_BoolIf(self, node):
        outp = OutP(); outp.down(); outp.down()
        #savname = 'sav%d' % self.savno; self.savno += 1
        #outp.prtln('%s = self.getpos()' % savname)
        self.skipcomment()
        vname = self.arglst[self.argno][0]; self.argno += 1
        #outp.prtln('%s = False' % vname)
        #outp.prtln('if self.handle_OpChar(%s) is not None:' % PythonString(node.s))
        #outp.prtln('    %s = True' % vname)
        #outp.prtln('else:')
        #outp.prtln('    self.setpos(%s)' % savname)
        outp.prtln('%s = self.handle_OpChar(%s) is not None' % (vname, PythonString(node.s)))

    def visit_basestrn(self, node):
        outp = OutP(2)
        self.skipcomment()

        if isinstance(node.v, LiuD_LitName):
            outp.prtln('if self.handle_%s() is None:' % node.v.n)
            outp.prtln('    self.setpos(sav0)')
            outp.prtln('    return None')
        elif isinstance(node.v, LiuD_stringchoice):
            vname = None
            first = True
            for s in node.v.slst:
                if first:
                    vname = self.arglst[self.argno][0]; self.argno += 1
                    outp.prtln('%s = self.%s' % (vname, Word_or_Symbol(s)))
                else:
                    outp.prtln('if %s is None:' % vname)
                    outp.prtln('    %s = self.%s' % (vname, Word_or_Symbol(s)))
                first = False
            outp.prtln('if %s is None:' % vname)
            outp.prtln('    self.setpos(sav0)')
            outp.prtln('    return None')
        else:
            assert False
        pass
    def visit_ident(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()

        outp.prtln('if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(node.s), self.cur_syntax))
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
    def visit_ifnext(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()

        savname = 'sav%d' % self.savno; self.savno += 1
        outp.prtln('%s = self.getpos()' % savname)
        for s in node.slst:
            outp.prtln('if self.%s is None:' % Word_or_Symbol(s))
            outp.down()
        outp.prtln('self.setpos(sav0)')
        outp.prtln('return None')
        for _ in node.slst:
            outp.up()

        outp.prtln('self.setpos(%s)' % savname)
    def visit_ifnotnext(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()

        for s in node.slst:
            outp.prtln('if self.%s is not None:' % Word_or_Symbol(s))
            outp.down()
            outp.prtln('self.setpos(sav0)')
            outp.prtln('return None')
            outp.up()

    def visit_choices(self, node):
        return self.visit_bracechoice(node)

    def visit_OtherSyntax(self, node):
        outp = OutP(); outp.down(); outp.down()
        self.skipcomment()
        vname1 = self.arglst[self.argno][0]; self.argno += 1
        vname2 = self.arglst[self.argno][0]; self.argno += 1
        vname3 = self.arglst[self.argno][0]; self.argno += 1


        outp.prtln("if self.handle_OpChar('$') is None:")
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        outp.prtln('%s = self.handle_NAME()' % vname1)
        outp.prtln('if %s is None:' % vname1)
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        outp.prtln("if self.handle_OpChar('.') is None:")
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        outp.prtln('%s = self.handle_NAME()' % vname2)
        outp.prtln('if %s is None:' % vname2)
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')

        self.skipcomment()
        outp.prtln("if self.handle_OpChar('{') is None:")
        outp.prtln('    self.setpos(sav0)')
        outp.prtln('    return None')
        self.skipcomment()
        s33 = '''
        if s1 == 'Python':
            import Ast_Python
            newparser = Ast_Python.Parser(self.srctxt)
            newparser.setpos(self.getpos())
            if s2 == 'item0':
                result = newparser.hdl_item0()
            elif s2 == 'value':
                result = newparser.handle_value()
            else:
                assert False
            if result is None:
                self.setpos(sav0)
                return None
            newpos = newparser.getpos()
            self.setpos(newpos)
            self.SkipComments(self.ignore_crlf)
            if self.handle_OpChar('}') is None:
                self.setpos(sav0)
                return None
            return LangL_OtherSyntax(s1, s2, result)

        self.setpos(sav0)
        return None
'''
        outp.prtln(s33)

    def visit_MoreDef(self, node):
        outp = OutP(2)
        first = node.vlst[0]
        if isinstance(first, LiuD_LitName):
            vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
            outp.prtln('%s = %s' % (vname, self.handle_LitName(first)))
            outp.prtln('if %s is None:' % vname)
            outp.prtln('    return None')
            outp.prtln('sav0 = self.getpos()')
            self.skipcomment()
            self.retv = vname
            for v in node.vlst[1:]:
                v.walkabout(self)
            self.retv = 'None'
            return

        if isinstance(first, LiuD_jiap):
            assert isinstance(first.v1, LiuD_LitName)
            assert len(node.vlst) == 1
            savname = 'tem%d' % self.savno; self.savno += 1
            outp.prtln('%s = %s' % (savname, self.handle_LitName(first.v1)))
            outp.prtln('if %s is None:' % savname)
            outp.prtln('    return None')
            vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
            outp.prtln('%s = [%s]' % (vname, savname))
            outp.prtln('while True:')
            #outp.down()
            outp.prtln('    sav0 = self.getpos()')
            if first.v2q:
                self.Skipcmt(3, first.v2q.n)
            elif self.cur_syntax != '-':
                outp.prtln('    self.SkipComments(self.ignore_%s)' % self.cur_syntax)
            if isinstance(first.v4, LiuD_LitString):
                outp.prtln('    if not self.handle_OpChar(%s):' % PythonString(first.v4.s))
            elif isinstance(first.v4, LiuD_LitName):
                name = first.v4.n
                assert name in base_def
                outp.prtln('    %s = self.handle_%s()' % (sav2name, name))
                outp.prtln('    if %s is None:' % sav2name)
                #assert isinstance(self.grmlst.dic[name][0], LiuD_stmt_tax)
                #assert False
            elif isinstance(first.v4, LiuD_basestrn):
                assert isinstance(first.v4.v, LiuD_LitName)
                outp.prtln('    if %s is None:' % self.handle_LitName(first.v4.v))
            else:
                outp.prtln('    if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(first.v4.s), self.cur_syntax))
            outp.prtln('        break')
            if first.v3q:
                outp.prtln('    self.SkipComments(self.ignore_%s)' % first.v3q.n)
            else: #if self.cur_syntax != '-':
                self.Skipcmt(3)
            outp.prtln('    v3 = %s' % self.handle_LitName(first.v1))
            outp.prtln('    if v3 is None:')
            outp.prtln('        break')
            outp.prtln('    %s.append(v3)' % vname)
            outp.prtln('self.setpos(sav0)')
            outp.prtln('if len(%s) == 1:' % vname)
            outp.prtln('    return %s' % savname)
            return
        if isinstance(first, LiuD_itemp):
            assert isinstance(first.v, LiuD_LitName)
            assert len(node.vlst) == 1
            savname = 'tem%d' % self.savno; self.savno += 1
            outp.prtln('%s = %s' % (savname, self.handle_LitName(first.v)))
            outp.prtln('if %s is None:' % savname)
            outp.prtln('    return None')
            vname,vtyp,vtyp2 = self.arglst[self.argno]; self.argno += 1
            outp.prtln('%s = [%s]' % (vname, savname))
            outp.prtln('while True:')
            #outp.down()
            outp.prtln('    sav0 = self.getpos()')
            self.Skipcmt(3)
            outp.prtln('    v3 = %s' % self.handle_LitName(first.v))
            outp.prtln('    if v3 is None:')
            outp.prtln('        break')
            outp.prtln('    %s.append(v3)' % vname)
            outp.prtln('self.setpos(sav0)')
            outp.prtln('if len(%s) == 1:' % vname)
            outp.prtln('    return %s' % savname)
            return
        assert(False)
        for v in node.vlst:
            v.walkabout(self)

def Word_or_Symbol(s):
    if (s[0], s[-1]) == ("'", "'"):
        s = s[1:-1]
    b = IfWordStr(s)

    if b:
        return "handle_NAME('%s')" % s
    return "handle_OpChar(%s)" % PythonString(s)

def To2PythonString(s):
    if (s[0], s[-1]) == ("'", "'"):
        s = s[1:-1]

    return PythonString(s)

def IfWordStr(s):
    restr = base_def['NAME'][1] #'[A-Za-z_][A-Za-z0-9_]*'
    lexed = re.compile(restr, re.VERBOSE)
    m = lexed.match(s, 0)
    if m and m.group() == s:
        return True
    return False

class CommentsStatus:
    def __init__(self, lst_skips, ignoresyntax, linecmt, blockcmt):
        self.all = (lst_skips, ignoresyntax, linecmt, blockcmt)

    def getskipn(self, s=''):
        (lst_skips, ignoresyntax, linecmt, blockcmt) = self.all
        if s == '':
            s = ignoresyntax
        ignoresyntax = s
        if ignoresyntax == '-' and linecmt == '':
            return -1
        return lst_skips.index((ignoresyntax, linecmt, blockcmt))

def GenPython02(grmlst, ignore_lst):
    outp = OutP()
    if True:
        outp.prtln('''
class Parser(Parser00):

    def __init__(self, srctxt):
        Parser00.__init__(self, srctxt)
''')
        outp.down(); outp.down()
        if False:
            for (name,syntax) in ignore_lst.items():
                s1 = PythonString(syntax[0])
                s2 = str(syntax[1])
                outp.prtln('self.ignore_%s = IgnoreCls(%s, %s)' % (name, s1, s2))
            outp.prtln('')
        if True:
            lst_skips = []
            for nodeinfo in grmlst.iter_all():
                (node, arglst, ignoresyntax, linecmt, blockcmt) = (nodeinfo.node, nodeinfo.arglst, nodeinfo.ign_syntax, nodeinfo.linecmt, nodeinfo.blockcmt)
                if (ignoresyntax, linecmt, blockcmt) == ('-', '', None):
                    continue
                if (ignoresyntax, linecmt, blockcmt) not in lst_skips:
                    lst_skips.append((ignoresyntax, linecmt, blockcmt))
            outp.prtln('self.skips = [')
            for (ignoresyntax, linecmt, blockcmt) in lst_skips:
                syntax = ignore_lst[ignoresyntax]
                s1 = PythonString(syntax[0])
                lsts2 = syntax[1]
                if linecmt:
                    lsts2.append('%s.*' % linecmt)
                if blockcmt:
                    (lh, rh) = blockcmt
                    lsts2.append(r'%s(.|\n)*?%s' % (lh, rh))
                s2 = str(lsts2)
                outp.prtln('    IgnoreCls(%s, %s),' % (s1, s2))
            outp.prtln(']')

        lst3 = [name for name in base_def if base_def_used[name] > 0]
        lst3.sort()
        for name in lst3:
            stype, lexdef = base_def[name]
            outp.prtln('self.lex_%s = HowRe(%s)' % (name, PythonString(lexdef)))
        outp.up()
        for name in lst3:
            typ, lexdef = base_def[name]
            outp.prtln('')
            if typ == 'Name':
                outp.prtln('def handle_%s(self, s = None):' % name)
                outp.prtln('return self.handle_Lex(self.lex_%s, s)' % name, 1)
            elif typ == 'String':
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('    s = self.handle_Lex(self.lex_%s)' % name)
                outp.prtln('    return tostr_%s_%s(s)' % (SynName, name))
            elif typ == 'Int':
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('    s = self.handle_Lex(self.lex_%s)' % name)
                outp.prtln('    return None if s is None else int(s)')
            elif typ == 'strtype1':
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('return self.handle_string_Lex(self.lex_%s)' % name, 1)
            elif typ == 'strtype3':
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('return self.handle_string_Lex(self.lex_%s)' % name, 1)
            elif typ == 'strtype4':
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('s = self.handle_string_Lex(self.lex_%s)' % name, 1)
                outp.prtln('return Escape(s)', 1)
            elif typ in ('type00', 'Double'):
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('return self.handle_Lex(self.lex_%s)' % name, 1)
            else:
                print 'type is', typ
                assert False
                outp.prtln('def handle_%s(self):' % name)
                outp.prtln('return self.handle_Lex(self.lex_%s)' % name, 1)

    for nodeinfo in grmlst.iter_all():
        (node, arglst, ignoresyntax, linecmt, blockcmt) = (nodeinfo.node, nodeinfo.arglst, nodeinfo.ign_syntax, nodeinfo.linecmt, nodeinfo.blockcmt)
        cmtsts = CommentsStatus(lst_skips, ignoresyntax, linecmt, blockcmt)
        print
        if node.s == 'output_rules':
            pass

        if isinstance(node, LiuD_stmt_inline):
            if IsTrailer(node, grmlst):
                continue
            PrtStmtInline(node, arglst, grmlst, cmtsts)
            continue

        if node.s.startswith('trailer'):
            PrtTrailer(node, arglst, ignoresyntax, grmlst)
            continue

        outp.prtln('def handle_%s(self):' % node.s)
        if node.s == 'choices':
            pass
        if node.s == 'Module': # and ignoresyntax != '-':
            n = cmtsts.getskipn()
            if n != -1:
                outp.prtln('    self.Skip(%d)' % n)
            # outp.prtln('    self.--SkipComments(self.ignore_%s)' % ignoresyntax)
        if not arglst:
            PrtNoArg(node, grmlst, cmtsts)
            continue
        if isinstance(node.v, LiuD_opt2):
            PrtOpt2(node, arglst, grmlst, cmtsts)
            continue
        elif isinstance(node.v, LiuD_choices):
            value = node.v
            visit = Visit_Gen02(ignoresyntax, arglst, grmlst)
            visit.cmtsts = cmtsts
            outp.prtln('    sav0 = self.getpos()')
            value.walkabout(visit)

            s6 = ', '.join([nam1 for nam1,_,_ in arglst])

            outp.prtln('    return %s_%s(%s)' % (SynName, node.s, s6))
            assert visit.argno == len(arglst)
            continue
        else:
            value = node.v
            visit = Visit_Gen02(ignoresyntax, arglst, grmlst)
            visit.cmtsts = cmtsts
            if not isinstance(value, LiuD_MoreDef):
                outp.prtln('    sav0 = self.getpos()')
            value.walkabout(visit)

            s6 = ', '.join([nam1 for nam1,_,_ in arglst])

            outp.prtln('    return %s_%s(%s)' % (SynName, node.s, s6))
            if visit.argno != len(arglst):
                pass
            assert visit.argno == len(arglst)

def PrtStmtInline(node, arglst, grmlst, cmtsts):
    (lst_skips, ignoresyntax, linecmt, blockcmt) = cmtsts.all
    skipn = cmtsts.getskipn()

    outp = OutP(1)
    assert len(arglst) == 1
    argname, argtyp, argtyp2 = arglst[0]

    outp.prtln('def hdl_%s(self):' % node.s)
    outp.down()
    if isinstance(node.v, LiuD_choices):
        if argtyp2 in ('slst','nlst','vlst'):
            outp.prtln('%s = []' % argname)
        PreDone = False
        for (i, v) in enumerate(node.v.vlst):
            blast = (i == len(node.v.vlst) - 1)
            if isinstance(v, LiuD_serie):
                if not PreDone:
                    outp.prtln('sav0 = self.getpos()')
                    PreDone = True

                outp.prtln('flag = True')
                PrtSerie(v.vlst, arglst, outp, ignoresyntax)
                if blast:
                    outp.prtln('if not flag:')
                    outp.prtln('    return None')
                    outp.prtln('return %s' % argname)
            elif isinstance(v, LiuD_jiap):
                if not PreDone:
                    outp.prtln('sav0 = self.getpos()')
                    PreDone = True
                outp.prtln('flag = True')
                PrtSerie([v], arglst, outp, ignoresyntax)
                if blast:
                    outp.prtln('if not flag:')
                    outp.prtln('    return None')
                    outp.prtln('return %s' % argname)
            elif isinstance(v, LiuD_inline):
                if blast:
                    outp.prtln('return self.handle_%s()' % v.v.s)
                    continue
                outp.prtln('%s = self.handle_%s()' % (argname, v.v.s))
                outp.prtln('if %s is not None:' % argname)
                outp.prtln('return %s' % argname, 1)
            elif isinstance(v, LiuD_LitName):
                if blast:
                    outp.prtln('return %s' % grmlst.handle_LitName(v))
                    continue
                outp.prtln('%s = %s' % (argname, grmlst.handle_LitName(v)))
                outp.prtln('if %s is not None:' % argname)
                outp.prtln('return %s' % argname, 1)
            else:
                assert False

        return
    if isinstance(node.v, LiuD_serie):
        value = node.v
        visit = Visit_Gen02(ignoresyntax, arglst, grmlst)
        visit.cmtsts = cmtsts
        outp.prtln('sav0 = self.getpos()')
        value.walkabout(visit)

        #PrtSerie(node.v.vlst, arglst, outp, ignoresyntax)
        #outp.prtln('if not flag:')
        #outp.prtln('    return None')
        outp.prtln('return %s' % argname)
        return
    if isinstance(node.v, LiuD_jiap):
        value = node.v
        visit = Visit_Gen02(ignoresyntax, arglst, grmlst)
        outp.prtln('sav0 = self.getpos()')
        value.walkabout(visit)

        outp.prtln('return %s' % argname)
        outp.up()
        return
    if isinstance(node.v, LiuD_LitName):
        outp.prtln('return %s' % grmlst.handle_LitName(node.v))
        return
    assert False

def PrtSerie(nodelst, arglst, outp, cur_syntax):
    argname = arglst[0]
    argno = 0
    savno = 1
    outp.prtln('')
    lst = []
    no = False
    for v in nodelst:
        if isinstance(v, LiuD_LitString):
            if no:
                outp.prtln('if flag:')
                outp.down()
                if cur_syntax != '-':
                    outp.prtln('self.SkipComments(self.ignore_%s)' % cur_syntax)

            outp.prtln('if self.%s is None:' % Word_or_Symbol(v.s))
            outp.prtln('flag = False', 1)
            if no:
                outp.up()
        elif isinstance(v, LiuD_LitName):
            vname = arglst[argno]; argno += 1
            lst.append(vname)
            if no:
                outp.prtln('%s = None' % vname)
                outp.prtln('if flag:')
                outp.down()
                if cur_syntax != '-':
                    outp.prtln('self.SkipComments(self.ignore_%s)' % cur_syntax)
            outp.prtln('%s = self.handle_%s()' % (vname, v.s))
            outp.prtln('if %s is None:' % vname)
            outp.prtln('flag = False', 1)
            if no:
                outp.up()
        elif isinstance(v, LiuD_ident):
            outp.prtln('if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(v.s), self.cur_syntax))
            outp.prtln('flag = False', 1)
        elif isinstance(v, LiuD_jiad):
            vname = arglst[argno][0]; argno += 1
            lst.append(vname)
            if no:
                outp.prtln('if flag:')
                outp.down()
                if cur_syntax != '-':
                    outp.prtln('self.SkipComments(self.ignore_%s)' % cur_syntax)
            node = v
            savname = 'sav%d' % savno; savno += 1
            assert isinstance(node.v1, LiuD_LitName)
            assert isinstance(node.v4, (LiuD_LitString, LiuD_ident, LiuD_basestrn))
            outp.prtln('%s = self.getpos()' % savname)
            outp.prtln('while True:')
            outp.prtln('    v3 = self.handle_%s()' % node.v1.n)
            outp.prtln('    if v3 is None:')
            outp.prtln('        break')
            outp.prtln('    %s.append(v3)' % vname)
            outp.prtln('    %s = self.getpos()' % savname)
            if node.v2q:
                outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v2q.s)
            elif cur_syntax != '-':
                outp.prtln('    self.SkipComments(self.ignore_%s)' % cur_syntax)
            if isinstance(node.v4, LiuD_LitString):
                outp.prtln('    if not self.handle_OpChar(%s):' % PythonString(node.v4.s))
            elif isinstance(node.v4, LiuD_basestrn):
                assert isinstance(node.v4.v, LiuD_LitName)
                outp.prtln('    if self.handle_%s() is None:' % node.v1.s)
            else:
                outp.prtln('    if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(node.v4.s), self.cur_syntax))
            outp.prtln('        break')
            if node.v3q:
                outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v3q.s)
            elif cur_syntax != '-':
                outp.prtln('    self.SkipComments(self.ignore_%s)' % cur_syntax)
            outp.prtln('self.setpos(%s)' % savname)
            if no:
                outp.up()
        elif isinstance(v, LiuD_jiap):
            vname = arglst[argno][0]; argno += 1
            lst.append(vname)
            if no:
                outp.prtln('if flag:')
                outp.down()
                if cur_syntax != '-':
                    outp.prtln('self.SkipComments(self.ignore_%s)' % cur_syntax)
            node = v
            savname = 'sav%d' % savno; savno += 1
            assert isinstance(node.v1, LiuD_LitName)
            assert isinstance(node.v4, (LiuD_LitString, LiuD_ident, LiuD_basestrn))
            outp.prtln('%s = self.getpos()' % savname)
            outp.prtln('while True:')
            outp.prtln('    v3 = self.handle_%s()' % node.v1.n)
            outp.prtln('    if v3 is None:')
            outp.prtln('        break')
            outp.prtln('    %s.append(v3)' % vname)
            outp.prtln('    %s = self.getpos()' % savname)
            if node.v2q:
                outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v2q.s)
            elif cur_syntax != '-':
                outp.prtln('    self.SkipComments(self.ignore_%s)' % cur_syntax)
            if isinstance(node.v4, LiuD_LitString):
                outp.prtln('    if not self.handle_OpChar(%s):' % PythonString(node.v4.s))
            elif isinstance(node.v4, LiuD_basestrn):
                assert isinstance(node.v4.v, LiuD_LitName)
                outp.prtln('    if self.handle_%s() is None:' % node.v1.s)
            else:
                outp.prtln('    if not self.handle_Ident(%s, self.ignore_%s):' % (PythonString(node.v4.s), self.cur_syntax))
            outp.prtln('        break')
            if node.v3q:
                outp.prtln('    self.SkipComments(self.ignore_%s)' % node.v3q.s)
            elif cur_syntax != '-':
                outp.prtln('    self.SkipComments(self.ignore_%s)' % cur_syntax)
            outp.prtln('if not %s:' % vname)
            outp.prtln('    flag = False')
            outp.prtln('else:')
            outp.prtln('    self.setpos(%s)' % savname)
            if no:
                outp.up()
        elif isinstance(v, LiuD_basestrn):
            if no:
                outp.prtln('if flag:')
                outp.down()
                if self.cur_syntax != '-':
                    outp.prtln('self.SkipComments(self.ignore_%s)' % cur_syntax)

            if isinstance(v.v, LiuD_LitName):
                outp.prtln('if self.handle_%s() is None:' % v.v.s)
                outp.prtln('flag = False', 1)
            else:
                assert False
            if no:
                outp.up()
        else:
            assert False
        no = True
    assert(len(lst) == 1)
    outp.prtln('if not flag:')
    argname, typ, typ2 = arglst[0]
    if argname.startswith('slst') or argname.startswith('vlst'):
        outp.prtln('    %s = []' % argname)
    else:
        outp.prtln('    %s = None' % argname)
    outp.prtln('    self.setpos(sav0)')
    outp.prtln('else:')
    outp.prtln('    return %s' % argname)


def PrtNoArg(node, grmlst, cmtsts):
    (lst_skips, ignoresyntax, linecmt, blockcmt) = cmtsts.all
    outp = OutP(2)
    visit = Visit_Gen02(ignoresyntax, [], grmlst)
    visit.cmtsts = cmtsts
    outp.prtln('sav0 = self.getpos()')

    visit.flgcomment = True
    node.v.walkabout(visit)

    outp.prtln('return %s_%s()' % (SynName, node.s))
    assert visit.argno == 0


def PrtOpt2(node, arglst, grmlst, cmtsts):
    (lst_skips, ignoresyntax, linecmt, blockcmt) = cmtsts.all
    skipn = cmtsts.getskipn()

    outp = OutP(1)
    def skipcmt():
        if skipn != -1:
            outp.prtln('self.Skip(%d)' % skipn)

    #print '    def handle_%s(self):' % node.s
    #outp.prtln('    v = %s' % grmlst.handle_LitName(node.v))
    if node.v.s in grmlst.dic and isinstance(grmlst.dic[node.v.s].node, LiuD_stmt_inline):
        s9 = 'self.hdl_%s()' % node.v.s
    else:
        s9 = 'self.handle_%s()' % node.v.s
    outp.prtln('    v = %s' % s9)
    outp.prtln('    if v is None:')
    outp.prtln('        return None')
    no = len(node.v.vlst)
    outp.prtln('    return self.step%d_%s(v)' % (no, node.s))

    no = 0
    for v in node.v.vlst:
        no += 1
        if isinstance(v, LiuD_stringchoice):
            s7 = ', '.join([PythonString(s) for s in v.slst])
            outp.prtln("")
            outp.prtln('def step%d_%s(self, v1):' % (no, node.s))
            outp.down()
            if no > 1:
                outp.prtln('v1 = self.step%d_%s(v1)' % (no-1, node.s))
            outp.prtln('sav0 = self.getpos()')
            skipcmt()
            outp.prtln('op = self.GetOpInLst([%s])' % s7)
            outp.prtln('if op is None:')
            outp.prtln('self.setpos(sav0)', 1)
            outp.prtln('return v1', 1)
            skipcmt()
            outp.prtln('v2 = %s' % s9)
            outp.prtln('if v2 is None:')
            outp.prtln('self.setpos(sav0)', 1)
            outp.prtln('return v1', 1)
            if no > 1:
                outp.prtln('v2 = self.step%d_%s(v2)' % (no-1, node.s))
            outp.prtln('v1 = %s_%s(v1, op, v2)' % (SynName, node.s))
            outp.prtln('return self.step%d_%s(v1)' % (no, node.s))
            outp.up()
        elif isinstance(v, LiuD_LitString):
            outp.prtln("")
            outp.prtln('def step%d_%s(self, v1):' % (no, node.s))
            outp.down()
            if no > 1:
                outp.prtln('v1 = self.step%d_%s(v1)' % (no-1, node.s))
            outp.prtln('sav0 = self.getpos()')
            skipcmt()
            outp.prtln('op = self.handle_OpChar(%s)' % PythonString(v.s))
            outp.prtln('if op is None:')
            outp.prtln('self.setpos(sav0)', 1)
            outp.prtln('return v1', 1)
            skipcmt()
            outp.prtln('v2 = %s' % s9)
            outp.prtln('if v2 is None:')
            outp.prtln('self.setpos(sav0)', 1)
            outp.prtln('return v1', 1)
            if no > 1:
                outp.prtln('v2 = self.step%d_%s(v2)' % (no-1, node.s))
            outp.prtln('v1 = %s_%s(v1, op, v2)' % (SynName, node.s))
            outp.prtln('return self.step%d_%s(v1)' % (no, node.s))
            outp.up()
        else:
            assert False


def PrtTrailer(node, arglst, ignoresyntax, grmlst):
    outp = OutP(); outp.down()
    outp.prtln('def handle_%s(self, %s):' % (node.s, arglst[0][0]))
    outp.down()
    assert not isinstance(node.v, LiuD_choices)
    vserie = node.v
    visit = Visit_Gen02(ignoresyntax, arglst, grmlst)
    outp.prtln('sav0 = self.getpos()')
    assert isinstance(vserie, LiuD_serie)

    visit.flgcomment = True
    visit.argno += 1
    for v in vserie.vlst[1:]:
        v.walkabout(visit)

    s6 = ', '.join([nam1 for nam1,_,_ in arglst])
    outp.prtln('return %s_%s(%s)' % (SynName, node.s, s6))
    assert visit.argno == len(arglst)

def IsTrailer(node, grmlst):
    if not isinstance(node.v, LiuD_choices):
        return False
    basenode = None
    trailer = []
    for v in node.v.vlst:
        if isinstance(v, LiuD_inline):
            v3 = v.v
            value = v3.v
            if isinstance(value, LiuD_choices):
                return False
            theserie = value
            if v3.s.startswith('trailer'):
                first = theserie.vlst[0]
                assert isinstance(first, LiuD_LitName) and first.n == node.s
                trailer.append(v3)
            else:
                if basenode is not None:
                    return False
                basenode = v3

        elif isinstance(v, LiuD_LitName):
            if basenode is not None:
                return False
            basenode = v
        else:
            return False
    if basenode is None:
        return False
    if not trailer:
        return False
    outp = OutP(); outp.down()
    outp.prtln('def hdl_%s(self):' % node.s)
    outp.down()
    if grmlst.ifinline(basenode.n):
        outp.prtln('v = self.hdl_%s()' % basenode.n)
    else:
        outp.prtln('v = self.handle_%s()' % basenode.n)
    outp.prtln('if v is None:')
    outp.prtln('return None', 1)
    #outp.prtln('pos0 = self.getpos()')
    outp.prtln('while True:')
    outp.down()
    for v in trailer:
        outp.prtln('v1 = self.handle_%s(v)' % v.s)
        outp.prtln('if v1 is not None:')
        outp.prtln('v = v1', 1)
        outp.prtln('continue', 1)
    outp.prtln('return v')
    #print outp.s
    return True

def GenPython03():
    print '\ndef Test_Parse_%s(srctxt):' % SynName
    print '''    parser = Parser(srctxt)
    mod = parser.handle_Module()
    if mod is None:
        lastpos, lastlineno, lastcolumn, lastline = parser.GetLast()
        print 'parse error, last pos = %d' % lastpos
        print 'last lineno = %d, column = %d' % (lastlineno, lastcolumn)
        print 'last line :', lastline
    else:
        print 'parse success'
    return mod
'''
    print '''
def Test_Out_%s(mod):
    outp = OutPrt()
    the = %s_out_visitor_01(outp)
    mod.walkabout(the)
    outp.newline()
''' % (SynName, SynName)

    print "s_sample_%s = %s" % (SynName, PythonString(s_sample))

    print '''
if __name__ == '__main__':
    mod = Test_Parse_%s(s_sample_%s)
    if mod :
        Test_Out_%s(mod)
    ''' % (SynName, SynName, SynName)

def gen_sample_01(grmlst):
    outp = OutP()
    outp.prtln('class %s_sample_visitor_01:' % SynName)
    outp.down()
    for nodeinfo in grmlst.iter_syntax():
        (node, arglst, ignoresyntax) = (nodeinfo.node, nodeinfo.arglst, nodeinfo.ign_syntax)
        outp.prtln('def visit_%s(self, node):' % node.s)
        outp.down()
        flg = False
        for s,typ,typ2 in arglst:
            if typ2 == 'vlstq':
                outp.prtln('if node.%s is not None:' % s)
                outp.prtln('for v in node.%s:' % s, 1)
                outp.prtln('v.walkabout(self)', 2)
                flg = True
                continue
            if typ2 == 'vlst':
                outp.prtln('for v in node.%s:' % s)
                outp.prtln('v.walkabout(self)', 1)
                flg = True
                continue
            if typ2 == 'v':
                outp.prtln('node.%s.walkabout(self)' % s)
                flg = True
                continue
            if typ2 == 'vq':
                outp.prtln('if node.%s is not None:' % s)
                outp.prtln('node.%s.walkabout(self)' % s, 1)
                flg = True
                continue
            if typ2 in ('i','f','s','b','sq','slst','n','nq','nlst'):
                continue
            if typ in ('.s', '.s?', '.s*'):
                continue
            assert False
        if not flg:
            outp.prtln('pass')
        outp.up()

def GenPythonSrc(SyntaxIn):
    global base_def, base_def_used, SynName, s_sample, base_def2
    #s_sample = SyntaxIn.s_sample
    #SynName = SyntaxIn.SynName

    # sSyntax = 'STRING :: STRING1 | STRING2 | STRING3\n' + SyntaxIn.s_tree
    sSyntax = SyntaxIn.s_tree

    parser = Parser(sSyntax)

    mod = parser.handle_Module()
    if mod is None:
        lastpos, lastlineno, lastcolumn, lastline = parser.GetLast()
        print 'parse error, last pos = %d' % lastpos
        print 'last lineno = %d, column = %d' % (lastlineno, lastcolumn)
        print 'last line :', lastline
        return


    base_def2 = ('STRING',)

    base_def = { 'NEWLINE'       : ('type00',       '\\n+'),
                 'NAME'          : ('Name',   '[A-Za-z_][A-Za-z0-9_]*'),
                 'STRING1' : ('strtype1', r'\$liud\$((.|\n)*?)\$duil\$'),
                 'STRING2' : ('strtype1', r'\$liut\$((.|\n)*?)\$tuil\$'),
                 'STRING3' : ('strtype3', r"'([^'\\]*(?:\\.[^'\\]*)*)'"),
                 'STRING4' : ('strtype4', r"'([^'\\]*(?:\\.[^'\\]*)*)'"),
                 #'STRING'        : ('String',  r"'[^'\\]*(?:\\.[^'\\]*)*'"), # "'.*?'"
                 #'STRINGR'       : ('String', r"'[^'\\]*(?:\\.[^'\\]*)*'"),
                 #'STRING'  :    ('String',  r"'(.|\n)*?'")
                 'CHAR'          : ('String', r'.'),
                 'NUMBER'        : ('Int',    r'\d+'),
                 'NUMBER_INT'    : ('Int',    r'0|[1-9]\d*'),
                 'NUMBER_DOUBLE' : ('Double', r'\d+\.\d+') }
    # r"'[^'\\]*(?:\\.[^'\\]*)*'"

    base_def_used = {name : 0 for name in base_def}
    base_def_used['STRING1'] = -1   # never used
    base_def_used['STRING2'] = -1
    base_def_used['STRING3'] = -1
    base_def_used['STRING4'] = -1
    base_def_used['NAME'] = -1
    base_def_used['NEWLINE'] = -1

    import libforgen
    libforgen.base_def = base_def
    libforgen.base_def2 = base_def2
    libforgen.base_def_used = base_def_used
    libforgen.Dest = 'py'

    syntax_lst = { # this is default comment syntax
        'crlf'   : ( ' \t\n', [  ] ),
        'wspace' : ( ' \t',   [  ] ),
        'no'     : ( '', [] )
    }

    grmlst, s_sample = GenPython01(mod)

    print '# auto generate code, LiuTaoTao\n'
    print 'from lib import *'

    SynName = libforgen.SynName

    for nodeinfo in grmlst.iter_syntax():
        report1(nodeinfo)

    print 'class %s_sample_visitor_00:' % SynName
    for nodeinfo in grmlst.iter_syntax():
        print '    def visit_%s(self, node): pass' % nodeinfo.node.s
    print
    gen_sample_01(grmlst)
    if True:
        output_rules = None
        for m in mod.vlst:
            if isinstance(m, LiuD_output_rules):
                output_rules = m
                break
        if output_rules:
            gen_Out_02(output_rules, grmlst)

    print
    if False:
        GenPython_save(lst)
        GenPython_load(lst)
    GenPython02(grmlst, syntax_lst)
    GenPython03()

def report1(nodeinfo):
    name = nodeinfo.node.s; lst = nodeinfo.arglst
    lst = [nam1 for nam1,_,_ in lst]
    s7 = ''
    if lst:
        s3 = ', '.join(lst)
        s5 = ''
        for s in lst:
            s5 += '        self.%s = %s\n' % (s,s)
        s7 = '''    def __init__(self, %s):
%s''' % (s3,s5)

    s = '''
class %s_%s:
%s
    def walkabout(self, visitor):
        return visitor.visit_%s(self)
''' % (SynName, name, s7, name)
    print s

def TestSave():
    parser = Parser(s_tree)

    mod = parser.handle_Module()
    if mod is None:
        lastlineno, lastcolumn, lastline = parser.GetLast()
        print 'parse error, last lineno = %d, column = %d' % (lastlineno, lastcolumn)
        print 'last line :', lastline
        return

    saver = Saver()
    the = LiuD_sample_save(saver)
    mod.walkabout(the)

def CheckOrIsInstance(nodes, name, lst):
    if name in lst:
        return 'self.check_%s(%s)' % (name, nodes)
    return 'isinstance(%s, %s_%s)' % (nodes, SynName, name)

def Test_Parse_Out(srctxt):
    import Ast_Out
    parser = Ast_Out.Parser(srctxt)
    mod = parser.handle_Module()
    if mod is None:
        lastpos, lastlineno, lastcolumn, lastline = parser.GetLast()
        print 'parse error, last pos = %d' % lastpos
        print 'last lineno = %d, column = %d' % (lastlineno, lastcolumn)
        print 'last line :', lastline
    else:
        #print 'parse success'
        pass
    return mod

def GetOutNode(mod, name):
    for v in mod.vlst:
        if v.s == name:
            return v
    assert False, 'not find %s' % name 

def gen_Out_02(output_rules, grmlst):
    mod2 = output_rules

    outp = OutP()
    outp.prtln('')
    outp.prtln('class %s_out_visitor_01:' % SynName)
    outp.down()
    outp.prtln('def __init__(self, outp):')
    outp.prtln('    self.outp = outp')
    for nodeinfo in grmlst.iter_syntax():
        (node, arglst, ignoresyntax) = (nodeinfo.node, nodeinfo.arglst, nodeinfo.ign_syntax)
        outp.prtln('def visit_%s(self, node):' % node.s)
        name = node.s
        outnode = GetOutNode(mod2, name)
        the = Out3_visitor(arglst)
        outnode.walkabout(the)
        if not the.outp.fDone:
            outp.prtln('    pass')
        continue


class Out3_visitor:
    def __init__(self, arglst):
        self.arglst = arglst
        self.argno = 0
        self.outp = OutP(2)
        self.temno = 1

    def visit_orule(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_oJiad(self, node):
        arg, argtyp, argtyp2 = self.arglst[self.argno]; self.argno += 1
        tem1 = 'tem%d' % self.temno; self.temno += 1
        tem2 = 'tem%d' % self.temno; self.temno += 1
        if isinstance(node.v2, LiuD_oX):
            argjia, jiatyp, jiatyp2 = self.arglst[self.argno]; self.argno += 1
            self.outp.prtln('fn%s = iter(node.%s)' % (tem1, arg))
            self.outp.prtln('for %s in node.%s:' % (tem2, argjia))
            self.outp.prtln('    %s = fn%s.next()' % (tem1, tem1))
            self.outp.prtln('    %s.walkabout(self)' % tem1)
            self.outp.prtln('    self.outp.puts(%s)' % tem2)
            self.outp.prtln('%s = fn%s.next()' % (tem1, tem1))
            self.outp.prtln('%s.walkabout(self)' % tem1)
            return

        #arg2 = self.arglst[self.argno]; self.argno += 1
        self.outp.prtln('%s = 0' % tem1)
        self.outp.prtln('for %s in node.%s:' % (tem2, arg))
        self.outp.prtln('    if %s > 0:' % tem1)
        if node.vq is not None:
            self.outp.prtln('        self.outp.lnk()')
        self.outp.down(); self.outp.down()
        node.v2.walkabout(self)
        self.outp.up(); self.outp.up()
        #if isinstance(node.v2, Ast_Out.Out_String):
        #    self.outp.prtln('        self.outp.puts(%s)' % node.v2.s)
        #else:
        #    self.outp.prtln('        %s.walkabout(self)' % arg2)
        self.outp.prtln('    %s = 1' % tem1)
        s5 = SmartType(argtyp, argtyp2).howwalkmember(tem2)
        self.outp.prtln('    %s' % s5)
        #if arg.startswith('s'):
        #    self.outp.prtln('    self.outp.puts(%s)' % tem2)
        #else:
        #    self.outp.prtln('    %s.walkabout(self)' % tem2)
    def visit_oString(self, node):
        if node.s == 'othersyntax':
            s33 = '''
        if node.s1 == 'Python':
            import Ast_Python
            the = Ast_Python.Python_out_visitor_01(self.outp)
            node.v.walkabout(the)
            self.outp.puts('}')
            return
        else:
            assert False
            '''
            self.outp.prtln(s33)
            return
        self.outp.prtln('self.outp.puts(%s)' % To2PythonString(node.s))
    def visit_ooptgroup(self, node):
        arg = self.arglst[self.argno][0]
        self.outp.prtln('if node.%s is not None:' % arg)
        self.outp.down()
        for v in node.vlst:
            #if isinstance(v, Ast_Out.Out_X):
            #    self.outp.prtln('self.outp.puts(node.%s)' % arg)
            #    continue
            v.walkabout(self)
        self.outp.up()
        self.inopt = False
    def visit_oitemd(self, node):
        arg, typ, typ2 = self.arglst[self.argno]; self.argno += 1
        tem2 = 'tem%d' % self.temno; self.temno += 1
        self.outp.prtln('for %s in node.%s:' % (tem2, arg))
        self.outp.down()
        for v in node.vlst:
            if isinstance(v, LiuD_oX):
                s5 = SmartType(typ, typ2).howwalkmember(tem2)
                self.outp.prtln(s5)
                #if typ2 == 'slst': #arg.startswith('s'):
                #    self.outp.prtln('self.outp.puts(%s)' % tem2)
                #else:
                #    self.outp.prtln('%s.walkabout(self)' % tem2)
                continue
            v.walkabout(self)
        self.outp.up()
    def visit_oident(self, node):
        if node.s == '+ident':
            self.outp.prtln('self.outp.identin()')
        else:
            self.outp.prtln('self.outp.identout()')
    def visit_onewline(self, node):
        self.outp.prtln('self.outp.newline()')
    def visit_olnk(self, node):
        self.outp.prtln('self.outp.lnk()')
    def visit_oXlst(self, node):
        arg, typ, typ2 = self.arglst[self.argno]; self.argno += 1
        tem2 = 'tem%d' % self.temno; self.temno += 1
        self.outp.prtln('for %s in node.%s:' % (tem2, arg))
        s5 = SmartType(typ, typ2).howwalkmember(tem2)
        self.outp.prtln('    %s' % s5)
        #if arg.startswith('s'):
        #    self.outp.prtln('self.outp.puts(%s)' % tem2)
        #else:
        #    self.outp.prtln('    %s.walkabout(self)' % tem2)
    def visit_oXchoice(self, node):
        arg, typ, typ2 = self.arglst[self.argno]; self.argno += 1
        self.outp.prtln('if node.%s:' % arg)
        self.outp.prtln('self.outp.puts(%s)' % To2PythonString(node.s1), 1)
        self.outp.prtln('else:')
        self.outp.prtln('self.outp.puts(%s)' % To2PythonString(node.s2), 1)
    def visit_oXif(self, node):
        arg, typ, typ2 = self.arglst[self.argno]; self.argno += 1
        self.outp.prtln('if node.%s:' % arg)
        self.outp.prtln('self.outp.puts(%s)' % To2PythonString(node.s), 1)
    def visit_oXq(self, node):
        arg,typ,typ2 = self.arglst[self.argno]; self.argno += 1
        self.outp.prtln('if node.%s is not None:' % arg)
        self.outp.down()
        tem2 = 'node.%s' % arg
        s5 = SmartType(typ, typ2).howwalk(tem2)
        self.outp.prtln(s5)
        #if typ2 == 'sq': #arg.startswith('s'):
        #    self.outp.prtln('self.outp.puts(node.%s!)' % arg)
        #else:
        #    self.outp.prtln('node.%s!.walkabout(self)' % arg)
        self.outp.up()
    def visit_oX(self, node):
        if self.argno >= len(self.arglst):
            pass
        arg,typ,typ2 = self.arglst[self.argno]; self.argno += 1
        #if not self.inopt and arg.endswith('q'):
        #    self.outp.prtln('if node.%s is not None:' % arg)
        #    self.outp.down()
        tem2 = 'node.%s' % arg
        s5 = SmartType(typ, typ2).howwalk(tem2)
        self.outp.prtln(s5)
        #if typ2 in ('vq','sq'): #.endswith('q'):
        #    arg += '!'
        #if typ2 in ('s','sq', 'i', 'iq'): #arg.startswith('s'):
        #    self.outp.prtln('self.outp.puts(node.%s)' % arg)
        #else:
        #    self.outp.prtln('node.%s.walkabout(self)' % arg)
        #if not self.inopt and arg.endswith('q'):
        #    self.outp.up()

